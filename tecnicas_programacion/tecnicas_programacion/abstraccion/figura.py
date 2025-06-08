from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

# Ejemplo de uso
if __name__ == "__main__":
    c = Circulo(5)
    print("Área del círculo:", c.calcular_area())
