class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__edad = 0

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad

    def get_edad(self):
        return self.__edad

# Ejemplo de uso
if __name__ == "__main__":
    p = Persona()
    p.set_nombre("Byron")
    p.set_edad(20)
    print(f"Nombre: {p.get_nombre()}, Edad: {p.get_edad()}")
