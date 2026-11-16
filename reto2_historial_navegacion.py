# Reto 2 - Historial de navegación

historial = []
actual = None


def visitar(pagina):
    global actual
    if actual is not None:
        historial.append(actual)
    actual = pagina
    print(f"Visitar: {pagina}")


def regresar():
    global actual
    if not historial:
        print("Regresar → sin anterior")
        return

    actual = historial.pop()
    print(f"Regresar → {actual}")


def mostrar_actual():
    if actual is None:
        print("Actual: sin página abierta")
    else:
        print(f"Actual: {actual}")


def mostrar_historial():
    if not historial:
        print("Historial: vacío")
        return

    print("Historial:")
    for pagina in reversed(historial):
        print(pagina)


def menu():
    while True:
        print("\n==== HISTORIAL DE NAVEGACIÓN ====")
        print("1. Visitar página")
        print("2. Regresar")
        print("3. Mostrar actual")
        print("4. Mostrar historial")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            pagina = input("Ingrese la página: ")
            visitar(pagina)
        elif opcion == "2":
            regresar()
        elif opcion == "3":
            mostrar_actual()
        elif opcion == "4":
            mostrar_historial()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


# Ejemplo de uso del reto
visitar("uam.edu.ni")
visitar("python.org")
visitar("github.com")
mostrar_actual()
mostrar_historial()
regresar()
regresar()
regresar()

# Descomenta esta línea si quieres probar el menú interactivo:
# menu()
