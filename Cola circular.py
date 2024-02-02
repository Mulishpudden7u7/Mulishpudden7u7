class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = self.final = -1

    def es_vacia(self):
        return self.frente == -1

    def es_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def encolar(self, elemento):
        if not self.es_llena():
            if self.es_vacia():
                self.frente = self.final = 0
            else:
                self.final = (self.final + 1) % self.capacidad

            self.cola[self.final] = elemento
            print(f"Se encoló el elemento {elemento}")
        else:
            print("La cola está llena, no se puede encolar más elementos.")

    def desencolar(self):
        if not self.es_vacia():
            elemento = self.cola[self.frente]

            if self.frente == self.final:
                self.frente = self.final = -1
            else:
                self.frente = (self.frente + 1) % self.capacidad

            print(f"Se desencoló el elemento {elemento}")
            return elemento
        else:
            print("La cola está vacía, no se puede desencolar.")


cola = ColaCircular(5)

cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

cola.desencolar()
cola.desencolar()

cola.encolar(6)
cola.encolar(7)


