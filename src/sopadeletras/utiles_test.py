from typing import List
import string
import random
from utiles import (
    buscar_palabra, 
    rellenar_celdas_vacias, 
    check_longitud_palabras, 
    inicializar_sopa_vacia, 
    elegir_posicion_y_direccion_aleatorias, 
    escribir_palabra, 
    comprobar_posicion_y_direccion_validas, 
    insertar_palabra, 
    generar_sopa,
    HORIZONTAL, VERTICAL, DIAGONAL)


def test_buscar_palabra():
    print("buscar_palabra...", end="")
    # Test para verificar si la palabra está en la lista y es eliminada
    lista_palabras = ['manzana', 'banana', 'cereza']
    palabra = 'banana'
    assert buscar_palabra(lista_palabras, palabra), f"Error: {palabra} debería estar en la lista y retornar True"
    assert palabra not in lista_palabras, f"Error: {palabra} no fue eliminada de la lista"

    # Reset de la lista de palabras para el siguiente test
    lista_palabras = ['manzana', 'banana', 'cereza']

    # Test para verificar si la palabra no está en la lista
    palabra_inexistente = 'pera'
    assert not buscar_palabra(lista_palabras, palabra_inexistente), f"Error: {palabra_inexistente} no debería estar en la lista y retornar False"
    assert palabra_inexistente not in lista_palabras, f"Error: {palabra_inexistente} no debería estar en la lista después de buscar"
    
    print("OK")


def test_rellenar_celdas_vacias():
    print("rellenar_celdas_vacias...", end="")
    # Creamos una sopa de letras con algunas celdas vacías (espacios en blanco)
    sopa_de_letras = [
        ['A', ' ', 'C'],
        [' ', 'E', ' '],
        ['G', ' ', 'I']
    ]

    # Hacemos una copia para verificar que las celdas no vacías permanezcan igual
    sopa_original = [fila[:] for fila in sopa_de_letras]

    # Definimos todas las letras mayúsculas del alfabeto español
    letras_mayusculas_espanol = string.ascii_uppercase + 'Ñ'

    # Llamamos a la función que rellena las celdas vacías
    rellenar_celdas_vacias(sopa_de_letras)

    # Recorremos la sopa de letras para verificar los dos puntos
    for i in range(len(sopa_de_letras)):
        for j in range(len(sopa_de_letras[i])):
            if sopa_original[i][j] == ' ':
                assert sopa_de_letras[i][j] in letras_mayusculas_espanol, f"La celda vacía no ha sido rellenada con una letra mayúscula válida: {sopa_de_letras[i][j]}"
            else:
                assert sopa_de_letras[i][j] == sopa_original[i][j], "Una celda no vacía ha sido modificada."

    print("OK")

def test_check_longitud_palabras():
    print("check_longitud_palabras...", end="")
        # Caso de prueba donde todas las palabras caben en el tablero ya sea horizontal o verticalmente
    palabras_que_caben = ['casa', 'auto', 'sol']
    filas = 4
    columnas = 4
    try:
        check_longitud_palabras(palabras_que_caben, filas, columnas)
    except ValueError:
        assert False, "ValueError lanzado incorrectamente cuando todas las palabras caben en el tablero."

    # Caso de prueba donde una palabra es demasiado larga para caber tanto horizontal como verticalmente
    palabras_no_caben = ['casa', 'automóvil']
    filas_pequenas = 3
    columnas_pequenas = 3
    try:
        check_longitud_palabras(palabras_no_caben, filas_pequenas, columnas_pequenas)
        assert False, "ValueError no fue lanzado cuando una palabra es demasiado larga para el tablero."
    except ValueError:
        pass  # Correcto, ValueError fue lanzado

    # Caso de prueba donde la palabra más larga cabe justo en el límite de las filas y columnas
    palabras_en_el_limite = ['casa', 'bar']
    filas_limite = 4
    columnas_limite = 3
    try:
        check_longitud_palabras(palabras_en_el_limite, filas_limite, columnas_limite)
    except ValueError:
        assert False, "ValueError lanzado incorrectamente cuando la palabra más larga cabe justo en el límite."

    print("OK")


