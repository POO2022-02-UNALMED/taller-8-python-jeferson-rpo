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
        return "Mi nombre es ", Persona.nombre, " soy profesional en el deporte ", Deportista.deporte," Tengo ", Persona.edad," anos de edad y llevo ",Deportista.anosPracticando," años en el deporte”"

  