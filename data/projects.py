# -*- coding: utf-8 -*-
"""
IMMO BUILDER - Module de Données
Contient les projets exemples, matériaux, coûts et phases de construction.
"""

import os

# Répertoire de base du projet (parent de data/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _img(relative_path: str) -> str:
    """Convertit un chemin relatif d'image en chemin absolu."""
    return os.path.join(BASE_DIR, relative_path)


# ============================================================================
# PROJETS EXEMPLES
# ============================================================================

PROJETS_EXEMPLES = [
    {
        "id": 1,
        "nom": "Villa Économique",
        "type": "Plain-pied",
        "surface": 80,
        "chambres": 2,
        "salles_de_bain": 1,
        "etages": 1,
        "garage": False,
        "piscine": False,
        "jardin": True,
        "panneau_solaire": False,
        "finition": "Basique",
        "description": (
            "Une villa compacte et fonctionnelle, idéale pour un jeune couple ou une petite famille. "
            "Construction économique avec des matériaux durables et un agencement optimisé pour "
            "maximiser l'espace de vie."
        ),
        "materiaux": {
            "structure": "Parpaing",
            "toiture": "Tôle ondulée",
            "sol": "Carrelage standard",
            "menuiserie": "Aluminium",
        },
        "emoji": "🏡",
        "couleur": "#27ae60",
        "image": _img("assets/villa_economique.png"),
        "pieces": [
            {"nom": "Salon / Salle à manger", "surface": 25},
            {"nom": "Chambre 1", "surface": 14},
            {"nom": "Chambre 2", "surface": 12},
            {"nom": "Cuisine", "surface": 10},
            {"nom": "Salle de bain", "surface": 6},
            {"nom": "Couloir / Entrée", "surface": 5},
            {"nom": "Terrasse", "surface": 8},
        ],
    },
    {
        "id": 2,
        "nom": "Maison Standard",
        "type": "R+1 (2 étages)",
        "surface": 150,
        "chambres": 3,
        "salles_de_bain": 2,
        "etages": 2,
        "garage": True,
        "piscine": False,
        "jardin": True,
        "panneau_solaire": False,
        "finition": "Standard",
        "description": (
            "Une maison familiale confortable à étage offrant un bel espace de vie. "
            "Le rez-de-chaussée accueille les espaces communs tandis que l'étage est dédié "
            "aux chambres et à l'intimité familiale."
        ),
        "materiaux": {
            "structure": "Béton armé",
            "toiture": "Tuiles",
            "sol": "Carrelage premium",
            "menuiserie": "PVC double vitrage",
        },
        "emoji": "🏠",
        "couleur": "#2980b9",
        "image": _img("assets/maison_standard.png"),
        "pieces": [
            {"nom": "Salon", "surface": 30},
            {"nom": "Salle à manger", "surface": 18},
            {"nom": "Cuisine équipée", "surface": 15},
            {"nom": "Chambre parentale + dressing", "surface": 20},
            {"nom": "Chambre 2", "surface": 14},
            {"nom": "Chambre 3", "surface": 14},
            {"nom": "Salle de bain 1", "surface": 8},
            {"nom": "Salle de bain 2", "surface": 6},
            {"nom": "Garage", "surface": 18},
            {"nom": "Terrasse", "surface": 12},
        ],
    },
    {
        "id": 3,
        "nom": "Villa de Luxe",
        "type": "R+1 avec sous-sol",
        "surface": 280,
        "chambres": 5,
        "salles_de_bain": 3,
        "etages": 2,
        "garage": True,
        "piscine": True,
        "jardin": True,
        "panneau_solaire": True,
        "finition": "Premium",
        "description": (
            "Une villa haut de gamme avec des finitions luxueuses. Équipée d'une piscine, "
            "d'un garage double, de panneaux solaires et d'un sous-sol aménageable. "
            "Architecture moderne avec de grands espaces lumineux et des matériaux nobles."
        ),
        "materiaux": {
            "structure": "Béton armé haute résistance",
            "toiture": "Tuiles plates design",
            "sol": "Marbre / Parquet massif",
            "menuiserie": "Aluminium thermolaqué",
        },
        "emoji": "🏰",
        "couleur": "#8e44ad",
        "image": _img("assets/villa_luxe.png"),
        "pieces": [
            {"nom": "Grand salon", "surface": 45},
            {"nom": "Salle à manger", "surface": 25},
            {"nom": "Cuisine américaine équipée", "surface": 22},
            {"nom": "Suite parentale (chambre + SDB + dressing)", "surface": 35},
            {"nom": "Chambre 2 avec SDB", "surface": 20},
            {"nom": "Chambre 3", "surface": 16},
            {"nom": "Chambre 4", "surface": 16},
            {"nom": "Chambre 5 / Bureau", "surface": 14},
            {"nom": "Salle de bain principale", "surface": 12},
            {"nom": "Buanderie", "surface": 8},
            {"nom": "Garage double", "surface": 36},
            {"nom": "Piscine + terrasse", "surface": 40},
            {"nom": "Jardin aménagé", "surface": 60},
        ],
    },
]

