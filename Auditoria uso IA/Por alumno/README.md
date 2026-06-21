# Bitácora de Auditoría de IA: Registro de Interacciones

Esta bitácora es un instrumento de recolección de datos diseñado para analizar la interacción humano-máquina en el desarrollo de software. Los datos aquí registrados serán procesados mediante técnicas de **Visual Analytics** para identificar patrones de dependencia, eficiencia y calidad de respuesta.

## Estructura de Registro

| Variable | Tipo de dato / Formato |
| :--- | :--- |
| **IA_Nombre** | Categoría (OpenAI, Anthropic, Google, Meta, Otros) |
| **Modelo** | Texto (ej: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro) |
| **Plan_Suscripcion** | Categoría (Free, Pro, Enterprise, API) |
| **Tipo_Consulta** | **Selección única (Dropdown)**: [Código, Teórica, Review, Emocional, Aspiracional, Otro] |
| **Descripcion_Prompt** | Texto breve (resumen de la solicitud realizada) |
| **Volumen_Mensajes** | Numérico (cantidad de iteraciones en el hilo) |
| **Uso_Documentos** | Binario (SÍ / NO - si se adjuntaron archivos o contextos extra) |
| **Precisa_Correccion** | Binario (SÍ / NO - si el código/respuesta tuvo errores técnicos) |
| **Replicabilidad_Autonoma** | Binario (SÍ / NO - ¿puedes explicar/reproducir la lógica sin la IA?) |
| **Alternativa_Manual** | Texto (¿Qué fuentes consultarías si la IA no existiera?) |

---

## Guía 

Si quieres aplicar este log donde sea **graficable** y tenga valor analítico, se recomienda respetar las siguientes directrices:

1.  **Tipo_Consulta:** Es la variable clave para la segmentación.
    *   *Código*: Solicitud directa de generación de scripts o funciones.
    *   *Teórica*: Consultas conceptuales sobre la cátedra.
    *   *Code Review*: Petición de refactorización o auditoría de código propio.
    *   *Emocional*: Consultas sobre frustración, bloqueo o síndrome del impostor (relevante para el estudio de salud mental en ingeniería).
    *   *Aspiracional*: Consultas sobre carrera, trayectoria profesional o visión de futuro.
2.  **Replicabilidad_Autonoma:** Esta es la variable de **"Integridad del Aprendizaje"**. Si la respuesta es "NO", significa que el alumno está en una fase de "caja negra" y debe priorizar la comprensión teórica antes que la ejecución automática.
3.  **Alternativa_Manual:** Esta columna nos permite auditar el nivel de **alfabetización informacional** del alumno (si sabe buscar en la documentación oficial, StackOverflow, libros o si depende de terceros).
