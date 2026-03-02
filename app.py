# -*- coding: utf-8 -*-
"""
🏗️ IMMO BUILDER — Application principale
Votre assistant intelligent pour construire la maison de vos rêves.
"""

import streamlit as st
import sys
import os

# Ajouter le répertoire racine au path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_DIR)

from views import accueil, exemples, personnalise, estimation, phases


# ============================================================================
# CONFIGURATION DE LA PAGE
# ============================================================================

st.set_page_config(
    page_title="IMMO BUILDER — Construction de maisons",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================================
# STYLES CSS PERSONNALISÉS
# ============================================================================

st.markdown(
    """
    <style>
        /* ---- Thème sombre premium ---- */
        .stApp {
            background: linear-gradient(180deg, #0a0a1a 0%, #121225 100%);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f0f2a, #1a1a35) !important;
            border-right: 1px solid rgba(233, 69, 96, 0.2);
        }
        section[data-testid="stSidebar"] .stMarkdown h1,
        section[data-testid="stSidebar"] .stMarkdown h2,
        section[data-testid="stSidebar"] .stMarkdown h3 {
            color: #e94560 !important;
        }

        /* Titres */
        h1 { color: #e94560 !important; }
        h2, h3 { color: #f0f0f0 !important; }
        h4 { color: #f39c12 !important; }

        /* Métriques */
        div[data-testid="stMetricValue"] {
            color: #2ecc71 !important;
            font-weight: bold;
        }
        div[data-testid="stMetricDelta"] {
            color: #a0aec0 !important;
        }

        /* Boutons radio sidebar */
        .stRadio > div {
            gap: 0.3rem;
        }
        .stRadio > div > label {
            background: rgba(255,255,255,0.03);
            padding: 0.7rem 1rem;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.06);
            transition: all 0.2s ease;
        }
        .stRadio > div > label:hover {
            background: rgba(233, 69, 96, 0.1);
            border-color: rgba(233, 69, 96, 0.3);
        }

        /* Expander */
        .streamlit-expanderHeader {
            background: #1e1e2f !important;
            border-radius: 10px;
        }

        /* Selectbox */
        .stSelectbox > div > div {
            background: #1e1e2f;
            border: 1px solid #333;
        }

        /* Slider */
        .stSlider > div > div > div {
            color: #e94560;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab"] {
            background: #1e1e2f;
            border-radius: 8px 8px 0 0;
            color: #a0aec0;
        }
        .stTabs [aria-selected="true"] {
            background: #e94560 !important;
            color: white !important;
        }

        /* DataFrame */
        .stDataFrame {
            border: 1px solid #333;
            border-radius: 10px;
        }

        /* Footer hide */
        footer { visibility: hidden; }
        #MainMenu { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================================
# SIDEBAR — NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding: 1rem 0;">
            <div style="font-size: 3rem;">🏗️</div>
            <h1 style="
                font-size: 1.8rem;
                background: linear-gradient(90deg, #e94560, #f39c12);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin: 0;
            ">IMMO BUILDER</h1>
            <p style="color: #a0aec0; font-size: 0.85rem; margin-top: 0.3rem;">
                Du plan à la maison terminée
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    page = st.radio(
        "📍 Navigation",
        options=[
            "🏠 Accueil",
            "📋 Exemples de Projets",
            "🛠️ Mon Projet",
            "💰 Estimation des Coûts",
            "📅 Phases de Construction",
        ],
        index=0,
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            background: rgba(233, 69, 96, 0.1);
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(233, 69, 96, 0.2);
        ">
            <div style="color: #e94560; font-weight: bold; margin-bottom: 0.5rem;">
                💡 Conseil
            </div>
            <div style="color: #a0aec0; font-size: 0.85rem;">
                Commencez par explorer les <strong>exemples</strong>,
                puis créez <strong>votre projet</strong> personnalisé
                pour obtenir une estimation précise.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; color: #555; font-size: 0.75rem;">
            IMMO BUILDER v1.0<br>
            © 2026 — Tous droits réservés
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================================
# ROUTAGE — AFFICHAGE DE LA PAGE SÉLECTIONNÉE
# ============================================================================

if page == "🏠 Accueil":
    accueil.afficher()
elif page == "📋 Exemples de Projets":
    exemples.afficher()
elif page == "🛠️ Mon Projet":
    personnalise.afficher()
elif page == "💰 Estimation des Coûts":
    estimation.afficher()
elif page == "📅 Phases de Construction":
    phases.afficher()
