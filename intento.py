import streamlit as st

st.set_page_config(page_title="WarEra Simulador PRO", layout="wide")

st.title("WarEra, haz que tus empresas camellen")

# ==========================
# TIPOS
# ==========================

TIPOS = [
    "piedra", "trigo", "hierro", "plomo", "coca",
    "vacas", "peces",
    "concreto", "vigas",
    "balas", "balasx", "balasxx",
    "pan", "carne", "pescado", "pastillas"
]

# ==========================
# FUNCIÓN PRODUCCIÓN
# ==========================

def calcular(tipo, nivel, bonus):
    puntos = nivel * 24
    p = puntos * (1 + bonus / 100)

    # BASE
    piedra = p
    trigo = p
    hierro = p
    plomo = p
    coca = p
    vacas = p / 20
    peces = p / 40

    # PRODUCCIÓN SEGÚN TIPO
    if tipo == "piedra":
        return p
    if tipo == "trigo":
        return p
    if tipo == "hierro":
        return p
    if tipo == "plomo":
        return p
    if tipo == "coca":
        return p
    if tipo == "vacas":
        return vacas
    if tipo == "peces":
        return peces

    if tipo == "concreto":
        return min(p/10, piedra/10)

    if tipo == "vigas":
        return min(p/10, hierro/10)

    if tipo == "balas":
        return min(p, plomo)

    if tipo == "balasx":
        return min(p/4, plomo/4)

    if tipo == "balasxx":
        return min(p/16, plomo/16)

    if tipo == "pan":
        return min(p/10, trigo/10)

    if tipo == "carne":
        return min(p/20, vacas)

    if tipo == "pescado":
        return min(p/40, peces)

    if tipo == "pastillas":
        return min(p/200, coca/200)

    return 0

# ==========================
# EMPRESA 1
# ==========================

st.sidebar.header("🏭 Empresa 1")

tipo1 = st.sidebar.selectbox("Tipo E1", TIPOS, key="t1")
nivel1 = st.sidebar.slider("Nivel E1", 1, 7, 5, key="n1")
bonus1 = st.sidebar.number_input("Bono E1 (%)", value=0.0, step=0.01, key="b1")

# ==========================
# EMPRESA 2
# ==========================

st.sidebar.header("🏭 Empresa 2")

tipo2 = st.sidebar.selectbox("Tipo E2", TIPOS, key="t2")
nivel2 = st.sidebar.slider("Nivel E2", 1, 7, 4, key="n2")
bonus2 = st.sidebar.number_input("Bono E2 (%)", value=0.0, step=0.01, key="b2")

# ==========================
# CALCULAR
# ==========================

prod1 = calcular(tipo1, nivel1, bonus1)
prod2 = calcular(tipo2, nivel2, bonus2)

# ==========================
# RESULTADOS
# ==========================

st.subheader("📊 Producción por empresa")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏭 Empresa 1")
    st.write(f"Tipo: {tipo1}")
    st.write(f"Nivel: {nivel1} → {nivel1*24} puntos/día")
    st.metric("Producción/día", round(prod1, 2))

with col2:
    st.markdown("### 🏭 Empresa 2")
    st.write(f"Tipo: {tipo2}")
    st.write(f"Nivel: {nivel2} → {nivel2*24} puntos/día")
    st.metric("Producción/día", round(prod2, 2))

# ==========================
# TOTAL
# ==========================

st.subheader("🔥 Producción total")

if tipo1 == tipo2:
    total = prod1 + prod2
    st.metric(f"Total {tipo1}", round(total, 2))
else:
    st.warning("⚠️ Tipos distintos: no se suman directamente")


# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<hr style="border:1px solid #30363d; margin-top:40px;">

<div style="
text-align:center;
color:#8b949e;
font-size:14px;
padding:20px;
">

Developed by <b>Antonio Pluas</b><br>
War Era Ecuadorian company© 2026

</div>
""", unsafe_allow_html=True)
