import random
def ingresonumero(mensaje):
    N=str(input(f"{mensaje}"))
    while True:
        if N=="":
            N=str(input(f"\nPor favor, ingrese un dato\n{mensaje}"))
        elif N[0]=="-":
            N=str(input(f"\nSolo se aceptan numeros positivos\n{mensaje}"))
        elif N.isdigit()==False:
            N=str(input(f"\nSolo se aceptan numeros\n{mensaje}"))
            i=0
        else:
            N=int(N)
            break
    return(N)
def matriz(N):
    aux=""
    fila=[]
    matriz=[]
    for i in range(N):
        fila.append(aux)
    for i in range(N):
        fila2=fila.copy()
        matriz.append(fila2)
    return(matriz)
def mostrarmatriz(matriz):
    for i in range(N):
        print(f"{matriz[i]}\n")
def barco(i,mensaje,quien,N,matriz):
    if quien=="Jugador":
        if len(mensaje)!=0:
            print(mensaje)
        x=ingresonumero(f"Ingrese la Coordenada Central 'X'de su {i+1}°barco: ")
        y=ingresonumero(f"Ingrese la Coordenada Central 'Y'de su {i+1}°barco: ")
        while x>N or y>N or matriz[y-1][x-1]=="B" or matriz[y-1][x-1]=="P":
            x=ingresonumero("Ingrese nuevamente la Coordenada Central 'X'de su {i+1}°barco: ")
            y=ingresonumero("Ingrese nuevamente la Coordenada Central 'Y'de su {i+1}°barco: ")
        orientacion=str(input(f"Ingrese la horientacion de su {i+1}°Barco(V o H): "))
        orientacion=orientacion.lower()
        while orientacion !="v" and orientacion !="h":
            orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la horientacion de su {i+1}°Barco(V o H): "))
            orientacion=orientacion.lower()
        cbarco=coordenadao(x,y,orientacion)
        for j in range(3):
            while cbarco[j][1]==0 or cbarco[j][1]>(len(matriz)) or cbarco[j][0]==0 or cbarco[j][0]>(len(matriz)):
                cbarco=barco(i,"El barco no es valido","Jugador",N,matriz)
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
def validacionbarco(i,cbarco,matriz):
    for j in range(3):
        while matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="B" or matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="P":
            cbarco=barco(i,"El barco no es valido","Jugador",N,matriz)
    return(cbarco)
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
    
    
N=ingresonumero("Ingrese el tamaño del tablero: ")              #Ingreso de N, el tamaño del lado del tablero
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10 y menor o igual a 1000\nIngrese el tamaño del tablero: ")

x=N
digitos=0
while x!=0:
    x=x//10
    digitos=digitos+1

matriz=matriz(N)       #Genera una matriz hecha por listas de N Filas y N Columnas 

barcostotales=ingresonumero("Ingrese la cantidad de barcos en juego por jugador: ")     #Ingreso de la cantidad de barcos por jugdor
while barcostotales<2 or barcostotales>N:
    barcostotales=ingresonumero(f"----------\nValor fuera de rango\nDebe ser mayor o igual a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: ")

#########################################################
#PARTE DE ASIGNACION DEL JUGADOR#
#########################################################
barcosjugador=[]
barcoa=[]
for i in range(barcostotales):
    cbarco=validacionbarco(i,barco(i,"","Jugador",N,matriz),matriz)
    for j in range(3):
        y=(cbarco[j][1]-1)
        x=(cbarco[j][0]-1)
        matriz[y][x]="B"
        aux=str(cbarco[i][0]).zfill(digitos)+str(cbarco[i][1]).zfill(digitos)
        barcoa.insert(0,aux)
    print(f"Estas son las coordenadas de su barco{cbarco}")
    barcosjugador.append(barcoa)
    matriz=perimetro2(cbarco,digitos,matriz)
    mostrarmatriz(matriz)
#########################################################
#PARTE DE ASIGNACION DE LA COMPUTADORA#
#########################################################
matrizcompu=matriz.copy()
barcoscomputadora=[]
barcoa=[]
for i in range(barcostotales):
    cbarco=validacionbarco(i,barco(i,"","Computadora",N,matrizcompu),matrizcompu)
    for j in range(3):
        y=(cbarco[j][1]-1)
        x=(cbarco[j][0]-1)
        matriz[y][x]="B"
        aux=str(cbarco[i][0]).zfill(digitos)+str(cbarco[i][1]).zfill(digitos)
        barcoa.insert(0,aux)
    barcoscomputadora.append(barcoa)
    matrizcompu=perimetro2(cbarco,digitos,matrizcompu)
    mostrarmatriz(matrizcompu)