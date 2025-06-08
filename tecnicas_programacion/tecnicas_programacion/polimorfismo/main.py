class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla")

def hacer_sonar(animal):
    animal.hacer_sonido()

# Ejemplo de uso
if __name__ == "__main__":
    animales = [Perro(), Gato()]
    for animal in animales:
        hacer_sonar(animal)