# ============================================================================
# PHASES DE CONSTRUCTION
# ============================================================================

PHASES_CONSTRUCTION = [
    {
        "numero": 1,
        "nom": "Études & Autorisations",
        "emoji": "📋",
        "couleur": "#3498db",
        "pourcentage_cout": 5,
        "duree_semaines_base": 4,
        "description": (
            "Étude du sol, plans architecturaux, permis de construire, "
            "étude de faisabilité et démarches administratives."
        ),
        "details": [
            "Étude géotechnique du terrain",
            "Réalisation des plans architecturaux",
            "Dépôt et obtention du permis de construire",
            "Étude de la structure (béton armé)",
            "Plan d'installation du chantier",
        ],
    },
    {
        "numero": 2,
        "nom": "Terrassement & Fondations",
        "emoji": "⛏️",
        "couleur": "#e67e22",
        "pourcentage_cout": 12,
        "duree_semaines_base": 3,
        "description": (
            "Préparation du terrain, excavation, coulage des fondations "
            "et mise en place du soubassement."
        ),
        "details": [
            "Nettoyage et nivellement du terrain",
            "Excavation des fouilles",
            "Coulage du béton de propreté",
            "Ferraillage et coulage des semelles",
            "Réalisation du soubassement (murs de fondation)",
            "Remblaiement et compactage",
        ],
    },
    {
        "numero": 3,
        "nom": "Gros Œuvre",
        "emoji": "🧱",
        "couleur": "#e74c3c",
        "pourcentage_cout": 25,
        "duree_semaines_base": 8,
        "description": (
            "Élévation des murs, réalisation des dalles, poteaux, poutres "
            "et structure porteuse de l'édifice."
        ),
        "details": [
            "Élévation des murs en parpaing / béton",
            "Coulage des poteaux et poutres",
            "Réalisation des dalles (plancher haut)",
            "Construction des escaliers (si étage)",
            "Mise en place des linteaux et chaînages",
            "Réservations pour les réseaux (eau, électricité)",
        ],
    },
    {
        "numero": 4,
        "nom": "Toiture & Charpente",
        "emoji": "🏗️",
        "couleur": "#9b59b6",
        "pourcentage_cout": 10,
        "duree_semaines_base": 3,
        "description": (
            "Installation de la charpente, pose de la couverture "
            "et étanchéité de la toiture."
        ),
        "details": [
            "Réalisation de la charpente (bois ou métallique)",
            "Pose de la couverture (tuiles, tôles, ardoises)",
            "Installation des gouttières et descentes d'eau",
            "Étanchéité de la toiture",
            "Isolation thermique sous toiture",
        ],
    },
    {
        "numero": 5,
        "nom": "Menuiseries Extérieures",
        "emoji": "🪟",
        "couleur": "#1abc9c",
        "pourcentage_cout": 8,
        "duree_semaines_base": 2,
        "description": (
            "Pose des fenêtres, portes extérieures, baies vitrées "
            "et mise hors d'eau / hors d'air du bâtiment."
        ),
        "details": [
            "Pose des fenêtres et baies vitrées",
            "Installation de la porte d'entrée",
            "Pose des portes de service et garage",
            "Volets roulants ou battants",
            "Étanchéité des joints et seuils",
        ],
    },
    {
        "numero": 6,
        "nom": "Réseaux & Second Œuvre",
        "emoji": "🔌",
        "couleur": "#f39c12",
        "pourcentage_cout": 18,
        "duree_semaines_base": 5,
        "description": (
            "Installation de la plomberie, électricité, chauffage/climatisation "
            "et réseaux divers."
        ),
        "details": [
            "Installation de la plomberie (eau chaude/froide, évacuation)",
            "Câblage électrique complet",
            "Pose du tableau électrique",
            "Installation de la climatisation / chauffage",
            "Mise en place des gaines de ventilation",
            "Raccordement aux réseaux publics (eau, électricité, assainissement)",
        ],
    },
    {
        "numero": 7,
        "nom": "Revêtements & Finitions Intérieures",
        "emoji": "🎨",
        "couleur": "#e91e63",
        "pourcentage_cout": 15,
        "duree_semaines_base": 5,
        "description": (
            "Enduits, peinture, carrelage, pose des sanitaires "
            "et finitions intérieures complètes."
        ),
        "details": [
            "Enduit intérieur des murs",
            "Pose du carrelage / parquet / revêtement de sol",
            "Peinture des murs et plafonds",
            "Installation des sanitaires (WC, lavabos, douches, baignoire)",
            "Pose des portes intérieures",
            "Installation de la cuisine équipée",
            "Pose des plinthes et finitions",
        ],
    },
    {
        "numero": 8,
        "nom": "Aménagements Extérieurs",
        "emoji": "🌳",
        "couleur": "#2ecc71",
        "pourcentage_cout": 7,
        "duree_semaines_base": 3,
        "description": (
            "Clôture, allées, jardin, terrasse, piscine (si prévue) "
            "et aménagement de l'espace extérieur."
        ),
        "details": [
            "Construction de la clôture et du portail",
            "Réalisation des allées et accès",
            "Aménagement de la terrasse",
            "Création du jardin (gazon, plantations)",
            "Installation de l'éclairage extérieur",
            "Construction de la piscine (si prévue)",
            "Enduit et peinture de la façade",
        ],
    },
]

