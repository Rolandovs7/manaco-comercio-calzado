# docs/estacion_5_exposicion.md
# Estación 5 — Guion de exposición (10 minutos)

**Formato:** 10 diapositivas · 1 min por diapositiva (aprox.) · Equipo de consultores Ciencia de Datos

---

## Diapositiva 1 — Portada (0:00–0:30)

**Título:** "Manaco: diagnóstico y propuesta estratégica basada en datos"
**Subtítulo:** Consultoría de Ciencia de Datos · octubre de 2026
**Qué se dice:** "Presentamos el resultado de un análisis de benchmark externo del comercio internacional de calzado, con el objetivo de apoyar las decisiones estratégicas de la Gerencia General de Manaco."
**Qué se muestra:** Logotipo del grupo / materia, integrantes.

---

## Diapositiva 2 — El problema de Manaco (0:30–1:30)

**Título:** "Tres presiones simultáneas sobre la competitividad"
**Qué se dice:** "Manaco enfrenta importaciones baratas, cambios en preferencias del consumidor y costos crecientes, sin datos integrados que le permitan tomar decisiones rápidas. Este es el punto de partida."
**Qué se muestra:** Diagrama de tres vectores (importaciones / consumidor / costos) convergiendo en Manaco. Sin datos: problema transversal.

---

## Diapositiva 3 — La base de datos y la metodología (1:30–2:15)

**Título:** "Benchmark externo: comercio de calzado de España, 2020-2024"
**Qué se dice:** "Analizamos 240 registros de importación y exportación de calzado español, organizados en tres categorías SA6. Esta base **no es de Bolivia ni de Manaco**; la usamos como referencia de valor aduanero y estructura de mercado. Todos los datos son de España; los supuestos sobre Manaco los declararemos explícitamente."
**Qué se muestra:** Tabla de diccionario de las 5 columnas clave + advertencia metodológica sobre valor por par.

---

## Diapositiva 4 — Hallazgo 1: la importación supera a la exportación (2:15–3:15)

**Título:** "Las importaciones pesan 1,7 veces más que las exportaciones en valor"
**Qué se dice:** "El benchmark registra 18.506 millones de USD importados frente a 10.917 millones exportados. La presión importadora es estructural. Para Manaco, esto implica que competir solo por precio no es viable: el calzado importado llega a un valor aduanero de referencia de 24–27 USD/par."
**Qué se muestra:** Gráfico 1 (`grafico_1_import_export.png`): líneas de valor y cantidad por año y flujo.

---

## Diapositiva 5 — Hallazgo 2: concentración en una categoría y nicho de cuero (3:15–4:15)

**Título:** "640399 domina el volumen; 640420 domina el valor por par"
**Qué se dice:** "La categoría de cuero con suela de caucho concentra el 63% del valor importado. Pero la categoría de suela de cuero tiene un valor por par de 41–45 USD, un 70% más alto, con menor competencia. Ese es el nicho defensivo de Manaco."
**Qué se muestra:** Gráfico 3 (`grafico_3_valor_par.png`): boxplot de valor por par por categoría y flujo.

---

## Diapositiva 6 — Hallazgo 3: valor ≠ cantidad (4:15–5:00)

**Título:** "Ordenar por valor o por pares cambia el mapa de competidores"
**Qué se dice:** "Irlanda: 4.° por valor, 14.° por cantidad; 42 USD/par → proveedor de nicho. República Checa: 3.ª por cantidad, 10.ª por valor; 9,3 USD/par → proveedor de volumen barato. Medir solo por valor oculta al competidor de precio."
**Qué se muestra:** Tabla de ranking doble (valor vs. cantidad) con los socios que más cambian de posición. Gráfico 2 (`grafico_2_top_socios.png`) como apoyo visual.

---

## Diapositiva 7 — Propuesta estratégica (5:00–6:30)

**Título:** "Sistema de pronóstico de demanda + segmentación de clientes"
**Qué se dice:** "Proponemos dos módulos: (1) pronóstico de demanda por SKU y región para planificar la producción con un error objetivo menor al 15%, y (2) segmentación RFM para identificar los clientes más rentables y diseñar acciones específicas. La condición es que Manaco empiece a capturar datos de ventas por SKU, canal y región de inmediato."
**Qué se muestra:** Diagrama de flujo: datos internos → modelos → decisiones (producción / marketing). Tabla de 3 objetivos SMART y sus KPI.

---

## Diapositiva 8 — Recomendación: diferenciación en cuero (6:30–7:45)

