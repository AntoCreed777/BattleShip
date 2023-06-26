##Integrantes:
#Antonio Benavides
#Pablo Villagrán
#Renato Galan
#Lucas Morales

import random
import os
def preguntas(N):                                               #Funcion para facilitar la funcion ingreso numero()
    if N=="":                                                   #Comprueba que se haya ingresado algun dato
        return "nada"
    if N[0]=="-":                                               #Comprueba que no sea negativo(Esto se podria verificar con el siguiente if pero deseamos es mostrar un mensaje especial para este caso)
        return "negativo"
    elif N.isdigit()==False:                                    #Comprueba que la entrada sea un numero
        return "nonum"
    N=float(N)
    if N==0:                                                    #Comprueba que el valor de la entrada no sea cero
        return "escero"
    else:
        return True                                             #Si llego hasta esta parte significa que el valor ingresado es correcto
def ingresonumero(mensaje):                                     #Funcion que verifica que sea un numero valido la entrada
    N=str(input(f"{mensaje}"))                                  #Ingreso de un dato
    while True:
        aux=preguntas(N)                                        #Se llama a la funcion preguntas que retornara un dato dependiendo del caso
        if aux==True:                                           #Si aux es True osea que el nuemro es valido, retornara ese numero en int
            N=int(N)
            return(N)
        if aux=="nada":                                         #Si ese dato no contenia nada, pide que lo vuelva a ingresar
            N=str(input(f"\nPor favor, ingrese un dato\n{mensaje}"))
        if aux=="negativo":                                     #Si ese dato era negativo, pide que lo vuelva a ingresar
            N=str(input(f"\nSolo se aceptan numeros positivos\n{mensaje}"))
        if aux=="nonum":                                        #Si ese dato no era un numero, pide que lo vuelva a ingresar
            N=str(input(f"\nSolo se aceptan numeros\n{mensaje}"))
        if aux=="escero":                                       #Si ese dato era un cero, pide que lo vuelva a ingresar
            N=str(input(f"\nEl 0 no es valido\n{mensaje}"))
def matriz(N):
    aux="_"                                                     #Variable auxiliar que almacena "_" para rellenar la matriz
    fila=[]                                                     #Lista que representa a una fila y que se ingresara en matriz con aux dentro de ella
    matriz=[]                                                   #Lista que representa a la matriz
    for i in range(N):
        fila.append(aux)                                        #Se ingresa N veces aux dentro de fila
    for i in range(N):
        fila2=fila.copy()                                       #Se copia la informacion en otra lista debido a que luego si mudificabamos una coordenada se modificaba en todas las demas filas
        matriz.append(fila2)                                    #Se ingresa N veces fila2 dentro de matriz
    return(matriz)                                              #Retorna la matriz creada
def mostrarmatriz(matriz):                                      #Funcion que imprime la matriz de forma limpia y como un plano cartesiano en el Cuadrante I
    for i in range(-1,-(N+1),-1):
        for j in range(N):
            print(matriz[i][j],"    ",end="")
        print("\n")
def barco(i,mensaje,quien,N,matriz):                            #Funcion que crea y verifica(Solo la coordenda central) los barcos
    if quien=="Jugador":
        if len(mensaje)!=0:
            print(mensaje)                                      #Si hay un mensaje que mostrar, lo muestra
        x=ingresonumero(f"Ingrese la Coordenada Central 'X'de su {i+1}°barco: ")    #Se ingresa la coordenada en X
        y=ingresonumero(f"Ingrese la Coordenada Central 'Y'de su {i+1}°barco: ")    #Se ingresa la coordenada en Y
        while x>N or y>N or matriz[y-1][x-1]=="B" or matriz[y-1][x-1]=="P":         #Verifica la valides de esas coordenadas
            x=ingresonumero(f"Ingrese nuevamente la Coordenada Central 'X'de su {i+1}°barco: ") #Se ingresa nuevamente la coordenada en X
            y=ingresonumero(f"Ingrese nuevamente la Coordenada Central 'Y'de su {i+1}°barco: ") #Se ingresa nuevamente la coordenada en Y
        orientacion=str(input(f"Ingrese la orientación de su {i+1}°Barco(V o H): "))    #Se ingresa la orientacion del barco
        orientacion=orientacion.lower() #Lo convierte en minusculas para aceptar las palabras sin importar como la escriban
        while orientacion !="v" and orientacion !="h":  #Verifica que hayan ingresado una orientacion valida
            orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la orientación de su {i+1}°Barco(V o H): "))
            orientacion=orientacion.lower()
        cbarco=coordenadao(x,y,orientacion)     #LLama a la funcion coordenadao debolviendo todas las coordenadas del barco 
    if quien=="Computadora":            #Lo mismo que en jugador, pero randomizado
        x=random.randint(1,N)
        y=random.randint(1,N)
        while matriz[y-1][x-1]=="B" or matriz[y-1][x-1]=="P":
            x=random.randint(1,N)
            y=random.randint(1,N)
        orientaciones=["v","h"]
        orientacion=random.choice(orientaciones)
        cbarco=coordenadao(x,y,orientacion)
    return(cbarco)                                      #Retorna las coordenadas del barco
def coordenadao(x,y,orientacion):                               #Funcion que genera las coordenadas de todo un barco
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
def validacionbarco(cbarco,matriz):                             #Funcion que valida las coordenadas de todo un barco
    for j in range(3):
        if cbarco[j][1]==0 or cbarco[j][0]==0:
            return(False)
        elif cbarco[j][1]>(len(matriz)) or cbarco[j][0]>(len(matriz)):
            return(False)
        elif matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="B" or matriz[(cbarco[j][1])-1][(cbarco[j][0])-1]=="P":
            return(False)
    return(True)
