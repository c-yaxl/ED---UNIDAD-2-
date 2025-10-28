# =====================================
# Node base (usado por pila y cola)
# =====================================
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


# =====================================
# Clase Pila (Stack)
# =====================================
class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, elem):
        new_node = Node(elem)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        elem = self.top.info
        self.top = self.top.next
        self.size -= 1
        return elem

    def peek(self):
        if self.is_empty():
            return None
        return self.top.info

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size

    def print_stack(self):
        print("\n---- CONTENIDO DE LA PILA ----")
        if self.is_empty():
            print("(vacía)")
        else:
            node = self.top
            pos = 1
            while node:
                print(f"{pos}. {node.info}")
                node = node.next
                pos += 1
        print("------------------------------")


# =====================================
# Clase Order (para la cola)
# =====================================
class Order:
    def __init__(self, qtty, customer):
        self.qtty = qtty
        self.customer = customer

    def print(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    def __str__(self):
        return f"Order({self.customer}, {self.qtty})"


# =====================================
# Clase Cola (Queue)
# =====================================
class LinkedQueue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        if self.top is None:
            self.tail = None
        self.size -= 1
        return info

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def get_nth(self, pos):
        if pos <= 0 or pos > self.size:
            return None
        node = self.top
        for _ in range(1, pos):
            node = node.next
        return node.info

    def print_info(self):
        print("\n********* QUEUE DUMP *********")
        print(f"   Size: {self.size}")
        node = self.top
        count = 1
        while node:
            print(f"   ** Element {count}")
            if isinstance(node.info, Order):
                node.info.print()
            else:
                print("     " + str(node.info))
            node = node.next
            count += 1
        print("******************************\n")


# =====================================
# MENÚ PRINCIPAL
# =====================================
def menu():
    stack = LinkedStack()
    queue = LinkedQueue()

    while True:
        print("""
=====================================
   MENÚ PRINCIPAL - ESTRUCTURAS
=====================================
1. Usar PILA (Stack)
2. Usar COLA (Queue)
3. Salir
""")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_pila(stack)
        elif opcion == "2":
            menu_cola(queue)
        elif opcion == "3":
            print("\nSaliendo del programa... 👋")
            break
        else:
            print("\nOpción inválida, intenta otra vez.\n")


# =====================================
# Submenú: Pila
# =====================================
def menu_pila(stack):
    while True:
        print("""
---- MENÚ PILA ----
1. Insertar elemento (push)
2. Extraer elemento (pop)
3. Ver cima (peek)
4. Ver contenido
5. Volver al menú principal
""")
        op = input("Elige una opción: ")

        if op == "1":
            val = input("Ingresa el valor a apilar: ")
            stack.push(val)
            print(f"Elemento '{val}' agregado.\n")
        elif op == "2":
            val = stack.pop()
            if val is None:
                print("La pila está vacía.\n")
            else:
                print(f"Elemento '{val}' eliminado.\n")
        elif op == "3":
            val = stack.peek()
            print(f"Cima actual: {val}\n" if val else "La pila está vacía.\n")
        elif op == "4":
            stack.print_stack()
        elif op == "5":
            break
        else:
            print("Opción inválida.\n")


# =====================================
# Submenú: Cola
# =====================================
def menu_cola(queue):
    while True:
        print("""
---- MENÚ COLA ----
1. Agregar pedido (enqueue)
2. Atender pedido (dequeue)
3. Ver primer pedido (front)
4. Ver n-ésimo pedido
5. Mostrar cola
6. Volver al menú principal
""")
        op = input("Elige una opción: ")

        if op == "1":
            cliente = input("Nombre del cliente: ")
            cantidad = int(input("Cantidad de producto: "))
            order = Order(cantidad, cliente)
            queue.enqueue(order)
            print("Pedido agregado correctamente.\n")

        elif op == "2":
            order = queue.dequeue()
            if order:
                print("Pedido atendido:")
                order.print()
            else:
                print("La cola está vacía.\n")

        elif op == "3":
            order = queue.front()
            if order:
                print("Primer pedido en la cola:")
                order.print()
            else:
                print("La cola está vacía.\n")

        elif op == "4":
            pos = int(input("Posición a consultar: "))
            order = queue.get_nth(pos)
            if order:
                print(f"Pedido en posición {pos}:")
                order.print()
            else:
                print("Posición inválida o vacía.\n")

        elif op == "5":
            queue.print_info()

        elif op == "6":
            break
        else:
            print("Opción inválida.\n")


# =====================================
# EJECUCIÓN
# =====================================
if __name__ == "__main__":
    menu()
