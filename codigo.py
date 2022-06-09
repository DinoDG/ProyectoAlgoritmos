import funciones as fn

fn.hola()
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
