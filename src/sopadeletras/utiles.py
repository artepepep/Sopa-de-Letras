import random
import string
from typing import List, Tuple

# Constantes para representar las direcciones en las que pueden aparecer las palabras
HORIZONTAL, VERTICAL, DIAGONAL = 1, 2, 3
direcciones = [HORIZONTAL, VERTICAL, DIAGONAL]

# Constante para representar todas las letras permitidas en la sopa de letras
LETRAS_MAYUSCULAS_ESPAÑOL = string.ascii_uppercase + 'Ñ'

def buscar_palabra(palabras: List[str], palabra: str) -> bool:
    """Busca una palabra en una lista de palabras. Si la encuentra, la elimina de la lista.

    Args:
        palabras: Lista de palabras.
        palabra: Palabra a buscar.

    Returns:
        True si la palabra está en la lista, False en caso contrario.

    Tests:
        >>> palabras = ["HOLA", "ADIOS", "HASTA", "LUEGO"]
        >>> busca_palabra(palabras, "HOLA")
        True
        >>> palabras
        ['ADIOS', 'HASTA', 'LUEGO']
        >>> busca_palabra(palabras, "HOLA")
        False
        >>> palabras
        ['ADIOS', 'HASTA', 'LUEGO']
    """
    pass


def rellenar_celdas_vacias(letras: List[List[str]]) -> None:
    """Rellena las celdas vacías de la sopa de letras con letras mayúsculas
    aleatorias. 

    Las letras válidas son las contenidas en la variable LETRAS_MAYUSCULAS_ESPAÑOL.

    Args:
        letras: Lista de listas de caracteres que representa la sopa de letras.

    Tests:
        >>> letras = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']]
        >>> rellena_celdas_vacias(letras)
        >>> letras
        [['Q', 'C', 'R', 'N', 'B'],
         ['A', 'C', 'G', 'H', 'P'],
         ['S', 'A', 'Q', 'G', 'V'],
         ['T', 'V', 'Q', 'N', 'H'],
         ['Ñ', 'R', 'I', 'Y', 'A']]
    """
    pass


def check_longitud_palabras(
    palabras: List[str], filas: int, columnas: int
) -> None:
    """Comprueba que las palabras caben en el tablero. Si no caben,
    lanza un error. Si caben, la función no hace ni devuelve nada.

    Args:
        palabras: Lista de palabras a insertar en la sopa de letras.
        filas: Número de filas de la sopa de letras.
        columnas: Número de columnas de la sopa de letras.

    Raises:
        ValueError: Si alguna de las palabras no cabe en el tablero.
        Para lanzar este error, use la instrucción:
        raise ValueError(mensaje)

    Tests:
        >>> check_longitud_palabras(["HOLA", "ADIOS"], 6, 6)
        >>> check_longitud_palabras(["HOLA", "ADIOS"], 2, 2)
        Traceback (most recent call last):
        ...
        ValueError: La palabra HOLA no cabe en un tablero de 2x2
    """
    pass


def inicializar_sopa_vacia(filas: int, columnas: int) -> List[List[str]]:
    """Inicializa una sopa de letras vacía, formada por caracteres de espacios.

    Args:
        filas: Número de filas de la sopa de letras.
        columnas: Número de columnas de la sopa de letras.

    Returns:
        Una lista de listas de caracteres que representa la sopa de letras.

    Tests:
        >>> inicializa_sopa_vacia(2, 3)
        [[' ', ' ', ' '], [' ', ' ', ' ']]
    """
    pass


def elegir_posicion_y_direccion_aleatorias(
    palabra: str, filas: int, columnas: int
) -> Tuple[int, int, int]:
    """Elige una posición y dirección aleatoria para una palabra.
    La posición y dirección escogidas deben ser válidas, es decir,
    deben permitir que la palabra quepa en el tablero.

    Args:
        palabra: Palabra a insertar en la sopa de letras.
        filas: Número de filas de la sopa de letras.
        columnas: Número de columnas de la sopa de letras.

    Returns:
        Una tupla con la dirección, la fila y la columna donde se insertaría
        la palabra.

    Tests:
        >>> elige_posicion_y_direccion("HOLA", 6, 6)
        (3, 0, 0)
        >>> elige_posicion_y_direccion("HOLA", 6, 6)
        (3, 1, 0)
        >>> elige_posicion_y_direccion("HOLA", 6, 6)
        (1, 1, 2)
        >>> elige_posicion_y_direccion("HOLA", 6, 6)
        (1, 5, 2)
    """
    pass


