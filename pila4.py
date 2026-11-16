# Pila con menú

pila = []


def validar_pila_vacia():
    if not pila:
        print("La pila está vacía.")
        return True
    return False


def apilar():
    valor = input("Ingrese el valor a apilar: ").strip()

    if valor == "":
        print("No se aceptan valores vacíos.")
        return

    if valor in pila:
        print(f"El valor '{valor}' ya existe en la pila. No se aceptan duplicados.")
        return

    pila.append(valor)
    print(f"Se apiló: {valor}")
    print(f"Cantidad de cajas en la pila: {len(pila)}")


def desapilar():
    if validar_pila_vacia():
        return

    valor = pila.pop()
    print(f"Se desapiló: {valor}")
    print(f"Cantidad de cajas en la pila: {len(pila)}")


def consultar_tope():
    if validar_pila_vacia():
        return

    print(f"El tope de la pila es: {pila[-1]}")


def mostrar_pila():
    if validar_pila_vacia():
        return

    print("Contenido de la pila:")
    print(f"Cantidad de cajas: {len(pila)}")
    for i in range(len(pila) - 1, -1, -1):
        print(f"[{i}] {pila[i]}")


def menu():
    while True:
        print("\n===== MENÚ DE PILA =====")
        print("1. Apilar caja")
        print("2. Desapilar")
        print("3. Consultar tope")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            apilar()
        elif opcion == "2":
            desapilar()
        elif opcion == "3":
            consultar_tope()
        elif opcion == "4":
            mostrar_pila()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()
