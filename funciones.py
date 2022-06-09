
valorVIP=240000
valorNORM=78900
contNORM,contVIP=0,0

valido=True
#Creacion avion
columna=[]
fila=[]
aux=[]
contAs=0
for x in range(14):
    for j in range(3):
        contAs +=1
        fila.append(contAs)
        aux=fila.copy()
    columna.append(aux)
    fila.clear()

def Selec_Asiento(nroPedido):
  
  nroAsiento=0
  proceso=True
  while proceso:
    for x in range(len(columna)):   
      for j in range(len(aux)):      
        nroAsiento +=1
        if nroPedido==nroAsiento:
          if columna[x][j]=="X":
            print("Asiento no disponible")
            proceso=False
            return False
            break
          else:
            columna[x][j]="X"
            proceso=False
            return True
            break
            
def Estado_Asientos():
  print("|",columna[0][0],columna[0][1],columna[0][2],"\t",columna[1][0],columna[1][1],columna[1][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[2][0],columna[2][1],columna[2][2],"\t",columna[3][0],columna[3][1],columna[3][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[4][0],columna[4][1],columna[4][2],"\t",columna[5][0],columna[5][1],columna[5][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[6][0],columna[6][1],columna[6][2],"\t",columna[7][0],columna[7][1],columna[7][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[8][0],columna[8][1],columna[8][2],"\t",columna[9][0],columna[9][1],columna[9][2],"|",sep="\t")

  print(" |","_"*23,"\t\t","     ","_"*23,"|")
  print(" |","_"*23,"\t\t","     ","_"*23,"|")


  print("|",columna[10][0],columna[10][1],columna[10][2],"\t",columna[11][0],columna[11][1],columna[11][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[12][0],columna[12][1],columna[12][2],"\t",columna[13][0],columna[13][1],columna[13][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  
  
def Anular_Asiento(recorrido):
  contador=0
  for x in range(14):
    for j in range(3):
      contador+=1
      if contador==recorrido:
        columna[x][j]=contador
        print("Asiento Anulado Exitosamente")
def Datos_Cliente():
    
  nombre=input(" ingrese su nombre para el registro y posterior compra : ")

  while True:
    try:
      rut = int(input(" ingrese su rut, en caso de poseer dígito verificador pertenciente al (K)  reemplace por un 0 : "))
      if len(str(rut))==9:
        break
      else:
        print(" ingrese un rut de 9 digitos considerando el dígito verificador")
    except:
        print(" debe responder a un rut valido")
  
  while True:
    try:
      telefono = int(input(" ingrese un número de contacto  :"))
      if len(str(telefono))==9:
        break
      else:
        print(" considere que el número es inferido en el sistema (+56) ")
    except:
      print(" debe ingresar un número de 9 dígitos numéricos")

  
  while True:
      try:
        banco=int(input(" pertenece al banco duoc ?  1/si   2/no  : "))
        if banco==1 or banco==2:
          break
        else:
          print(" ingrese o 1 o 2 (opciones)")
      except:
        print("ingrese una opción válida")
  return[nombre,rut,telefono,banco]
