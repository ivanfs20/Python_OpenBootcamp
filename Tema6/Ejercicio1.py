class Vehiculo():
    _color=None
    _ruedas=0
    _puerta=0
    def __init__(self) -> None:
        pass
    #Funciones para cambiar los atributos
    def cambiaColor(self, color):
        self._color=color
    def cambiaRuedas(self, ruedas):
        self._ruedas=ruedas
    def cambiaPuertas(self,puertas):
        self._puertas=puertas

class Coche(Vehiculo):
    _velocidad=0
    _cilindra=True
    def __init__(self) -> None:
        super().__init__()
    #Funciones para cambiar los atributos
    def cambiaVelocidad(self, velocidad):
        self._velocidad=velocidad
    def cambiaCilindra(self, cilindra):
        self._cilindra=cilindra

c=Coche()

c.cambiaColor("Rojo")
c.cambiaPuertas(61)
c.cambiaRuedas(62)
c.cambiaCilindra(False)
c.cambiaVelocidad(124)

print("Color: ",c._color,"Velocidad: ",c._velocidad,"Puertas: ",c._puertas,"Ruedas: ",c._ruedas,"Cilindra: ",c._cilindra)