import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Riesgo de Morosidad",
    layout="wide"
)

st.title("📊 Dashboard Analítico - Riesgo de Morosidad Bancaria")

df = pd.read_csv("dataset_personal.csv")

st.sidebar.header("Filtros")

historial = st.sidebar.multiselect(
    "Historial Crediticio",
    df["Historial_Crediticio"].unique(),
    default=df["Historial_Crediticio"].unique()
)

df = df[df["Historial_Crediticio"].isin(historial)]

# =====================
# KPI
# =====================

total = len(df)

morosos = df["Riesgo_Morosidad"].sum()

porcentaje = (morosos/total)*100

col1,col2,col3 = st.columns(3)

col1.metric("Clientes", total)

col2.metric("Clientes Morosos", morosos)

col3.metric("% Morosidad", f"{porcentaje:.2f}%")

st.divider()

# =====================
# Barras
# =====================

st.subheader("Clientes según Historial Crediticio")

fig1 = px.bar(
    df,
    x="Historial_Crediticio",
    color="Historial_Crediticio"
)

st.plotly_chart(fig1,use_container_width=True)

# =====================
# Histograma
# =====================

st.subheader("Distribución del Ingreso Mensual")

fig2 = px.histogram(
    df,
    x="Ingreso_Mensual",
    nbins=30
)

st.plotly_chart(fig2,use_container_width=True)

# =====================
# Heatmap
# =====================

st.subheader("Correlación")

corr = df.corr(numeric_only=True)

fig3 = px.imshow(
    corr,
    text_auto=True
)

st.plotly_chart(fig3,use_container_width=True)

# =====================
# Scatter
# =====================

st.subheader("Ingreso vs Deuda")

fig4 = px.scatter(
    df,
    x="Ingreso_Mensual",
    y="Deuda_Actual",
    color="Riesgo_Morosidad"
)

st.plotly_chart(fig4,use_container_width=True)

st.divider()

st.header("Hallazgos")

st.success("""
1. Los clientes con mayor ratio de deuda presentan una mayor probabilidad de morosidad.
""")

st.success("""
2. El historial crediticio influye significativamente en el riesgo de incumplimiento.
""")

st.success("""
3. Los ingresos altos suelen estar asociados a menores niveles de morosidad.
""")

st.divider()

st.header("Recomendaciones")

st.info("""
• Implementar alertas tempranas para clientes con alto ratio de deuda.
""")

st.info("""
• Evaluar el historial crediticio antes de aprobar nuevos préstamos.
""")

st.info("""
• Diseñar planes de refinanciamiento para clientes en riesgo.
""")