# -*- coding: utf-8 -*-
"""IMMO BUILDER - Page Phases de Construction."""

import streamlit as st
import plotly.graph_objects as go

from data.projects import PHASES_CONSTRUCTION
from utils.calculations import formater_prix


def _creer_gantt(planning: list) -> go.Figure:
    """Crée un diagramme de Gantt simplifié."""
    fig = go.Figure()

    for i, tache in enumerate(reversed(planning)):
        fig.add_trace(
            go.Bar(
                y=[tache["nom"]],
                x=[tache["duree"]],
                base=[tache["debut"] - 1],
                orientation="h",
                marker=dict(
                    color=PHASES_CONSTRUCTION[len(planning) - 1 - i]["couleur"],
                    line=dict(width=0),
                ),
                text=f'{tache["duree"]} sem.',
                textposition="inside",
                textfont=dict(color="white", size=12),
                hovertemplate=(
                    f"<b>{tache['nom']}</b><br>"
                    f"Début : Semaine {tache['debut']}<br>"
                    f"Fin : Semaine {tache['fin']}<br>"
                    f"Durée : {tache['duree']} semaines<extra></extra>"
                ),
                showlegend=False,
            )
        )

    fig.update_layout(
        title="📅 Diagramme de Gantt — Planning de Construction",
        xaxis_title="Semaines",
        barmode="stack",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#a0aec0"),
        height=450,
        margin=dict(l=10, r=10, t=50, b=40),
        xaxis=dict(gridcolor="rgba(255,255,255,0.1)"),
    )
    return fig


def afficher():
    """Affiche la page des phases de construction."""

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:2rem;">
            <h1>📅 Phases de Construction</h1>
            <p style="color:#a0aec0; font-size:1.1rem;">
                Découvrez les 8 étapes clés de la construction de votre maison,
                de la conception à la remise des clés.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Barre de progression globale ---
    st.markdown("### 🔄 Vue d'ensemble")

    # Phase selector
    phase_actuelle = st.slider(
        "Simulez la progression du chantier (phase en cours)",
        min_value=0,
        max_value=8,
        value=0,
        format="Phase %d",
    )

    pct_progress = int(phase_actuelle / 8 * 100)

    st.markdown(
        f"""
        <div style="
            background: #0f0f1a;
            border-radius: 12px;
            height: 40px;
            overflow: hidden;
            margin: 1rem 0;
            position: relative;
        ">
            <div style="
                background: linear-gradient(90deg, #e94560, #f39c12, #2ecc71);
                width: {pct_progress}%;
                height: 100%;
                border-radius: 12px;
                transition: width 0.5s ease;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
                font-size: 1rem;
            ">{pct_progress}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if phase_actuelle == 0:
        st.info("👆 Déplacez le curseur pour simuler la progression du chantier.")
    elif phase_actuelle == 8:
        st.success("🎉 Félicitations ! Votre maison est terminée ! Bienvenue chez vous ! 🏠🔑")
    else:
        phase_en_cours = PHASES_CONSTRUCTION[phase_actuelle - 1]
        st.warning(
            f"🚧 Phase en cours : **{phase_en_cours['emoji']} {phase_en_cours['nom']}** — "
            f"{phase_en_cours['description']}"
        )

    st.markdown("---")

    # --- Détail des 8 phases ---
    st.markdown("### 📋 Les 8 phases détaillées")

    for phase in PHASES_CONSTRUCTION:
        est_terminee = phase["numero"] <= phase_actuelle
        est_en_cours = phase["numero"] == phase_actuelle

        if est_terminee:
            statut_badge = '<span style="background:#2ecc71; color:white; padding:0.2rem 0.6rem; border-radius:20px; font-size:0.8rem;">✅ Terminé</span>'
            border_color = "#2ecc71"
            opacity = "0.85"
        elif est_en_cours:
            statut_badge = '<span style="background:#f39c12; color:white; padding:0.2rem 0.6rem; border-radius:20px; font-size:0.8rem;">🚧 En cours</span>'
            border_color = "#f39c12"
            opacity = "1"
        else:
            statut_badge = '<span style="background:#555; color:#aaa; padding:0.2rem 0.6rem; border-radius:20px; font-size:0.8rem;">⏳ À venir</span>'
            border_color = "#333"
            opacity = "0.6"

        with st.expander(
            f"{phase['emoji']} Phase {phase['numero']} — {phase['nom']}  ({phase['pourcentage_cout']}% du budget)",
            expanded=est_en_cours,
        ):
            st.markdown(
                f"""
                <div style="opacity: {opacity};">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                        <div>
                            <span style="
                                background: {phase['couleur']}22;
                                color: {phase['couleur']};
                                padding: 0.3rem 0.8rem;
                                border-radius: 8px;
                                font-weight: bold;
                            ">⏱️ ~{phase['duree_semaines_base']} semaines</span>
                            <span style="
                                background: #f39c1222;
                                color: #f39c12;
                                padding: 0.3rem 0.8rem;
                                border-radius: 8px;
                                font-weight: bold;
                                margin-left: 0.5rem;
                            ">💰 {phase['pourcentage_cout']}% du budget</span>
                        </div>
                        {statut_badge}
                    </div>
                    <p style="color: #e0e0e0; margin-bottom: 1rem;">
                        {phase['description']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Liste des détails
            for detail in phase["details"]:
                check = "✅" if est_terminee else "🔲"
                st.markdown(f"  {check} {detail}")

    st.markdown("---")

    # --- Diagramme de Gantt ---
    st.markdown("### 📊 Planning de Construction (Gantt)")

    # Construire un planning de base
    planning = []
    debut = 1
    for phase in PHASES_CONSTRUCTION:
        duree = phase["duree_semaines_base"]
        planning.append(
            {
                "nom": f"{phase['emoji']} {phase['nom']}",
                "debut": debut,
                "fin": debut + duree - 1,
                "duree": duree,
            }
        )
        debut += duree

    fig = _creer_gantt(planning)
    st.plotly_chart(fig, use_container_width=True)

    total_semaines = sum(p["duree_semaines_base"] for p in PHASES_CONSTRUCTION)

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
            padding: 1.2rem;
            border-radius: 12px;
            text-align: center;
            margin-top: 1rem;
        ">
            <span style="color:#a0aec0;">Durée totale estimée :</span>
            <span style="color:#f39c12; font-weight:bold; font-size:1.3rem; margin-left:0.5rem;">
                {total_semaines} semaines (~{round(total_semaines / 4.33, 1)} mois)
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        > **💡 Note :** Les durées indiquées sont des estimations de base pour une maison
        > de ~100m². Elles varient selon la surface, le nombre d'étages, les matériaux
        > et les conditions du chantier. Pour une estimation personnalisée,
        > utilisez la section **🛠️ Mon Projet**.
        """
    )
