stack = []


def push(item, capacity):
    if not is_full(capacity):
        stack.append(item)
        return "Se agregó el valor"
    return "La pila está llena"


def isEmpty():
    return len(stack) == 0


def is_full(capacity):
    return len(stack) == capacity

def peek():
    if not isEmpty():
        return stack[-1]
    return "pila vacía..."

def pop_stack():
    return stack.pop() 



capacity = int(input("Dime el tamaño de la pila: "))

while True:
    item = input("Dime el valor: ")
    print(push(item, capacity))
    answer = input("Desea ingresar otro dato [s/n]: ")
    if answer.lower() == "n":
        break
    
print("Mostrar tope")
print(peek())
print(peek())


while True:
    aswer = input("Desea desapilar [s/n]: ")
    if answer.lower() == "s":
        print(pop())
    elif answer.lower() == "n":
        break
    else:
        print("Opciones invalida...")
        


    