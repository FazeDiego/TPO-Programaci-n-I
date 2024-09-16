class cola:
    """Representa a una cola, con operaciones de primero, acolar, desacolar. El primero en ser acolado es tambien el
    primero en ser desacolado. """

    def incializar_cola(self):
        """Inicializar cola. Crea una cola vacia."""
        self.items = []

    def esta_vacia(self):
        """Devuelve True si la cola esta vacia, False si no."""
        return len(self.items) == 0

    def acolar(self, x):
        """Agrega el elemento x como ultimo de la cola."""
        self.items.append(x)

    def desacolar(self):
        """Desacola el primer elemento. No devuelve su valor. Si la cola esta vacia, levanta ValueError."""
        if self.esta_vacia():
            raise ValueError("La cola esta vacia.")
        self.items.pop(0)

    def primero(self):
        """Devuelve el valor del primer elemento. No desacola el elemento. Si la cola esta vacia levanta ValueError."""
        if self.esta_vacia():
            raise ValueError("La cola esta vacia.")
        return self.items[0]

    def ultimo(self):
        """Devuelve el valor del ultimo elemento. No desacola el elemento. Si la cola esta vacia levanta ValueError."""
        if self.esta_vacia():
            raise ValueError("La cola esta vacia.")
        return self.items[len(self.items) - 1]

    def imprimir_cola(self):
        for c in range(len(self.items)):
            print(self.items[c])
