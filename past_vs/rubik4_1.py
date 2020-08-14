import copy
import time
import random

class Cubo:
    def __init__(self, cubo, listaMovimientos,idCubo,nota):
        self.cubo = cubo
        self.nota = nota
        self.listaMovimientos = listaMovimientos
        self.idCubo=idCubo
        self.nota = nota
        self.siguiente=[]
        self.anterior=[]
    def ubicar(anterior,siguiente):
        self.anterior=anterior
        self.siguiente=siguiente
    
#Set de prueba
cuboInicial=Cubo([0, 10, 2, 3, 4, 5, 6, 16, 8, 9, 46, 11, 39, 13, 41,
              15, 52, 17, 18, 19, 20, 12, 22, 14, 24, 25, 26, 27,
              7, 29, 21, 31, 23, 33, 1, 35, 36, 37, 38, 30, 40, 32, 42,
              43, 44, 45, 34, 47, 48, 49, 50, 51, 28, 53],[],0,0)

idCubo=1

#Este es el cubo ordenado
meta=[ 0,1 ,2 ,3 ,4 ,5 ,6 ,7 , 8,
       9,10,11,12,13,14,15,16,17,
      18,19,20,21,22,23,24,25,26,
      27,28,29,30,31,32,33,34,35,
      36,37,38,39,40,41,42,43,44,
      45,46,47,48,49,50,51,52,53]

abiertos=[]
cerrados=[]
explorados={}

#Lista de movimientos
movimientos=[[[0,9],[3,12],[6,15],[9,45],[12,48],[15,51],[45,35],[48,32],[51,29],[35,0],[32,3],[29,6],[36,38],[37,41],[38,44],[41,43],[44,42],[43,39],[42,36],[39,37]],#verticalIzquierda
            [[1,10],[4,13],[7,16],[10,46],[13,49],[16,52],[46,34],[49,31],[52,28],[34,1],[31,4],[28,7]],#VerticalCentro
            [[2,11],[5,14],[8,17],[11,47],[14,50],[17,53],[47,33],[50,30],[53,27],[33,2],[30,5],[27,8],[18,24],[19,21],[20,18],[23,19],[26,20],[25,23],[24,26],[21,25]],#verticalDerecha
            [[36,9],[37,10],[38,11],[9,18],[10,19],[11,20],[18,27],[19,28],[20,29],[27,36],[28,37],[29,38],[0,6],[3,7],[6,8],[7,5],[8,2],[5,1],[2,0],[1,3]],#horizontalArriba
            [[39,12],[40,13],[41,14],[12,21],[13,22],[14,23],[21,30],[22,31],[23,32],[30,39],[31,40],[32,41]],#horizontalCentro
            [[42,15],[43,16],[44,17],[15,24],[16,25],[17,26],[24,33],[25,34],[26,35],[33,42],[34,43],[35,44],[45,47],[46,50],[47,53],[50,52],[53,51],[52,48],[51,45],[48,46]],#horizontalAbajo
            [[9,11],[10,14],[11,17],[14,16],[17,15],[16,12],[15,9],[12,10],[38,8],[41,7],[44,6],[6,18],[7,21],[8,24],[18,47],[21,46],[24,45],[47,44],[46,41],[45,38]],#rotacionAdelante
            [[3,19],[4,22],[5,25],[19,50],[22,49],[25,48],[50,43],[49,40],[48,37],[43,3],[40,4],[37,5]],#rotacionMedio
            [[0,20],[1,23],[2,26],[20,53],[23,52],[26,51],[53,42],[52,39],[51,36],[42,0],[39,1],[36,2],[29,27],[28,30],[27,33],[30,34],[33,35],[34,32],[35,29],[32,28]]#rotacionatras
            ]
movDesorden=[]
            