def test_inicializar_sopa_vacia():
    print("inicializar_sopa_vacia...", end="")
    # Caso de prueba con un número específico de filas y columnas
    filas = 5
    columnas = 3
    sopa_vacia = inicializar_sopa_vacia(filas, columnas)

    # Verificamos que se devuelve una lista
    assert type(sopa_vacia) is list, "Debe devolverse una lista de listas"    

    # Verificamos que la sopa de letras tiene el número correcto de filas
    assert len(sopa_vacia) == filas, f"El número de filas debería ser {filas}."

    # Verificamos que se devuelve una lista de listas
    assert type(sopa_vacia[0]) is list, "Debe devolverse una lista de listas"

    # Verificamos que cada fila de la sopa de letras tiene el número correcto de columnas
    for fila in sopa_vacia:
        assert len(fila) == columnas, f"Cada fila debería tener {columnas} columnas."
        for celda in fila:
            assert celda == ' ', "Cada celda debería ser un espacio en blanco."

    # Caso de prueba para verificar el manejo de cero filas y cero columnas
    sopa_vacia_cero = inicializar_sopa_vacia(0, 0)
    assert sopa_vacia_cero == [], "La sopa de letras con 0 filas y 0 columnas debería ser una lista vacía."

    print("OK")

def test_elegir_posicion_y_direccion_aleatorias():
    print("elegir_posicion_y_direccion_aleatorias...", end="")
    # Configuramos la semilla del generador de números aleatorios para reproducibilidad
    random.seed(0)

    palabra = "python"
    filas = 10
    columnas = 10
    posiciones_validas = []

    # Ejecutamos la función varias veces para obtener un conjunto de posiciones
    for _ in range(10000):
        res = elegir_posicion_y_direccion_aleatorias(palabra, filas, columnas)
        assert (type(res) is tuple and 
                len(res) == 3 and 
                type(res[0]) is int and 
                type(res[1]) is int and 
                type(res[2]) is int), "Debe devolverse una tupla de tres enteros"
        direccion, fila, columna = elegir_posicion_y_direccion_aleatorias(palabra, filas, columnas)
        
        # Verificamos que la dirección es válida
        assert direccion in (HORIZONTAL, VERTICAL, DIAGONAL), "La dirección elegida no es válida."
        
        # Verificamos que la fila y columna son válidas
        assert 0 <= fila < filas, "La fila elegida está fuera del rango."
        assert 0 <= columna < columnas, "La columna elegida está fuera del rango."
        
        # Verificamos que la palabra cabe en la dirección seleccionada
        if direccion == HORIZONTAL:
            assert columna + len(palabra) <= columnas, f"La palabra {palabra} no cabe horizontalmente en la posición {fila}, {columna}."
        elif direccion == VERTICAL:
            assert fila + len(palabra) <= filas, f"La palabra {palabra} no cabe verticalmente en la posición {fila}, {columna}."
        elif direccion == DIAGONAL:
            assert columna + len(palabra) <= columnas and fila + len(palabra) <= filas, f"La palabra {palabra} no cabe diagonalmente en la posición {fila}, {columna}."
        
        posiciones_validas.append((direccion, fila, columna))

    assert len(set(posiciones_validas)) == 125, "Debería haber más variedad de posiciones y direcciones."

    print("OK")


