"""Gráficos del análisis exploratorio de comercio de calzado (España, benchmark)."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

RAIZ = Path(__file__).resolve().parents[1]
DIR_DOCS = RAIZ / "docs"
DPI = 130
PALETA_FLUJO = {"Importación": "#c0392b", "Exportación": "#1f77b4"}
ETIQUETAS_SA6 = {
    "640411": "640411\nDeportivo",
    "640399": "640399\nCuero superior\n(suela caucho/plástico)",
    "640420": "640420\nSuela de cuero",
}

sns.set_theme(style="whitegrid")


def _preparar_ruta(ruta):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    return ruta


def grafico_import_export(df, ruta=DIR_DOCS / "grafico_1_import_export.png"):
    """Líneas de valor (millones USD) y cantidad (millones de pares) por año y flujo."""
    ruta = _preparar_ruta(ruta)
    anual = (
        df.groupby(["Año", "Flujo_comercial"], as_index=False)[["Valor_USD", "Cantidad_pares"]].sum()
    )
    anual["Valor_millones_USD"] = anual["Valor_USD"] / 1e6
    anual["Cantidad_millones_pares"] = anual["Cantidad_pares"] / 1e6

    fig, ejes = plt.subplots(1, 2, figsize=(13, 5))
    for eje, col, titulo, etiqueta in [
        (ejes[0], "Valor_millones_USD", "Valor comercial por año", "Millones de USD"),
        (ejes[1], "Cantidad_millones_pares", "Cantidad de pares por año", "Millones de pares"),
    ]:
        sns.lineplot(data=anual, x="Año", y=col, hue="Flujo_comercial",
                     palette=PALETA_FLUJO, marker="o", linewidth=2.2, ax=eje)
        eje.set_title(titulo)
        eje.set_xlabel("Año")
        eje.set_ylabel(etiqueta)
        eje.set_xticks(sorted(anual["Año"].unique()))
        eje.legend(title="Flujo")
    fig.suptitle("Importaciones vs. exportaciones de calzado de España, 2020-2024", fontsize=14)
    fig.tight_layout()
    fig.savefig(ruta, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return ruta


def grafico_top_socios(df, ruta=DIR_DOCS / "grafico_2_top_socios.png", top_n=10):
    """Barras horizontales apiladas (importación + exportación) de los top N socios por valor total."""
    ruta = _preparar_ruta(ruta)
    pivote = (
        df.pivot_table(index="Socio_comercial", columns="Flujo_comercial",
                       values="Valor_USD", aggfunc="sum", fill_value=0) / 1e6
    )
    for flujo in PALETA_FLUJO:
        if flujo not in pivote.columns:
            pivote[flujo] = 0.0
    pivote["Total"] = pivote["Importación"] + pivote["Exportación"]
    top = pivote.nlargest(top_n, "Total").sort_values("Total")

    fig, eje = plt.subplots(figsize=(11, 6))
    izquierda = None
    for flujo in ["Importación", "Exportación"]:
        eje.barh(top.index, top[flujo], left=izquierda, label=flujo, color=PALETA_FLUJO[flujo])
        izquierda = top[flujo] if izquierda is None else izquierda + top[flujo]
    eje.set_title(f"Top {top_n} socios comerciales por valor total (2020-2024)")
    eje.set_xlabel("Millones de USD acumulados")
    eje.set_ylabel("Socio comercial")
    eje.legend(title="Flujo")
    fig.tight_layout()
    fig.savefig(ruta, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return ruta


def grafico_valor_par(df, ruta=DIR_DOCS / "grafico_3_valor_par.png"):
    """Boxplot de Valor_USD_por_par por Código_SA6 y flujo (valores extremos recortados al P95)."""
    ruta = _preparar_ruta(ruta)
    p95 = df.groupby(["Código_SA6", "Flujo_comercial"])["Valor_USD_por_par"].transform(
        lambda s: s.quantile(0.95)
    )
    datos = df[df["Valor_USD_por_par"] <= p95].copy()
    datos["Categoría"] = datos["Código_SA6"].map(ETIQUETAS_SA6)
    orden = [ETIQUETAS_SA6[c] for c in ["640411", "640399", "640420"] if c in set(df["Código_SA6"])]

    fig, eje = plt.subplots(figsize=(11, 6))
    sns.boxplot(data=datos, x="Categoría", y="Valor_USD_por_par", hue="Flujo_comercial",
                order=orden, palette=PALETA_FLUJO, showfliers=False, ax=eje)
    eje.set_title("Valor aduanero por par según categoría y flujo (recortado al percentil 95)")
    eje.set_xlabel("Código SA6 y tipo de calzado")
    eje.set_ylabel("USD por par (valor FOB/CIF aduanero, no precio al consumidor)")
    eje.legend(title="Flujo")
    fig.tight_layout()
    fig.savefig(ruta, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    return ruta


if __name__ == "__main__":
    from carga import cargar

    datos, _ = cargar()
    for funcion in (grafico_import_export, grafico_top_socios, grafico_valor_par):
        print("Generado:", funcion(datos))
