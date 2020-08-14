import copy
import time
import random
import operator

class Cubo:
    def __init__(self, cubo, listaMovimientos,idCubo,nota):
        self.cubo = cubo
        self.nota = nota
        self.listaMovimientos = listaMovimientos
        self.idCubo=idCubo
        self.nota = nota
    


cerrados=[]
seleccionado=0
notaMaxima=0

idCubo=1
meta=[ 0,1 ,2 ,3 ,4 ,5 ,6 ,7 , 8,
       9,10,11,12,13,14,15,16,17,
      18,19,20,21,22,23,24,25,26,
      27,28,29,30,31,32,33,34,35,
      36,37,38,39,40,41,42,43,44,
      45,46,47,48,49,50,51,52,53]


explorados={}


movimientos=[[[12,48],[9,45],[0,9],[3,12],[15,51],[6,15],[45,35],[48,32],[51,29],[35,0],[32,3],[29,6],[36,38],[37,41],[38,44],[41,43],[44,42],[43,39],[42,36],[39,37]],#verticalIzquierda
            [[2,11],[5,14],[8,17],[11,47],[14,50],[17,53],[47,33],[50,30],[53,27],[33,2],[30,5],[27,8],[18,24],[19,21],[20,18],[23,19],[26,20],[25,23],[24,26],[21,25]],#verticalDerecha
            [[36,9],[37,10],[38,11],[9,18],[10,19],[11,20],[18,27],[19,28],[20,29],[27,36],[28,37],[29,38],[0,6],[3,7],[6,8],[7,5],[8,2],[5,1],[2,0],[1,3]],#horizontalArriba
            [[42,15],[43,16],[44,17],[15,24],[16,25],[17,26],[24,33],[25,34],[26,35],[33,42],[34,43],[35,44],[45,47],[46,50],[47,53],[50,52],[53,51],[52,48],[51,45],[48,46]],#horizontalAbajo
            [[9,11],[10,14],[11,17],[14,16],[17,15],[16,12],[15,9],[12,10],[38,8],[41,7],[44,6],[6,18],[7,21],[8,24],[18,47],[21,46],[24,45],[47,44],[46,41],[45,38]],#rotacionAdelante
            [[39,1],[36,2],[27,33],[30,34],[35,29],[32,28],[0,20],[1,23],[2,26],[20,53],[23,52],[26,51],[53,42],[52,39],[51,36],[42,0],[29,27],[28,30],[33,35],[34,32]]#rotacionatras
            ]

##FUNCIONES DE SOLUCION 
def permutaciones(abierto):
    global idCubo,movimientos,explorados,abiertos,cerrados,seleccionado,notaMaxima
    cerrados+=[abierto]
    i=0
    movs=len(abierto.listaMovimientos)
    seleccionado=None
    if(movs>22):
        return
    for movimiento in movimientos:
        cuboNuevo = copy.copy(abierto.cubo)
        cuboNuevoR= copy.copy(abierto.cubo)
        for instruccion in movimiento:
            cuboNuevo [instruccion[0]]=abierto.cubo[instruccion[1]]
            cuboNuevoR[instruccion[1]]=abierto.cubo[instruccion[0]]

        if(str(cuboNuevo) not in explorados):
            nota= (22-movs)*120 + medir(cuboNuevo)
            explorados[str(cuboNuevo)]=1
            if(nota>notaMaxima):
                notaMaxima=nota
                seleccionado=len(abiertos)
            abiertos+=[Cubo(cuboNuevo,abierto.listaMovimientos+[i+1],idCubo,nota)]
            
        if(str(cuboNuevoR)not in explorados):
            nota= (22-movs)*120 + medir(cuboNuevoR)
            explorados[str(cuboNuevoR)]=1
            if(nota>notaMaxima):
                notaMaxima=nota
                seleccionado=len(abiertos)
            abiertos+=[Cubo(cuboNuevoR,abierto.listaMovimientos+[-(i+1)],idCubo,nota)]
        i+=1

def main():
    global meta,abiertos,notaMaxima,seleccionado,cerrados
    i=0
    seleccionado=abiertos.pop(0)
    while(True):
        if(i==1000):
            print(len(abiertos))
            i=0
        if(seleccionado.cubo==meta):
            mostrarCubo2D(seleccionado.cubo)
            print("Movimientos",seleccionado.listaMovimientos,len(seleccionado.listaMovimientos))
            return seleccionado
        permutaciones(seleccionado)
        if(seleccionado==None):
            abiertos=sorted(abiertos,key=lambda cubo : cubo.nota )
            seleccionado=abiertos.pop(len(abiertos)-1)
            notaMaxima=abiertos[0].nota
        else:
            seleccionado=abiertos[seleccionado]
            notaMaxima=0
        i+=1
    


