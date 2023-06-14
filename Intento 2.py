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
    aux=[""]
    fila=[]
    matriz=[]
    for i in range(N):
        fila.append(aux)
    for i in range(N):
        matriz.append(fila)
    return(matriz)
def mostrarmatriz(matriz):
    for i in range(N):
        print(f"{matriz(N)[i]}\n")
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


N=ingresonumero("Ingrese el tamaño del tablero: ")              #Ingreso de N, el tamaño del lado del tablero
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10 y menor o igual a 1000\nIngrese el tamaño del tablero: ")

matriz=matriz(N)       #Genera una matriz hecha por listas de N Filas y N Columnas 

barcostotales=ingresonumero("Ingrese la cantidad de barcos en juego por jugador: ")     #Ingreso de la cantidad de barcos por jugdor
while barcostotales<2 or barcostotales>N:
    barcostotales=ingresonumero(f"----------\nValor fuera de rango\nDebe ser mayor o igual a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: ")

#########################################################
#PARTE DE ASIGNACION DEL JUGADOR#
#########################################################

for i in range(barcostotales):
    cbarco=validacionbarco(i,barco(i,"","Jugador",N,matriz),matriz)
    print(cbarco)
    None