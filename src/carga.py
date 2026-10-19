"""Carga, tipificación y validación de la base de comercio de calzado de España.

Fuente: base de comercio exterior de calzado de España (2020-2024), usada como
BENCHMARK EXTERNO para el caso Manaco. No contiene datos internos de Manaco.
"""
from pathlib import Path

import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
RUTA_XLSX = RAIZ / "data" / "raw" / "Base_de_Datos.xlsx"
RUTA_CSV = RAIZ / "data" / "processed" / "comercio_calzado.csv"
HOJA = "Base de Datos"

COLUMNAS_NUMERICAS = ["Valor_miles_USD", "Cantidad_pares", "Valor_USD", "Valor_USD_por_par"]
CLAVE = ["Flujo_comercial", "Año", "Código_SA6", "Socio_comercial"]


def cargar(ruta_xlsx=RUTA_XLSX, guardar=True):
    """Lee, tipifica y valida la base. Devuelve (df_paises, df_mundo).

    - df_paises: registros por socio comercial (sin agregados "Mundo").
    - df_mundo: registros agregados "Mundo" (vacío si no existen), separados
      para evitar doble conteo.
    Lanza AssertionError si falla la integridad numérica.
    """
    ruta_xlsx = Path(ruta_xlsx)
    if not ruta_xlsx.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo {ruta_xlsx}. Copie el Excel como "
            "data/raw/Base_de_Datos.xlsx."
        )

    df = pd.read_excel(ruta_xlsx, sheet_name=HOJA)

    # --- Conversión de tipos ---
    df["Año"] = df["Año"].astype(int)
    df["Código_SA6"] = df["Código_SA6"].astype(str)
    for col in COLUMNAS_NUMERICAS:
        df[col] = df[col].astype(float)

    # --- Validación de integridad numérica ---
    assert np.allclose(df["Valor_miles_USD"] * 1000, df["Valor_USD"], rtol=1e-3), (
        "Inconsistencia: Valor_miles_USD * 1000 no coincide con Valor_USD."
    )
    esperado = df["Valor_USD"] / df["Cantidad_pares"]
    assert np.allclose(esperado, df["Valor_USD_por_par"], atol=0.01), (
        "Inconsistencia: Valor_USD / Cantidad_pares no coincide con Valor_USD_por_par."
    )

    # --- Separación de registros agregados "Mundo" (doble conteo) ---
    es_mundo = df["Socio_comercial"].str.strip().str.lower() == "mundo"
    df_mundo = df[es_mundo].copy()
    df_paises = df[~es_mundo].copy().reset_index(drop=True)
    if len(df_mundo) > 0:
        print(f"Aviso: se separaron {len(df_mundo)} registros 'Mundo' para evitar doble conteo.")

    if guardar:
        RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)
        df_paises.to_csv(RUTA_CSV, index=False, encoding="utf-8")

    return df_paises, df_mundo


def resumen_calidad(df):
    """Imprime un resumen de calidad de la base."""
    print("=" * 60)
    print("RESUMEN DE CALIDAD DE DATOS")
    print("=" * 60)
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print("\nNulos por columna:")
    print(df.isna().sum().to_string())
    print(f"\nAños cubiertos: {sorted(df['Año'].unique().tolist())}")
    print(f"Países socios únicos: {df['Socio_comercial'].nunique()}")
    print(f"Categorías SA6 únicas: {sorted(df['Código_SA6'].unique().tolist())}")
    repetidas = int(df.duplicated(subset=CLAVE, keep=False).sum())
    print(f"Filas con clave repetida (flujo, año, SA6, socio): {repetidas}")
    print("=" * 60)


if __name__ == "__main__":
    datos, mundo = cargar()
    resumen_calidad(datos)
    print(f"\nArchivo procesado guardado en: {RUTA_CSV}")
