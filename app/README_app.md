# App · Dashboard de Comercio — Manaco

## Cómo ejecutar

```bash
# Desde la raíz del repositorio
streamlit run app/dashboard.py
```

Se abrirá automáticamente en http://localhost:8501

## Funcionalidades

| Pestaña | Contenido |
|---|---|
| 📈 Importación vs Exportación | Gráficos de línea interactivos con valor (millones USD) y pares por año. |
| 🌍 Socios comerciales | Barras apiladas Top N socios; tablas de ranking por valor y cantidad. |
| 💰 Valor por par | Boxplot interactivo por categoría SA6 y flujo; tabla de VPP ponderado. |
| 📊 Indicadores | Tabla de indicadores con participación %; ranking dual valor vs. cantidad con Δ posiciones resaltado. |
| 🔍 Calidad de datos | Validación de integridad numérica, nulos, duplicados, distribución por año. |

## Filtros disponibles (sidebar)
- Cargar tu propio Excel (o usa el de `data/raw/` automáticamente).
- Flujo comercial (Importación / Exportación).
- Rango de años.
- Categoría SA6.
