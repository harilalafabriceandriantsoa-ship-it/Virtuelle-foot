import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import json

st.set_page_config(
    page_title="⚽ VIRTUEL FOOTBALL 2026",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 ULTRA STYLING
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }
    
    /* BACKGROUND GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        min-height: 100vh;
    }
    
    body { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%) !important; }
    
    /* CONTAINER */
    div[data-testid="stAppViewContainer"] {
        max-width: 520px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* CARDS */
    .card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(226, 232, 240, 0.1);
        border-radius: 24px;
        padding: 28px;
        margin: 16px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }
    
    .card-highlight {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
        border: 1px solid rgba(168, 85, 247, 0.3);
    }
    
    .card-danger {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05));
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    .card-success {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(34, 197, 94, 0.05));
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    
    /* TITLES */
    .title-main {
        color: #06b6d4;
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 8px;
        text-align: center;
        text-shadow: 0 4px 12px rgba(6, 182, 212, 0.3);
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 14px;
        text-align: center;
        margin-bottom: 24px;
        font-weight: 500;
    }
    
    .section-title {
        color: #f1f5f9;
        font-size: 16px;
        font-weight: 800;
        margin: 20px 0 12px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .sub-section {
        color: #cbd5e1;
        font-size: 13px;
        font-weight: 600;
        margin: 12px 0 8px 0;
        opacity: 0.9;
    }
    
    /* INPUT STYLING */
    .stNumberInput > label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }
    
    .stNumberInput input {
        background: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        color: #06b6d4 !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }
    
    .stNumberInput input:focus {
        border: 1px solid rgba(6, 182, 212, 0.6) !important;
        box-shadow: 0 0 12px rgba(6, 182, 212, 0.3) !important;
    }
    
    /* RESULT CARD */
    .result-card {
        background: linear-gradient(135deg, #06b6d4, #0891b2, #06b6d4);
        border-radius: 24px;
        padding: 32px 28px;
        margin: 20px 0;
        color: white;
        box-shadow: 0 20px 60px rgba(6, 182, 212, 0.4);
        animation: slideIn 0.6s ease-out;
    }
    
    .result-card.green {
        background: linear-gradient(135deg, #34d399, #10b981, #34d399);
        box-shadow: 0 20px 60px rgba(52, 211, 153, 0.4);
    }
    
    .result-card.red {
        background: linear-gradient(135deg, #f87171, #ef4444, #f87171);
        box-shadow: 0 20px 60px rgba(239, 68, 68, 0.4);
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .result-label {
        font-size: 13px;
        font-weight: 700;
        opacity: 0.9;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .result-winner {
        font-size: 42px;
        font-weight: 900;
        margin: 8px 0;
        line-height: 1.1;
    }
    
    .result-prob {
        font-size: 18px;
        font-weight: 700;
        opacity: 0.95;
        margin-bottom: 20px;
    }
    
    .result-score {
        font-size: 48px;
        font-weight: 900;
        text-align: center;
        margin: 12px 0;
        font-family: 'Courier New', monospace;
        letter-spacing: 2px;
    }
    
    .result-score-small {
        font-size: 14px;
        opacity: 0.85;
        text-align: center;
        margin-top: 8px;
    }
    
    /* PROBABILITY BOXES */
    .prob-row {
        display: flex;
        gap: 14px;
        justify-content: space-between;
        margin-top: 16px;
    }
    
    .prob-box {
        flex: 1;
        background: rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 14px 10px;
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .prob-box:hover {
        background: rgba(255, 255, 255, 0.18);
        transform: translateY(-2px);
    }
    
    .prob-box.active {
        background: rgba(255, 255, 255, 0.25);
        border: 2px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    
    .prob-label {
        font-size: 13px;
        font-weight: 700;
        opacity: 0.85;
        margin-bottom: 4px;
        text-transform: uppercase;
    }
    
    .prob-value {
        font-size: 26px;
        font-weight: 900;
    }
    
    /* POINTS BREAKDOWN */
    .points-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-top: 14px;
    }
    
    .points-box {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 12px;
        padding: 12px;
        text-align: center;
    }
    
    .points-label {
        font-size: 12px;
        opacity: 0.8;
        margin-bottom: 4px;
    }
    
    .points-value {
        font-size: 24px;
        font-weight: 900;
    }
    
    /* BUTTONS */
    .stButton > button {
        background: linear-gradient(135deg, #06b6d4, #0891b2) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 16px 24px !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        width: 100% !important;
        margin-top: 12px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 20px rgba(6, 182, 212, 0.3) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #0891b2, #06b6d4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 28px rgba(6, 182, 212, 0.5) !important;
    }
    
    /* LOCK SCREEN */
    .lock-card {
        background: rgba(30, 41, 59, 0.9);
        border: 1px solid rgba(168, 85, 247, 0.3);
        border-radius: 28px;
        padding: 48px 32px;
        margin: 60px auto;
        max-width: 400px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(168, 85, 247, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .lock-icon { font-size: 64px; margin-bottom: 20px; }
    
    .lock-title {
        color: #06b6d4;
        font-size: 28px;
        font-weight: 900;
        margin-bottom: 12px;
    }
    
    .lock-sub {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 28px;
        font-weight: 500;
    }
    
    /* VALUE BET */
    .value-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(30, 41, 59, 0.6);
        border-radius: 14px;
        padding: 12px 16px;
        margin-bottom: 10px;
        border: 1px solid rgba(148, 163, 184, 0.1);
        transition: all 0.3s ease;
    }
    
    .value-row:hover {
        background: rgba(30, 41, 59, 0.8);
        border-color: rgba(148, 163, 184, 0.2);
    }
    
    .value-label { font-weight: 700; color: #f1f5f9; }
    .value-cote { color: #94a3b8; font-weight: 600; }
    .value-edge { font-weight: 800; }
    .value-positive { color: #34d399; }
    .value-negative { color: #f87171; }
    
    /* ACCURACY */
    .accuracy-box {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(52, 211, 153, 0.15));
        border: 2px solid rgba(34, 197, 94, 0.4);
        border-radius: 16px;
        padding: 16px 20px;
        margin: 16px 0;
        color: #86efac;
    }
    
    .accuracy-title { font-weight: 800; font-size: 15px; }
    .accuracy-sub { font-size: 12px; color: #a7f3d0; margin-top: 6px; opacity: 0.9; }
    
    /* FOOTER */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        margin-top: 28px;
        padding-bottom: 20px;
        opacity: 0.8;
    }
    
    /* MATCH INFO */
    .match-info {
        background: rgba(99, 102, 241, 0.1);
        border-left: 4px solid #6366f1;
        border-radius: 12px;
        padding: 14px 16px;
        margin: 12px 0;
        color: #c7d2fe;
    }
    
    .match-info-title { font-weight: 700; margin-bottom: 6px; }
    .match-info-text { font-size: 13px; }
    
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 🔐 AUTHENTICATION
# ═══════════════════════════════════════════════════════════════════════════════
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("""
    <div class='lock-card'>
        <div class='lock-icon'>🔐</div>
        <div class='lock-title'>VIRTUEL FOOTBALL 2026</div>
        <div class='lock-sub'>Prédiction IA Ultra-Précise • Accès Sécurisé</div>
    </div>
    """, unsafe_allow_html=True)
    
    pwd = st.text_input("🔑 MOT DE PASSE", type="password", placeholder="Entrez le code d'accès...")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ CONNEXION", use_container_width=True):
            if pwd == "VIRTUEL2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Accès refusé")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# 📊 ADVANCED PREDICTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_advanced_prediction(cote1, coteN, cote2, rank1, rank2, form1, form2, home_advantage=True):
    """
    Ultra-advanced prediction algorithm avec exact scores
    """
    
    # ▶ DÉMARGINALIZATION (retirer marge bookmaker)
    p1_raw = 1 / cote1
    pN_raw = 1 / coteN
    p2_raw = 1 / cote2
    total_raw = p1_raw + pN_raw + p2_raw
    
    p1_base = p1_raw / total_raw
    pN_base = pN_raw / total_raw
    p2_base = p2_raw / total_raw
    
    # ▶ RANKING FACTOR (classement des équipes)
    rank_diff = rank2 - rank1  # positif = équipe1 mieux classée
    rank_factor = np.tanh(rank_diff / 10) * 0.12
    
    # ▶ FORM FACTOR (forme récente)
    form_
    
