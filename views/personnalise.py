# -*- coding: utf-8 -*-
"""IMMO BUILDER - Page Projet Personnalisé."""

import os
import streamlit as st
from PIL import Image

from data.projects import (
    TYPES_MAISON,
    MATERIAUX,
    FINITIONS,
    OPTIONS_SUPPLEMENTAIRES,
)
from utils.calculations import (
    calculer_cout_total,
    calculer_cout_par_phase,
    estimer_duree,
    generer_planning,
    formater_prix,
)


def afficher():
    """Affiche la page de configuration personnalisée."""

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:2rem;">
            <h1>🛠️ Mon Projet Personnalisé</h1>
            <p style="color:#a0aec0; font-size:1.1rem;">
                Configurez votre maison idéale et obtenez une estimation instantanée.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ================================================================
    # SECTION 1 : Configuration de base
    # ================================================================
    st.markdown("### 📐 Configuration de base")

    col1, col2 = st.columns(2)

    with col1:
        type_maison = st.selectbox(
            "Type de maison",
            options=list(TYPES_MAISON.keys()),
            format_func=lambda x: f"{TYPES_MAISON[x]['emoji']} {x} — {TYPES_MAISON[x]['description']}",
        )

        surface = st.slider(
            "Surface habitable (m²)",
            min_value=40,
            max_value=500,
            value=120,
            step=10,
        )

        chambres = st.slider("Nombre de chambres", 1, 8, 3)

    with col2:
        etages = st.selectbox("Nombre d'étages", [1, 2, 3], index=0)

        salles_de_bain = st.slider("Nombre de salles de bain", 1, 5, 2)

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1rem;
                border-radius: 12px;
                text-align: center;
                margin-top: 0.5rem;
            ">
                <div style="color: #a0aec0;">Surface par pièce (moyenne)</div>
                <div style="color: #e94560; font-size: 1.5rem; font-weight: bold;">
                    {surface // (chambres + salles_de_bain + 2)} m²
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ================================================================
    # SECTION 2 : Matériaux
    # ================================================================
    st.markdown("### 🧱 Choix des matériaux")

    mat_col1, mat_col2 = st.columns(2)

    with mat_col1:
        struct = st.selectbox(
            "🏗️ Structure / Murs",
            options=list(MATERIAUX["structure"].keys()),
            format_func=lambda x: f"{x} — {MATERIAUX['structure'][x]['description']}",
        )

        toiture = st.selectbox(
            "🏠 Toiture",
            options=list(MATERIAUX["toiture"].keys()),
            format_func=lambda x: f"{x} — {MATERIAUX['toiture'][x]['description']}",
        )

    with mat_col2:
        sol = st.selectbox(
            "🏡 Revêtement de sol",
            options=list(MATERIAUX["sol"].keys()),
            format_func=lambda x: f"{x} — {MATERIAUX['sol'][x]['description']}",
        )

        menuiserie = st.selectbox(
            "🪟 Menuiseries",
            options=list(MATERIAUX["menuiserie"].keys()),
            format_func=lambda x: f"{x} — {MATERIAUX['menuiserie'][x]['description']}",
        )

    materiaux_choisis = {
        "structure": struct,
        "toiture": toiture,
        "sol": sol,
        "menuiserie": menuiserie,
    }

    st.markdown("---")

    # ================================================================
    # SECTION 3 : Finitions
    # ================================================================
    st.markdown("### 🎨 Niveau de finition")

    fin_cols = st.columns(3)
    for col, (nom, details) in zip(fin_cols, FINITIONS.items()):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                    padding: 1.2rem;
                    border-radius: 14px;
                    min-height: 220px;
                ">
                    <div style="text-align:center; margin-bottom: 0.5rem;">
                        <span style="font-size:1.3rem;">{details['emoji']}</span>
                        <h4 style="margin:0.3rem 0;">{nom}</h4>
                    </div>
                    <p style="color: #a0aec0; font-size: 0.85rem;">{details['description']}</p>
                    <ul style="color: #a0aec0; font-size: 0.8rem; padding-left: 1.2rem;">
                        {''.join(f'<li>{d}</li>' for d in details['details'][:4])}
                    </ul>
                    <div style="text-align:center; color:#f39c12; font-weight:bold;">
                        ×{details['multiplicateur']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    finition = st.selectbox(
        "Choisissez votre niveau de finition",
        options=list(FINITIONS.keys()),
        index=1,
    )

    st.markdown("---")

    # ================================================================
    # SECTION 4 : Options supplémentaires
    # ================================================================
    st.markdown("### ⚙️ Options supplémentaires")

    options_choisies = []
    opt_cols = st.columns(4)
    for idx, (nom, details) in enumerate(OPTIONS_SUPPLEMENTAIRES.items()):
        with opt_cols[idx % 4]:
            if st.checkbox(
                f"{details['emoji']} {nom}",
                key=f"opt_{nom}",
            ):
                options_choisies.append(nom)

    st.markdown("---")

    # ================================================================
    # SECTION 5 : Récapitulatif et Résultats
    # ================================================================
    st.markdown("### 📊 Récapitulatif de votre projet")

    # Calculer
    couts = calculer_cout_total(
        surface=surface,
        etages=etages,
        materiaux=materiaux_choisis,
        finition=finition,
        options=options_choisies,
    )

    durees = estimer_duree(surface, etages, options_choisies)

    # Récap visuel
    recap_col1, recap_col2 = st.columns(2)

    with recap_col1:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1.5rem;
                border-radius: 16px;
                border-left: 4px solid #e94560;
            ">
                <h4 style="color: #e94560;">🏠 Votre Maison</h4>
                <table style="width:100%; color: #e0e0e0;">
                    <tr><td>Type</td><td style="text-align:right; font-weight:bold;">{type_maison}</td></tr>
                    <tr><td>Surface</td><td style="text-align:right; font-weight:bold;">{surface} m²</td></tr>
                    <tr><td>Chambres</td><td style="text-align:right; font-weight:bold;">{chambres}</td></tr>
                    <tr><td>Salles de bain</td><td style="text-align:right; font-weight:bold;">{salles_de_bain}</td></tr>
                    <tr><td>Étages</td><td style="text-align:right; font-weight:bold;">{etages}</td></tr>
                    <tr><td>Finition</td><td style="text-align:right; font-weight:bold;">{finition}</td></tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with recap_col2:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(145deg, #0f3460, #1a1a2e);
                padding: 1.5rem;
                border-radius: 16px;
                border: 2px solid #f39c12;
                text-align: center;
            ">
                <h4 style="color: #f39c12;">💰 Coût Total Estimé</h4>
                <div style="
                    font-size: 2rem;
                    font-weight: bold;
                    color: #2ecc71;
                    margin: 1rem 0;
                ">{formater_prix(couts['total'])}</div>
                <div style="color: #a0aec0; font-size: 0.9rem;">
                    Construction : {formater_prix(couts['cout_base'])}<br>
                    Matériaux : {formater_prix(couts['cout_materiaux'])}<br>
                    Finitions (×{FINITIONS[finition]['multiplicateur']}) : {formater_prix(couts['cout_apres_finition'] - couts['sous_total_avant_finition'])}<br>
                    Options : {formater_prix(couts['cout_options'])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Image de la maison terminée ---
    image_path = TYPES_MAISON.get(type_maison, {}).get("image", "")
    if image_path and os.path.exists(image_path):
        st.markdown("### 🏠 Aperçu de votre maison terminée")
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1rem;
                border-radius: 20px;
                border: 2px solid #e9456044;
                margin-bottom: 1rem;
                text-align: center;
            ">
                <div style="
                    color: #e94560;
                    font-weight: bold;
                    font-size: 1.1rem;
                ">🌟 Rendu 3D de votre future maison</div>
                <div style="color: #a0aec0; font-size: 0.85rem;">Voici à quoi pourrait ressembler votre habitation une fois terminée</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        img = Image.open(image_path)
        st.image(img, caption=f"Rendu 3D — {type_maison} ({surface}m², finition {finition})", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Durée ---
    dur1, dur2, dur3 = st.columns(3)
    dur1.metric("⏱️ Durée totale", f"{durees['total_semaines']} semaines")
    dur2.metric("📆 Soit environ", f"{durees['total_mois']} mois")
    dur3.metric("💵 Coût / m²", formater_prix(int(couts["total"] / surface)))

    st.markdown("---")

    # --- Détail des coûts par phase ---
    st.markdown("### 📋 Détail par phase de construction")

    phases_couts = calculer_cout_par_phase(couts["total"])

    import plotly.graph_objects as go

    # Graphique en barres
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=[f"{p['emoji']} {p['nom']}" for p in phases_couts],
            y=[p["cout"] for p in phases_couts],
            marker_color=[p["couleur"] for p in phases_couts],
            text=[formater_prix(p["cout"]) for p in phases_couts],
            textposition="outside",
            textfont=dict(color="#a0aec0", size=10),
        )
    )
    fig.update_layout(
        title="Coût estimé par phase de construction",
        yaxis_title="Coût (FCFA)",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#a0aec0"),
        height=450,
        margin=dict(l=10, r=10, t=40, b=80),
        xaxis_tickangle=-25,
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Tableau de synthèse ---
    st.markdown("### 📄 Tableau de synthèse")
    import pandas as pd

    df = pd.DataFrame(
        {
            "Phase": [f"{p['emoji']} {p['nom']}" for p in phases_couts],
            "Coût (FCFA)": [formater_prix(p["cout"]) for p in phases_couts],
            "Pourcentage": [f"{p['pourcentage']}%" for p in phases_couts],
            "Durée (sem.)": [
                d["duree_semaines"]
                for d in durees["phases"]
            ],
        }
    )
    st.dataframe(df, use_container_width=True, hide_index=True)