def medir(cubo):
    global meta
    r=0
    anterior=0
    dif=[]
    aUnMov=[[9, 35, 6, 2, 20, 42], [5, 3, 39, 23], [11, 33, 8, 0, 36, 26], [12, 32, 7, 1], [14, 30, 7, 1], [15, 29, 0, 8, 44, 18], [3, 5, 41, 21], [17, 27, 6, 2, 38, 24],
     [45, 0, 36, 18, 11, 15], [37, 19, 14, 12], [2, 47, 38, 20, 9, 17], [48, 3, 16, 10], [5, 50, 10, 16], [51, 6, 42, 24, 17, 9], [43, 25, 14, 12], [8, 53, 44, 26, 11, 15],
     [24, 20, 9, 27, 6, 47], [21, 23, 10, 28], [18, 26, 11, 29, 0, 53], [19, 25, 7, 46], [19, 25, 1, 52], [18, 26, 15, 33, 8, 45], [23, 21, 16, 34], [20, 24, 17, 35, 2, 51],
     [53, 8, 18, 36, 33, 29], [19, 37, 32, 30], [51, 6, 20, 38, 35, 27], [50, 5, 34, 28], [48, 3, 28, 34], [47, 2, 24, 42, 27, 35], [25, 43, 30, 32], [45, 0, 26, 44, 29, 33],
     [38, 42, 9, 27, 2, 51], [41, 39, 10, 28], [36, 44, 11, 29, 8, 45], [43, 37, 1, 52], [37, 43, 7, 46], [44, 36, 15, 33, 53, 0], [41, 39, 16, 34], [38, 42, 17, 35, 6, 47],
     [9, 35, 47, 51, 24, 38], [50, 48, 21, 41], [11, 33, 45, 53, 18, 44], [12, 32, 52, 46], [14, 30, 46, 52], [15, 29, 53, 45, 26, 36], [50, 48, 23, 39], [17, 27, 47, 51, 20, 42]]
    bonusCara=0
    for i in range(0,len(meta)):
        centro=(i//9)*9+4

        #Cambio de cara
        if(i%9==0):
            bonusCara=0

        #Lugar correcto
        if (cubo[i]==meta[i]):
            r+=15

        #Pertenencia a una cara
        elif(cubo[i]-1==centro or cubo[i]-2==centro or cubo[i]-3==centro or cubo[i]-4==centro or cubo[i]+4==centro or cubo[i]+3>centro or cubo[i]+2>centro or cubo[i]+1>centro):#en el rango del centro, por eso tanto if
            r+=5
            bonusCara+=1

        #A un movimiento de donde debe estar
        else:
            for v in aUnMov:
                if(cubo[i]==v):
                    r+=3
                    break

        #Toda la cara
        if(bonusCara==8):
            r+=30
        
    return r

    


##FUNCIONES DE PRUEBAS
def aplicarMovimiento(cubo,movimientos):
    r=copy.copy(cubo)
    for movimiento in movimientos:
        r[movimiento[1]]=cubo[movimiento[0]]
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
    print()

def randomCube(cubo,cantidadMovimientos):
    global movimientos
    while(cantidadMovimientos>0):
        selected=random.randrange(0,len(movimientos)-1)
        cubo=aplicarMovimiento(cubo,movimientos[selected])
       # print(selected)
        cantidadMovimientos-=1
    return cubo

##FUNCIONES DE EXPERIMENTOS
#imprimirAbiertos
def inotas():
    global abiertos
    for cubo in range(0,len(abiertos)):
        print(len(cubo.listaMovimientos),abiertos[len(abiertos)-cubo].nota)
            
def ipuntajeMovimientos():
    global meta
    for i in range(0,10):
        print(medir(randomCube(meta,i)))



cantidadMovs=int(input("Cantidad de movimientos para cubo random: "))
abiertos=[Cubo(randomCube(meta,cantidadMovs),[],0,0)]
print("Entrada")
mostrarCubo2D(meta)
mostrarCubo2D(abiertos[0].cubo)
print(medir(meta))
input()
print("Corriendo...")
time1 = time.time()
abierto=main()
time2 = time.time()
print("Tiempo: ",(time2-time1))


