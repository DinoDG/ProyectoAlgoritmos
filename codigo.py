import funciones as fn

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

    
    menu=1
while menu==1:
  try:
    op=int(input("""
  ****** VUELOS-DUOC ******
  MENU:
  1.-Ver asientos disponibles
  2.-Comprar asiento
  3.-Anular vuelo
  4.-Modificar datos de pasajero
  5.- Salir
  """))
    if op in "12345":
      break
    else:
      print(" debe ingresar una opción válida señalada en el menú")
  except:
    print("1 o 2 o 3 o 4 o 5")
    
  if op==1:
    fn.Estado_Asientos()

  if op==2:
    print("valor asientos")
    print(" asientos del  1 al 30 (normales) : $78900")
    print(" asientos del 31 al 42 (vip) : $240000\n")
    while valido:
      try: 
        asiento=int(input("Indique numero de asiento:\n")) 
        if asiento >= 1 and asiento <= 42:
          break
        else:
          print("debe seleccionar uno de los asientos disponibles ")
      except:
        print(" ingrese un asiento en el rango  1 a 30 (normales) 31 al 42 (vip)")
          
    if fn.Selec_Asiento(asiento)==True:
      if asiento>0 and asiento<=30:
        contNORM +=1
      elif asiento>=31 and asiento <=42:
        contVIP +=1
      total=0
      total=(contNORM*valorNORM)+(contVIP*valorVIP)

      cliente=fn.Datos_Cliente()

      if cliente[3]==1:
        
        total=int(total*0.85)
        print(" se aplicado un descuento de un 15% por asiento, al pertenecer al Banco Duoc")
      print("\nSu total es de:  $ ",total)
