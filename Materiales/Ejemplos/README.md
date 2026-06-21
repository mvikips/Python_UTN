# Código Fuente, Ejemplos Prácticos y Reproducibilidad — Programación 1 (UTN)

Bienvenido/a al repositorio de artefactos de código y ejemplos prácticos de **Programación 1**. Este espacio está diseñado como el complemento operativo directo de nuestro módulo [Audio Visual](../Audio_Visual/). Aquí se aloja el código fuente exacto expuesto en las sesiones de *Rubberducking*, garantizando la reproducibilidad, el análisis estático y la consulta offline.

---

## Ejecución y Buenas Prácticas

El código alojado en esta sección no es meramente funcional; está diseñado bajo estándares rigurosos de ingeniería de software:
*   **Legibilidad Absoluta:** Alineado estrictamente a las directrices de estilo de la [PEP 8](../Links/).
*   **Documentación Interna:** Cada script cuenta con comentarios estructurados que desglosan la complejidad del algoritmo, el tipo de datos utilizado y la justificación de las estructuras de control elegidas.
*   **Modularidad:** Fomento del aislamiento de lógica mediante funciones, manejo limpio de excepciones y control de ámbitos de variables.

---

## Índice de Scripts y Correspondencia Audiovisual

Para facilitar el autoaprendizaje y la auditoría técnica, podés localizar los archivos de código organizados según el flujo de la currícula oficial:

### 1. Fundamentos y Sintaxis Estructurada
*   `00_HolaMundo.py`: Primer código.
*   `01_definicion_algoritmo.py`: Estructura secuencial base y flujos de control iniciales.
*   `02_manejo_numeros.py`: Operaciones nativas y tipos numéricos.
*   `03_declaracion_variables.py`: Asignación de memoria y nomenclatura estandarizada.
*   `04_strings_inmutabilidad.py`: Manipulación de cadenas de caracteres y métodos integrados.
*   `05_inspeccion_type_casting.py`: Coerción explícita de tipos de datos y funciones de diagnóstico.
*   `06_ambito_variables.py`: Demostración práctica de variables locales, globales y ciclos de vida (*Escopo*).

### 2. Lógica Condicional y Operadores Avanzados
*   `07_operadores_aritmeticos_modulares.py`: Uso de división entera y residuo (`%`) para control de paridad.
*   `08_algebra_booleana_cortocircuito.py`: Tablas de verdad aplicadas y evaluación de cortocircuito con `OR`.
*   `09_captura_segura_input.py`: Flujos de entrada de usuario con parseo y validación de tipos.
*   `10_estructuras_if_elif_else.py`: Bifurcaciones complejas y lógica de negocio condicional.
*   `11_operador_ternario.py`: Simplificación de sentencias asignativas en una sola línea de código.

### 3. Estructuras de Repetición (Bucles)
*   `12_bucle_while_estados.py`: Iteración condicional basada en banderas de control.
*   `13_interrupcion_break_else.py`: Control de flujo avanzado y salidas prematuras de ciclos.
*   `14_bucle_for_iterables.py`: Iteración definida sobre secuencias complejas.
*   `15_secuencias_range.py`: Generación eficiente de rangos inmutables en memoria.
*   `16_simulacion_do_while.py`: Implementación del patrón *repetir-hasta* en la sintaxis de Python.
*   `17_control_continue_pass.py`: Desvío de iteraciones frente a marcadores de posición (*placeholders*).

### 4. Estructuras de Datos Avanzadas (Colecciones)
*   `18_listas_mutabilidad.py`: Secuencias mutables, indexación y direccionamiento.
*   `19_tecnicas_slicing.py`: Particionamiento y sub-indexación avanzada de colecciones.
*   `20_metodos_insercion_mutacion.py`: Uso de `append()`, `extend()`, `sort()` y optimización de ordenamiento.
*   `21_copia_referencia_memoria.py`: Análisis de asignación en memoria: Copia Superficial (*Shallow*) vs. Copia Profunda (*Deep Copy*).
*   `22_tuplas_inmutabilidad.py`: Empaquetado, desempaquetado y seguridad de datos persistentes.
*   `23_diccionarios_hash.py`: Mapeos clave-valor eficientes y métodos de extracción segura (`get()`).
*   `24_conjuntos_sets.py`: Colecciones desordenadas de elementos únicos y operaciones matemáticas de conjuntos.

### 5. Modularización y Funciones de Aridad Dinámica
*   `25_definicion_funciones_retorno.py`: Abstracción de bloques lógicos y flujos de salida con `return`.
*   `26_argumentos_nombrados_defecto.py`: Flexibilidad en firmas de funciones mediante parámetros predeterminados.
*   `27_argumentos_dinamicos_args.py`: Procesamiento de argumentos posicionales variables (`*args`).
*   `28_mapeos_dinamicos_kwargs.py`: Ingesta dinámica de diccionarios por palabra clave (`**kwargs`).
*   `29_recursión_caso_base.py`: Diseño recursivo y control del Stack de llamadas (*Call Stack*).

---
*Última actualización: Junio 26'*

## Instrucciones de Ejecución Local

Para replicar, testear y auditar estos scripts en tu entorno local:

1.  **Clonar el repositorio** (si aún no lo hiciste):
```
bash
    git clone [https://github.com/mvikips/Python_UTN.git](https://github.com/mvikips/Python_UTN.git)
```
2.  **Navegar hasta el directorio de ejercicios**:
```
bash
    cd Python_UTN/Materiales/Ejercicios
```
3.  **Ejecutar el script deseado** utilizando el intérprete de Python instalado:
```
bash
    python nombre_del_archivo.py
```


---
 
 *La teoría se comprende cuando se escucha, pero la ingeniería se domina cuando el código se compila, se ejecuta y se rompe de forma controlada.*
