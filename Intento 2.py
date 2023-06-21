import random
import os
def preguntas(N):
    if N=="":
        return "nada"
    if N[0]=="-":
        return "negativo"
    elif N.isdigit()==False:
        return "nonum"
    N=float(N)
    if N==0:
        return "escero"
    else:
        return True
def ingresonumero(mensaje):
    N=str(input(f"{mensaje}"))
    while True:
        aux=preguntas(N)
        if aux==True:
            N=int(N)
            return(N)
        if aux=="nada":
            N=str(input(f"\nPor favor, ingrese un dato\n{mensaje}"))
        if aux=="negativo":
            N=str(input(f"\nSolo se aceptan numeros positivos\{mensaje}"))
        if aux=="nonum":
            N=str(input(f"\nSolo se aceptan numeros\n{mensaje}"))
        if aux=="escero":
            N=str(input(f"\nEl 0 no es valido\n{mensaje}"))
def matriz(N):
    aux="_"
    fila=[]
    matriz=[]
    for i in range(N):
        fila.append(aux)
    for i in range(N):
        fila2=fila.copy()
        matriz.append(fila2)
    return(matriz)
def mostrarmatriz(matriz):
    for i in range(-1,-(N+1),-1):
        for j in range(N):
            print(matriz[i][j],"    ",end="")
        print("\n")
def barco(i,mensaje,quien,N,matriz):
    if quien=="Jugador":
        if len(mensaje)!=0:
            print(mensaje)
        x=ingresonumero(f"Ingrese la Coordenada Central 'X'de su {i+1}°barco: ")
        y=ingresonumero(f"Ingrese la Coordenada Central 'Y'de su {i+1}°barco: ")
        while x>N or y>N or matriz[y-1][x-1]=="B" or matriz[y-1][x-1]=="P":
            x=ingresonumero(f"Ingrese nuevamente la Coordenada Central 'X'de su {i+1}°barco: ")
            y=ingresonumero(f"Ingrese nuevamente la Coordenada Central 'Y'de su {i+1}°barco: ")
        orientacion=str(input(f"Ingrese la orientación de su {i+1}°Barco(V o H): "))
        orientacion=orientacion.lower()
        while orientacion !="v" and orientacion !="h":
            orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la orientación de su {i+1}°Barco(V o H): "))
            orientacion=orientacion.lower()
        cbarco=coordenadao(x,y,orientacion)
    if quien=="Computadora":
        x=random.randint(1,N)
        y=random.randint(1,N)
        while matriz[y-1][x-1]=="B" or matriz[y-1][x-1]=="P":
            x=random.randint(1,N)
            y=random.randint(1,N)
        orientaciones=["v","h"]
        orientacion=random.choice(orientaciones)
        cbarco=coordenadao(x,y,orientacion)
    return(cbarco)
def coordenadao(x,y,orientacion):
    cbarco=[]
    c=[]
    if orientacion=="v":
        y=y-1
        for q in range(3):
            c.append(x)
            c.append(y)
            cbarco.append(c)
            y=y+1
            c=[]
    if orientacion=="h":
        x=x-1
        for q in range(3):
            c.append(x)
            c.append(y)
            cbarco.append(c)
            x=x+1
            c=[]
    return(cbarco)
def validacionbarco(cbarco,matriz):
    for j in range(3):
        if cbarco[j][1]==0 or cbarco[j][0]==0:
            return(False)
        elif cbarco[j][1]>(len(matriz)) or cbarco[j][0]>(len(matriz)):
            return(False)
        elif matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="B" or matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="P":
            return(False)
    return(True)
