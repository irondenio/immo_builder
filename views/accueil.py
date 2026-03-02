# -*- coding: utf-8 -*-
"""IMMO BUILDER - Page d'Accueil."""

import streamlit as st


def afficher():
    """Affiche la page d'accueil de l'application."""

    # --- Hero Section ---
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            padding: 3rem 2rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        ">
            <h1 style="
                font-size: 3rem;
                background: linear-gradient(90deg, #e94560, #f39c12, #e94560);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
            ">🏗️ IMMO BUILDER</h1>
            <p style="
                color: #a0aec0;
                font-size: 1.25rem;
                max-width: 700px;
                margin: 0 auto 1.5rem;
            ">
                Votre assistant intelligent pour construire la maison de vos rêves,
                du plan architectural à la remise des clés.
            </p>
            <div style="
                display: flex;
                justify-content: center;
                gap: 1rem;
                flex-wrap: wrap;
            ">
                <span style="
                    background: rgba(233, 69, 96, 0.2);
                    color: #e94560;
                    padding: 0.5rem 1rem;
                    border-radius: 50px;
                    font-size: 0.9rem;
                ">📐 Plans détaillés</span>
                <span style="
                    background: rgba(243, 156, 18, 0.2);
                    color: #f39c12;
                    padding: 0.5rem 1rem;
                    border-radius: 50px;
                    font-size: 0.9rem;
                ">💰 Estimations précises</span>
                <span style="
                    background: rgba(46, 204, 113, 0.2);
                    color: #2ecc71;
                    padding: 0.5rem 1rem;
                    border-radius: 50px;
                    font-size: 0.9rem;
                ">📅 Planning complet</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Comment ça marche ---
    st.markdown("## 🚀 Comment ça marche ?")
    st.markdown("---")

    cols = st.columns(4)
    etapes = [
        ("1️⃣", "Choisissez", "Sélectionnez un projet exemple ou créez le vôtre", "#e94560"),
        ("2️⃣", "Configurez", "Définissez la surface, les matériaux et finitions", "#f39c12"),
        ("3️⃣", "Estimez", "Obtenez une estimation détaillée des coûts", "#3498db"),
        ("4️⃣", "Planifiez", "Visualisez le planning phase par phase", "#2ecc71"),
    ]

    for col, (num, titre, desc, couleur) in zip(cols, etapes):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                    padding: 1.5rem;
                    border-radius: 16px;
                    text-align: center;
                    border: 1px solid {couleur}33;
                    min-height: 200px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                ">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{num}</div>
                    <h3 style="color: {couleur}; margin-bottom: 0.5rem;">{titre}</h3>
                    <p style="color: #a0aec0; font-size: 0.9rem;">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Fonctionnalités ---
    st.markdown("## ✨ Fonctionnalités")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1.5rem;
                border-radius: 16px;
                margin-bottom: 1rem;
                border-left: 4px solid #e94560;
            ">
                <h4>🏠 Projets Exemples</h4>
                <p style="color: #a0aec0;">
                    Explorez 3 projets prédéfinis : Villa Économique (80m²),
                    Maison Standard (150m²) et Villa de Luxe (280m²).
                    Chacun avec des détails complets.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1.5rem;
                border-radius: 16px;
                margin-bottom: 1rem;
                border-left: 4px solid #3498db;
            ">
                <h4>💰 Estimation des Coûts</h4>
                <p style="color: #a0aec0;">
                    Calcul précis du budget par poste et par phase,
                    avec graphiques interactifs et comparaison budgétaire.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1.5rem;
                border-radius: 16px;
                margin-bottom: 1rem;
                border-left: 4px solid #f39c12;
            ">
                <h4>🛠️ Projet Personnalisé</h4>
                <p style="color: #a0aec0;">
                    Configurez votre propre maison : type, surface, nombre de pièces,
                    matériaux, finitions et options supplémentaires.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="
                background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                padding: 1.5rem;
                border-radius: 16px;
                margin-bottom: 1rem;
                border-left: 4px solid #2ecc71;
            ">
                <h4>📅 Phases de Construction</h4>
                <p style="color: #a0aec0;">
                    Suivez les 8 étapes de construction avec un diagramme de Gantt,
                    de la conception à la remise des clés.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- Statistiques ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 📊 En quelques chiffres")
    st.markdown("---")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projets Exemples", "3", "Éco / Standard / Luxe")
    m2.metric("Phases détaillées", "8", "Étude → Finitions")
    m3.metric("Matériaux", "16+", "4 catégories")
    m4.metric("Options", "8", "Garage, Piscine…")