def permutaciones(cubo):
    global idCubo,movimientos,explorados
    hijos=[]
    i=0
    for movimiento in movimientos:
        cuboNuevo = copy.copy(cubo.cubo)
        cuboNuevoR= copy.copy(cubo.cubo)
        for instruccion in movimiento:
            cuboNuevo [instruccion[0]]=cubo.cubo[instruccion[1]]
            cuboNuevoR[instruccion[1]]=cubo.cubo[instruccion[0]]
        if(str(cuboNuevo) not in explorados):
            hijos+=[Cubo(cuboNuevo,cubo.listaMovimientos+[i],idCubo,medir(cuboNuevo))]
            explorados[str(cuboNuevo)]=1
            idCubo+=1
        if(str(cuboNuevoR)not in explorados):
            hijos+=[Cubo(cuboNuevoR,cubo.listaMovimientos+[-i],idCubo,medir(cuboNuevoR))]
            explorados[str(cuboNuevoR)]=1
            idCubo+=1
        i+=1
    return hijos


def main():
    global meta,abiertos,cerrados,cuboInicial
    abiertos=permutaciones(cuboInicial)
    while(len(abiertos)!=0):
        mayor=0
        abiertosTemp=abiertos
        abiertos=[]
        seleccionado=[]
        i=0
        for cubo in abiertosTemp:
            if(cubo.cubo==meta):
                mostrarCubo2D(cubo.cubo)
                print("Movimientos: ", cubo.listaMovimientos, len(cubo.listaMovimientos))
                return cubo
            if cubo.nota>mayor:
                mayor=cubo.nota
                if(seleccionado!=[]):
                    abiertos+=[seleccionado]
                seleccionado=cubo
                continue
            abiertos+=[cubo]
        cerrados+=[seleccionado.cubo]
        abiertos+= permutaciones(seleccionado)

def medir(cubo):
    global meta
    r=0
    anterior=0
    for i in range(0,len(meta)):
        if (cubo[i]==meta[i]):
            r+=1
        if (cubo[i]+1==anterior+1 and cubo[i]-1==anterior-1):
            r+=3
        anterior=cubo[i]
    return r

def aplicarMovimiento(cubo,movimientos):
    global movDesorden 
    r=copy.copy(cubo)
    for movimiento in movimientos:
        r[movimiento[1]]=cubo[movimiento[0]]
    movDesorden+=[movimiento]
    mostrarCubo2D(cubo)
    return r

def mostrarCubo2D(cubo):
    print(" "*12 + str(cubo[:3]))
    print(" "*12 + str(cubo[3:6]))
    print(" "*12 + str(cubo[6:9]))
    
    print(str(cubo[36:39])+ str(cubo[9:12])+ str(cubo[18:21])+ str(cubo[27:30]))
    print(str(cubo[39:42])+str(cubo[12:15])+str(cubo[21:24])+str(cubo[30:33]))
    print(str(cubo[42:45])+ str(cubo[15:18])+ str(cubo[24:27])+ str(cubo[33:36]))

    print(" "*12 + str(cubo[45:48]))
    print(" "*12 + str(cubo[48:51]))
    print(" "*12 + str(cubo[51:54]))

def randomCube(cubo,cantidadMovimientos):
    global movimientos, movDesorden 
    while(cantidadMovimientos>0):
        cubo=aplicarMovimiento(cubo,movimientos[random.randrange(0,len(movimientos)-1)])
        cantidadMovimientos-=1
    return cubo

#Funcion para obtener la lista de indices de los movimientos para desordenar el cubo
def obtenerCuboDesordenado():
    global movDesorden, movimientos
    cont1=0
    cont2=0
    movInicial=[]
    while cont1<len(movDesorden):
        while cont2<len(movimientos):
            if movDesorden[cont1] in movimientos[cont2]:
                movInicial+=[cont2]
                cont2+=1
            else:
                movInicial=movInicial
                cont2+=1
        cont1+=1
        cont2=0
    return movInicial

movs=int(input("Cantidad de movimientos para cubo random: "))
cuboInicial.cubo=randomCube(meta,movs)
mostrarCubo2D(cuboInicial.cubo)                
main()
