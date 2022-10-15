from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,anosPracticando,golesMarcados,tarjetasRojas,piernaHabil,):
        Persona.__init__(self,nombre,edad,altura, sexo)
        Deportista.__init__(self,anosPracticando)
        self.golesMarcados= golesMarcados
        self.tarjetasRojas= tarjetasRojas
        self.piernaHabil= piernaHabil
    
    def setGolesMarcados(self,golesMarcados):
        self.golesMarcados = golesMarcados
    def getGolesMarcados(self):
        return self.golesMarcados
    def setTarjetasRojas(self,tarjetasRojas):
        self.tarjetasRojas = tarjetasRojas
    def getTarjetasRojas(self):
        return self.tarjetasRojas
    def setPiernaHabil(self,piernaHabil):
        self.piernaHabil = piernaHabil
    def getPiernaHabil(self):
        return self.piernaHabil

    def __str__(self):
       def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"

futbolista1 = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
futbolista1.__str__()