# manaco-comercio-calzado

Consultoría de Ciencia de Datos para **MANACO** (Bolivia): análisis del comercio exterior de calzado de España (2020-2024) como **benchmark externo**.

## 1. Contexto de Manaco
Manaco es una empresa boliviana de calzado con trayectoria en el mercado nacional. Enfrenta importaciones de bajo costo, cambios en las preferencias del consumidor, presión de costos (producción, almacenamiento, distribución) y canales digitales. Necesita convertir información de mercado en decisiones comerciales y operativas.

**Rol del equipo:** consultores de Ciencia de Datos contratados por la Gerencia General. Cada gráfico e indicador se conecta con un problema de negocio y una decisión concreta.

## 2. Advertencia metodológica
- La base es de **España**, no de Bolivia ni de Manaco. Se usa como **referencia externa**; no sustituye datos internos.
- `Valor_USD_por_par` es un **valor aduanero (FOB/CIF) por par**. **No es el precio al consumidor**: excluye márgenes de distribución y retail, impuestos y logística.
- La base contiene 240 registros (40 por combinación categoría × flujo), con distribución desigual por año; debe leerse como una muestra, no como el universo del comercio español.

## 3. Base de datos
Archivo: `data/raw/Base_de_Datos.xlsx`, hoja `Base de Datos` (no se versiona el binario).

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| País_reportante | texto | — | País que reporta (España) |
| Flujo_comercial | texto | — | Importación / Exportación |
| Año | entero | año | 2020 a 2024 |
| Código_SA6 | texto | — | Código del Sistema Armonizado a 6 dígitos |
| Categoría_calzado | texto | — | Descripción de la categoría SA6 |
| Socio_comercial | texto | — | País de origen (importación) o destino (exportación) |
| Valor_miles_USD | decimal | miles de USD | Valor comercial |
| Cantidad_pares | decimal | pares | Volumen |
| Valor_USD | decimal | USD | Valor_miles_USD × 1000 |
| Valor_USD_por_par | decimal | USD/par | Valor_USD / Cantidad_pares |

| Código SA6 | Tipo de calzado |
|---|---|
| 640411 | Calzado deportivo con suela de caucho/plástico |
| 640399 | Calzado con suela de caucho/plástico y parte superior de cuero |
| 640420 | Calzado con suela de cuero y parte superior de cuero/material similar |

## 4. Informe de consultoría
El informe escrito completo (14 tablas, 3 figuras, 4 estaciones) está en:

📄 [`docs/Informe_Manaco_Ciencia_de_Datos.pdf`](docs/Informe_Manaco_Ciencia_de_Datos.pdf)

## 5. Estructura del repositorio
```
manaco-comercio-calzado/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/Base_de_Datos.xlsx          ← no versionado
│   └── processed/.gitkeep
├── notebooks/
│   ├── 01_inspeccion.ipynb
│   ├── 02_eda_graficos.ipynb
│   └── 03_indicadores_sintesis.ipynb
├── src/
│   ├── carga.py
│   └── graficos.py
├── app/
│   └── dashboard.py                    ← app web Streamlit
└── docs/
    ├── Informe_Manaco_Ciencia_de_Datos.pdf
    ├── estacion_1_problemas.md
    ├── estacion_2_sintesis.md
    ├── estacion_3_propuesta.md
    ├── estacion_4_alternativas.md
    ├── estacion_5_exposicion.md
    ├── grafico_1_import_export.png
    ├── grafico_2_top_socios.png
    └── grafico_3_valor_par.png
```

## 6. Cómo reproducir
```bash
# 1. Crear entorno virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Copiar el Excel original
cp /ruta/al/Documento_de_R.xlsx data/raw/Base_de_Datos.xlsx

# 4. Validar la base y generar el CSV procesado
python src/carga.py

# 5. Ejecutar los notebooks en orden
jupyter notebook

# 6. Lanzar el dashboard interactivo
streamlit run app/dashboard.py
```

El dashboard se abre automáticamente en http://localhost:8501

## 7. Hallazgos principales
1. **Mercado importador y en expansión:** 18.506 M USD importados vs. 10.917 M USD exportados (déficit de 7.589 M USD); importaciones crecieron 324,3% entre 2020 y 2024.
2. **Dos juegos comerciales por valor por par:** categorías 640399 y 640411 compiten en el rango 23–27 USD/par; la categoría 640420 (cuero) opera a 41–45 USD/par, casi el doble.
3. **Valor ≠ cantidad:** Irlanda es 4.ª por valor y 14.ª por pares (42 USD/par); República Checa es 3.ª por pares y 10.ª por valor (9,3 USD/par). Un ranking por una sola métrica oculta la naturaleza del competidor.

## 8. Limitaciones
- No existen datos internos de Manaco (ventas, costos, inventario, defectos, clientes).
- La base es de España; no representa el mercado boliviano.
- El valor por par es valor aduanero, no precio al consumidor.

## 9. Autor
Rolando Velasco Soliz · Materia: Ciencia de Datos e Inteligencia de Negocios · 6.º Semestre · Octubre 2026
