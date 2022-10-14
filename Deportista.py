class Deportista:
    
    def __init__(self,anosPracticando):
        self._deporte="Futbol"
        self._anosPracticando= anosPracticando
    
    def setDeporte(self,deporte):
        self._deporte = deporte
    def getDeporte(self):
        return self._deporte
    
    def setAnosPracticando(self,anosPracticando):
        self._deporte = anosPracticando
    def getAnosPracticando(self):
        return self._anosPracticando    