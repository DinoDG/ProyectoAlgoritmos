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
            
