# -*- coding: utf-8 -*-
"""IMMO BUILDER - Page Exemples de Projets."""

import os
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

from data.projects import PROJETS_EXEMPLES, PHASES_CONSTRUCTION, FINITIONS
from utils.calculations import (
    calculer_cout_total,
    calculer_cout_par_phase,
    estimer_duree,
    formater_prix,
)


def _creer_graphique_cout_phases(phases_couts: list) -> go.Figure:
    """Crée un graphique en barres horizontales des coûts par phase."""
    noms = [f"{p['emoji']} {p['nom']}" for p in phases_couts]
    couts = [p["cout"] for p in phases_couts]
    couleurs = [p["couleur"] for p in phases_couts]

    fig = go.Figure(
        go.Bar(
            y=noms,
            x=couts,
            orientation="h",
            marker_color=couleurs,
            text=[formater_prix(c) for c in couts],
            textposition="auto",
            textfont=dict(color="white", size=11),
        )
    )
    fig.update_layout(
        title="Répartition des coûts par phase",
        xaxis_title="Coût (FCFA)",
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#a0aec0"),
        height=400,
        margin=dict(l=10, r=10, t=40, b=10),
    )
    return fig


def _creer_graphique_camembert(phases_couts: list) -> go.Figure:
    """Crée un camembert de répartition des coûts."""
    noms = [p["nom"] for p in phases_couts]
    couts = [p["cout"] for p in phases_couts]
    couleurs = [p["couleur"] for p in phases_couts]

    fig = go.Figure(
        go.Pie(
            labels=noms,
            values=couts,
            marker=dict(colors=couleurs),
            hole=0.4,
            textinfo="label+percent",
            textfont=dict(size=11),
        )
    )
    fig.update_layout(
        title="Répartition en pourcentage",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#a0aec0"),
        height=400,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
    )
    return fig


