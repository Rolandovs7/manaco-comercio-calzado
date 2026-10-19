# Checklist de verificación — manaco-comercio-calzado

## ✅ Completado

### Archivos raíz
- [x] `README.md` — contexto, diccionario de datos, advertencia metodológica, hallazgos, limitaciones, cómo reproducir.
- [x] `requirements.txt` — versiones fijadas (pandas, openpyxl, matplotlib, seaborn, jupyter).
- [x] `.gitignore` — excluye .venv/, __pycache__/, .ipynb_checkpoints/, data/processed/*.csv, *.png fuera de docs/.
- [x] `data/raw/` — carpeta creada; el binario `Base_de_Datos.xlsx` no se versiona.
- [x] `data/processed/.gitkeep` — carpeta versionada sin datos.

### src/
- [x] `carga.py` — función `cargar()`: lee el Excel, convierte tipos, valida integridad numérica (AssertionError si falla), separa "Mundo", guarda CSV.
- [x] `carga.py` — función `resumen_calidad()`: imprime filas, columnas, nulos, años, países, SA6, filas con clave repetida.
- [x] `graficos.py` — `grafico_import_export()`: líneas valor y cantidad por año y flujo.
- [x] `graficos.py` — `grafico_top_socios()`: barras apiladas top 10 socios.
- [x] `graficos.py` — `grafico_valor_par()`: boxplot por SA6 y flujo, recortado al P95.
- [x] Todos los gráficos exportan PNG a `docs/` con dpi=130 y devuelven la ruta.
- [x] Estilo seaborn "whitegrid", paleta diferenciada por flujo, títulos en español.

### notebooks/ (ejecutados y verificados sin errores)
- [x] `01_inspeccion.ipynb` — 5 celdas: objetivo, carga + resumen, diccionario, calidad + duplicados, integridad numérica, conclusiones.
- [x] `02_eda_graficos.ipynb` — 8 celdas: objetivo, carga, 3 gráficos con interpretación empresarial, pivote categoría × flujo, valor por par ponderado, hallazgos.
- [x] `03_indicadores_sintesis.ipynb` — 5 celdas: objetivo, tabla de indicadores con participación %, rankings por valor y cantidad, comparación de posiciones, síntesis ejecutiva.

### docs/
- [x] `estacion_1_problemas.md` — factores internos y externos, tabla de 5 problemas priorizados, respuesta a las 6 preguntas orientadoras.
- [x] `estacion_2_sintesis.md` — 3 hallazgos con evidencia numérica, 2 limitaciones, 1 pregunta estratégica, referencias a los 3 PNG.
- [x] `estacion_3_propuesta.md` — problema, solución (pronóstico + segmentación), 3 objetivos SMART con KPI, áreas y roles, 2 riesgos con mitigación, datos a capturar.
- [x] `estacion_4_alternativas.md` — comparación A vs. B, recomendación ejecutiva justificada con datos, segmento + acción comercial, 3 indicadores con fórmula y meta.
- [x] `estacion_5_exposicion.md` — guion de 10 diapositivas (~1 min c/u), cierre con distinción dato/supuesto/conclusión, 5 preguntas del jurado con respuesta.

---

## ⚠️ Requiere datos internos de Manaco (no disponibles en la base externa)

| Ítem | Por qué es necesario | Dónde se necesita |
|---|---|---|
| Ventas históricas por SKU, canal y región | Sin esto, el modelo de pronóstico no puede construirse ni evaluarse. | Estación 3, modelo de pronóstico; notebooks para validar supuestos. |
| Costo unitario de producción por línea | Sin esto, no se puede calcular el margen ni confirmar que la diferenciación en cuero es rentable. | Estaciones 3 y 4; KPI de margen bruto. |
| Datos de clientes (ID, frecuencia, ticket, canal) | Sin esto, la segmentación RFM no puede ejecutarse. | Estación 3, módulo de segmentación. |
| Registros de defectos y devoluciones | Sin esto, no se puede medir la calidad del proceso ni modelar la causa raíz. | Estación 4, análisis de calidad mencionado como dato complementario. |
| Importaciones de calzado a Bolivia por origen, categoría y valor | Sin esto, los rangos de valor aduanero del benchmark de España no pueden validarse como referencia del mercado boliviano. | Estación 1, problema 1; Estaciones 2 y 4. |
| Stock y tiempos de producción por línea | Sin esto, el modelo de inventario no puede construirse. | Estación 3, módulo de pronóstico. |

---

## 📋 Notas de reproducibilidad

- El código fue desarrollado y probado con **pandas 3.0.2** y **matplotlib 3.10.8**; es compatible con las versiones fijadas en `requirements.txt` (pandas 2.2.2, matplotlib 3.8.4) porque no usa API específica de versión.
- Los notebooks deben ejecutarse en orden: primero `01`, luego `02`, luego `03`.
- `src/carga.py` debe ejecutarse antes de los notebooks para generar `data/processed/comercio_calzado.csv`.
- Los 3 PNG se generan automáticamente al ejecutar `02_eda_graficos.ipynb` o `python src/graficos.py`.
- La base tiene 240 registros (sin filas "Mundo" ni nulos). Hay 20 filas con clave repetida (flujo, año, SA6, socio) con valores distintos; se conservan porque no son duplicados exactos.
