import utiles
import tkinter as tk
from tkinter import messagebox
import random
import time
from typing import List

# Filas y columnas del tablero
NUM_FILAS = 12
NUM_COLS = 12

# Número de palabras a adivinar
NUM_PALABRAS = 10

# Fichero con las palabras a adivinar
FICHERO_PALABRAS = "data/animales.txt"


class SopaDeLetrasGUI(tk.Tk):
    """Interfaz gráfica de la sopa de letras."""

    def __init__(self, sopa: List[List[str]], palabras: List[str]) -> None:
        """
        Inicializa la interfaz gráfica de la sopa de letras con la sopa dada.
        """
        super().__init__()

        self.__sopa = sopa
        self.__palabras = palabras

        # Colores palabras adivinidas
        self.__colores_adivinadas = [
            "green",
            "red",
            "pink",
            "magenta",
            "cyan",
            "orange",
            "brown",
        ]

        # Inicializa el estado de la selección
        self._inicializa_estado_seleccion()

        # Colores de los labels de la sopa
        self.colores_sopa = [
            ["white" for _ in range(self._get_columnas())]
            for _ in range(self._get_filas())
        ]

        self._crea_componentes()

        self.__start_time = time.time()

    def _inicializa_estado_seleccion(self) -> None:
        """
        Inicializa el estado de la selección de palabras en la sopa de letras.
        """
        self.marca_columna_init = None
        self.marca_fila_init = None
        self.marca_coords = []
        self.palabra_marcada = ""

    def _crea_componentes(self) -> None:
        """
        Crea todos los componentes de la interfaz de la sopa de letras.
        """
        # Crear ventana principal
        self.title("Sopa de letras")

        # Crear marco superior
        self.top_frame = tk.Frame(self)

        # Crear matriz de botones
        self.etiquetas = []
        for fila in range(self._get_filas()):
            self.etiquetas.append([])
            for columna in range(self._get_columnas()):
                # Crear botón y añadirlo a la ventana
                etiqueta = tk.Label(
                    self.top_frame,
                    text=self.__sopa[fila][columna],
                    font=("Arial", 24),
                    bg="white",
                    width=2,
                    height=1,
                )
                etiqueta.grid(row=fila, column=columna)
                self.etiquetas[fila].append(etiqueta)

        # Añadir evento de clic a cada botón
        for fila in range(self._get_filas()):
            for columna in range(self._get_columnas()):
                self.etiquetas[fila][columna].bind(
                    "<Button-1>", self._evento_clic
                )
                self.etiquetas[fila][columna].bind(
                    "<B1-Motion>", self._evento_clic_desplaza
                )
                self.etiquetas[fila][columna].bind(
                    "<ButtonRelease-1>", self._evento_clic_fin
                )

        # Crear zona de texto
        self.__mensaje = tk.StringVar()
        self._actualiza_mensaje()
        etiqueta = tk.Label(
            self.top_frame,
            textvariable=self.__mensaje,
            font=("Arial", 16),
            justify="center",
            bg="pink",
        )
        etiqueta.grid(
            row=self._get_filas(),
            column=0,
            columnspan=self._get_columnas(),
            sticky="ew",
        )
        self.top_frame.pack(fill=tk.BOTH, expand=True)

    def _evento_clic(self, event: tk.Event) -> None:
        """Este método es llamado cuando el usuario hace clic en una casilla de la sopa de letras.

        Este método actualiza la posición de inicio de la selección de la sopa de letras,
        y llama a _marca_casillas para marcar la casilla clicada.

        Parameters:
        - event: el evento de clic generado por el usuario.
        """
        if self.marca_columna_init is None:
            self.marca_fila_init = event.widget.grid_info()["row"]
            self.marca_columna_init = event.widget.grid_info()["column"]
            self._marca_casillas(self.marca_fila_init, self.marca_columna_init)
        else:
            self._marca_casillas(
                event.widget.grid_info()["row"],
                event.widget.grid_info()["column"],
            )
            self._evento_clic_fin(None)

    def _evento_clic_desplaza(self, event: tk.Event) -> None:
        """Evento que se ejecuta al desplazarse con el botón izquierdo del ratón pulsado
        sobre una casilla de la sopa de letras.

        Se capturan las coordenadas (fila y columna) del label sobre el que está el ratón,
        y se le mandan al método _marca_casillas. El método marcará de amarillo aquellas
        casillas que estén en línea recta (horizontal, vertical o diagonalmente) desde
        la casilla en la que se hizo clic hasta la casilla por la que actualmente se
        desplaza el ratón.

        Parameters:
        - event: el evento de clic generado por el usuario.
        """
        current_widget = event.widget.winfo_containing(
            event.x_root, event.y_root
        )
        if current_widget is not None:
            # Obtenemos la fila y columna del widget actual
            fila, columna = (
                int(current_widget.grid_info()["row"]),
                int(current_widget.grid_info()["column"]),
            )
            self._marca_casillas(fila, columna)

    def _evento_clic_fin(self, event: tk.Event) -> None:
        """Este método se llama al finalizar un clic en una casilla de la sopa de letras.
        Se verifica si la palabra marcada es válida, si lo es se cambia el color de las casillas correspondientes
        y se verifica si el usuario ganó la partida.
        """
        if len(self.palabra_marcada) > 1:
            if utiles.buscar_palabra(
                self.__palabras, self.palabra_marcada
            ):
                color = random.choice(self.__colores_adivinadas)
                for f, c in self.marca_coords:
                    self.colores_sopa[f][c] = color
                self._actualiza_mensaje()
                if len(self.__palabras) == 0:
                    self._victoria()
        self._restaura_colores()
        self._inicializa_estado_seleccion()

    def _restaura_colores(self) -> None:
        """Colorea cada una de las casillas del color que estuviera almacenado en
        colores_sopa. Esto permite restablecer los colores del tablero tras la selección
        de una palabra candidata por parte del usuario.
        """
        for f in range(self._get_filas()):
            for c in range(self._get_columnas()):
                self.etiquetas[f][c]["bg"] = self.colores_sopa[f][c]

    def _marca_casillas(self, fila: int, columna: int) -> None:
        """Marca de amarillo aquellas casillas que estén en línea recta (horizontal,
        vertical o diagonalmente) desde la casilla situada en la fila self.marca_fila_init y
        la columna self.marca_columna_init hasta la casilla situada en la fila y columna
        recibidas por parámetros.

        También almacena la palabra formada por las letras de la linea recta en cuestión
        en self.palabra_marcada.

        Si no hay una línea recta de casillas entre las coordenadas en cuestión, el método
        mantiene los colores originales de cada casilla y almacena la cadena vacía en
        self.palabra_marcada.

        Parameters:
        - fila: la fila de la casilla extrema de la línea a marcar.
        - columna: la columna de la casilla extrema de la línea a marcar.

        """
        self._restaura_colores()
        self.palabra_marcada = ""
        self.marca_coords = []
        if fila == self.marca_fila_init:
            # La línea es horizontal
            for c in range(
                min(columna, self.marca_columna_init),
                max(columna, self.marca_columna_init) + 1,
            ):
                self.etiquetas[fila][c]["bg"] = "yellow"
                self.palabra_marcada += self.etiquetas[fila][c]["text"]
                self.marca_coords.append((fila, c))
        elif columna == self.marca_columna_init:
            # La línea es vertical
            for f in range(
                min(fila, self.marca_fila_init),
                max(fila, self.marca_fila_init) + 1,
            ):
                self.etiquetas[f][columna]["bg"] = "yellow"
                self.palabra_marcada += self.etiquetas[f][columna]["text"]
                self.marca_coords.append((f, columna))

        elif fila - self.marca_fila_init == columna - self.marca_columna_init:
            # La línea es diagonal
            for f, c in zip(
                range(
                    min(fila, self.marca_fila_init),
                    max(fila, self.marca_fila_init) + 1,
                ),
                range(
                    min(columna, self.marca_columna_init),
                    max(columna, self.marca_columna_init) + 1,
                ),
            ):
                self.etiquetas[f][c]["bg"] = "yellow"
                self.palabra_marcada += self.etiquetas[f][c]["text"]
                self.marca_coords.append((f, c))

    def _actualiza_mensaje(self) -> None:
        """Escribe las instrucciones del juego y cuántas palabras quedan por
        encontrar en self.__mensaje, para que sea visualizado en la interfaz.
        """
        if len(self.__palabras) > 1:
            self.__mensaje.set(
                f"Busca las palabras de ANIMALES.\nQuedan {len(self.__palabras)} palabras por encontrar."
            )
        else:
            self.__mensaje.set(
                f"Busca las palabras de ANIMALES.\nQueda una sola palabra por encontrar."
            )

    def _victoria(self):
        """Muestra un mensaje indicando al jugador que ha completado el juego, y el
        tiempo que ha empleado. Posteriormente, finaliza la aplicación.
        """
        end_time = time.time()
        minutos, segundos = map(int, divmod(end_time - self.__start_time, 60))
        messagebox.showinfo(
            "¡Victoria!",
            f"¡Enhorabuena! ¡Las has encontrado todas!\nHas tardado {minutos} minutos y {segundos} segundos.",
            command=self.quit(),
        )

    def _get_filas(self):
        """Devuelve el número de filas de la sopa de letras.

        Returns:
        - El número de filas de la sopa de letras.
        """
        return len(self.__sopa)

    def _get_columnas(self):
        """Devuelve el número de columnas de la sopa de letras.

        Returns:
        - El número de columnas de la sopa de letras.
        """
        return len(self.__sopa[0])


# Programa principal

if __name__ == "__main__":
    # Cargar palabras
    with open(FICHERO_PALABRAS, encoding="utf-8") as f:
        palabras = [p.strip().upper() for p in f.readlines()]

    # Mezclar palabras
    random.shuffle(palabras)

    # Seleccionar palabras del tamaño adecuado
    palabras = [
        p for p in palabras if len(p) <= NUM_FILAS or len(p) <= NUM_COLS
    ][:NUM_PALABRAS]

    # Comprobar que hay suficientes palabras
    if len(palabras) < NUM_PALABRAS:
        raise (ValueError("No hay suficientes palabras del tamaño adecuado"))

    # Generar sopa de letras
    sopa = utiles.generar_sopa(palabras, NUM_FILAS, NUM_COLS)

    # Crear interfaz gráfica
    ventana = SopaDeLetrasGUI(sopa, palabras)

    # Mostrar interfaz gráfica
    ventana.mainloop()
