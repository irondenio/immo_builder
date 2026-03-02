# -*- coding: utf-8 -*-
"""IMMO BUILDER - Page Estimation des Coûts."""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from data.projects import FINITIONS, DEVISE
from utils.calculations import formater_prix


def afficher():
    """Affiche la page d'estimation des coûts."""

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:2rem;">
            <h1>💰 Estimation des Coûts</h1>
            <p style="color:#a0aec0; font-size:1.1rem;">
                Analysez en détail le budget de votre projet et comparez avec votre budget disponible.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Vérifier si un projet a été configuré
    if "projet_couts" not in st.session_state:
        st.info(
            "⬅️ Veuillez d'abord configurer votre projet dans la section "
            "**🛠️ Mon Projet** ou explorer un **🏠 Exemple** pour voir l'estimation détaillée ici."
        )

        st.markdown("---")
        st.markdown("### 📊 Simulation rapide")
        st.markdown("Entrez un budget pour voir ce que vous pouvez construire :")

        budget = st.number_input(
            "💵 Votre budget (FCFA)",
            min_value=5_000_000,
            max_value=500_000_000,
            value=30_000_000,
            step=1_000_000,
            format="%d",
        )

        st.markdown("---")

        from data.projects import PRIX_M2_BASE

        for nom_fin, details in FINITIONS.items():
            prix_m2 = int(PRIX_M2_BASE * details["multiplicateur"])
            surface_possible = int(budget / prix_m2)

            barre_pct = min(100, int(surface_possible / 3))

            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(145deg, #1e1e2f, #2a2a3e);
                    padding: 1rem 1.5rem;
                    border-radius: 12px;
                    margin-bottom: 0.8rem;
                ">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span style="font-size:1.1rem;">{details['emoji']} <strong>{nom_fin}</strong></span>
                            <span style="color:#a0aec0; margin-left:0.5rem;">({formater_prix(prix_m2)}/m²)</span>
                        </div>
                        <div style="
                            color: #2ecc71;
                            font-size: 1.3rem;
                            font-weight: bold;
                        ">≈ {surface_possible} m²</div>
                    </div>
                    <div style="
                        background: #0f0f1a;
                        border-radius: 8px;
                        height: 8px;
                        margin-top: 0.5rem;
                        overflow: hidden;
                    ">
                        <div style="
                            background: linear-gradient(90deg, #e94560, #f39c12);
                            width: {barre_pct}%;
                            height: 100%;
                            border-radius: 8px;
                        "></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            > **💡 Note :** Ces estimations sont approximatives et incluent uniquement
            > la construction de base (hors options et aménagements extérieurs).
            """
        )

        return

    # ================================================================
    # Si un projet existe en session
    # ================================================================
    couts = st.session_state["projet_couts"]
    phases_couts = st.session_state.get("projet_phases_couts", [])
    config = st.session_state.get("projet_config", {})

    # --- KPIs ---
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("🏗️ Construction", formater_prix(couts["cout_base"]))
    k2.metric("🧱 Matériaux", formater_prix(couts["cout_materiaux"]))
    k3.metric("🎨 Finitions", formater_prix(couts["cout_apres_finition"] - couts["sous_total_avant_finition"]))
    k4.metric("⚙️ Options", formater_prix(couts["cout_options"]))

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #0f3460, #1a1a2e);
            padding: 1.5rem;
            border-radius: 16px;
            text-align: center;
            border: 2px solid #2ecc71;
            margin: 1rem 0;
        ">
            <div style="color:#a0aec0; font-size:1rem;">COÛT TOTAL ESTIMÉ</div>
            <div style="color:#2ecc71; font-size:2.5rem; font-weight:bold;">
                {formater_prix(couts['total'])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # --- Comparaison avec budget ---
    st.markdown("### 🎯 Comparaison avec votre budget")

    budget_user = st.number_input(
        "Entrez votre budget disponible (FCFA)",
        min_value=1_000_000,
        max_value=1_000_000_000,
        value=couts["total"],
        step=1_000_000,
        format="%d",
    )

    diff = budget_user - couts["total"]
    if diff >= 0:
        st.success(f"✅ Votre budget est suffisant ! Excédent : **{formater_prix(diff)}**")
    else:
        st.error(f"❌ Budget insuffisant. Il manque : **{formater_prix(abs(diff))}**")

    # Jauge
    pct = min(100, int(budget_user / couts["total"] * 100))
    couleur_jauge = "#2ecc71" if pct >= 100 else "#f39c12" if pct >= 70 else "#e74c3c"

    st.markdown(
        f"""
        <div style="
            background: #0f0f1a;
            border-radius: 10px;
            height: 30px;
            overflow: hidden;
            margin: 1rem 0;
        ">
            <div style="
                background: {couleur_jauge};
                width: {pct}%;
                height: 100%;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
            ">{pct}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # --- Graphiques détaillés ---
    st.markdown("### 📊 Analyse détaillée")

    if phases_couts:
        tab1, tab2 = st.tabs(["📊 Barres", "🍩 Répartition"])

        with tab1:
            fig_bar = go.Figure(
                go.Bar(
                    x=[f"{p['emoji']} {p['nom']}" for p in phases_couts],
                    y=[p["cout"] for p in phases_couts],
                    marker_color=[p["couleur"] for p in phases_couts],
                    text=[formater_prix(p["cout"]) for p in phases_couts],
                    textposition="outside",
                    textfont=dict(color="#a0aec0", size=10),
                )
            )
            fig_bar.update_layout(
                yaxis_title="Coût (FCFA)",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#a0aec0"),
                height=450,
                margin=dict(l=10, r=10, t=10, b=80),
                xaxis_tickangle=-25,
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with tab2:
            fig_pie = go.Figure(
                go.Pie(
                    labels=[p["nom"] for p in phases_couts],
                    values=[p["cout"] for p in phases_couts],
                    marker=dict(colors=[p["couleur"] for p in phases_couts]),
                    hole=0.45,
                    textinfo="label+percent",
                    textfont=dict(size=11),
                )
            )
            fig_pie.update_layout(
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#a0aec0"),
                height=450,
                showlegend=False,
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    # --- Tableau ---
    st.markdown("### 📄 Devis récapitulatif")

    postes = [
        ("🏗️ Construction de base", couts["cout_base"]),
        ("🧱 Matériaux", couts["cout_materiaux"]),
        ("📊 Sous-total", couts["sous_total_avant_finition"]),
        ("🎨 Finitions appliquées", couts["cout_apres_finition"] - couts["sous_total_avant_finition"]),
        ("⚙️ Options supplémentaires", couts["cout_options"]),
    ]

    df = pd.DataFrame(postes, columns=["Poste", "Montant"])
    df["Montant (FCFA)"] = df["Montant"].apply(formater_prix)
    df["% du total"] = df["Montant"].apply(
        lambda x: f"{x / couts['total'] * 100:.1f}%"
    )

    st.dataframe(
        df[["Poste", "Montant (FCFA)", "% du total"]],
        use_container_width=True,
        hide_index=True,
    )

    st.markdown(
        f"""
        <div style="
            background: #1e1e2f;
            padding: 1rem;
            border-radius: 10px;
            text-align: right;
            font-size: 1.2rem;
        ">
            <strong>TOTAL GÉNÉRAL : </strong>
            <span style="color: #2ecc71; font-weight: bold;">
                {formater_prix(couts['total'])}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
