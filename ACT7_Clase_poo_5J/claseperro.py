print("Programación POO")
# Definición de clases
class Perro:
    # Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre, edad):
        print(f"Nombre: {nombre} edad: {edad}")


# Zona de creación de objeto 
pitbull = Perro()

# Zona de uso de objeto
pitbull.Datos_perro("Boby", 4)
pitbull.morder()

