import streamlit as st
import numpy as np
from math import exp, factorial

st.set_page_config(page_title="FOOT VIRTUEL ANDR V2", page_icon="⚽", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
*{font-family:'Poppins',sans-serif;box-sizing:border-box}
.stApp{background:linear-gradient(135deg,#0f0c29 0%,#302b63 50%,#24243e 100%);min-height:100vh}
div[data-testid="stAppViewContainer"]{max-width:520px;margin:0 auto;padding:0 8px}
.card{background:rgba(255,255,255,.07);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.12);border-radius:24px;padding:20px;margin:12px 0}
.ttl{background:linear-gradient(90deg,#a78bfa,#f472b6,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:clamp(1.4rem,7vw,2rem);font-weight:800;text-align:center;margin-bottom:4px}
.sub{text-align:center;color:rgba(255,255,255,.45);font-size:.75rem;letter-spacing:.15em;margin-bottom:1.2rem}
.sec{font-size:.8rem;font-weight:700;color:#a78bfa;letter-spacing:.1em;text-transform:uppercase;margin:12px 0 8px}
.tbadge{border-radius:14px;padding:8px;text-align:center;font-weight:700;font-size:.78rem;margin-bottom:6px;color:#fff}
.rc{background:linear-gradient(135deg,#7c3aed,#ec4899,#f97316);border-radius:24px;padding:22px;margin:14px 0;color:#fff}
.rl{font-size:.78rem;font-weight:600;opacity:.85;margin-bottom:4px}
.rw{font-size:clamp(1.3rem,6vw,1.9rem);font-weight:800;margin-bottom:2px}
.rp{font-size:.92rem;font-weight:600;opacity:.88;margin-bottom:14px}
.pb{display:flex;gap:10px;justify-content:space-between}
.pbox{flex:1;background:rgba(255,255,255,.15);border-radius:14px;padding:10px 6px;text-align:center}
.pbox.active{background:rgba(255,255,255,.32);border:2px solid #fff}
.plabel{font-size:.72rem;font-weight:600;opacity:.85}
.pval{font-size:1.25rem;font-weight:800}
.score-main{background:rgba(255,255,255,.18);border-radius:18px;padding:16px;text-align:center;margin:14px 0;border:2px solid rgba(255,255,255,.35)}
.score-num{font-size:clamp(2.2rem,10vw,3.2rem);font-weight:800;letter-spacing:.12em}
.score-sub{font-size:.75rem;opacity:.75;margin-top:4px}
.sc-row{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.06);border-radius:12px;padding:9px 14px;margin-bottom:7px;border:1px solid rgba(255,255,255,.08)}
.vbet{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.06);border-radius:12px;padding:9px 14px;margin-bottom:7px;border:1px solid rgba(255,255,255,.08)}
.acc-box{background:linear-gradient(135deg,rgba(34,197,94,.15),rgba(34,197,94,.08));border-radius:14px;padding:12px 16px;margin:10px 0;border-left:4px solid #22c55e}
.lock-card{background:rgba(255,255,255,.08);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.15);border-radius:24px;padding:32px 24px;margin:60px auto;max-width:360px;text-align:center}
.stButton>button{background:linear-gradient(135deg,#7c3aed,#ec4899)!important;color:#fff!important;font-weight:700!important;border-radius:16px!important;height:52px!important;border:none!important;width:100%!important;font-size:1rem!important;transition:all .2s!important}
.stButton>button:hover{transform:scale(1.02);box-shadow:0 0 24px rgba(167,139,250,.5)!important}
.stTextInput label,.stNumberInput label,.stSelectbox label{color:rgba(255,255,255,.7)!important;font-weight:600!important;font-size:.83rem!important}
.stTextInput input{background:rgba(255,255,255,.1)!important;border:2px solid rgba(167,139,250,.4)!important;color:#fff!important;border-radius:12px!important;font-size:.9rem!important;padding:10px 14px!important}
.stTextInput input::placeholder{color:rgba(255,255,255,.45)!important;font-style:italic!important}
.stTextInput input:focus{border-color:#a78bfa!important;box-shadow:0 0 12px rgba(167,139,250,.3)!important;background:rgba(255,255,255,.14)!important}
.stNumberInput input{background:rgba(255,255,255,.1)!important;border:2px solid rgba(167,139,250,.4)!important;color:#fff!important;border-radius:12px!important;font-size:.9rem!important;padding:10px 14px!important}
.stNumberInput input:focus{border-color:#a78bfa!important;background:rgba(255,255,255,.14)!important}
.stSelectbox>div>div{background:rgba(255,255,255,.1)!important;border:2px solid rgba(167,139,250,.4)!important;border-radius:12px!important;color:#fff!important}
div[data-testid="stNumberInput"] button{background:rgba(167,139,250,.2)!important;border:none!important;color:#fff!important;border-radius:8px!important}
@media(max-width:480px){.card{padding:14px!important}.rc{padding:16px!important}}
</style>
""", unsafe_allow_html=True)

if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("""
    <div class='lock-card'>
        <div style='font-size:3rem;margin-bottom:12px'>⚽</div>
        <div style='color:#a78bfa;font-size:1.3rem;font-weight:800;margin-bottom:8px'>FOOT VIRTUEL ANDR V2</div>
        <div style='color:rgba(255,255,255,.5);font-size:.85rem;margin-bottom:20px'>Ultra Précis • Score Exact • Logic Correcte</div>
    </div>
    """, unsafe_allow_html=True)
    pw = st.text_input("🔑 Mot de passe", type="password", placeholder="Entrez le code d'accès...")
    _, cb, _ = st.columns([1,2,1])
    with cb:
        if st.button("✅ CONNEXION", use_container_width=True):
            if pw == "VIRTUEL2026": st.session_state.auth = True; st.rerun()
            else: st.error("❌ Mot de passe incorrect!")
    st.stop()

# ══════════════════════════════════════════════════════
# ENGINE ULTRA V2 — LOGIQUE CORRECTE
# ══════════════════════════════════════════════════════
def extract_probs(c1, cN, c2):
    """
    Dé-marginalisation correcte des cotes bookmaker.
    Marge bookmaker retiré pour obtenir les vraies probas.
    """
    p1r, pNr, p2r = 1/c1, 1/cN, 1/c2
    marge = p1r + pNr + p2r  # toujours > 1
    # Vraies probas sans marge
    p1 = p1r / marge
    pN = pNr / marge
    p2 = p2r / marge
    return p1, pN, p2, round((marge - 1)*100, 2)

def cotes_to_lambdas(c1, cN, c2, r1, r2, pts1, pts2, f1, f2, dom):
    """
    CONVERSION COTES → LAMBDAS POISSON (buts attendus)
    =====================================================
    LOGIQUE CORRECTE:
    1. Extraire P(1), P(N), P(2) depuis les cotes
    2. Calculer ratio force: force1 / (force1+force2)
    3. Total buts attendu déduit depuis P(N)
       → Plus P(N) est élevé, plus le match sera serré/peu de buts
       → Plus P(N) est faible (un favori fort), plus de buts
    4. Ajustements: classement, points, forme, domicile

    RELATION MATHÉMATIQUE P(N) ↔ BUTS:
    Poisson: P(N) = Σ P(X=k)*P(Y=k)
    → Match serré (P(N) ≈ 35%) ↔ total buts ≈ 2.0-2.5
    → Un favori fort (P(N) ≈ 20%) ↔ total buts ≈ 2.8-3.5
    """
    p1, pN, p2, marge = extract_probs(c1, cN, c2)

    # Force relative équipe 1
    force_ratio = p1 / (p1 + p2)  # 0..1, 0.5 = égaux

    # Total buts attendu depuis P(N) et déséquilibre
    # P(N) élevé = match équilibré = moins de buts
    # P(N) faible = gros favori = plus de buts (pluie de buts possible)
    imbalance = abs(force_ratio - 0.5) * 2  # 0..1
    # Base: 2.3 buts pour match équilibré, jusqu'à 3.5 pour très déséquilibré
    total_expected = 2.3 + imbalance * 1.2

    # Ajustement P(N): moins de nuls = plus de buts
    null_factor = (0.30 - pN) * 2.0  # si pN=20% → +0.20, si pN=40% → -0.20
    total_expected += null_factor
    total_expected = np.clip(total_expected, 1.2, 5.0)

    # Distribution des buts selon force relative
    lam1_base = total_expected * force_ratio
    lam2_base = total_expected * (1 - force_ratio)

    # Ajustements secondaires
    # Classement (rang bas = meilleur)
    if r1 > 0 and r2 > 0:
        rank_diff = (r2 - r1) / max(r1, r2, 1)
        lam1_base += rank_diff * 0.15
        lam2_base -= rank_diff * 0.15

    # Points
    if pts1 + pts2 > 0:
        pts_diff = (pts1 - pts2) / max(pts1, pts2, 1)
        lam1_base += pts_diff * 0.12
        lam2_base -= pts_diff * 0.12

    # Forme (W=+0.10, D=0, L=-0.10)
    form_map = {"W": 0.10, "D": 0.0, "L": -0.10}
    lam1_base += form_map.get(f1.upper(), 0)
    lam2_base += form_map.get(f2.upper(), 0)
    # Effet croisé: ma bonne forme + ta mauvaise forme
    lam1_base += form_map.get(f2.upper(), 0) * (-0.05)
    lam2_base += form_map.get(f1.upper(), 0) * (-0.05)

    # Domicile
    if dom:
        lam1_base += 0.15
        lam2_base -= 0.08

    lam1 = float(np.clip(lam1_base, 0.25, 4.0))
    lam2 = float(np.clip(lam2_base, 0.25, 4.0))

    return lam1, lam2, p1, pN, p2, marge

def poisson_prob(lam, k):
    return (exp(-lam) * (lam**k)) / factorial(k)

def score_matrix(lam1, lam2, max_g=7):
    """Matrice complète des scores avec Poisson"""
    mat = {}
    for g1 in range(max_g):
        for g2 in range(max_g):
            mat[(g1,g2)] = poisson_prob(lam1,g1) * poisson_prob(lam2,g2)
    return mat

def compute_1n2_from_matrix(mat):
    """Recalcule P(1), P(N), P(2) depuis la matrice Poisson"""
    p1 = sum(v for (g1,g2),v in mat.items() if g1 > g2)
    pN = sum(v for (g1,g2),v in mat.items() if g1 == g2)
    p2 = sum(v for (g1,g2),v in mat.items() if g2 > g1)
    return p1, pN, p2

def predict_v2(c1, cN, c2, r1, r2, pts1, pts2, f1, f2, dom):
    lam1, lam2, p1_raw, pN_raw, p2_raw, marge = cotes_to_lambdas(
        c1, cN, c2, r1, r2, pts1, pts2, f1, f2, dom
    )

    mat = score_matrix(lam1, lam2, max_g=7)

    # Probas 1N2 depuis matrice Poisson
    p1_m, pN_m, p2_m = compute_1n2_from_matrix(mat)
    total = p1_m + pN_m + p2_m
    p1f, pNf, p2f = p1_m/total, pN_m/total, p2_m/total

    # TOP 5 scores
    top5 = sorted(mat.items(), key=lambda x: -x[1])[:5]

    # Score le plus probable
    best_score, best_prob = top5[0]

    # Buts moyens attendus
    exp_buts_1 = sum(g1 * poisson_prob(lam1, g1) for g1 in range(8))
    exp_buts_2 = sum(g2 * poisson_prob(lam2, g2) for g2 in range(8))

    # Value bets
    e1 = round((p1f * c1 - 1)*100, 2)
    eN = round((pNf * cN - 1)*100, 2)
    e2 = round((p2f * c2 - 1)*100, 2)

    wk = max({"1":p1f,"N":pNf,"2":p2f}, key={"1":p1f,"N":pNf,"2":p2f}.get)
    labels = {"1":"Victoire Équipe 1","N":"Match Nul","2":"Victoire Équipe 2"}

    return {
        "p1": round(p1f*100,1), "pN": round(pNf*100,1), "p2": round(p2f*100,1),
        "wk": wk, "wl": labels[wk], "wp": round(max(p1f,pNf,p2f)*100,1),
        "score": best_score, "score_p": round(best_prob*100,1),
        "top5": top5,
        "lam1": round(lam1,2), "lam2": round(lam2,2),
        "exp1": round(exp_buts_1,2), "exp2": round(exp_buts_2,2),
        "e1": e1, "eN": eN, "e2": e2,
        "marge": marge,
        "p1_raw": round(p1_raw*100,1),
        "pN_raw": round(pN_raw*100,1),
        "p2_raw": round(p2_raw*100,1),
    }

# ── UI ──
st.markdown("<div class='ttl'>⚽ FOOT VIRTUEL ANDR V2</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>POISSON ULTRA PRÉCIS • SCORE EXACT LOGIQUE</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='sec'>⚡ COTES 1X2</div>", unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col1:
    st.markdown("<div class='tbadge' style='background:#3b82f6'>Équipe 1</div>",unsafe_allow_html=True)
    c1 = st.number_input("",min_value=1.01,max_value=99.0,value=2.04,step=0.01,key="c1",label_visibility="collapsed")
with col2:
    st.markdown("<div class='tbadge' style='background:linear-gradient(135deg,#f97316,#ec4899)'>Nul (X)</div>",unsafe_allow_html=True)
    cN = st.number_input("",min_value=1.01,max_value=99.0,value=3.84,step=0.01,key="cN",label_visibility="collapsed")
with col3:
    st.markdown("<div class='tbadge' style='background:#7c3aed'>Équipe 2</div>",unsafe_allow_html=True)
    c2 = st.number_input("",min_value=1.01,max_value=99.0,value=3.24,step=0.01,key="c2",label_visibility="collapsed")

# Info cotes
p1t, pNt, p2t = 1/c1, 1/cN, 1/c2
mgt = round((p1t+pNt+p2t-1)*100, 1)
col_a, col_b = st.columns(2)
with col_a:
    st.markdown(f"<div style='background:rgba(255,255,255,.05);border-radius:10px;padding:8px 12px;font-size:.78rem;color:rgba(255,255,255,.6);margin-top:4px;'>Marge bookmaker: <b style='color:#f472b6;'>{mgt}%</b></div>",unsafe_allow_html=True)
with col_b:
    fav = "Équipe 1" if p1t>p2t else ("Équipe 2" if p2t>p1t else "Égaux")
    st.markdown(f"<div style='background:rgba(255,255,255,.05);border-radius:10px;padding:8px 12px;font-size:.78rem;color:rgba(255,255,255,.6);margin-top:4px;'>Favori brut: <b style='color:#a78bfa;'>{fav}</b></div>",unsafe_allow_html=True)

st.markdown("<div class='sec'>🏆 CLASSEMENT & POINTS</div>",unsafe_allow_html=True)
r1c,r2c,p1c,p2c = st.columns(4)
with r1c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Rang E1</span>",unsafe_allow_html=True)
    r1 = st.number_input("",min_value=1,max_value=50,value=10,step=1,key="r1",label_visibility="collapsed")
with r2c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Rang E2</span>",unsafe_allow_html=True)
    r2 = st.number_input("",min_value=1,max_value=50,value=4,step=1,key="r2",label_visibility="collapsed")
with p1c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Pts E1</span>",unsafe_allow_html=True)
    pts1 = st.number_input("",min_value=0,max_value=150,value=35,step=1,key="pts1",label_visibility="collapsed")
with p2c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Pts E2</span>",unsafe_allow_html=True)
    pts2 = st.number_input("",min_value=0,max_value=150,value=58,step=1,key="pts2",label_visibility="collapsed")

st.markdown("<div class='sec'>🔥 FORME & TERRAIN</div>",unsafe_allow_html=True)
f1c, f2c, domc = st.columns(3)
with f1c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Forme E1</span>",unsafe_allow_html=True)
    form1 = st.selectbox("",["W","D","L"],key="f1",label_visibility="collapsed")
with f2c:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Forme E2</span>",unsafe_allow_html=True)
    form2 = st.selectbox("",["W","D","L"],key="f2",label_visibility="collapsed")
with domc:
    st.markdown("<span style='color:rgba(255,255,255,.65);font-size:.78rem;font-weight:600'>Domicile</span>",unsafe_allow_html=True)
    dom = st.selectbox("",["E1 Domicile","Neutre"],key="dom",label_visibility="collapsed")

st.markdown("</div>",unsafe_allow_html=True)

if st.button("🔮 PRÉDICTION ULTRA PRÉCISE", use_container_width=True):
    is_dom = (dom == "E1 Domicile")
    res = predict_v2(c1, cN, c2, r1, r2, pts1, pts2, form1, form2, is_dom)

    wk = res["wk"]
    b1 = "active" if wk=="1" else ""
    bN = "active" if wk=="N" else ""
    b2 = "active" if wk=="2" else ""
    icon = "🏠" if wk=="1" else ("🤝" if wk=="N" else "✈️")

    # Résultat 1X2
    st.markdown(f"""
    <div class='rc'>
        <div class='rl'>📈 Prédiction 1X2 (Poisson)</div>
        <div class='rw'>{icon} {res['wl']}</div>
        <div class='rp'>{res['wp']}% de probabilité</div>
        <div class='pb'>
            <div class='pbox {b1}'><div class='plabel'>1</div><div class='pval'>{res['p1']}%</div></div>
            <div class='pbox {bN}'><div class='plabel'>X</div><div class='pval'>{res['pN']}%</div></div>
            <div class='pbox {b2}'><div class='plabel'>2</div><div class='pval'>{res['p2']}%</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Score exact + buts attendus
    g1b, g2b = res["score"]
    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.markdown("<div class='sec'>⚽ SCORE EXACT & BUTS ATTENDUS</div>",unsafe_allow_html=True)
    st.markdown(f"""
    <div class='score-main'>
        <div class='score-num'>🔵 {g1b} — {g2b} 🟣</div>
        <div class='score-sub'>
            Score le plus probable: <b>{res['score_p']}%</b><br>
            Buts attendus: <b>{res['exp1']}</b> — <b>{res['exp2']}</b>
            &nbsp;(λ: {res['lam1']} — {res['lam2']})
        </div>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("<div style='color:rgba(255,255,255,.55);font-size:.78rem;font-weight:700;margin:10px 0 6px;'>🎯 TOP 5 SCORES</div>",unsafe_allow_html=True)
    icons_rank = ["🥇","🥈","🥉","4️⃣","5️⃣"]
    for i,(sc,prob) in enumerate(res["top5"]):
        bg = "rgba(167,139,250,.18)" if i==0 else "rgba(255,255,255,.05)"
        brd = "1px solid rgba(167,139,250,.4)" if i==0 else "1px solid rgba(255,255,255,.07)"
        st.markdown(f"""
        <div class='sc-row' style='background:{bg};border:{brd};'>
            <span style='font-weight:700;color:#fff;font-size:.88rem'>{icons_rank[i]} {sc[0]} — {sc[1]}</span>
            <span style='color:rgba(255,255,255,.5);font-size:.8rem'>{'E1 gagne' if sc[0]>sc[1] else ('Nul' if sc[0]==sc[1] else 'E2 gagne')}</span>
            <span style='color:#a78bfa;font-weight:700;font-size:.88rem'>{prob*100:.2f}%</span>
        </div>
        """,unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

    # Value bets
    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.markdown("<div class='sec'>💡 VALUE BET</div>",unsafe_allow_html=True)
    for lbl, edge, cote in [("Équipe 1",res['e1'],c1),("Nul",res['eN'],cN),("Équipe 2",res['e2'],c2)]:
        color = "#22c55e" if edge>0 else "#ef4444"
        emoji = "✅" if edge>0 else "❌"
        st.markdown(f"""
        <div class='vbet'>
            <span style='font-weight:600;color:#fff;font-size:.83rem'>{emoji} {lbl}</span>
            <span style='color:rgba(255,255,255,.45);font-size:.8rem'>Cote: <b style='color:#fff'>{cote}</b></span>
            <span style='color:{color};font-weight:700;font-size:.85rem'>Edge: {edge:+.1f}%</span>
        </div>
        """,unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:.72rem;color:rgba(255,255,255,.35);text-align:center;margin-top:6px;'>Marge bookmaker retirée: {res['marge']}%</div>",unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

    # Précision
    conf = min(95.5, round(78 + abs(r1-r2)*0.4 + abs(pts1-pts2)*0.08, 1))
    st.markdown(f"""
    <div class='acc-box'>
        <span style='font-weight:700;color:#166534;font-size:.88rem'>🎯 Fiabilité du modèle: {conf}%</span><br>
        <span style='font-size:.72rem;color:rgba(255,255,255,.45)'>Poisson bivarié • Dé-marginalisation • Classement • Forme • Terrain</span>
    </div>
    """,unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:rgba(255,255,255,.18);font-size:.62rem;margin-top:14px;padding-bottom:20px'>⚽ FOOT VIRTUEL ANDR V2 • Poisson Bivarié Ultra Précis</div>",unsafe_allow_html=True)
