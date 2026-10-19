"""
dashboard.py — App web Manaco · Análisis de Comercio de Calzado
Ejecutar: streamlit run app/dashboard.py
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from carga import RUTA_XLSX, cargar, resumen_calidad

# ── Configuración de página ─────────────────────────────────────────────────
st.set_page_config(
    page_title="Manaco · Dashboard de Comercio",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded",
)

PALETA = {"Importación": "#e74c3c", "Exportación": "#2980b9"}
SA6_NOMBRE = {
    "640411": "640411 — Deportivo",
    "640399": "640399 — Cuero superior",
    "640420": "640420 — Suela de cuero",
}

# ── Helpers ─────────────────────────────────────────────────────────────────
@st.cache_data
def cargar_datos(ruta_o_bytes):
    df = pd.read_excel(ruta_o_bytes, sheet_name="Base de Datos")
    df["Año"] = df["Año"].astype(int)
    df["Código_SA6"] = df["Código_SA6"].astype(str)
    for c in ["Valor_miles_USD", "Cantidad_pares", "Valor_USD", "Valor_USD_por_par"]:
        df[c] = df[c].astype(float)
    es_mundo = df["Socio_comercial"].str.strip().str.lower() == "mundo"
    return df[~es_mundo].copy().reset_index(drop=True), df[es_mundo].copy()


def fmt_m(v):
    return f"${v/1e6:,.1f} M"


def fmt_par(v):
    return f"${v:,.2f}"


# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/emoji/96/running-shoe.png", width=72)
    st.title("Manaco · Dashboard")
    st.caption("Benchmark comercio calzado · España 2020-2024")
    st.divider()

    archivo = st.file_uploader(
        "📂 Cargar Base_de_Datos.xlsx",
        type=["xlsx"],
        help="Hoja 'Base de Datos' con las 10 columnas del caso.",
    )

    ruta_def = Path(__file__).resolve().parents[1] / "data" / "raw" / "Base_de_Datos.xlsx"

    if archivo is None:
        if ruta_def.exists():
            fuente = str(ruta_def)
            st.success("✅ Base de datos cargada automáticamente")
        else:
            st.warning("⬆️ Sube el archivo Excel para comenzar.")
            st.stop()
    else:
        fuente = archivo

    df, mundo = cargar_datos(fuente)

    st.divider()
    flujos = st.multiselect(
        "Flujo comercial",
        options=df["Flujo_comercial"].unique().tolist(),
        default=df["Flujo_comercial"].unique().tolist(),
    )
    años = st.slider(
        "Rango de años",
        int(df["Año"].min()), int(df["Año"].max()),
        (int(df["Año"].min()), int(df["Año"].max())),
    )
    categorias = st.multiselect(
        "Categoría SA6",
        options=df["Código_SA6"].unique().tolist(),
        default=df["Código_SA6"].unique().tolist(),
        format_func=lambda x: SA6_NOMBRE.get(x, x),
    )

    st.divider()
    st.caption("⚠️ Base de referencia de **España**, no de Bolivia ni de Manaco.")

# ── Filtro ───────────────────────────────────────────────────────────────────
dff = df[
    df["Flujo_comercial"].isin(flujos)
    & df["Año"].between(años[0], años[1])
    & df["Código_SA6"].isin(categorias)
].copy()

if dff.empty:
    st.error("No hay datos con los filtros seleccionados.")
    st.stop()

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("## 👟 Manaco — Dashboard de Comercio de Calzado")
st.caption(
    f"Benchmark externo · España {años[0]}–{años[1]} · "
    f"{len(dff):,} registros · {dff['Socio_comercial'].nunique()} socios"
)
st.divider()

# ── KPI cards ────────────────────────────────────────────────────────────────
tot = dff.groupby("Flujo_comercial")[["Valor_USD", "Cantidad_pares"]].sum()
imp_v = tot.get("value", tot).loc["Importación", "Valor_USD"] if "Importación" in tot.index else 0
exp_v = tot.loc["Exportación", "Valor_USD"] if "Exportación" in tot.index else 0
imp_p = tot.loc["Importación", "Cantidad_pares"] if "Importación" in tot.index else 0
exp_p = tot.loc["Exportación", "Cantidad_pares"] if "Exportación" in tot.index else 0
razon_v = imp_v / exp_v if exp_v > 0 else float("nan")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("📥 Importación (valor)", fmt_m(imp_v))
col2.metric("📤 Exportación (valor)", fmt_m(exp_v))
col3.metric("⚖️ Razón imp/exp valor", f"{razon_v:.2f}×" if not np.isnan(razon_v) else "—")
col4.metric("📥 Importación (pares)", f"{imp_p/1e6:,.1f} M")
col5.metric("📤 Exportación (pares)", f"{exp_p/1e6:,.1f} M")

st.divider()

# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Importación vs Exportación",
    "🌍 Socios comerciales",
    "💰 Valor por par",
    "📊 Indicadores",
    "🔍 Calidad de datos",
])

# ── TAB 1: Import vs Export ───────────────────────────────────────────────────
with tab1:
    st.subheader("Importación vs. Exportación — Valor y Cantidad por año")

    anual = dff.groupby(["Año", "Flujo_comercial"], as_index=False).agg(
        Valor_M_USD=("Valor_USD", lambda s: s.sum() / 1e6),
        Pares_M=("Cantidad_pares", lambda s: s.sum() / 1e6),
    )

    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Valor comercial (millones de USD)", "Cantidad de pares (millones)"),
    )
    for flujo, color in PALETA.items():
        sub = anual[anual["Flujo_comercial"] == flujo]
        if sub.empty:
            continue
        fig.add_trace(
            go.Scatter(x=sub["Año"], y=sub["Valor_M_USD"], mode="lines+markers",
                       name=flujo, line=dict(color=color, width=2.5),
                       marker=dict(size=8), legendgroup=flujo),
            row=1, col=1,
        )
        fig.add_trace(
            go.Scatter(x=sub["Año"], y=sub["Pares_M"], mode="lines+markers",
                       name=flujo, line=dict(color=color, width=2.5),
                       marker=dict(size=8), legendgroup=flujo, showlegend=False),
            row=1, col=2,
        )
    fig.update_layout(height=420, legend_title="Flujo", hovermode="x unified",
                      plot_bgcolor="white", paper_bgcolor="white")
    fig.update_xaxes(tickformat="d")
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📌 Lectura empresarial"):
        st.info(
            "**[Dato]** En el período analizado, las importaciones superan a las exportaciones "
            "en valor (~1,7×) y en pares (~1,8×).  \n"
            "**[Conclusión]** La presión importadora es estructural en el mercado de referencia.  \n"
            "**[Supuesto]** Si Bolivia replica esta estructura, Manaco no puede competir solo por "
            "precio: la diferenciación y el control de costos son prioritarios."
        )

    col_a, col_b = st.columns(2)
    with col_a:
        st.dataframe(
            anual.pivot(index="Año", columns="Flujo_comercial", values="Valor_M_USD").round(1),
            use_container_width=True,
        )
    with col_b:
        st.dataframe(
            anual.pivot(index="Año", columns="Flujo_comercial", values="Pares_M").round(1),
            use_container_width=True,
        )

# ── TAB 2: Socios ─────────────────────────────────────────────────────────────
with tab2:
    st.subheader("Principales socios comerciales por valor acumulado")

    top_n = st.slider("Número de socios a mostrar", 5, min(30, dff["Socio_comercial"].nunique()), 10)

    pivote = (
        dff.pivot_table(index="Socio_comercial", columns="Flujo_comercial",
                        values="Valor_USD", aggfunc="sum", fill_value=0) / 1e6
    )
    for fl in PALETA:
        if fl not in pivote.columns:
            pivote[fl] = 0.0
    pivote["Total"] = pivote.sum(axis=1)
    top = pivote.nlargest(top_n, "Total").sort_values("Total")

    fig2 = go.Figure()
    for flujo, color in PALETA.items():
        if flujo in top.columns:
            fig2.add_trace(go.Bar(
                y=top.index, x=top[flujo], name=flujo,
                orientation="h", marker_color=color,
            ))
    fig2.update_layout(
        barmode="stack", height=max(350, top_n * 32),
        xaxis_title="Millones de USD acumulados",
        yaxis_title="Socio comercial",
        legend_title="Flujo",
        plot_bgcolor="white", paper_bgcolor="white",
    )
    st.plotly_chart(fig2, use_container_width=True)

    with st.expander("📌 Lectura empresarial"):
        top3_imp = pivote["Importación"].nlargest(3) if "Importación" in pivote.columns else pd.Series()
        st.info(
            f"**[Dato]** Los {top_n} primeros socios concentran "
            f"{top['Total'].sum() / pivote['Total'].sum():.1%} del valor total.  \n"
            "**[Conclusión]** La oferta importada está diversificada entre varios orígenes.  \n"
            "**[Supuesto]** Para Manaco, monitorear los orígenes de importación a Bolivia "
            "por categoría es el primer insumo a obtener."
        )

    col_c, col_d = st.columns(2)
    for flujo, col in zip(["Importación", "Exportación"], [col_c, col_d]):
        if flujo in dff["Flujo_comercial"].values:
            with col:
                st.markdown(f"**Top 10 por valor — {flujo}**")
                rank = (
                    dff[dff["Flujo_comercial"] == flujo]
                    .groupby("Socio_comercial")
                    .agg(Valor_M_USD=("Valor_USD", lambda s: s.sum() / 1e6),
                         Pares_M=("Cantidad_pares", lambda s: s.sum() / 1e6))
                    .assign(USD_par=lambda x: (x["Valor_M_USD"] * 1e6) / (x["Pares_M"] * 1e6))
                    .nlargest(10, "Valor_M_USD")
                    .round(2)
                )
                st.dataframe(rank, use_container_width=True)

# ── TAB 3: Valor por par ──────────────────────────────────────────────────────
with tab3:
    st.subheader("Valor aduanero por par — por categoría SA6 y flujo")
    st.caption("⚠️ Valor FOB/CIF aduanero, **no el precio al consumidor**.")

    p95 = dff.groupby(["Código_SA6", "Flujo_comercial"])["Valor_USD_por_par"].transform(
        lambda s: s.quantile(0.95)
    )
    dff_clip = dff[dff["Valor_USD_por_par"] <= p95].copy()
    dff_clip["Categoría"] = dff_clip["Código_SA6"].map(SA6_NOMBRE)

    fig3 = px.box(
        dff_clip,
        x="Categoría",
        y="Valor_USD_por_par",
        color="Flujo_comercial",
        color_discrete_map=PALETA,
        points=False,
        labels={"Valor_USD_por_par": "USD por par (valor aduanero)",
                "Flujo_comercial": "Flujo", "Categoría": "Categoría SA6"},
        height=440,
    )
    fig3.update_layout(plot_bgcolor="white", paper_bgcolor="white",
                       legend_title="Flujo")
    st.plotly_chart(fig3, use_container_width=True)

    with st.expander("📌 Lectura empresarial"):
        st.info(
            "**[Dato]** La categoría 640420 tiene el mayor valor por par "
            "(≈ 41–45 USD), frente a ≈ 24–27 USD en 640399 y 640411.  \n"
            "**[Conclusión]** Las líneas de cuero compiten en un nicho de mayor valor unitario "
            "con menor presión de precio.  \n"
            "**[Supuesto]** Son las candidatas naturales a diferenciación para Manaco, "
            "si el costo unitario interno lo permite."
        )

    resumen_par = (
        dff.groupby(["Código_SA6", "Flujo_comercial"])
        .agg(
            Valor_total_MUSD=("Valor_USD", lambda s: round(s.sum() / 1e6, 1)),
            Pares_M=("Cantidad_pares", lambda s: round(s.sum() / 1e6, 1)),
            VPP_ponderado=("Valor_USD", "sum"),
            _pares=("Cantidad_pares", "sum"),
            VPP_media=("Valor_USD_por_par", "mean"),
        )
    )
    resumen_par["VPP_ponderado"] = (resumen_par["VPP_ponderado"] / resumen_par["_pares"]).round(2)
    resumen_par["VPP_media"] = resumen_par["VPP_media"].round(2)
    resumen_par = resumen_par.drop(columns="_pares")
    resumen_par.index = resumen_par.index.set_levels(
        [SA6_NOMBRE.get(x, x) for x in resumen_par.index.levels[0]], level=0
    )
    st.dataframe(resumen_par, use_container_width=True)

# ── TAB 4: Indicadores ────────────────────────────────────────────────────────
with tab4:
    st.subheader("Tabla de indicadores por categoría × flujo")

    ind = dff.groupby(["Código_SA6", "Flujo_comercial"]).agg(
        Valor_total_MUSD=("Valor_USD", lambda s: round(s.sum() / 1e6, 2)),
        Pares_totales_M=("Cantidad_pares", lambda s: round(s.sum() / 1e6, 2)),
        Socios_distintos=("Socio_comercial", "nunique"),
    )
    agr = dff.groupby(["Código_SA6", "Flujo_comercial"])
    ind["VPP_ponderado"] = (agr["Valor_USD"].sum() / agr["Cantidad_pares"].sum()).round(2)
    ind["Part_valor_%"] = (
        ind["Valor_total_MUSD"] / ind.groupby("Flujo_comercial")["Valor_total_MUSD"].transform("sum") * 100
    ).round(1)
    ind["Part_pares_%"] = (
        ind["Pares_totales_M"] / ind.groupby("Flujo_comercial")["Pares_totales_M"].transform("sum") * 100
    ).round(1)
    ind.index = ind.index.set_levels(
        [SA6_NOMBRE.get(x, x) for x in ind.index.levels[0]], level=0
    )
    st.dataframe(ind, use_container_width=True)

    st.divider()
    st.subheader("Ranking de socios: valor vs. cantidad")
    flujo_rank = st.selectbox("Seleccionar flujo", options=dff["Flujo_comercial"].unique().tolist())
    sub_rank = (
        dff[dff["Flujo_comercial"] == flujo_rank]
        .groupby("Socio_comercial")
        .agg(Valor_MUSD=("Valor_USD", lambda s: round(s.sum() / 1e6, 1)),
             Pares_M=("Cantidad_pares", lambda s: round(s.sum() / 1e6, 1)))
    )
    sub_rank["Rank_valor"] = sub_rank["Valor_MUSD"].rank(ascending=False, method="min").astype(int)
    sub_rank["Rank_pares"] = sub_rank["Pares_M"].rank(ascending=False, method="min").astype(int)
    sub_rank["Δ_posiciones"] = sub_rank["Rank_pares"] - sub_rank["Rank_valor"]
    sub_rank["VPP_USD"] = (sub_rank["Valor_MUSD"] * 1e6 / (sub_rank["Pares_M"] * 1e6)).round(2)
    sub_rank = sub_rank.sort_values("Rank_valor")
    st.dataframe(
        sub_rank.style.background_gradient(subset=["Δ_posiciones"], cmap="RdYlGn_r"),
        use_container_width=True,
    )
    st.caption(
        "Δ positivo = el socio sube posiciones al ordenar por cantidad (más volumen, menor valor/par). "
        "Δ negativo = baja posiciones (menos volumen, mayor valor/par)."
    )

# ── TAB 5: Calidad de datos ────────────────────────────────────────────────────
with tab5:
    st.subheader("Inspección de calidad de la base")

    col_q1, col_q2, col_q3 = st.columns(3)
    col_q1.metric("Total de filas", f"{len(df):,}")
    col_q2.metric("Nulos en toda la base", int(df.isna().sum().sum()))
    col_q3.metric("Registros 'Mundo' separados", len(mundo))

    st.markdown("**Nulos por columna**")
    nulos = df.isna().sum().reset_index()
    nulos.columns = ["Columna", "Nulos"]
    st.dataframe(nulos, use_container_width=True, hide_index=True)

    st.markdown("**Validación de integridad numérica**")
    dif_v = ((df["Valor_miles_USD"] * 1000 - df["Valor_USD"]).abs() / df["Valor_USD"]).max()
    dif_p = (df["Valor_USD"] / df["Cantidad_pares"] - df["Valor_USD_por_par"]).abs().max()
    ok_v = "✅" if dif_v < 1e-3 else "❌"
    ok_p = "✅" if dif_p < 0.01 else "❌"
    st.markdown(f"- {ok_v} `Valor_miles_USD × 1000 ≈ Valor_USD` — diferencia máxima: `{dif_v:.2e}`")
    st.markdown(f"- {ok_p} `Valor_USD / Cantidad_pares ≈ Valor_USD_por_par` — diferencia máxima: `{dif_p:.4f} USD`")

    clave = ["Flujo_comercial", "Año", "Código_SA6", "Socio_comercial"]
    rep = df[df.duplicated(clave, keep=False)]
    st.markdown(f"**Filas con clave repetida (flujo, año, SA6, socio):** {len(rep)} "
                f"({'conservadas — valores distintos, no son duplicados exactos' if len(rep) > 0 else 'ninguna'})")
    if len(rep) > 0:
        st.dataframe(rep.head(8), use_container_width=True)

    st.markdown("**Distribución de registros por año y flujo**")
    dist = df.groupby(["Año", "Flujo_comercial"]).size().unstack(fill_value=0)
    st.dataframe(dist, use_container_width=True)