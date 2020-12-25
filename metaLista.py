class MetaLista:
  def __init__(self, nombre):
    posNum = {}  #Diccionario con los indices y el valor del numero asociado
    for i in range(len(nombre)):
      letra = nombre[i]
      if letra.isdigit():
        posNum[i] = ({'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[letra])

    self.nombre = nombre  #String
    self.numeros = posNum   #{Integer,Integer}

    del posNum
    del nombre

  def __str__(self):
    return self.nombre
  
  def __repr__(self):
    return "MetaLista(" + self.nombre + str(self.numeros.values()) + ")"
  
  def giveNum(self, k): #Devuelve el k-ésimo elemento de la metalista, empezando por cero  MATES
    numero = self.numeros.values()[k]
    return numero

  def suma(self, index, valor):   #Suma "valor" al k-ésimo numero  MATES
    if index <= len(self.numeros):
      listaValores = list(self.numeros.values())
      valorNuevo = listaValores[index] + valor
      listaValores[index] = valorNuevo
      self.numeros = dict(zip(list(self.numeros.keys()), listaValores))

      nombreEnLista = list(self.nombre)
      nombreEnLista[list(self.numeros.keys())[index]] = str(valorNuevo)
      self.nombre = "".join(nombreEnLista)
      del listaValores
      del valorNuevo
      del nombreEnLista
    else:
      print("ESTO DEBE LANZAR UN ERROR, PERO NO SE CÓMO SE HACE :(")
  
  def resta(self, index, valor):   #Resta "valor" al k-ésimo numero    MATES
    if index <= len(self.numeros):
      listaValores = list(self.numeros.values())
      valorNuevo = listaValores[index] - valor
      listaValores[index] = valorNuevo
      self.numeros = dict(zip(list(self.numeros.keys()), listaValores))

      nombreEnLista = list(self.nombre)
      if valorNuevo >= 0:
        nombreEnLista[list(self.numeros.keys())[index]] = str(valorNuevo)
      else:
        nombreEnLista[list(self.numeros.keys())[index]] = "(" + str(valorNuevo) + ")"
      self.nombre = "".join(nombreEnLista)
      del listaValores
      del valorNuevo
      del nombreEnLista
    else:
      print("ESTO DEBE LANZAR UN ERROR, PERO NO SE CÓMO SE HACE :(")
  
  def multi(self, index, valor):   #Multiplica "valor" por k-ésimo numero    MATES
    if index <= len(self.numeros):
      listaValores = list(self.numeros.values())
      valorNuevo = listaValores[index] * valor
      listaValores[index] = valorNuevo
      self.numeros = dict(zip(list(self.numeros.keys()), listaValores))

      nombreEnLista = list(self.nombre)
      if valorNuevo >= 0:
        nombreEnLista[list(self.numeros.keys())[index]] = str(valorNuevo)
      else:
        nombreEnLista[list(self.numeros.keys())[index]] = "(" + str(valorNuevo) + ")"
      self.nombre = "".join(nombreEnLista)
      del listaValores
      del valorNuevo
      del nombreEnLista
    else:
      print("ESTO DEBE LANZAR UN ERROR, PERO NO SE CÓMO SE HACE :(")
  
  def divi(self, index, valor):   #Divide el k-ésimo numero entre "valor"    MATES
    if index <= len(self.numeros):
      listaValores = list(self.numeros.values())
      valorNuevo = listaValores[index] / valor
      listaValores[index] = valorNuevo
      self.numeros = dict(zip(list(self.numeros.keys()), listaValores))

      nombreEnLista = list(self.nombre)
      if valorNuevo >= 0:
        nombreEnLista[list(self.numeros.keys())[index]] = str(valorNuevo)
      else:
        nombreEnLista[list(self.numeros.keys())[index]] = "(" + str(valorNuevo) + ")"
      self.nombre = "".join(nombreEnLista)
      del listaValores
      del valorNuevo
      del nombreEnLista
    else:
      print("ESTO DEBE LANZAR UN ERROR, PERO NO SE CÓMO SE HACE :(")
  
  def potencia(self, index, valor):   #Eleva "valor" a la k-ésima potencia    MATES
    if index <= len(self.numeros):
      listaValores = list(self.numeros.values())
      valorNuevo = listaValores[index] ** valor
      listaValores[index] = valorNuevo
      self.numeros = dict(zip(list(self.numeros.keys()), listaValores))

      nombreEnLista = list(self.nombre)
      if valorNuevo >= 0:
        nombreEnLista[list(self.numeros.keys())[index]] = str(valorNuevo)
      else:
        nombreEnLista[list(self.numeros.keys())[index]] = "(" + str(valorNuevo) + ")"
      self.nombre = "".join(nombreEnLista)
      del listaValores
      del valorNuevo
      del nombreEnLista
    else:
      print("ESTO DEBE LANZAR UN ERROR, PERO NO SE CÓMO SE HACE :(")
  
  def listaNums(self):  #Da la lista de los numeros dela metalista     ACCESO
    return list(self.numeros.values())
  
  def nombreSinNum(self): #Da el string sin los numeros    ACCESO
    listaLetras = []
    for i in range(len(self.nombre)):
      if not self.nombre[i].isdigit():
        listaLetras.append(self.nombre[i])
    return "".join(listaLetras)
  
  def charAt(self, indx):     #Devuelve el caracter en pos indx del total  ACCESO
    return self.nombre[indx]