def escribir_palabra(
    letras: List[List[str]],
    fila: int,
    columna: int,
    direccion: int,
    palabra: str,
) -> None:
    """Escribe una palabra en la posición dada de la sopa de letras. Se da 
    por supuesto que la posición y la dirección indicadas para escribir la 
    palabra son válidas, es decir, que permiten escribir la palabra sin 
    salirse del tablero.

    Args:
        letras: Lista de listas de caracteres que representa la sopa de letras.
        fila: Fila de la sopa de letras en la que se quiere insertar la palabra.
        columna: Columna de la sopa de letras en la que se quiere insertar la palabra.
        direccion: Dirección en la que se quiere insertar la palabra.
        palabra: Palabra a insertar en la sopa de letras.

    Tests:
        >>> letras = [
            ['Q', 'C', 'R', 'N', 'B'],
            ['A', 'C', 'G', 'H', 'P'],
            ['S', 'A', 'Q', 'G', 'V'],
            ['T', 'V', 'Q', 'N', 'H'],
            ['Ñ', 'R', 'I', 'Y', 'A']
            ]
        >>> escribe_palabra(letras, 0, 0, HORIZONTAL, "ADIOS")
        >>> letras
        [['A', 'D', 'I', 'O', 'S'],
         ['A', 'C', 'G', 'H', 'P'],
         ['S', 'A', 'Q', 'G', 'V'],
         ['T', 'V', 'Q', 'N', 'H'],
         ['Ñ', 'R', 'I', 'Y', 'A']]
        >>> escribe_palabra(letras, 0, 0, VERTICAL, "ADIOS")
        >>> letras
        [['A', 'D', 'I', 'O', 'S'],
         ['D', 'C', 'G', 'H', 'P'],
         ['I', 'A', 'Q', 'G', 'V'],
         ['O', 'V', 'Q', 'N', 'H'],
         ['S', 'R', 'I', 'Y', 'A']]
        >>> escribe_palabra(letras, 0, 0, DIAGONAL, "ADIOS")
        >>> letras
        [['A', 'D', 'I', 'O', 'S'],
         ['A', 'D', 'G', 'H', 'P'],
         ['S', 'A', 'I', 'G', 'V'],
         ['T', 'V', 'Q', 'O', 'H'],
         ['Ñ', 'R', 'I', 'Y', 'S']]
    """
    pass


def comprobar_posicion_y_direccion_validas(
    letras: List[List[str]],
    fila: int,
    columna: int,
    direccion: int,
    palabra: str,
) -> bool:
    """Comprueba si una palabra se pueda escribir en la posición y dirección dadas.
    Para ello, debe cumplirse poder escribir en la posición y
    dirección indicadas sin tener que cambiar ninguna letra ya escrita
    en la sopa de letras, o bien ocupando posiciones que sean espacios en blanco.
    No es necesario comprobar si la palabra se sale del tablero (se supone 
    que la posición y dirección recibidas son válidas en este sentido).

    Args:
        letras: Lista de listas de caracteres que representa la sopa de letras.
        fila: Fila de la sopa de letras en la que se quiere insertar la palabra.
        columna: Columna de la sopa de letras en la que se quiere insertar la palabra.
        direccion: Dirección en la que se quiere insertar la palabra.
        palabra: Palabra a insertar en la sopa de letras.

    Returns:
        True si la palabra se puede escribir en la posición dada, False en caso contrario.

    Tests:
        >>> letras = [
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            ['H', 'O', 'L', 'A', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']
            ]
        >>> comprueba_posicion(letras, 0, 0, HORIZONTAL, "ADIOS")
        True
        >>> comprueba_posicion(letras, 1, 0, VERTICAL, "ADIOS")
        False
        >>> comprueba_posicion(letras, 0, 1, VERTICAL, "ADIOS")
        True
        >>> comprueba_posicion(letras, 0, 3, DIAGONAL, "ADIOS")
        False
    """
    pass


def insertar_palabra(
    palabra: str, letras: List[List[str]], filas: int, columnas: int
) -> None:
    """Inserta una palabra en la sopa de letras, en una posición aleatoria y
    con una dirección aleatoria.
    Compruebe el diagrama de descomposición del problema en el README.md. Debe
    hacer uso de las funciones elegir_posicion_y_direccion_aleatorias,
    comprobar_posicion_y_direccion_validas y escribir_palabra.

    Args:
        palabra: palabra a insertar 
        letras: Lista de listas de caracteres que representa la sopa de letras.
        filas: número de filas de la sopa de letras
        columnas: número de columnas de la sopa de letras
        

    Tests:
        >>> letras = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']]
        >>> random.seed(42)
        >>> inserta_palabra("VAYA", letras, 4, 4)
        >>> letras
        [['V', ' ', ' ', ' '],
         [' ', 'A', ' ', ' '],
         [' ', ' ', 'Y', ' '],
         [' ', ' ', ' ', 'A']]
        >>> inserta_palabra("VOY", letras, 4, 4)
        >>> letras
        [['V', ' ', ' ', ' '],
         ['V', 'A', ' ', ' '],
         [' ', 'O', 'Y', ' '],
         [' ', ' ', 'Y', 'A']]
        >>> inserta_palabra("RASA", letras, 4, 4)
        >>> letras
        [['V', ' ', ' ', 'R'],
         ['V', 'A', ' ', 'A'],
         [' ', 'O', 'Y', 'S'],
         [' ', ' ', 'Y', 'A']]
    """
    pass


def generar_sopa(
    palabras: List[str], filas: int, columnas: int
) -> List[List[str]]:
    """Inicializa una sopa de letras con las palabras dadas.

    Args:
        palabras: Lista de palabras a insertar en la sopa de letras.
        filas: Número de filas de la sopa de letras.
        columnas: Número de columnas de la sopa de letras.

    Returns:
        Una lista de listas de caracteres que representa la sopa de letras.

    Raises:
        ValueError: Si alguna de las palabras no cabe en el tablero.

    Tests:
        >>> inicializar_sopa(["HOLA", "ADIOS"], 6, 6)
        [['J', 'A', 'S', 'E', 'Ñ', 'I'],
         ['J', 'S', 'D', 'S', 'L', 'Y'],
         ['Y', 'M', 'X', 'I', 'L', 'Q'],
         ['F', 'R', 'H', 'F', 'O', 'I'],
         ['Z', 'M', 'K', 'T', 'N', 'S'],
         ['H', 'O', 'L', 'A', 'T', 'X']]

        >>> inicializar_sopa(["hola", "adios"], 2, 2)
        Traceback (most recent call last):
        ...
        ValueError: La palabra adios no cabe en el tablero
    """
    pass