def afficher():
    """Affiche la page des exemples de projets."""

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:2rem;">
            <h1>🏠 Exemples de Projets</h1>
            <p style="color:#a0aec0; font-size:1.1rem;">
                Découvrez nos 3 modèles de maisons avec plans détaillés,
                estimations de coûts et planning de construction.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Sélection du projet ---
    cols_select = st.columns(3)
    for i, projet in enumerate(PROJETS_EXEMPLES):
        with cols_select[i]:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                    padding: 1.5rem;
                    border-radius: 16px;
                    text-align: center;
                    border: 2px solid {projet['couleur']}44;
                    min-height: 180px;
                ">
                    <div style="font-size: 3rem;">{projet['emoji']}</div>
                    <h3 style="color: {projet['couleur']};">{projet['nom']}</h3>
                    <p style="color: #a0aec0;">{projet['surface']}m² · {projet['chambres']} ch. · {projet['type']}</p>
                    <span style="
                        background: {projet['couleur']}22;
                        color: {projet['couleur']};
                        padding: 0.3rem 0.8rem;
                        border-radius: 20px;
                        font-size: 0.85rem;
                    ">{projet['finition']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    projet_choisi = st.selectbox(
        "Sélectionnez un projet à explorer :",
        options=[p["nom"] for p in PROJETS_EXEMPLES],
        index=0,
    )

    projet = next(p for p in PROJETS_EXEMPLES if p["nom"] == projet_choisi)

    st.markdown("---")

    # --- Fiche détaillée ---
    st.markdown(f"## {projet['emoji']} {projet['nom']}")
    st.markdown(f"*{projet['description']}*")

    # --- Image de la maison terminée ---
    image_path = projet.get("image", "")
    if image_path and os.path.exists(image_path):
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1rem;
                border-radius: 20px;
                border: 2px solid {projet['couleur']}44;
                margin: 1rem 0;
                text-align: center;
            ">
                <div style="
                    color: {projet['couleur']};
                    font-weight: bold;
                    font-size: 1.1rem;
                    margin-bottom: 0.5rem;
                ">🏠 Aperçu de votre maison terminée</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        img = Image.open(image_path)
        st.image(img, caption=f"Rendu 3D — {projet['nom']} ({projet['surface']}m²)", use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    # Infos principales
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📐 Surface", f"{projet['surface']} m²")
    c2.metric("🛏️ Chambres", projet["chambres"])
    c3.metric("🚿 Salles de bain", projet["salles_de_bain"])
    c4.metric("🏢 Étages", projet["etages"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Options
    opt_col1, opt_col2, opt_col3, opt_col4 = st.columns(4)
    opt_col1.markdown(f"{'✅' if projet['garage'] else '❌'} Garage")
    opt_col2.markdown(f"{'✅' if projet['piscine'] else '❌'} Piscine")
    opt_col3.markdown(f"{'✅' if projet['jardin'] else '❌'} Jardin")
    opt_col4.markdown(f"{'✅' if projet['panneau_solaire'] else '❌'} Panneaux solaires")

    st.markdown("---")

    # --- Matériaux ---
    st.markdown("### 🧱 Matériaux utilisés")
    mat_cols = st.columns(4)
    labels = {"structure": "🏗️ Structure", "toiture": "🏠 Toiture", "sol": "🏡 Sol", "menuiserie": "🪟 Menuiseries"}
    for col, (cat, label) in zip(mat_cols, labels.items()):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: #1e1e2f;
                    padding: 1rem;
                    border-radius: 12px;
                    text-align: center;
                ">
                    <div style="font-size: 0.85rem; color: #a0aec0;">{label}</div>
                    <div style="color: white; font-weight: bold; margin-top: 0.3rem;">
                        {projet['materiaux'].get(cat, 'N/A')}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # --- Distribution des pièces ---
    st.markdown("### 🏠 Distribution des pièces")
    pieces_data = projet.get("pieces", [])
    if pieces_data:
        cols_pieces = st.columns(3)
        for idx, piece in enumerate(pieces_data):
            with cols_pieces[idx % 3]:
                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                        padding: 0.8rem 1rem;
                        border-radius: 10px;
                        margin-bottom: 0.5rem;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                    ">
                        <span style="color: #e0e0e0;">{piece['nom']}</span>
                        <span style="
                            background: {projet['couleur']}33;
                            color: {projet['couleur']};
                            padding: 0.2rem 0.6rem;
                            border-radius: 8px;
                            font-weight: bold;
                        ">{piece['surface']} m²</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.markdown("---")

    # --- Estimation financière ---
    st.markdown("### 💰 Estimation Financière")

    options_list = []
    if projet["garage"]:
        options_list.append("Garage simple")
    if projet["piscine"]:
        options_list.append("Piscine")
    if projet["jardin"]:
        options_list.append("Jardin aménagé")
    if projet["panneau_solaire"]:
        options_list.append("Panneaux solaires")

    couts = calculer_cout_total(
        surface=projet["surface"],
        etages=projet["etages"],
        materiaux=projet["materiaux"],
        finition=projet["finition"],
        options=options_list,
    )

    mc1, mc2, mc3 = st.columns(3)
    mc1.metric("🏗️ Construction", formater_prix(couts["sous_total_avant_finition"]))
    mc2.metric("🎨 Avec finitions", formater_prix(couts["cout_apres_finition"]))
    mc3.metric("💰 **TOTAL**", formater_prix(couts["total"]))

    # Graphiques
    phases_couts = calculer_cout_par_phase(couts["total"])

    graph_col1, graph_col2 = st.columns(2)
    with graph_col1:
        fig_bar = _creer_graphique_cout_phases(phases_couts)
        st.plotly_chart(fig_bar, use_container_width=True)
    with graph_col2:
        fig_pie = _creer_graphique_camembert(phases_couts)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")

    # --- Planning ---
    st.markdown("### 📅 Durée estimée de construction")
    durees = estimer_duree(projet["surface"], projet["etages"], options_list)

    dur1, dur2 = st.columns(2)
    dur1.metric("⏱️ Durée totale", f"{durees['total_semaines']} semaines")
    dur2.metric("📆 Soit environ", f"{durees['total_mois']} mois")

    for phase in durees["phases"]:
        st.markdown(
            f"""
            <div style="
                background: #1e1e2f;
                padding: 0.6rem 1rem;
                border-radius: 8px;
                margin-bottom: 0.4rem;
                display: flex;
                justify-content: space-between;
            ">
                <span>{phase['emoji']} {phase['nom']}</span>
                <span style="color: #f39c12; font-weight: bold;">{phase['duree_semaines']} semaines</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
