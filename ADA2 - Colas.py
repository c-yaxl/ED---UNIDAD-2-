class Cola:
    def __init__(self):
        self.colas = [[], [], []]  
        self.solicitar()
        
    def solicitar(self):
        for i in range(2):
            print(f'Ingrese los numeros para la cola {i + 1}')
            while True:
                numero = input("Ingrese un numero entero: (o 'terminar' para terminar) ")
                if numero == 'terminar':
                    break
                try:
                    numero = int(numero)
                    self.colas[i].append(numero)
                except ValueError: 
                    print("Por favor, ingrese un numero entero valido.")
                    
        if len(self.colas[0]) != len(self.colas[1]):
            dif = abs(len(self.colas[0]) - len(self.colas[1]))  
            if len(self.colas[0]) < len(self.colas[1]):
                for i in range(dif):
                    self.colas[0].append(0)
                    self.sumacolas()
            else:
                for i in range(dif):
                    self.colas[1].append(0)
                    self.sumacolas()

    def sumacolas(self):
        for i in range(len(self.colas[0])):
            suma = self.colas[0][i] + self.colas[1][i]
            self.colas[2].append(suma)
        print("Cola 0:", self.colas[0])
        print("Cola 1:", self.colas[1])
        print("Cola 2 (suma):", self.colas[2])
        
ejemplo = Cola()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class Filas(Cola):
    def __init__(self):
        self.cola1 = Cola()
        self.cola2 = Cola()
        self.menu()
        
    def colaC(self):
        servicio = len(self.cola1)
        self.cola1.encolar('C'+str(servicio+1))
        print(f'Su numero de servicio es: C{servicio+1}')
        
    def colaA(self):
        servicio = len(self.cola2)
        self.cola2.encolar('A'+str(servicio+1))
        print(f'Su numero de servicio es: A{servicio+1}')
        
    def atender(self): 
        if len(self.cola1) == 0:
            print('No hay clientes en la cola C')
        if self.cola1.desencolar(): 
            self.colaA()
    
    def menu(self):
        while True:
            opcion = input("Ingrese el comando: ").lower()
            if opcion == "c":
                self.colaC()
            elif opcion == "a": 
                self.atender()
            else:
                print("Comando no valido")

fila = Filas()