def perimetro1(cbarco,digitos):
     perimetro=[]
     coordenadas=[]
     for i in range(3):
         aux=str(cbarco[i][0]).zfill(digitos)+str(cbarco[i][1]).zfill(digitos)
         coordenadas.insert(0,aux)
     for i in range(3):
        perimetro.insert(1,coordenadas[i])
        x=coordenadas[i]
        x=int(x)
        superior=str(x+100)
        inferior=str(x-100)
        derecha=str(x+1)
        izquierda=str(x-1)
        arrribaderecha=str(x+101)
        arribaizquierda=str(x+99)
        abajoderecha=str(x-99)
        abajoizquierda=str(x-101)
        superior=superior.zfill(digitos*2)
        inferior=inferior.zfill(digitos*2)
        derecha=derecha.zfill(digitos*2)
        izquierda=izquierda.zfill(digitos*2)
        arrribaderecha=arrribaderecha.zfill(digitos*2)
        arribaizquierda=arribaizquierda.zfill(digitos*2)
        abajoderecha=abajoderecha.zfill(digitos*2)
        abajoizquierda=abajoizquierda.zfill(digitos*2)
        perimetro.insert(1,superior)
        perimetro.insert(1,inferior)
        perimetro.insert(1,derecha)
        perimetro.insert(1,izquierda)
        perimetro.insert(1,arrribaderecha)
        perimetro.insert(1,arribaizquierda)
        perimetro.insert(1,abajoderecha)
        perimetro.insert(1,abajoizquierda)
     c=0
     for i in range(len(coordenadas)):
          cantidad=perimetro.count(coordenadas[i])
          while cantidad>0:
              perimetro.remove(coordenadas[i])
              perimetro.insert(0,"")
              cantidad=cantidad-1
              c+=1
     for i in range(c):
        perimetro.remove("")
     c=0
     for i in range(len(perimetro)):
          cantidad=perimetro.count(perimetro[i])
          if cantidad>1:
              perimetro.remove(perimetro[i])
              perimetro.insert(0,"")
              c+=1
     for i in range(c):
        perimetro.remove("")
     return(perimetro)     
def perimetro2(cbarco,digitos,matriz):
    c=perimetro1(cbarco,digitos)
    for i in range(len(c)):
        x=int(c[i])//(10**digitos)-1
        y=int(c[i])%(10**digitos)-1
        if x<len(matriz) and y<len(matriz) and y>=0 and x>=0:
            matriz[y][x]="P"
    return(matriz)
def hundimiento(quien):
     if quien=="Jugador":
          for i in range(len(barcoscomputadora)):
               if len(barcoscomputadora[i])==0:
                    print("!!!BARCO HUNDIDO, CADA VES MÁS CERCA DE LA VICTORIA CAMARADA!!!")
                    barcoscomputadora.pop(i)
                    break
     if quien=="Computadora":
          for i in range(len(barcosjugador)):
               if len(barcosjugador[i])==0:
                    print("!!!NOS HAN HUNDIDO UN BARCO, DEBEMOS RESPONDER!!!")
                    barcosjugador.pop(i)
                    break
    
N=ingresonumero("Ingrese el tamaño del tablero: ")              #Ingreso de N, el tamaño del lado del tablero
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10 y menor o igual a 1000\nIngrese el tamaño del tablero: ")

x=N
digitos=0
while x!=0:
    x=x//10
    digitos=digitos+1

matrizjugadorByP=matriz(N)      #Genera una matriz hecha por listas de N Filas y N Columnas 
matrizjugador=matriz(N)
matrizcompuByP=matriz(N)
matrizcompu=matriz(N)

barcostotales=ingresonumero("Ingrese la cantidad de barcos en juego por jugador: ")     #Ingreso de la cantidad de barcos por jugdor
while barcostotales<2 or barcostotales>N:
    barcostotales=ingresonumero(f"----------\nValor fuera de rango\nDebe ser mayor o igual a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: ")


#########################################################
#PARTE DE ASIGNACION DEL JUGADOR#
#########################################################
barcosjugador=[]
barcoa=[]
for i in range(barcostotales):
    cbarco=barco(i,"","Jugador",N,matrizjugadorByP)
    while validacionbarco(cbarco,matrizjugadorByP)==False:
        cbarco=barco(i,"Barco Invalido","Jugador",N,matrizjugadorByP)
    for j in range(3):
        y=(cbarco[j][1]-1)
        x=(cbarco[j][0]-1)
        matrizjugadorByP[y][x]="B"
        matrizjugador[y][x]="B"
        aux=str(cbarco[j][0]).zfill(digitos)+str(cbarco[j][1]).zfill(digitos)
        barcoa.insert(0,aux)
    barcosjugador.append(barcoa)
    barcoa=[]
    if N<20:
        matrizjugadorByP=perimetro2(cbarco,digitos,matrizjugadorByP)
        os.system("cls")
    print(f"Estas son las coordenadas de su barco{cbarco}")
    mostrarmatriz(matrizjugadorByP)
    
