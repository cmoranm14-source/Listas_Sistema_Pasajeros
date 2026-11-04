from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython
from utils import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo ✅ -------------------------
def pausa():
    input("\nPresione Enter para continuar...")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    imprimir_titulo(f" {titulo} ")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")

# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if lista1.añadir(pasajero):                # 2. LLAMAR
                imprimir_exito(" Pasajero añadido")          # 3. MOSTRAR
        elif op == "2":
            lista1.listar()
        elif op == "3":
            posicion = leer_entero("Ingrese en la posicion que va insertar")
            pasajero = leer_pasajero()
            if lista1.insertar(posicion, pasajero):
                imprimir_info(" Pasajero insertado")
        elif op == "4":      
            numero = leer_entero("Ingrese el numero que desea buscar: ")          # 1. LEER
            pasajero = lista1.buscar(numero)                                            # 2. LLAMAR
            if pasajero:                
                imprimir_exito(f" Pasajero encontrado {pasajero}")       # 3. MOSTRAR
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "5":
            numero = leer_entero(" Ingrese el número que desea buscar: ")
            pasajero = lista1.buscar_binaria(numero)
            if pasajero:
                imprimir_exito(f" Pasajero encontrado: {pasajero}")
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero: ")
            if lista1.buscar(numero) is None:
                imprimir_error(" No se encontró ningún pasajero con ese número ")
            else:
                imprimir_exito(f" Pasajero encontrado {lista1.buscar(numero)}")

                confirmar("¿Desea modificar sus datos? (si/no): ")
                if confirmar:
                    nuevo_destino = input("Ingrese el nuevo destino: ").strip()
                    nuevo_asiento = input("Ingrese el nuevo asiento: ").strip().upper()
                    lista1.modificar(numero, nuevo_destino, nuevo_asiento)
                    imprimir_exito(" Pasajero modificado ")
                else:
                    imprimir_error(" Operacion cancelada ")   
        elif op == "7":
            posicion = leer_entero("Ingrese el numero que desea eliminar: ")
            if lista1.eliminar_por_posicion(posicion):
                imprimir_info("valor eliminado")
            pass 
        elif op == "8":
            numero = leer_entero("Ingrese el numero que desea eliminar: ")
            if lista1.eliminar_por_valor(numero):
                imprimir_exito(" Pasajero eliminado por número")
            else:
                imprimir_error(" No se encontró un pasajero con ese número")
            
        elif op == "9":
            lista1.ordenar_asc()
            imprimir_exito(" Lista ordenada de forma ascendente")
        elif op == "10":
            lista1.ordenar_desc()
            imprimir_exito(" Lista ordenada de forma descendente")
        elif op == "11":
            lista1.reversar()
            imprimir_exito(" Lista invertida")
        elif op == "12":
            copia = lista1.copiar()
            imprimir_exito(f"  Copia creada: {copia.listar()}") 
        elif op == "13":
           imprimir_info(f" Cantidad de pasajeros: {lista1.longitud()}")

        elif op == "C":
            cargar_datos_prueba(lista1)
        elif op == "0":
            break
        else:
            imprimir_error("  Opción no válida")
        pausa()

# ---------------------- MENÚ 2 · list de Python ----------------------
def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista2.añadir(pasajero):
                imprimir_exito(" Pasajero añadido")
        elif op == "2":
            lista2.listar()
        elif op == "3":
            posicion = leer_entero("  Ingrese la posición en la que va a insertar: ")
            pasajero = leer_pasajero()
            if lista2.insertar(posicion, pasajero):
                imprimir_exito("  Pasajero insertado exitosamente")
        elif op == "4":
            numero = leer_entero("  Ingrese el número que desea buscar: ")
            pasajero = lista2.buscar(numero)
            if pasajero:
                imprimir_exito(f" Pasajero encontrado: {pasajero}")
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "5":
            numero = leer_entero("  Ingrese el número que desea buscar: ")
            pasajero = lista2.buscar_binaria(numero)
            if pasajero:
                imprimir_exito(f" Pasajero encontrado: {pasajero}")
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            pasajero = lista2.buscar(numero)
            if pasajero is None:
                imprimir_error(" No se encontró ningún pasajero con ese número")
            else:
                imprimir_exito(f" Pasajero encontrado: {pasajero}")
                confirmar("  ¿Desea modificar sus datos? (si/no): ")
                if confirmar:
                    nuevo_destino = input("  Ingrese el nuevo destino: ").strip()
                    nuevo_asiento = input("  Ingrese el nuevo asiento: ").strip().upper()
                    lista2.modificar(numero, nuevo_destino, nuevo_asiento)
                    imprimir_exito("  Pasajero modificado")
                else:
                    imprimir_error("  Operación cancelada")
        elif op == "7":
            posicion = leer_entero("  Ingrese la posición que desea eliminar: ")
            eliminado = lista2.eliminar_por_posicion(posicion)
            if eliminado is not None:
                imprimir_exito(f" Pasajero eliminado: {eliminado}")
            else:
                imprimir_error(" Posición no válida")
        elif op == "8":
            numero = leer_entero("  Ingrese el número de pasajero que desea eliminar: ")
            if lista2.eliminar_por_valor(numero):
                imprimir_exito(" Pasajero eliminado")
            else:
                imprimir_error(" No se encontró ningún pasajero con ese número")
        elif op == "9":
            lista2.ordenar_asc()
            imprimir_exito(" Lista ordenada de forma ascendente")
        elif op == "10":
            lista2.ordenar_desc()
            imprimir_exito(" Lista ordenada de forma descendente")
        elif op == "11":
            lista2.reversar()
            imprimir_exito(" Lista invertida")
        elif op == "12":
            copia = lista2.copiar()
            imprimir_exito(" Copia creada exitosamente:")
            copia.listar()
        elif op == "13":
            imprimir_exito(f" Cantidad de elementos: {lista2.longitud()}")
        elif op == "14":
            destino = input("  Ingrese el destino a filtrar: ").strip()
            filtrados = lista2.filtrar_por_destino(destino)
            if filtrados:
                imprimir_exito(f" Pasajeros con destino '{destino}':")
                for p in filtrados:
                    print(f"    {p}")
            else:
                imprimir_info(f" no hay pasajeros hacia {destino}")
        elif op == "15":
            mayores = lista2.mayores_de_edad()
            if mayores:
                imprimir_exito(" Pasajeros mayores de edad (>= 18):")
                for p in mayores:
                    print(f" {p}")
            else:
                imprimir_info(" No hay pasajeros mayores de edad")
        elif op == "C":
            cargar_datos_prueba(lista2)
        elif op == "0":
            break
        else:
            imprimir_error("  Opción no válida")
    pausa()

# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()