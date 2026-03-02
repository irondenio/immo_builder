# -*- coding: utf-8 -*-
"""
IMMO BUILDER - Module Utilitaire
Fonctions de calcul des coûts, surfaces, durées et planning.
"""

from data.projects import (
    PHASES_CONSTRUCTION,
    MATERIAUX,
    FINITIONS,
    OPTIONS_SUPPLEMENTAIRES,
    PRIX_M2_BASE,
    DEVISE,
)


def calculer_cout_materiaux(surface: float, materiaux: dict) -> int:
    """Calcule le coût des matériaux pour la surface donnée."""
    cout = 0
    for categorie, choix in materiaux.items():
        if categorie in MATERIAUX and choix in MATERIAUX[categorie]:
            cout += MATERIAUX[categorie][choix]["prix_m2"] * surface * 0.3
    return int(cout)


def calculer_cout_base(surface: float, etages: int = 1) -> int:
    """Calcule le coût de base selon la surface et le nombre d'étages."""
    facteur_etage = 1.0 + (etages - 1) * 0.15
    return int(surface * PRIX_M2_BASE * facteur_etage)


def calculer_cout_finition(cout_base: float, niveau_finition: str) -> int:
    """Applique le multiplicateur de finition au coût de base."""
    mult = FINITIONS.get(niveau_finition, {}).get("multiplicateur", 1.0)
    return int(cout_base * mult)


def calculer_cout_options(options: list) -> int:
    """Calcule le coût total des options sélectionnées."""
    total = 0
    for option in options:
        if option in OPTIONS_SUPPLEMENTAIRES:
            total += OPTIONS_SUPPLEMENTAIRES[option]["prix"]
    return total


def calculer_cout_total(
    surface: float,
    etages: int,
    materiaux: dict,
    finition: str,
    options: list,
) -> dict:
    """
    Calcule le coût total du projet avec ventilation détaillée.
    Retourne un dictionnaire avec le détail de chaque poste.
    """
    cout_base = calculer_cout_base(surface, etages)
    cout_mat = calculer_cout_materiaux(surface, materiaux)
    sous_total = cout_base + cout_mat
    cout_fini = calculer_cout_finition(sous_total, finition)
    cout_opt = calculer_cout_options(options)
    total = cout_fini + cout_opt

    return {
        "cout_base": cout_base,
        "cout_materiaux": cout_mat,
        "sous_total_avant_finition": sous_total,
        "cout_apres_finition": cout_fini,
        "cout_options": cout_opt,
        "total": total,
    }


def calculer_cout_par_phase(total: int) -> list:
    """Ventile le coût total par phase de construction."""
    phases = []
    for phase in PHASES_CONSTRUCTION:
        cout_phase = int(total * phase["pourcentage_cout"] / 100)
        phases.append(
            {
                "numero": phase["numero"],
                "nom": phase["nom"],
                "emoji": phase["emoji"],
                "couleur": phase["couleur"],
                "cout": cout_phase,
                "pourcentage": phase["pourcentage_cout"],
                "description": phase["description"],
                "details": phase["details"],
            }
        )
    return phases


def estimer_duree(surface: float, etages: int, options: list) -> dict:
    """
    Estime la durée totale de construction en semaines.
    Retourne le détail par phase.
    """
    facteur_surface = max(1.0, surface / 100)
    facteur_etage = 1.0 + (etages - 1) * 0.2

    phases_durees = []
    total_semaines = 0

    for phase in PHASES_CONSTRUCTION:
        duree = phase["duree_semaines_base"] * facteur_surface * facteur_etage
        # Les études ne dépendent pas beaucoup de la surface
        if phase["numero"] == 1:
            duree = phase["duree_semaines_base"]
        # Les aménagements extérieurs augmentent avec les options
        if phase["numero"] == 8:
            if "Piscine" in options:
                duree += 4
            if "Jardin aménagé" in options:
                duree += 2

        duree = round(duree)
        total_semaines += duree
        phases_durees.append(
            {
                "numero": phase["numero"],
                "nom": phase["nom"],
                "emoji": phase["emoji"],
                "duree_semaines": duree,
            }
        )

    return {
        "phases": phases_durees,
        "total_semaines": total_semaines,
        "total_mois": round(total_semaines / 4.33, 1),
    }


def generer_planning(durees: dict) -> list:
    """
    Génère un planning de construction (diagramme de Gantt).
    Retourne une liste de dictionnaires avec semaine de début et fin.
    """
    planning = []
    semaine_debut = 1

    for phase in durees["phases"]:
        semaine_fin = semaine_debut + phase["duree_semaines"] - 1
        planning.append(
            {
                "nom": f"{phase['emoji']} {phase['nom']}",
                "debut": semaine_debut,
                "fin": semaine_fin,
                "duree": phase["duree_semaines"],
            }
        )
        semaine_debut = semaine_fin + 1

    return planning


def formater_prix(montant: int) -> str:
    """Formate un montant en FCFA avec séparateur de milliers."""
    return f"{montant:,.0f} {DEVISE}".replace(",", " ")