#########################################################
#PARTE DE ASIGNACION DE LA COMPUTADORA#
#########################################################
barcoscomputadora=[]
barcoa=[]
for i in range(barcostotales):
    cbarco=barco(i,"","Computadora",N,matrizcompuByP)
    while validacionbarco(cbarco,matrizcompuByP)==False:
        cbarco=barco(i,"","Computadora",N,matrizcompuByP)
    for j in range(3):
        y=(cbarco[j][1]-1)
        x=(cbarco[j][0]-1)
        matrizcompuByP[y][x]="B"
        matrizcompu[y][x]="B"
        aux=str(cbarco[j][0]).zfill(digitos)+str(cbarco[j][1]).zfill(digitos)
        barcoa.insert(0,aux)
    barcoscomputadora.append(barcoa)
    barcoa=[]
    matrizcompuByP=perimetro2(cbarco,digitos,matrizcompuByP)
#print("\n\n")
#mostrarmatriz(matrizjugador)
#print("\n\n")
#mostrarmatriz(matrizcompu)

#########################################################
#PARTE DE JUEGO#
#########################################################
matriztiroscompu=matriz(N)
matriztirosjugador=matriz(N)

comienzo=str(input("Ingrese quien comienza(jugador o computadora): "))
comienzo=comienzo.lower()
while comienzo!="jugador" and comienzo!="computadora":
     comienzo=str(input("Ingrese quien comienza(jugador o computadora): "))
while True:
     if comienzo=="jugador":
        x=ingresonumero(f"Ingrese la Coordenada de ataque 'X': ")
        y=ingresonumero(f"Ingrese la Coordenada de ataque 'Y': ")
        while x>N or y>N or matriztirosjugador[y-1][x-1]=="X" or  matriztirosjugador[y-1][x-1]=="A":
            x=ingresonumero(f"Ingrese nuevamente la Coordenada de ataque 'X': ")
            y=ingresonumero(f"Ingrese nuevamente la Coordenada de ataque 'Y': ")
        os.system("cls")
        if matrizcompu[y-1][x-1]=="B":
            print("Has dado en un barco")
            matriztirosjugador[y-1][x-1]="X"
            matrizcompu[y-1][x-1]="X"
            aux=str(x).zfill(digitos)+str(y).zfill(digitos)
            for i in range(len(barcoscomputadora)):
                a=0
                for j in range(len(barcoscomputadora[i])):
                    if barcoscomputadora[i][j]==aux:
                        (barcoscomputadora[i]).remove(aux)
                        a=1
                        break
                if a==1:
                    break
        else:
            print("Has dado al agua")
            matriztirosjugador[y-1][x-1]="A"
            matrizcompu[y-1][x-1]="A"
        hundimiento("Jugador")
        if len(barcoscomputadora)==0:
            Ganador="Jugador"
            break
        mostrarmatriz(matriztirosjugador)
        print(f"Al enemigo le quedan {len(barcoscomputadora)} barcos.")
        comienzo="computadora"
     if comienzo=="computadora":
        x=random.randint(1,N)
        y=random.randint(1,N)
        while matriztiroscompu[y-1][x-1]=="X" or  matriztiroscompu[y-1][x-1]=="A":
            x=random.randint(1,N)
            y=random.randint(1,N)
        print("\nEl enemigo ")
        if matrizjugador[y-1][x-1]=="B":
            print("nos ha dado en un barco!!\n")
            matriztiroscompu[y-1][x-1]="X"
            matrizjugador[y-1][x-1]="X"
            aux=[]
            x=str(x)
            x.zfill(digitos)
            y=str(y)
            y.zfill(digitos)
            aux.insert(1,y)
            aux=str(x).zfill(digitos)+str(y).zfill(digitos)
            for i in range(len(barcosjugador)):
                a=0
                for j in range(len(barcosjugador[i])):
                    if barcosjugador[i][j]==aux:
                        (barcosjugador[i]).remove(aux)
                        a=1
                        break
                if a==1:
                    break
        else:
            print("no nos ha dado\n")
            matriztiroscompu[y-1][x-1]="A"
            matrizjugador[y-1][x-1]="A"
        hundimiento("Computadora")
        print(f"Nos quedan {len(barcosjugador)} barcos.\n")
        if len(barcosjugador)==0:
            Ganador="Computadora"
            break
        comienzo="jugador"
if Ganador=="Jugador":
     print("Bien hecho camarada, habéis demostrado vuestra valia, POR LA MADRE PATRIA!!!!!")
if Ganador=="Computadora":
     print("NOS HAN DERROTADO, RETIRADAAAA!!!!")