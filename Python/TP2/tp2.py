import random

class tateti:
    def __init__(self):
        self.reiniciar_tablero()
        self.memoria_jugadas = []  # Memoria de jugadas exitosas
        self.secuencia_actual = []  # Secuencia temporal de jugadas de la partida actual

    def reiniciar_tablero(self):
        self.B = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        self.J = 1
        self.secuencia_actual = []

    def movimientos_libres(self):
        return [[f, c] for f in range(3) for c in range(3) if self.B[f][c] == 0]

    def movimiento_valido(self, f, c):
        return 0 <= f <= 2 and 0 <= c <= 2 and self.B[f][c] == 0

    def hacer_movimiento(self, f, c):
        if self.movimiento_valido(f, c):
            self.B[f][c] = self.J
            self.J = (self.J % 2) + 1

    def hacer_movimiento_bot(self):
        # 1. Intento de victoria
        for f, c in self.movimientos_libres():
            self.B[f][c] = self.J
            if self.verificar_victoria() == self.J:
                self.secuencia_actual.append((f, c))
                return
            self.B[f][c] = 0  # Deshacer movimiento

        # 2. Bloqueo del oponente
        oponente = (self.J % 2) + 1  # Identificar al oponente sin cambiar el jugador global
        for f, c in self.movimientos_libres():
            self.B[f][c] = oponente
            if self.verificar_victoria() == oponente:
                self.B[f][c] = self.J  # Hacer el bloqueo real
                self.secuencia_actual.append((f, c))
                return
            self.B[f][c] = 0  # Deshacer movimiento del bloqueo simulado

        # 3. Memoria de jugadas
        for f, c in self.memoria_jugadas:
            if self.movimiento_valido(f, c):
                self.hacer_movimiento(f, c)
                self.secuencia_actual.append((f, c))
                return

        # 4. Jugada aleatoria
        f, c = random.choice(self.movimientos_libres())
        self.hacer_movimiento(f, c)
        self.secuencia_actual.append((f, c))

    def verificar_victoria(self):
        # Verificar columnas
        for c in range(3):
            if self.B[0][c] == self.B[1][c] == self.B[2][c] != 0:
                return self.B[0][c]
        # Verificar filas
        for r in range(3):
            if self.B[r][0] == self.B[r][1] == self.B[r][2] != 0:
                return self.B[r][0]
        # Verificar diagonales
        if self.B[0][0] == self.B[1][1] == self.B[2][2] != 0:
            return self.B[0][0]
        if self.B[2][0] == self.B[1][1] == self.B[0][2] != 0:
            return self.B[2][0]
        # Empate
        if self.movimientos_libres() == []:
            return 0
        return -1

    def actualizar_memoria(self, resultado):
        if resultado == self.J:  # Bot gana
            self.memoria_jugadas = self.secuencia_actual + self.memoria_jugadas
        elif resultado != 0:  # Bot pierde
            random.shuffle(self.secuencia_actual)
            self.memoria_jugadas = [jugada for jugada in self.memoria_jugadas if jugada not in self.secuencia_actual]

def main():
    juego = tateti()

    def tabla():
        caracteres = ['-', 'X', 'O']
        for f in range(3):
            for c in range(3):
                print(caracteres[juego.B[f][c]], end=' ')
            print()  # Salto de línea al final de cada fila

    def fin_del_juego():
        x = juego.verificar_victoria()
        juego.actualizar_memoria(x)
        if x == 0:
            print("Hubo un empate")
        else:
            print(f"¡Jugador {x} gana!")

    def jugar():
        while True:
            tabla()
            try:
                # Movimiento del jugador
                f, c = map(int, input(f"Ingrese la ubicación (fila, columna), jugador {str(juego.J)}: ").split(','))
                if not juego.movimiento_valido(f, c):
                    print("Movimiento inválido. Asegúrate de que la posición esté dentro del rango y no esté ocupada.")
                    continue
                juego.hacer_movimiento(f, c)

                # Verificar si el jugador ganó
                if juego.verificar_victoria() != -1:
                    break

            except ValueError:
                print("Entrada inválida. Ingrese dos números separados por coma.")
                continue

            # Movimiento del bot
            print("Movimiento BOT")
            juego.hacer_movimiento_bot()

            # Verificar si el bot ganó
            if juego.verificar_victoria() != -1:
                break

        tabla()
        fin_del_juego()

    while True:
        jugar()
        replay = input("¿Desea jugar otra partida? (si/no): ").lower()
        if replay == "si":
            juego.reiniciar_tablero()  # Reiniciar el tablero para una nueva partida
        else:
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