**Título:** "Priorizar la diferenciación en cuero sobre el volumen deportivo"
**Qué se dice:** "El nicho de cuero tiene un valor de referencia 70% superior y menos saturación competitiva. La acción comercial concreta: lanzar una línea de cuero con identidad boliviana en Santa Cruz, La Paz y Cochabamba, con precio en el rango 300–450 BOB. Meta año 1: cuero = 20% de las ventas, margen bruto ≥ 35%."
**Qué se muestra:** Tabla comparativa Alternativa A vs. B (beneficio, costos, riesgos). Segmento: profesionales urbanos 25-45 años.

---

## Diapositiva 9 — Limitaciones y datos que faltan (7:45–8:45)

**Título:** "Lo que la evidencia soporta y lo que requiere datos internos"
**Qué se dice:** "Toda esta presentación se basa en un benchmark externo de España. No tenemos datos de Bolivia ni de Manaco. El valor por par es valor aduanero, no precio al consumidor. Antes de comprometer inversión, Manaco debe validar los costos unitarios de sus líneas de cuero."
**Qué se muestra:** Tabla de 3 columnas: **[Dato]** / **[Supuesto]** / **[Conclusión]**. Resumen de lo que falta: costos, ventas por SKU, datos de clientes.

---

## Diapositiva 10 — Cierre y próximos pasos (8:45–10:00)

**Título:** "La pregunta que Manaco debe responder primero"
**Qué se dice:** "¿Cuál es el costo por par de las líneas de cuero y cuánto margen tiene Manaco para competir? Con esa cifra, la estrategia de diferenciación pasa de ser un supuesto a ser una decisión fundada. El siguiente paso es capturar ese dato y construir el modelo de pronóstico."
**Qué se muestra:** Cronograma de 3 hitos a 6 meses: (1) captura de datos → (2) modelo piloto → (3) tablero de control para Gerencia. Contacto del equipo.

---

## Distinción explícita: dato, supuesto y conclusión

| Tipo | Definición | Ejemplos en esta exposición |
|---|---|---|
| **[Dato]** | Cifra o hecho extraído directamente del Excel de España. | 18.506 millones de USD importados; valor por par 640420 = 41–45 USD. |
| **[Supuesto]** | Extrapolación por analogía entre España y Bolivia/Manaco, no verificada. | "Manaco podría tener ventajas de abastecimiento local en cuero." |
| **[Conclusión]** | Afirmación que se puede sostener con la evidencia disponible. | "La presión importadora es estructural en el mercado de referencia." |

---

## Cinco preguntas anticipadas del jurado

**P1: ¿Por qué el valor por par no equivale al precio al consumidor?**
El `Valor_USD_por_par` es el valor aduanero (FOB en origen o CIF en destino) registrado en aduana. No incluye los márgenes del importador, distribuidor y retailer, ni los impuestos nacionales (IVA, aranceles de internación) ni los costos de logística interna. El precio al consumidor puede ser 2–4 veces mayor según el canal y el país de destino.

**P2: ¿Cómo cambian las conclusiones si se mide por cantidad en lugar de valor?**
Cambia el mapa de competidores: República Checa sube del 10.° al 3.° puesto en importación al ordenar por pares. Un ranking solo por valor subestima al competidor de volumen barato. Por eso el notebook 03 presenta ambos rankings y muestra explícitamente qué socios cambian de posición.

**P3: ¿Por qué usan datos de España si Manaco opera en Bolivia?**
No existen datos públicos de comercio de calzado de Bolivia en el nivel de granularidad requerido para este ejercicio. España es el benchmark externo disponible: permite ilustrar la metodología (categorías SA6, valor aduanero por par, estructura importación/exportación) y establecer rangos de referencia, con la limitación explícita de que no son datos de Bolivia.

**P4: ¿Qué tan confiables son los rangos de valor por par como referencia para Bolivia?**
Son una referencia de orden de magnitud, no un precio de mercado boliviano. El calzado ingresa a Bolivia por distintos canales (formal, informal, zona franca) y con estructuras de costo diferentes a las de España. La recomendación solo usa el diferencial relativo entre categorías (cuero vs. deportivo) como argumento de posicionamiento, no los valores absolutos.

**P5: ¿Qué pasaría si Manaco decide no capturar datos internos?**
Sin datos de ventas por SKU, canal y región, los modelos de pronóstico y segmentación no son viables. La empresa seguiría tomando decisiones de producción y marketing basadas en intuición, con el riesgo de sobreproducir líneas sin demanda, perder cuota frente a importaciones y no poder medir el retorno de ninguna acción comercial. La captura de datos es la condición previa a cualquier solución de Ciencia de Datos.
