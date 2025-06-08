class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

# Ejemplo de uso
if __name__ == "__main__":
    a = Animal()
    a.hacer_sonido()
    p = Perro()
    p.hacer_sonido()
