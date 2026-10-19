# docs/estacion_3_propuesta.md
# Estación 3 — Propuesta estratégica de Ciencia de Datos

---

## Ficha de propuesta estratégica

**Empresa:** Manaco S.A. (Bolivia)
**Área impulsora:** Gerencia General / Dirección Comercial
**Fecha:** octubre de 2026
**Vigencia del plan:** 3 años (2027-2029)

---

### Problema que resuelve

Manaco no puede anticipar la demanda por línea de producto y región, lo que genera sobreproducción en algunas líneas, desabasto en otras e ineficiencia en la asignación de recursos. Al mismo tiempo, la empresa desconoce qué segmentos de clientes son más rentables y cuáles tienen mayor potencial de crecimiento. Esta doble ceguera —sin pronóstico y sin segmentación— impide responder a tiempo a la presión de las importaciones y a los cambios en las preferencias del consumidor.

---

### Solución propuesta: Sistema integrado de pronóstico de demanda y segmentación de clientes

La solución combina dos módulos de Ciencia de Datos que se alimentan de los datos internos de Manaco:

1. **Módulo de pronóstico de demanda (Forecasting):** modelos de series de tiempo (Prophet o SARIMA según la frecuencia de los datos disponibles) que proyectan la demanda por SKU, línea y región con horizonte de 3 a 6 meses. El modelo se reentrenará mensualmente. Las salidas alimentan directamente la planificación de producción y el reabastecimiento de inventario.

2. **Módulo de segmentación de clientes (RFM + clustering):** segmentación basada en Recencia, Frecuencia y Valor monetario de las compras, más variables de canal (tienda física, distribuidor, digital) y región. Permite identificar los segmentos de mayor rentabilidad y diseñar acciones comerciales específicas para cada uno.

**Datos que la solución necesita (hoy no disponibles en formato analítico):**
ventas históricas por SKU, fecha, canal y región (mínimo 2 años); datos de clientes (ID, canal, frecuencia, ticket); costos unitarios por línea; registros de devoluciones y defectos.

---

### Tres objetivos SMART y sus KPI

| N.° | Objetivo | Indicador (KPI) | Meta a 3 años |
|---|---|---|---|
| 1 | **Reducir el error de pronóstico de demanda** para las 5 líneas de mayor volumen. | MAPE (Mean Absolute Percentage Error) por línea, calculado mensualmente. | MAPE ≤ 15% en las 5 líneas al cierre de 2029. |
| 2 | **Incrementar el margen bruto** de las líneas de cuero y diferenciadas, redirigiendo recursos de las líneas de bajo margen. | Margen bruto (%) por línea, reportado trimestralmente. | Incremento de 5 pp en el margen bruto de las líneas de cuero al cierre de 2028. |
| 3 | **Aumentar la retención del segmento de mayor valor** (clientes top 20% por valor de compra). | Tasa de retención anual del segmento de mayor valor (compras en los últimos 12 meses). | Tasa de retención ≥ 75% al cierre de 2028. |

---

### Áreas involucradas y su rol

| Área | Rol |
|---|---|
| **Comercial / Marketing** | Define los segmentos objetivo, valida los perfiles de cliente y ejecuta las acciones comerciales derivadas de la segmentación. |
| **Producción** | Consume los pronósticos de demanda para ajustar el plan de producción; reporta capacidad instalada y tiempos de ciclo. |
| **Logística / Distribución** | Ajusta el reabastecimiento de almacenes según el pronóstico; reporta niveles de stock y tiempos de entrega. |
| **Finanzas** | Provee costos unitarios por línea y valida los KPI de margen; aprueba el presupuesto de implementación. |
| **TI** | Integra las fuentes de datos (ERP, punto de venta, CRM) en un repositorio analítico; mantiene la infraestructura de modelos. |

---

### Dos riesgos de implementación y su mitigación

| Riesgo | Probabilidad | Impacto | Medida de mitigación |
|---|---|---|---|
| **Datos internos insuficientes o de baja calidad** (ventas sin granularidad de SKU, sin fechas, sin canal). | Alta | Alto | Iniciar de inmediato un proceso de captura estructurada de datos en el ERP y el punto de venta antes del desarrollo del modelo; establecer un diccionario de datos y un responsable de calidad del dato en TI. |
| **Baja adopción por parte de las áreas de negocio** (producción y comercial no usan las salidas del modelo). | Media | Alto | Diseñar un tablero de control simple (no técnico) que presente los pronósticos y segmentos en lenguaje de negocio; involucrar a los gerentes de área en la definición de los KPI desde el inicio del proyecto. |

---

### Datos internos que Manaco debe empezar a capturar ahora

1. Ventas diarias por SKU, canal (tienda propia / distribuidor / digital) y región (ciudad o departamento).
2. Datos de cliente: identificador único, frecuencia de compra, ticket promedio, línea preferida.
3. Costos unitarios de producción por línea y por SKU.
4. Registros de devoluciones y defectos (motivo, línea, fecha, volumen).
5. Stock en almacén por SKU con fecha de ingreso y salida.