# ============================================================================
# MATÉRIAUX DISPONIBLES
# ============================================================================

MATERIAUX = {
    "structure": {
        "Parpaing": {"prix_m2": 35000, "description": "Économique et résistant"},
        "Béton armé": {"prix_m2": 55000, "description": "Solide et durable"},
        "Béton armé haute résistance": {"prix_m2": 75000, "description": "Premium, très solide"},
        "Brique": {"prix_m2": 45000, "description": "Bon isolant thermique"},
    },
    "toiture": {
        "Tôle ondulée": {"prix_m2": 8000, "description": "Économique"},
        "Tuiles": {"prix_m2": 18000, "description": "Esthétique et durable"},
        "Tuiles plates design": {"prix_m2": 28000, "description": "Haut de gamme"},
        "Ardoises": {"prix_m2": 25000, "description": "Élégant et durable"},
    },
    "sol": {
        "Ciment lissé": {"prix_m2": 5000, "description": "Très économique"},
        "Carrelage standard": {"prix_m2": 12000, "description": "Bon rapport qualité/prix"},
        "Carrelage premium": {"prix_m2": 22000, "description": "Haute qualité"},
        "Marbre / Parquet massif": {"prix_m2": 45000, "description": "Luxueux"},
    },
    "menuiserie": {
        "Bois": {"prix_m2": 30000, "description": "Classique et chaleureux"},
        "Aluminium": {"prix_m2": 45000, "description": "Moderne et résistant"},
        "PVC double vitrage": {"prix_m2": 55000, "description": "Excellente isolation"},
        "Aluminium thermolaqué": {"prix_m2": 75000, "description": "Haut de gamme"},
    },
}

# ============================================================================
# NIVEAUX DE FINITION
# ============================================================================

FINITIONS = {
    "Basique": {
        "multiplicateur": 1.0,
        "description": "Finitions fonctionnelles et économiques",
        "details": [
            "Peinture standard",
            "Carrelage basique",
            "Sanitaires simples",
            "Portes en bois standard",
        ],
        "emoji": "⭐",
    },
    "Standard": {
        "multiplicateur": 1.35,
        "description": "Bon rapport qualité / finition",
        "details": [
            "Peinture de qualité avec finitions soignées",
            "Carrelage grès cérame",
            "Sanitaires de marque",
            "Portes en bois laqué",
            "Faux plafonds décoratifs",
        ],
        "emoji": "⭐⭐",
    },
    "Premium": {
        "multiplicateur": 1.85,
        "description": "Finitions haut de gamme et luxueuses",
        "details": [
            "Peinture premium multi-couches",
            "Marbre, parquet massif ou carrelage haut de gamme",
            "Sanitaires design / marque luxe",
            "Menuiseries intérieures sur mesure",
            "Domotique et éclairage design",
            "Cuisine équipée haut de gamme",
        ],
        "emoji": "⭐⭐⭐",
    },
}

# ============================================================================
# OPTIONS SUPPLÉMENTAIRES
# ============================================================================

OPTIONS_SUPPLEMENTAIRES = {
    "Garage simple": {"prix": 2500000, "emoji": "🚗"},
    "Garage double": {"prix": 4500000, "emoji": "🚗🚗"},
    "Piscine": {"prix": 8000000, "emoji": "🏊"},
    "Jardin aménagé": {"prix": 1500000, "emoji": "🌳"},
    "Panneaux solaires": {"prix": 5000000, "emoji": "☀️"},
    "Clôture complète": {"prix": 2000000, "emoji": "🏗️"},
    "Forage d'eau": {"prix": 3000000, "emoji": "💧"},
    "Groupe électrogène": {"prix": 2500000, "emoji": "⚡"},
}

# ============================================================================
# TYPES DE MAISON
# ============================================================================

TYPES_MAISON = {
    "Plain-pied": {"emoji": "🏡", "description": "Maison sur un seul niveau", "image": _img("assets/maison_plainpied.png")},
    "R+1 (2 étages)": {"emoji": "🏠", "description": "Rez-de-chaussée + 1 étage", "image": _img("assets/maison_r1.png")},
    "R+1 avec sous-sol": {"emoji": "🏰", "description": "Sous-sol + RDC + 1 étage", "image": _img("assets/villa_luxe.png")},
    "Duplex": {"emoji": "🏢", "description": "Deux niveaux avec double hauteur", "image": _img("assets/maison_duplex.png")},
}

# ============================================================================
# DEVISE ET PARAMÈTRES
# ============================================================================

DEVISE = "FCFA"
PRIX_M2_BASE = 180000  # Prix de base au m² (construction standard)