def test_escribir_palabra():
    print("escribir_palabra...", end="")
    palabra = "python"
    filas = columnas = 10  # Aseguramos un tamaño de tablero donde la palabra siempre quepa

    # Prueba en diferentes posiciones y direcciones
    posiciones_direcciones = [
        (0, 0, HORIZONTAL),
        (2, 2, VERTICAL),
        (0, 0, DIAGONAL),
        (1, 3, HORIZONTAL),
        (4, 2, VERTICAL),
        (3, 3, DIAGONAL),
    ]

    for fila, columna, direccion in posiciones_direcciones:
        # Creamos una sopa de letras vacía para cada prueba
        letras = [[' ' for _ in range(columnas)] for _ in range(filas)]
        
        escribir_palabra(letras, fila, columna, direccion, palabra)

        if direccion == HORIZONTAL:
            assert all(letras[fila][columna + i] == letra for i, letra in enumerate(palabra)), \
                f"La palabra {palabra} no se escribió correctamente en la dirección horizontal desde la posición {fila, columna}."
        
        elif direccion == VERTICAL:
            assert all(letras[fila + i][columna] == letra for i, letra in enumerate(palabra)), \
                f"La palabra {palabra} no se escribió correctamente en la dirección vertical desde la posición {fila, columna}."
        
        elif direccion == DIAGONAL:
            assert all(letras[fila + i][columna + i] == letra for i, letra in enumerate(palabra)), \
                f"La palabra {palabra} no se escribió correctamente en la dirección diagonal desde la posición {fila, columna}."

    print("OK")

def test_insertar_palabra():
    print("insertar_palabra...", end="")
    filas = columnas = 4
    letras = [[' ' for _ in range(columnas)] for _ in range(filas)]

    # Palabras a insertar
    palabras = ["VAYA", "VOY", "RASA"]

    for palabra in palabras:
        insertar_palabra(palabra, letras, filas, columnas)
        assert palabra_en_tablero(palabra, letras), f"La palabra '{palabra}' no se encontró en el tablero como se esperaba."

    print("OK")

def palabra_en_tablero(palabra, tablero):
    """Comprueba si una palabra está en el tablero en alguna dirección."""
    filas = len(tablero)
    columnas = len(tablero[0])
    longitud = len(palabra)

    for i in range(filas):
        for j in range(columnas):
            if cabe_horizontalmente(palabra, tablero, i, j, longitud) or \
               cabe_verticalmente(palabra, tablero, i, j, longitud) or \
               cabe_diagonalmente(palabra, tablero, i, j, longitud):
                return True
    return False

def cabe_horizontalmente(palabra, tablero, fila, columna, longitud):
    if columna + longitud > len(tablero[0]):
        return False
    return all(tablero[fila][columna + i] == palabra[i] for i in range(longitud))

def cabe_verticalmente(palabra, tablero, fila, columna, longitud):
    if fila + longitud > len(tablero):
        return False
    return all(tablero[fila + i][columna] == palabra[i] for i in range(longitud))

def cabe_diagonalmente(palabra, tablero, fila, columna, longitud):
    if fila + longitud > len(tablero) or columna + longitud > len(tablero[0]):
        return False
    return all(tablero[fila + i][columna + i] == palabra[i] for i in range(longitud))


