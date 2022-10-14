from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    _listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,anosPracticando,golesMarcados,tarjetasRojas,piernaHabil,):
        Persona.__init__(self,nombre,edad,altura, sexo)
        Deportista.__init__(self,anosPracticando)
        self._golesMarcados= golesMarcados
        self._tarjetasRojas= tarjetasRojas
        self._piernaHabil= piernaHabil
        
    def __str__(self):
        return "Mi nombre es ", Persona._nombre, " soy profesional en el deporte ", Deportista._deporte," Tengo ", Persona._edad," anos de edad y llevo ",Deportista._anosPracticando," años en el deporte”"

  