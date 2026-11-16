pila = []
pila.append("Matematica")
pila.append("programacion")
pila.append("base de datos")

print("Tope:", pila[-1])
print("Retiro:", pila.pop())
print("Quedan:", pila)

stack = []


def isEmpty():
    return len(stack) == 0


def is_full(capacity):
    return len(stack) >= capacity


def push(item, capacity):
    if not is_full(capacity):
        stack.append(item)
        return "Elemento apilado"
    return "La pila esta llena"


def peak():
    if not isEmpty():
        return stack[-1]
    return "Pila vacia"


def pop():
    if not isEmpty():
        return stack.pop()
    return "Pila vacia"


capacity = int(input("Dime el tamaño de la pila: "))

while True:
    item = input("Dime un valor: ")
    print(push(item, capacity))

    answer = input("Desea ingresar otro dato [S/N]: ")

    if answer.lower() == "n":
        break

print("Mostrar tope:")
print(peak())

print("Desapilar:")

while True:
    answer = input("Desea retirar un dato [S/N]: ")

    if answer.lower() == "n":
        break

    print(pop())

    if isEmpty():
        break

print("Quedan:", stack)