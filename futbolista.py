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
        
    def __str__(self):
        return "Mi nombre es ", Persona.getNombre(self), " soy profesional en el deporte ", Deportista.getDeporte(self)," Tengo ", Persona.getEdad(self)," anos de edad y llevo ",Deportista.getAnosPracticando(self)," años en el deporte”"  