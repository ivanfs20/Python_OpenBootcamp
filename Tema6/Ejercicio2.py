"""En este segundo ejercicio, tendréis que crear un
programa que tenga una clase llamada Alumno que
tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para 
inicializar sus atributos,
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""

class Nota():
    def resultado(self, valor):
        if(valor<6 and valor>0):
            print("Estas reprobado")
        elif(valor>=6 and valor<=9):
            print("Estas aprobado")
        elif(valor==10):
            print("Tu calificacion es excelente")
        else:
            print("Ingresa un numero o un valor que este en el rango de 0 a 10")

class Alumno():
    _nombre=None
    _nota=Nota()
    def ingresaNombre(self, nombre):
        self._nombre=nombre
    
a=Alumno()

a.ingresaNombre("Raul")
print(a._nombre)
a._nota.resultado(3)
