class jugadas:
    
  def __init__(self, fecha, nivel, tiempo, jugadorJ, jugadorC, turno, letras, puntos):
    self._fecha = fecha
    self._nivel = nivel 
    self._tiempo = 0
    self._jugadorJ = jugadorJ
    self._jugadorC = jugadorC
    self._turno = turno 
    self._cantCambios = 0
    self._letras = letras
    self._puntos = puntos 
    
  def set_fecha(self, fecha):
    self._fecha = fecha
     
  def set_nivel(self, nivel):
    self._nivel = nivel
 
  def set_tiempo(self, tiempo):
    self._tiempo = tiempo
    
  def set_jugadorJ(self, jugadorJ):
    self._jugadorJ = jugadorJ
 
  def set_jugadorC(self, jugadorC):
    self._jugadorC = jugadorC
    
  def set_turno(self, turno):
    self._turno = turno
  
  def set_letras(self, letras):
    self._letras = letras

  def get_letras(self):
    return self._letras

  def get_puntos(self):
    return self._puntos
  
  def set_turno(self, turno):
    self._turno = turno
  
  def get_jugadorJ(self):
    return self._jugadorJ 
	 
  def get_jugadorC(self):  
    return self._jugadorC
 
  def get_cantCambios(self):  
    return self._cantCambios
 
  def sumarCambio(self):  
    self._cantCambios+=1 
     
    
    