def test_comprobar_posicion_y_direccion_validas():
    print("comprobar_posicion_y_direccion_validas...", end="")
    filas = columnas = 10
    palabra = "python"
    tamaño_minimo = len(palabra)

    # Crear sopa de letras vacía
    letras_vacias = [[' ' for _ in range(columnas)] for _ in range(filas)]
    
    # Crear sopa de letras con una letra coincidente
    letras_con_coincidencia = [[' ' for _ in range(columnas)] for _ in range(filas)]
    letras_con_coincidencia[0][1] = 'y'  # Letra coincidente para la dirección horizontal
    
    # Crear sopa de letras con una letra coincidente para la dirección vertical
    letras_con_coincidencia_vertical = [[' ' for _ in range(columnas)] for _ in range(filas)]
    letras_con_coincidencia_vertical[1][0] = 'y'  # Letra coincidente para la dirección vertical
    
    # Crear sopa de letras con una letra coincidente para la dirección diagonal
    letras_con_coincidencia_diagonal = [[' ' for _ in range(columnas)] for _ in range(filas)]
    letras_con_coincidencia_diagonal[1][1] = 'y'  # Letra coincidente para la dirección diagonal

    # Casos de prueba
    casos_de_prueba = [
        (1, letras_vacias, 0, 0, HORIZONTAL, palabra, True),
        (2, letras_vacias, 0, 0, VERTICAL, palabra, True),
        (3, letras_vacias, 0, 0, DIAGONAL, palabra, True),
        (4, letras_vacias, 2, 2, HORIZONTAL, palabra, True),
        (5, letras_vacias, 2, 2, VERTICAL, palabra, True),
        (6, letras_vacias, 2, 2, DIAGONAL, palabra, True),
        (7, letras_vacias, filas - 1, 2, HORIZONTAL, palabra, True),
        (8, letras_vacias, 2, columnas - 1, VERTICAL, palabra, True),        
        (9, letras_con_coincidencia, 0, 0, HORIZONTAL, palabra, True),  # Coincidencia horizontal
        (10, letras_con_coincidencia_vertical, 0, 0, VERTICAL, palabra, True),  # Coincidencia vertical
        (11, letras_con_coincidencia_diagonal, 0, 0, DIAGONAL, palabra, True),  # Coincidencia diagonal
        # Supongamos una letra que no coincide en una posición donde debería ir la palabra
        (12, letras_con_coincidencia_vertical, 1, 0, HORIZONTAL, palabra, False),  # Interfiere con otra letra no coincidente
    ]

    for num_caso, letras, fila, columna, direccion, palabra, resultado_esperado in casos_de_prueba:
        resultado_obtenido = comprobar_posicion_y_direccion_validas(letras, fila, columna, direccion, palabra)
        assert resultado_obtenido == resultado_esperado, (
            f"Falló la verificación {num_caso} con la palabra '{palabra}' en la fila {fila}, columna {columna}, dirección {direccion}. "
            f"Esperado: {resultado_esperado}, Obtenido: {resultado_obtenido}, "
            f"Tablero: {letras}, Obtenido: {resultado_obtenido}"
        )

    print("OK")

def test_generar_sopa():
    print("generar_sopa...", end="")
    # Test 1: Verificar que las palabras se insertan correctamente en un tablero lo suficientemente grande
    palabras = ["HOLA", "ADIOS"]
    filas = columnas = 6
    sopa = generar_sopa(palabras, filas, columnas)

    assert (type(sopa) is list and
            len(sopa) == filas and
            type(sopa[0]) is list and
            len(sopa[0]) == columnas), f"Debe devolverse una lista de listas del tamaño adecuado"

    for palabra in palabras:
        assert palabra_en_tablero(palabra, sopa), f"La palabra '{palabra}' no se encontró en el tablero como se esperaba."

    # Verificamos que todas las celdas están llenas
    for fila in sopa:
        for celda in fila:
            assert celda != ' ', "Se encontró una celda vacía en el tablero."

    # Test 2: Verificar que se lanza una excepción si una palabra no cabe
    palabras_dificiles = ["hola", "adios"]
    filas_pequeñas = columnas_pequeñas = 2
    try:
        generar_sopa(palabras_dificiles, filas_pequeñas, columnas_pequeñas)
        assert False, "Se esperaba una excepción ValueError."
    except ValueError:
        pass  # Correcto, se lanzó ValueError

    print("OK")



if __name__ == '__main__':
    print("Ejecutando tests de sopa_utiles")    
    test_buscar_palabra()
    test_rellenar_celdas_vacias()
    test_check_longitud_palabras()
    test_inicializar_sopa_vacia()
    test_elegir_posicion_y_direccion_aleatorias()
    test_escribir_palabra()
    test_comprobar_posicion_y_direccion_validas()
    test_insertar_palabra()
    test_generar_sopa()
    print("Todos los tests superados.")