def perimetro1(cbarco,digitos):                                 #Funcion que genera el perimetro de un barco pero con Strings
     perimetro=[]
     coordenadas=[]
     for i in range(3):
         aux=str(cbarco[i][0]).zfill(digitos)+str(cbarco[i][1]).zfill(digitos)
         coordenadas.insert(0,aux)                              #El formato de las coordenadas en Strings es XXYY
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
def perimetro2(cbarco,digitos,matriz):                          #Funcion que coloca P de perimetro en donde le indica la funcion perimetro1()
    c=perimetro1(cbarco,digitos)
    for i in range(len(c)):
        x=int(c[i])//(10**digitos)-1
        y=int(c[i])%(10**digitos)-1
        if x<len(matriz) and y<len(matriz) and y>=0 and x>=0:
            matriz[y][x]="P"
    return(matriz)
def hundimiento(quien):                                         #Funcion que verifica si un barco se hundio(y luego lo elimina) o no
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

matrizjugadorByP=matriz(N)      #Genera la matriz del jugador para sus barcos y perimetro hecha por listas de N Filas y N Columnas 
matrizjugador=matriz(N)         #Genera la matriz del jugador sin barcos ni perimetro hecha por listas de N Filas y N Columnas
matrizcompuByP=matriz(N)        #Genera la matriz de la computadora para sus barcos y perimetro hecha por listas de N Filas y N Columnas
matrizcompu=matriz(N)           #Genera la matriz de la computadora sin barcos ni perimetro hecha por listas de N Filas y N Columnas

barcostotales=ingresonumero("Ingrese la cantidad de barcos en juego por jugador: ")     #Ingreso de la cantidad de barcos por jugdor
while barcostotales<2 or barcostotales>N:   #Valida que el valor este dentro del rango
    barcostotales=ingresonumero(f"----------\nValor fuera de rango\nDebe ser mayor o igual a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: ")


#########################################################
#PARTE DE ASIGNACION DEL JUGADOR#
#########################################################
barcosjugador=[]            #Lista donde se guardaran las listas de los barcos del jugador
barcoa=[]                   #Lista auxiliar que almacena las coordenadas de un solo barco las cuales se ingresaran en barcosjugador
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
    mostrarmatriz(matrizjugadorByP)         #Muestra la matriz donde se estan guardando los barcos
    
#########################################################
#PARTE DE ASIGNACION DE LA COMPUTADORA#
#########################################################
barcoscomputadora=[]        #Lista donde se guardaran las listas de los barcos de la compuatdora
barcoa=[]                   #Lista auxiliar que almacena las coordenadas de un solo barco las cuales se ingresaran en barcoscomputadora
for i in range(barcostotales):  #genera los barcos de forma random
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
matriztiroscompu=matriz(N)      #Genera la matriz de tiros de la computadora hecha por listas de N Filas y N Columnas
matriztirosjugador=matriz(N)    #Genera la matriz de tiros del jugador hecha por listas de N Filas y N Columnas

comienzo=str(input("Ingrese quien comienza(jugador o computadora): "))  #Se ingresa quien comienza con el juego
comienzo=comienzo.lower()
while comienzo!="jugador" and comienzo!="computadora":  #Se verifica que este bien ingresado
     comienzo=str(input("Ingrese quien comienza(jugador o computadora): "))
while True:         #Bucle de los turnos de juego
     if comienzo=="jugador":
        x=ingresonumero(f"Ingrese la Coordenada de ataque 'X': ")   #Se ingresan las coordenadas de ataque
        y=ingresonumero(f"Ingrese la Coordenada de ataque 'Y': ")
        while x>N or y>N or matriztirosjugador[y-1][x-1]=="X" or  matriztirosjugador[y-1][x-1]=="A":    #Se verifican esas coordenadas
            x=ingresonumero(f"Ingrese nuevamente la Coordenada de ataque 'X': ")
            y=ingresonumero(f"Ingrese nuevamente la Coordenada de ataque 'Y': ")
        os.system("cls")        #Se limpia la terminal para que se vea mas pulido la interfas de juego
        if matrizcompu[y-1][x-1]=="B":
            print("Has dado en un barco")
            matriztirosjugador[y-1][x-1]="X"
            matrizcompu[y-1][x-1]="X"
            aux=str(x).zfill(digitos)+str(y).zfill(digitos)         #Transforma la coordenada a un formato de String para poder eliminarla de la lista de los barcos
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
        hundimiento("Jugador")                                  #Verifica si se a hundido algun barco en este turno 
        if len(barcoscomputadora)==0:                           #verifica que a la computadora le queden barcos
            Ganador="Jugador"                                   #Si no le quedan da por ganador al jugador
            break
        mostrarmatriz(matriztirosjugador)                       #Muestra la matriz en que se almacena donde se a disparado hasta el momento
        print(f"Al enemigo le quedan {len(barcoscomputadora)} barcos.")
        comienzo="computadora"
     if comienzo=="computadora":        #Lo mismo que en la parte del jugador, pero con todos los valores en random
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
if Ganador=="Jugador":      #Mensaje si el jugador gana
     print("Bien hecho camarada, habéis demostrado vuestra valia, POR LA MADRE PATRIA!!!!!")
if Ganador=="Computadora":  #Mensaje si la computadora gana
     print("NOS HAN DERROTADO, RETIRADAAAA!!!!")