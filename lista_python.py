from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if 0 <= posicion <= len(self.pasajeros):
            self.pasajeros.insert(posicion, pasajero)
            return True
        print("  ⚠ Posición no válida")
        return False

    def buscar(self, numero):
        for p in self.pasajeros:
            if p.numero == numero:
                return p
        return None

    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        indice = bisect_left(numeros, numero)
        if indice < len(self.pasajeros) and self.pasajeros[indice].numero == numero:
            return self.pasajeros[indice]
        return None

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pasajero = self.buscar(numero)
        if pasajero is None:
            return False
        pasajero.destino = nuevo_destino
        pasajero.asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if 0 <= posicion < len(self.pasajeros):
            return self.pasajeros.pop(posicion)
        return None

    def eliminar_por_valor(self, numero):
        pasajero = self.buscar(numero)
        if pasajero:
            self.pasajeros.remove(pasajero)
            return True
        return False

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.edad >= 18]

