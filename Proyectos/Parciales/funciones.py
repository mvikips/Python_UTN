import csv

# Estado global del programa utilizando estructuras básicas
matriz_sopa = []
diccionarioH = {}
diccionarioV = {}
diccionarioTotal = {}
letra_repetida = None
cantidad_repeticiones = 0
archivo_cargado = False


def cargar_csv(ruta_archivo):
    # Importa las variables del ámbito global (examen) para poder modificarlas 
    # de manera persistente en todo el ciclo de ejecución.
    global matriz_sopa, letra_repetida, cantidad_repeticiones, archivo_cargado
    
    try:
        # Abre el archivo en modo lectura controlando la codificación utf-8.
        with open(ruta_archivo, mode='r', encoding='utf-8') as f:
            lector = csv.reader(f)
            
            # Inicializa la matriz limpia y descarta líneas vacías 
            # evaluando la existencia de datos en cada fila del lector.
            matriz_sopa = []
            for fila in lector:
                if fila:
                    matriz_sopa.append(fila)
            
        # Validación de seguridad por si el archivo no contiene registros.
        if len(matriz_sopa) == 0:
            print("El archivo CSV está vacío.")
            return False

        # Recorre cada posición de la matriz bidimensional para limpiar
        # los caracteres y acumular sus apariciones en un diccionario.
        conteo_letras = {}
        for fila in matriz_sopa:
            for celda in fila:
                letra = celda.strip().upper()
                if letra != "":
                    if letra in conteo_letras:
                        conteo_letras[letra] = conteo_letras[letra] + 1
                    else:
                        conteo_letras[letra] = 1
                        
        # Determina la clave con mayor frecuencia absoluta iterando de 
        # forma secuencial sobre las claves generadas en el paso anterior.
        max_letra = None
        max_conteo = 0
        for letra in conteo_letras:
            if conteo_letras[letra] > max_conteo:
                max_conteo = conteo_letras[letra]
                max_letra = letra

        # Actualiza el estado de las variables de control globales.
        letra_repetida = max_letra
        cantidad_repeticiones = max_conteo
        archivo_cargado = True
        
        print("\nDatos procesados correctamente.")
        return True

    # Bloques de contingencia para capturar errores de ruta o de ejecución.
    except FileNotFoundError:
        print("No se pudo encontrar el archivo especificado. Intente de nuevo.")
        return False
    except Exception as e:
        print("Ocurrió un error al procesar el archivo:", e)
        return False


def ordenar_diccionario_alfabeticamente(diccionario_original):
    # Extrae las claves del diccionario en una lista indexada.
    claves = list(diccionario_original.keys())
    
    # Implementación del algoritmo de ordenamiento por burbuja para 
    # posicionar las claves según su valor de orden alfabético.
    n = len(claves)
    for i in range(n):
        for j in range(0, n - i - 1):
            if claves[j] > claves[j + 1]:
                # Intercambio de posiciones contiguas
                aux = claves[j]
                claves[j] = claves[j + 1]
                claves[j + 1] = aux
                
    # Construye un mapa ordenado asociando las claves ya posicionadas 
    # con sus respectivos bloques de datos originales.
    diccionario_ordenado = {}
    for clave in claves:
        diccionario_ordenado[clave] = diccionario_original[clave]
    return diccionario_ordenado


def actualizar_diccionario_total():
    # Sincroniza el diccionario general del programa.
    global diccionarioTotal
    combinado = {}
    
    # Agrupa los registros guardados en la estructura horizontal.
    for clave in diccionarioH:
        combinado[clave] = diccionarioH[clave]
        
    # Agrupa los registros guardados en la estructura vertical.
    for clave in diccionarioV:
        combinado[clave] = diccionarioV[clave]
        
    # Aplica la función de ordenamiento alfabético sobre el conjunto.
    diccionarioTotal = ordenar_diccionario_alfabeticamente(combinado)


def mostrar_matriz():
    # Verifica que existan filas cargadas antes de imprimir.
    if len(matriz_sopa) == 0:
        return

    filas = len(matriz_sopa)
    columnas = len(matriz_sopa[0])

    print("\n--- MATRIZ SOPA DE LETRAS ---")
    
    # Genera el espaciado y los identificadores numéricos de las columnas.
    cabecera = "   "
    for j in range(columnas):
        num_col = str(j + 1)
        if len(num_col) == 1:
            cabecera = cabecera + num_col + "  "
        else:
            cabecera = cabecera + num_col + " "
    print(cabecera)
    
    # Formatea y muestra cada fila de la matriz anteponiendo su índice numérico.
    for i in range(filas):
        num_fila = str(i + 1)
        if len(num_fila) == 1:
            linea = num_fila + "  "
        else:
            linea = num_fila + " "
            
        for j in range(columnas):
            linea = linea + matriz_sopa[i][j] + "  "
        print(linea)
        
    print("-----------------------------\n")


def buscar_palabra(palabra):
    # Permite la escritura y modificación de las bases de datos globales.
    global diccionarioH, diccionarioV
    palabra = palabra.strip().upper()
    
    if palabra == "":
        print("La palabra no puede estar vacía.")
        return False

    filas = len(matriz_sopa)
    columnas = len(matriz_sopa[0]) if filas > 0 else 0
    largo_palabra = len(palabra)

    # 1. Búsqueda Horizontal (Fila por fila)
    for i in range(filas):
        # Consolida los caracteres de la fila en una sola cadena de texto.
        fila_texto = ""
        for celda in matriz_sopa[i]:
            fila_texto = fila_texto + celda.upper()
            
        # Busca la coincidencia del patrón mediante el método indexado find.
        posicion = fila_texto.find(palabra)
        if posicion != -1:
            print("¡Encontré tu palabra en la fila", i + 1, "!")
            if palabra not in diccionarioH:
                col_inicio = posicion + 1
                col_fin = posicion + largo_palabra
                
                # Almacena las coordenadas espaciales dentro de la estructura.
                diccionarioH[palabra] = {
                    "fila": i + 1,
                    "columna_inicio": col_inicio,
                    "columna_fin": col_fin
                }
                # Mantiene el orden y actualiza el consolidado total.
                diccionarioH = ordenar_diccionario_alfabeticamente(diccionarioH)
                actualizar_diccionario_total()
            return True

    # 2. Búsqueda Vertical (Columna por columna)
    for j in range(columnas):
        # Extrae los elementos verticales para conformar la cadena lineal.
        columna_texto = ""
        for i in range(filas):
            columna_texto = columna_texto + matriz_sopa[i][j].upper()
            
        # Evalúa la presencia del patrón string en la columna procesada.
        posicion = columna_texto.find(palabra)
        if posicion != -1:
            print("¡Encontré tu palabra en la columna", j + 1, "!")
            if palabra not in diccionarioV:
                fila_inicio = posicion + 1
                fila_fin = posicion + largo_palabra
                
                # Registra los datos de posicionamiento de la palabra hallada.
                diccionarioV[palabra] = {
                    "columna": j + 1,
                    "fila_inicio": fila_inicio,
                    "fila_fin": fila_fin
                }
                # Reordena las estructuras y sincroniza el diccionario general.
                diccionarioV = ordenar_diccionario_alfabeticamente(diccionarioV)
                actualizar_diccionario_total()
            return True

    # Retorna falso si no se hallaron coincidencias en ninguna dirección.
    print("Esa palabra no hay.")
    return False