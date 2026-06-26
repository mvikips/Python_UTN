import funciones

# SANTIAGOOOOOOO OJO CON LOS COMENTARIOS!!!!
# SANTIAGO ojo con los comentarios y como llame algunas cosas para no pasar vergüenza! 
# Para la línea x def mostrar_menu(): = Se define una función propia que se puede llamar en cualquier momento
# sin necesidad de reescribir todo el texto.
# Y, en la línea x print("\n================...") = El carácter \n da un salto de línea inicial para que
# el menú no aparezca pegado a los outputs anteriores, y las líneas de símbolos = sirven como un separador
# visual limpio, o sea, meramenté estético. Justificativa: The zen of python: bonito mejor que feo.
def mostrar_menu():
    print("\n=======================================================")
    print("¡Bienvenido a la Sopa de Letras, para jugar seleccione una opción!")
    print("A. Cargar archivo CSV")
    print("B. Buscar una palabra")
    print("C. Vea esta estadísticas")
    print("D. Vea las palabras mas encontradas por fila y columna")
    print("E. Vea el total de palabras encontradas")
    print("F. Salir del programa")
    print("=======================================================")

# Explicación de def main() y while True
# La función def main es la principal debajo se usa while para que no se detenga a no ser que
# se seleccione F para salir del programa. Esto significa: 
# "repite todo lo que está acá adentro de forma infinita hasta que el usuario decida salir explícitamente".
# Gracias a este bucle, el programa no se cierra después de hacer una sola acción (como buscar una palabra);
# en su lugar, vuelve a mostrar el menú una y otra vez para que pueda seguir jugando.
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip().upper() # upper es para hacerlas mayusculas

        # Explicación del If de la opción A
        # Aquí el objetivo principal es solicitar la ubicación de la sopa de letras (el archivo), enviársela al módulo de 
        # funciones para que la procese y pedir una confirmación manual antes de continuar.
        # En el input vos digitas el nombre del archivo (que en este caso se llama sopa.csv pero podría llamarse archivo.csv por ejemplo),
        # Ruta es una variable que guarda lo que escribiste y strip limpia caso se escriba con espacios para que quede todo junto y no de pow.
        # el if.funciones llama a funciones.py porque si la variable ruta se corresponde con un archivo existente entonces
        # se activa el if (true) entonces tenemos la siguiente línea que es es proceder=input, pero si no lo encuentra
        # no se activa el if (false) entonces el programa ignora el resto del código y vuelve al menú principal
        if opcion == 'A':
            ruta = input("Por favor selecciona un archivo CSV (ej. sopa.csv): ").strip()
            if funciones.cargar_csv(ruta):
                proceder = input("Datos procesados, ¿desea proceder? s/n: ").strip().lower() # lower es para hacer minuscula
                if proceder != 's':
                    print("Regresando al menú principal.")

        # Explicación de la opción B
        # Acá metemos un filtro: si el flag archivo_cargado está en False, 
        # te frena el programa porque no podés buscar nada en una matriz vacía. El 'continue' hace que el
        # bucle salte directo al inicio a pedir opción de nuevo sin ejecutar lo de abajo. 
        # Si pasamos el filtro (True), dibuja la matriz y abre un bucle interno:
        # 'while ejecutando_busqueda' para que busques todas las palabras que quieras de corrido sin 
        # tener que volver al menú principal cada vez, controlando el corte con la variable 'otra'
        # mapeada a minúsculas (n).
        elif opcion == 'B':
            if funciones.archivo_cargado == False:
                print("Aún no cargaste un archivo CSV, por favor selecciona A y carga tu archivo.")
                continue
            
            funciones.mostrar_matriz()
            
            # Control de flujo secuencial iterativo simple
            ejecutando_busqueda = True
            while ejecutando_busqueda:
                palabra = input("Escriba la palabra a buscar: ")
                funciones.buscar_palabra(palabra)
                
                otra = input("\n¿Desea buscar otra palabra? s/n: ").strip().lower()
                if otra != 's':
                    ejecutando_busqueda = False

        # Explicación de la opción C
        # Acá levantamos las variables de control que calculamos a mano en funciones.py cuando
        # barrimos el CSV en la opción A. Mismo filtro de seguridad: si no hay archivo cargado, 
        # da error simulado en consola. Si está todo Ok, lee del módulo 'funciones' la letra ganadora
        # en frecuencia absoluta y cuántas veces sumó.
        elif opcion == 'C':
            if funciones.archivo_cargado == False:
                print("Aún no cargaste un archivo CSV, por favor selecciona A y carga tu archivo.")
            else:
                print("\nEsta es la letra más repetida:", funciones.letra_repetida)
                print("Se repite:", funciones.cantidad_repeticiones, "veces.")

        # Explicación de la opción D
        # Esta opción expone la base de datos dividida. Chequea que los diccionarios paralelos H
        # (horizontal) y V (vertical) tengan elementos comparando su longitud (len). Si están en cero
        # absoluto es porque no buscaste nada en la opción B, así que te manda a jugar primero. Si
        # tienen datos, imprime las estructuras con sus índices de posicionamiento de inicio y fin ordenados
        # alfabeticamente por la clave.
        elif opcion == 'D':
            if funciones.archivo_cargado == False:
                print("Aún no cargaste un archivo CSV, por favor selecciona A y carga tu archivo.")
            elif len(funciones.diccionarioH) == 0 and len(funciones.diccionarioV) == 0:
                print("No haz buscado palabras para generar base de datos, por favor busca palabras seleccionando B.")
            else:
                print("\nPalabras halladas horizontalmente:", funciones.diccionarioH)
                print("Palabras halladas verticalmente:", funciones.diccionarioV)

        # Explicación de la opción E
        # La opción de unificación total. Muestra el diccionarioTotal que combina bit a bit H y V y 
        # que fue ordenado con nuestro algoritmo en funciones.py. Es el historial limpio de todo lo que
        # encontraste con éxito.
        elif opcion == 'E':
            if funciones.archivo_cargado == False:
                print("Aún no cargaste un archivo CSV, por favor selecciona A y carga tu archivo.")
            elif len(funciones.diccionarioTotal) == 0:
                print("No haz buscado palabras para generar base de datos, por favor busca palabras seleccionando B.")
            else:
                print("\nestas han sido todas las palabras buscadas:", funciones.diccionarioTotal)

        # Explicación de la opción F y Validación Final
        # La puerta de salida. El 'break' rompe de manera violenta pero limpia el 'while True' de la
        # función main. Sin el break nos quedamos atrapados acá para siempre. Y el 'else' del final atrapa
        # cualquier fruta que meta el usuario en la consola que no sea de la A a la F.
        elif opcion == 'F':
            print("Saliendo del programa. ¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Disparador del Script
# Bloque de control de ejecución nativo. Si corremos examen.py directo desde la terminal, __name__
# vale "__main__" por lo que Python arranca automáticamente el juego llamando a main(). Si lo importáramos
# desde otro script, se quedaría quieto.
if __name__ == "__main__":
    main()

# Cuellos de botella que he tenido:
# Identación, uso del stack limitado al nivel starter/trainee, aplicación a pseudo.