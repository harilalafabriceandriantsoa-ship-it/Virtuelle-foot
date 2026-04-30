import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="FOOT VIRTUEL ANDR", page_icon="⚽", layout="centered")

# ─── CSS AMBOARINA NY INPUT (MAINTY STYLÉ) ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
*{font-family:'Poppins',sans-serif;box-sizing:border-box}
.stApp{background:linear-gradient(135deg,#0f0c29 0%,#302b63 50%,#24243e 100%);min-height:100vh}
div[data-testid="stAppViewContainer"]{max-width:500px;margin:0 auto;padding:0 8px}
.card{background:rgba(255,255,255,.07);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.12);border-radius:24px;padding:20px;margin:12px 0}
.ttl{background:linear-gradient(90deg,#a78bfa,#f472b6,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:clamp(1.4rem,7vw,2rem);font-weight:800;text-align:center;margin-bottom:4px}
.sub{text-align:center;color:rgba(255,255,255,.5);font-size:.78rem;letter-spacing:.15em;margin-bottom:1.2rem}
.sec{font-size:.82rem;font-weight:700;color:#a78bfa;letter-spacing:.1em;text-transform:uppercase;margin:12px 0 8px}
.team-badge{border-radius:14px;padding:8px;text-align:center;font-weight:700;font-size:.8rem;margin-bottom:6px;color:#fff}
.rc{background:linear-gradient(135deg,#7c3aed,#ec4899,#f97316);border-radius:24px;padding:24px;margin:14px 0;color:#fff}
.rl{font-size:.8rem;font-weight:600;opacity:.85;margin-bottom:4px}
.rw{font-size:clamp(1.4rem,7vw,2rem);font-weight:800;margin-bottom:2px}
.rp{font-size:.95rem;font-weight:600;opacity:.88;margin-bottom:16px}
.pb{display:flex;gap:10px;justify-content:space-between}
.pbox{flex:1;background:rgba(255,255,255,.15);border-radius:14px;padding:10px 6px;text-align:center}
.pbox.active{background:rgba(255,255,255,.32);border:2px solid #fff}
.plabel{font-size:.75rem;font-weight:600;opacity:.85}
.pval{font-size:1.3rem;font-weight:800}
.score-box{background:rgba(255,255,255,.18);border-radius:16px;padding:14px;text-align:center;margin:14px 0;border:2px solid rgba(255,255,255,.3)}
.score-val{font-size:clamp(2rem,10vw,3rem);font-weight:800;letter-spacing:.1em}
.score-lbl{font-size:.78rem;opacity:.8;margin-top:4px}
.vbet{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.06);border-radius:12px;padding:10px 14px;margin-bottom:8px;border:1px solid rgba(255,255,255,.08)}
.acc-box{background:linear-gradient(135deg,rgba(34,197,94,.15),rgba(34,197,94,.08));border-radius:14px;padding:12px 16px;margin:10px 0;border-left:4px solid #22c55e}
.lock-card{background:rgba(255,255,255,.08);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.15);border-radius:24px;padding:32px 24px;margin:60px auto;max-width:360px;text-align:center}

/* --- KAJY HO AN'NY INPUT (SORATRA MAINTY SY STYLÉ) --- */
.stTextInput label, .stNumberInput label, .stSelectbox label {
    color:rgba(255,255,255,0.9)!important; 
    font-weight:700!important;
}
.stTextInput input, .stNumberInput input {
    background: #ffffff !important; /* Fotsy ny ao anaty vata */
    color: #000000 !important; /* Soratra mainty tanteraka */
    border: 2px solid #a78bfa !important;
    border-radius: 12px !important;
    font-size: 1rem !important;
    font-weight: 800 !important;
}
.stTextInput input::placeholder {
    color: #333333 !important; /* Placeholder mainty somary matetika */
    opacity: 0.7 !important;
}
.stSelectbox>div>div {
    background: #ffffff !important;
    color: #000000 !important;
    border: 2px solid #a78bfa !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}

.stButton>button{background:linear-gradient(135deg,#7c3aed,#ec4899)!important;color:#fff!important;font-weight:700!important;border-radius:16px!important;height:52px!important;border:none!important;width:100%!important;font-size:1rem!important;letter-spacing:.04em!important;transition:all .2s!important}
.stButton>button:hover{transform:scale(1.02);box-shadow:0 0 24px rgba(167,139,250,.5)!important}
@media(max-width:480px){.card{padding:14px!important}.rc{padding:18px!important}}
</style>
""", unsafe_allow_html=True)

# ── AUTH ──
if "auth" not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("""
    <div class='lock-card'>
        <div style='font-size:3rem;margin-bottom:12px'>⚽</div>
        <div style='color:#a78bfa;font-size:1.3rem;font-weight:800;margin-bottom:8px'>FOOT VIRTUEL ANDR</div>
        <div style='color:rgba(255,255,255,.5);font-size:.85rem;margin-bottom:20px'>Entrez le mot de passe pour accéder</div>
    </div>
    """, unsafe_allow_html=True)
    pw = st.text_input("🔑 Mot de passe", type="password", placeholder="CODE: VIRTUEL2026")
    _, cb, _ = st.columns([1,2,1])
    with cb:
        if st.button("✅ CONNEXION", use_container_width=True):
            if pw == "VIRTUEL2026": st.session_state.auth = True; st.rerun()
            else: st.error("❌ Mot de passe incorrect!")
    st.stop()

# ── ENGINE ULTRA (FIXED ERROR) ──
def predict(c1, cN, c2, r1, r2, pts1, pts2, f1, f2, dom):
    pi1, piN, pi2 = 1/c1, 1/cN, 1/c2
    tot = pi1+piN+pi2
    p1, pN, p2 = pi1/tot, piN/tot, pi2/tot

    rd = (r2-r1)/max(r1,r2,1)
    rank_adj = np.tanh(rd*1.2)*0.10

    ptot = max(pts1+pts2, 1)
    pts_adj = ((pts1-pts2)/ptot)*0.08

    form_map = {"W":3,"D":1,"L":0}
    sc1 = form_map.get(f1.upper(),1)/3
    sc2 = form_map.get(f2.upper(),1)/3
    form_adj = (sc1-sc2)*0.07

    home_adj = 0.05 if dom else 0.0

    adj_total = rank_adj + pts_adj + form_adj + home_adj
    p1a = p1 + adj_total*0.65
    pNa = pN - abs(adj_total)*0.08
    p2a = p2 - adj_total*0.65

    def norm(a,b,c):
        t=max(0.001, a+b+c)
        return (max(0.04,a/t), max(0.04,b/t), max(0.04,c/t))
    
    p1f,pNf,p2f = norm(p1a,pNa,p2a)

    lam1 = np.clip(1.3 * (p1f/(p1f+p2f+0.01)) * 2.2, 0.3, 3.5)
    lam2 = np.clip(1.3 * (p2f/(p1f+p2f+0.01)) * 2.2, 0.3, 3.5)

    best_s, best_p = (0,0), 0.0
    all_scores = {}
    for g1 in range(7):
        for g2 in range(7):
            p_g1 = np.exp(-lam1)*(lam1**g1)/math.factorial(g1)
            p_g2 = np.exp(-lam2)*(lam2**g2)/math.factorial(g2)
            prob = p_g1*p_g2
            all_scores[(g1,g2)] = round(prob*100,2)
            if prob > best_p:
                best_p = prob
                best_s = (g1,g2)

    top3 = sorted(all_scores.items(), key=lambda x:-x[1])[:3]
    e1 = round((p1f*c1-1)*100,2)
    eN = round((pNf*cN-1)*100,2)
    e2 = round((p2f*c2-1)*100,2)

    probs = {"1":p1f,"N":pNf,"2":p2f}
    winner_k = max(probs, key=probs.get)
    labels = {"1":"Victoire Équipe 1","N":"Match Nul","2":"Victoire Équipe 2"}

    return {
        "p1":round(p1f*100,1),"pN":round(pNf*100,1),"p2":round(p2f*100,1),
        "wk":winner_k,"wl":labels[winner_k],"wp":round(max(p1f,pNf,p2f)*100,1),
        "score":best_s,"score_p":round(best_p*100,1),
        "top3":top3,"lam1":round(lam1,2),"lam2":round(lam2,2),
        "e1":e1,"eN":eN,"e2":e2
    }

# ── UI ──
st.markdown("<div class='ttl'>⚽ FOOT VIRTUEL ANDR</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>PRÉDICTION ULTRA PUISSANTE • SCORE EXACT</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='sec'>⚡ COTES DU MATCH</div>", unsafe_allow_html=True)
c1,c2,c3=st.columns(3)
with c1:
    st.markdown("<div class='team-badge' style='background:#3b82f6'>Équipe 1</div>",unsafe_allow_html=True)
    cote1=st.number_input("",min_value=1.01,max_value=50.0,value=2.04,step=0.01,key="c1",label_visibility="collapsed")
with c2:
    st.markdown("<div class='team-badge' style='background:linear-gradient(135deg,#f97316,#ec4899)'>Nul</div>",unsafe_allow_html=True)
    coteN=st.number_input("",min_value=1.01,max_value=50.0,value=3.84,step=0.01,key="cN",label_visibility="collapsed")
with c3:
    st.markdown("<div class='team-badge' style='background:#7c3aed'>Équipe 2</div>",unsafe_allow_html=True)
    cote2=st.number_input("",min_value=1.01,max_value=50.0,value=3.24,step=0.01,key="c2",label_visibility="collapsed")

st.markdown("<div class='sec'>🏆 CLASSEMENT & POINTS</div>",unsafe_allow_html=True)
r1,r2=st.columns(2)
with r1:
    rank1=st.number_input("Rang É1",min_value=1,max_value=50,value=10)
    pts1=st.number_input("Points É1",min_value=0,max_value=120,value=35)
with r2:
    rank2=st.number_input("Rang É2",min_value=1,max_value=50,value=4)
    pts2=st.number_input("Points É2",min_value=0,max_value=120,value=58)

st.markdown("<div class='sec'>🔥 FORME RÉCENTE</div>",unsafe_allow_html=True)
f1c,f2c=st.columns(2)
with f1c:
    form1=st.selectbox("Forme É1",["W","D","L"])
with f2c:
    form2=st.selectbox("Forme É2",["W","D","L"])

dom=st.toggle("Équipe 1 joue à domicile",value=False)
st.markdown("</div>",unsafe_allow_html=True)

if st.button("🔮 LANCER LA PRÉDICTION", use_container_width=True):
    res = predict(cote1,coteN,cote2,rank1,rank2,pts1,pts2,form1,form2,dom)
    wk=res["wk"]
    b1="active" if wk=="1" else ""
    bN="active" if wk=="N" else ""
    b2="active" if wk=="2" else ""
    icon="🏠" if wk=="1" else("🤝" if wk=="N" else"✈️")

    st.markdown(f"""
    <div class='rc'>
        <div class='rl'>📈 Prédiction 1N2</div>
        <div class='rw'>{icon} {res['wl']}</div>
        <div class='rp'>{res['wp']}% de probabilité</div>
        <div class='pb'>
            <div class='pbox {b1}'><div class='plabel'>1</div><div class='pval'>{res['p1']}%</div></div>
            <div class='pbox {bN}'><div class='plabel'>N</div><div class='pval'>{res['pN']}%</div></div>
            <div class='pbox {b2}'><div class='plabel'>2</div><div class='pval'>{res['p2']}%</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    g1,g2=res["score"]
    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.markdown("<div class='sec'>⚽ SCORE EXACT PRÉDIT</div>",unsafe_allow_html=True)
    st.markdown(f"""
    <div class='score-box'>
        <div class='score-val'>🔵 {g1} — {g2} 🟣</div>
        <div class='score-lbl'>Probabilité: <b>{res['score_p']}%</b></div>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("<div style='color:rgba(255,255,255,.6);font-size:.78rem;font-weight:600;margin-bottom:6px;'>🎯 TOP 3 SCORES</div>",unsafe_allow_html=True)
    for i,(sc,prob) in enumerate(res["top3"]):
        rank_icons=["🥇","🥈","🥉"]
        st.markdown(f"""
        <div class='vbet'>
            <span style='font-weight:700;color:#fff;'>{rank_icons[i]} {sc[0]} — {sc[1]}</span>
            <span style='color:#a78bfa;font-weight:700;'>{prob}%</span>
        </div>
        """,unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

    st.markdown("<div class='card'>",unsafe_allow_html=True)
    st.markdown("<div class='sec'>💡 VALUE BET ANALYSIS</div>",unsafe_allow_html=True)
    for lbl,edge,cote in [("É1",res['e1'],cote1),("Nul",res['eN'],coteN),("É2",res['e2'],cote2)]:
        color="#22c55e" if edge>0 else "#ef4444"
        st.markdown(f"<div class='vbet'><span>{lbl}</span><span>Cote: {cote}</span><span style='color:{color};font-weight:700;'>Edge: {edge:+.1f}%</span></div>",unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)

st.markdown("<div style='text-align:center;color:rgba(255,255,255,.2);font-size:.65rem;margin-top:16px;padding-bottom:24px'>⚽ FOOT VIRTUEL ANDR • Prédiction IA Ultra Puissante</div>",unsafe_allow_html=True)
