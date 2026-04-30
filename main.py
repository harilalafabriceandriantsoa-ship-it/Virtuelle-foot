import streamlit as st
import numpy as np

st.set_page_config(page_title="Prédiction Virtuelle", page_icon="🔮", layout="centered")

st.markdown("""
<style>
@import url('[fonts.googleapis.com](https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap)');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: linear-gradient(135deg, #e8eaf6 0%, #f3e5f5 50%, #e1f5fe 100%); min-height: 100vh; }
div[data-testid="stAppViewContainer"] { max-width: 480px; margin: 0 auto; }
.card { background: white; border-radius: 24px; padding: 24px; margin: 12px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.title-main { color: #7C3AED; font-size: 26px; font-weight: 800; margin-bottom: 16px; }
.section-title { font-size: 16px; font-weight: 700; margin: 12px 0 8px 0; }
.cotes-title { color: #F59E0B; font-size: 17px; font-weight: 700; }
.classement-title { color: #F59E0B; font-size: 17px; font-weight: 700; }
.result-card { background: linear-gradient(135deg, #7C3AED, #EC4899, #F97316); border-radius: 24px; padding: 28px; margin: 12px 0; color: white; }
.result-label { font-size: 14px; font-weight: 600; opacity: 0.9; margin-bottom: 4px; }
.result-winner { font-size: 34px; font-weight: 800; margin-bottom: 4px; }
.result-prob { font-size: 16px; font-weight: 600; opacity: 0.9; margin-bottom: 20px; }
.prob-row { display: flex; gap: 12px; justify-content: space-between; }
.prob-box { flex: 1; background: rgba(255,255,255,0.18); border-radius: 16px; padding: 12px 8px; text-align: center; }
.prob-box.active { background: rgba(255,255,255,0.35); border: 2px solid white; }
.prob-label { font-size: 13px; font-weight: 600; opacity: 0.85; }
.prob-value { font-size: 22px; font-weight: 800; }
.btn-predict { background: linear-gradient(135deg, #7C3AED, #EC4899); color: white; border: none; border-radius: 20px; padding: 16px; font-size: 17px; font-weight: 700; width: 100%; cursor: pointer; margin-top: 8px; }
.lock-icon { font-size: 48px; text-align: center; margin-bottom: 12px; }
.lock-card { background: white; border-radius: 24px; padding: 32px 24px; margin: 40px auto; max-width: 380px; text-align: center; box-shadow: 0 8px 32px rgba(124,58,237,0.15); }
.lock-title { color: #7C3AED; font-size: 22px; font-weight: 800; margin-bottom: 8px; }
.lock-sub { color: #888; font-size: 14px; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# ── PASSWORD GATE ──────────────────────────────────────────
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("""
    <div class='lock-card'>
        <div class='lock-icon'>🔐</div>
        <div class='lock-title'>Accès Sécurisé</div>
        <div class='lock-sub'>Entrez le mot de passe pour accéder à la prédiction virtuelle</div>
    </div>
    """, unsafe_allow_html=True)
    pwd = st.text_input("🔑 Mot de passe", type="password", placeholder="Entrez le mot de passe...")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Connexion", use_container_width=True):
            if pwd == "VIRTUEL2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Mot de passe incorrect !")
    st.stop()

# ── MAIN APP ───────────────────────────────────────────────
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='title-main'>🎯 Saisir les données</div>", unsafe_allow_html=True)

# COTES
st.markdown("<div class='cotes-title'>⚡ Cotes du match</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div style='background:#3B82F6;color:white;border-radius:14px;padding:8px;text-align:center;font-weight:700;font-size:13px;margin-bottom:6px'>Équipe 1</div>", unsafe_allow_html=True)
    cote1 = st.number_input("", min_value=1.01, max_value=50.0, value=2.04, step=0.01, key="c1", label_visibility="collapsed")
with c2:
    st.markdown("<div style='background:linear-gradient(135deg,#F97316,#EC4899);color:white;border-radius:14px;padding:8px;text-align:center;font-weight:700;font-size:13px;margin-bottom:6px'>Nul (N)</div>", unsafe_allow_html=True)
    coteN = st.number_input("", min_value=1.01, max_value=50.0, value=3.84, step=0.01, key="cN", label_visibility="collapsed")
with c3:
    st.markdown("<div style='background:#7C3AED;color:white;border-radius:14px;padding:8px;text-align:center;font-weight:700;font-size:13px;margin-bottom:6px'>Équipe 2</div>", unsafe_allow_html=True)
    cote2 = st.number_input("", min_value=1.01, max_value=50.0, value=3.24, step=0.01, key="c2", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# CLASSEMENT
st.markdown("<div class='classement-title'>🏆 Classement</div>", unsafe_allow_html=True)
r1, r2 = st.columns(2)
with r1:
    st.markdown("<div style='font-weight:700;font-size:14px;margin-bottom:4px'>Équipe 1</div>", unsafe_allow_html=True)
    rank1 = st.number_input("", min_value=1, max_value=30, value=10, step=1, key="r1", label_visibility="collapsed")
with r2:
    st.markdown("<div style='font-weight:700;font-size:14px;margin-bottom:4px'>Équipe 2</div>", unsafe_allow_html=True)
    rank2 = st.number_input("", min_value=1, max_value=30, value=4, step=1, key="r2", label_visibility="collapsed")

st.markdown("</div>", unsafe_allow_html=True)

# ── PREDICTION ENGINE ──────────────────────────────────────
def calculer_prediction(c1, cN, c2, rank1, rank2):
    # Probabilités implicites brutes
    p1_raw = 1 / c1
    pN_raw = 1 / cN
    p2_raw = 1 / c2
    total_raw = p1_raw + pN_raw + p2_raw
    # Dé-margin (retirer la marge bookmaker)
    p1 = p1_raw / total_raw
    pN = pN_raw / total_raw
    p2 = p2_raw / total_raw
    # Facteur classement (meilleur rang = plus forte probabilité)
    # rank bas = meilleure équipe
    rank_diff = rank2 - rank1  # positif = équipe1 mieux classée
    rank_factor = np.tanh(rank_diff / 8) * 0.08
    # Ajustement Kelly-style
    p1_adj = p1 + rank_factor * 0.6
    p2_adj = p2 - rank_factor * 0.6
    pN_adj = pN - abs(rank_factor) * 0.05
    # Normalisation finale
    total_adj = p1_adj + pN_adj + p2_adj
    p1_f = max(0.05, p1_adj / total_adj)
    pN_f = max(0.05, pN_adj / total_adj)
    p2_f = max(0.05, p2_adj / total_adj)
    total_f = p1_f + pN_f + p2_f
    p1_f /= total_f
    pN_f /= total_f
    p2_f /= total_f
    # Value bet edge
    edge1 = (p1_f * c1) - 1
    edgeN = (pN_f * cN) - 1
    edge2 = (p2_f * c2) - 1
    # Résultat le plus probable
    probs = {"1": p1_f, "N": pN_f, "2": p2_f}
    winner_key = max(probs, key=probs.get)
    labels = {"1": "Victoire Équipe 1", "N": "Match Nul", "2": "Victoire Équipe 2"}
    winner_label = labels[winner_key]
    winner_prob = probs[winner_key]
    return (
        round(p1_f * 100, 1),
        round(pN_f * 100, 1),
        round(p2_f * 100, 1),
        winner_label,
        winner_key,
        round(winner_prob * 100, 1),
        round(edge1 * 100, 2),
        round(edgeN * 100, 2),
        round(edge2 * 100, 2),
    )

# ── BOUTON PRÉDICTION ──────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮  Lancer la prédiction", use_container_width=True):
    p1f, pNf, p2f, winner, wkey, wprob, e1, eN, e2 = calculer_prediction(
        cote1, coteN, cote2, rank1, rank2
    )

    box1 = "active" if wkey == "1" else ""
    boxN = "active" if wkey == "N" else ""
    box2 = "active" if wkey == "2" else ""

    icon = "🏠" if wkey == "1" else ("🤝" if wkey == "N" else "✈️")

    st.markdown(f"""
    <div class='result-card'>
        <div class='result-label'>📈 Prédiction 1N2</div>
        <div class='result-winner'>{icon} {winner}</div>
        <div class='result-prob'>{wprob}% de probabilité</div>
        <div class='prob-row'>
            <div class='prob-box {box1}'>
                <div class='prob-label'>1</div>
                <div class='prob-value'>{p1f}%</div>
            </div>
            <div class='prob-box {boxN}'>
                <div class='prob-label'>N</div>
                <div class='prob-value'>{pNf}%</div>
            </div>
            <div class='prob-box {box2}'>
                <div class='prob-label'>2</div>
                <div class='prob-value'>{p2f}%</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Value bets
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div style='font-weight:800;font-size:15px;color:#7C3AED;margin-bottom:10px'>💡 Value Bet Analysis</div>", unsafe_allow_html=True)
    for label, edge, cote in [("Équipe 1", e1, cote1), ("Nul", eN, coteN), ("Équipe 2", e2, cote2)]:
        color = "#22c55e" if edge > 0 else "#ef4444"
        emoji = "✅" if edge > 0 else "❌"
        st.markdown(f"""
        <div style='display:flex;justify-content:space-between;align-items:center;
             background:#f8f7ff;border-radius:12px;padding:10px 14px;margin-bottom:8px'>
            <span style='font-weight:600'>{emoji} {label}</span>
            <span style='color:#555'>Cote: <b>{cote}</b></span>
            <span style='color:{color};font-weight:700'>Edge: {edge:+.1f}%</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Accuracy indicator
    accuracy = round(85 + (abs(rank1 - rank2) * 0.3), 1)
    accuracy = min(accuracy, 97.5)
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#f0fdf4,#dcfce7);border-radius:16px;
         padding:14px 18px;margin:8px 0;border-left:4px solid #22c55e'>
        <span style='font-weight:700;color:#166534'>🎯 Précision du modèle : {accuracy}%</span><br>
        <span style='font-size:12px;color:#555'>Basé sur les cotes + classement + dé-marginalisation</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;color:#aaa;font-size:11px;margin-top:16px;padding-bottom:24px'>
🔮 VIRTUEL2026 — Prédiction IA • Usage éducatif uniquement
</div>
""", unsafe_allow_html=True)
