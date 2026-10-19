# docs/estacion_1_problemas.md
# Estación 1 — Comprensión del caso empresarial

**Contexto (resumen ejecutivo).** Manaco es una empresa boliviana de calzado con presencia nacional en múltiples segmentos. Enfrenta un entorno de creciente competencia por importaciones de bajo costo, cambios en preferencias del consumidor y adopción acelerada de canales digitales, mientras presiona sus costos de producción, almacenamiento y distribución. La Ciencia de Datos es el eje estratégico para transformar registros en decisiones.

---

## Factores externos que afectan a Manaco

- **Importaciones de bajo costo:** productos de Asia y otros mercados a precios que difícilmente la manufactura local puede igualar sin diferenciación.
- **Cambio en preferencias del consumidor:** crecimiento del calzado deportivo y casual; mayor sensibilidad al diseño y la marca.
- **Digitalización del comercio:** marketplaces y redes sociales desplazan parte del canal físico tradicional.
- **Tipo de cambio y política arancelaria:** variaciones cambiarias y aranceles impactan el costo relativo de importar frente a producir localmente.
- **Entrada de marcas internacionales:** ampliación de la oferta formal e informal en el mercado boliviano.

## Factores internos que afectan a Manaco

- **Presión en costos de producción, almacenamiento y distribución.**
- **Falta de integración entre datos de mercado e información interna** (ventas, inventario, calidad, clientes).
- **Ausencia de sistemas analíticos** para anticipar la demanda o detectar patrones de devolución y defectos.
- **Segmentación de clientes incipiente:** sin perfiles de cliente claros es difícil diseñar acciones comerciales precisas.
- **Canales digitales subdesarrollados** frente a competidores internacionales con presencia en e-commerce.

---

## Tabla de problemas priorizados

| N.° | Problema prioritario | Justificación | Datos necesarios para analizarlo | ¿Se puede responder con la base externa? |
|---|---|---|---|---|
| 1 | **Presión de importaciones baratas sobre la competitividad de Manaco** | Las importaciones de calzado de bajo costo reducen el margen de precio disponible para Manaco. | Importaciones de calzado a Bolivia por origen, categoría, valor y volumen; costos unitarios internos de Manaco. | Parcial (la base externa muestra el rango de valor aduanero por par como referencia, no los datos de Bolivia). |
| 2 | **Desconocimiento del posicionamiento por categoría de producto** | Sin datos de ventas por línea, Manaco no sabe qué categorías son rentables ni cuáles tienen potencial. | Ventas internas por línea, costo por par, margen por categoría. | No (requiere datos internos). |
| 3 | **Incapacidad de anticipar la demanda y gestionar el inventario** | La sobreproducción y el desabasto generan costos financieros y pérdida de ventas. | Histórico de ventas por SKU, tiempos de producción, capacidad instalada, datos de pedidos. | No (requiere datos internos). |
| 4 | **Falta de segmentación de clientes y canales** | Sin perfiles de cliente definidos, los recursos de marketing y distribución se asignan sin criterio. | CRM o base de clientes con frecuencia de compra, ticket promedio, canal, región, edad, línea preferida. | No (requiere datos internos). |
| 5 | **Canales digitales subdesarrollados frente a la competencia** | El canal digital es el principal punto de contacto de los competidores importados con el consumidor boliviano. | Tráfico web/app de Manaco, tasa de conversión, comparación con competidores en plataformas digitales. | No (requiere datos de mercado digital boliviano). |

**Criterio de priorización:** impacto sobre competitividad (presión de precio y posición en el mercado), rentabilidad (margen y eficiencia operativa) y sostenibilidad (continuidad de la empresa a 3 años).

---

## Respuesta a las preguntas orientadoras

**¿Cuáles son los principales desafíos que enfrenta Manaco?**
La combinación de importaciones baratas, fragmentación del mercado por canales digitales y falta de información interna integrada. El riesgo mayor es tomar decisiones de precio y producción sin datos que sustenten esas decisiones.

**¿Qué factores podrían estar afectando su rentabilidad?**
El costo unitario de producción no necesariamente competitivo frente al valor aduanero de referencia del calzado importado (aprox. 24–27 USD/par en las categorías de mayor volumen, según el benchmark externo), más la ineficiencia en inventario y distribución.

**¿Qué diferencias existen entre las regiones y las líneas de productos?**
No se puede responder con la base externa. Requiere datos internos de ventas por región y por línea. Es, precisamente, uno de los primeros datos que Manaco debe capturar de forma sistemática.

**¿Qué información adicional se necesitaría?**
Ventas históricas por SKU y región, costo unitario por línea, datos de clientes (frecuencia, ticket, canal), registros de defectos y devoluciones, importaciones de calzado a Bolivia por origen y categoría.

**¿Qué decisiones mejorarían con mejor uso de datos?**
Política de precios por línea, planificación de producción e inventario, diseño de campañas por segmento de cliente, decisión de qué líneas priorizar o descontinuar, y evaluación del canal digital.

**¿Cuáles son los principales riesgos de decidir sin información suficiente?**
Sobreproducción de líneas sin demanda, subproducción de líneas rentables, pérdida de cuota de mercado por desconocer el precio de referencia del mercado y no poder diferenciarse antes de que sea tarde.
