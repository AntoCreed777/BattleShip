def eliminarcaracter(s,p,digitos):
    lista=list(s)
    a=p
    for i in range(digitos):
        lista.pop(a)
        a=a-1
    lista=("").join(lista)
    return lista
def coordenadasverticales(coordenada,i):
        guardadomomentaneo=[]
        coordenada=int(coordenada)
        coordenada=coordenada-1
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
        for q in range(3):
                guardadomomentaneo.insert(1,coordenada)
                coordenada=int(coordenada)
                coordenada=coordenada+1
                coordenada=str(coordenada)
                coordenada=coordenada.zfill(digitos*2)
        return(guardadomomentaneo)
def coordenadashorizontales(coordenada,i):
        guardadomomentaneo=[]
        coordenada=int(coordenada)
        coordenada=coordenada-10**digitos
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
        for q in range(3):
                guardadomomentaneo.insert(1,coordenada)
                coordenada=int(coordenada)
                coordenada=coordenada+10**digitos
                coordenada=str(coordenada)
                coordenada=coordenada.zfill(digitos*2)
        return(guardadomomentaneo)
def coordenadacentral(i,mensaje):
    if len(mensaje)!=0:
        coordenada=ingresonumero(f"{mensaje}\nIngrese la Coordenada Central de su {i+1}°barco: ")
    else:
        coordenada=ingresonumero(f"Ingrese la Coordenada Central de su {i+1}°barco: ")
    coordenada=coordenada.zfill(digitos*2)
    if celdasasignacionjugador.count(coordenada)==0:
        coordenada=ingresonumero(f"----------\nCelda invalida\nIngrese de nuevo la Coordenada Central de su {i+1}°barco: ")
        coordenada=coordenada.zfill(digitos*2)
    return(coordenada)
def orientacionf(i,coordenada,mensaje):
    orientacion=str(input(f"Ingrese la horientacion de su {i+1}°Barco(V o H): "))
    orientacion=orientacion.lower()
    while orientacion !="v" and orientacion !="h":
        orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la horientacion de su {i+1}°Barco(V o H): "))
        orientacion=orientacion.lower()
    if orientacion == "v":
        CBarco=coordenadasverticales(coordenada,i)
    if orientacion == "h":
        CBarco=coordenadashorizontales(coordenada,i)    
    return(CBarco)
def perimetrodelbarco(coordenadas,digitos):
     perimetro=[]
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
     for i in range(len(perimetro)):
          cantidad=perimetro.count(perimetro[i])
          if cantidad>1:
              perimetro.remove(perimetro[i])
              perimetro.insert(1,"")
              c+=1
     for i in range(c):
        perimetro.remove("")
     return(perimetro)
def ingresonumero(mensaje):
    N=str(input(f"{mensaje}"))
    while True:
        if N[0]=="-":
            N=str(input(f"Solo se aceptan numeros positivos\n{mensaje}"))
        if N.isdigit()==False:
            N=str(input(f"Solo se aceptan numeros\n{mensaje}"))
            i=0
        else:
            break
    return(N)
def validacioncasilla(coordenadas):
    for j in range(len(coordenadas)):
        if celdasasignacionjugador.count(coordenadas[j])==0:
            return False
    return True     

N=ingresonumero("Ingrese el tamaño del tablero: ")
N=int(N)
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10\nIngrese el tamaño del tablero: ")
    N=int(N)
#Ingreso de N, el tamaño del lado del tablero

x=N
digitos=0
while x!=0:
    x=x//10
    digitos=digitos+1
#Generacion de digitos, la cual almacena el tamaño del cual deberan ser las coordenadas

p=digitos*2-1
jugador=[]
coordenada=[]
for i in range(N):
    x=i+1
    x=str(x)
    x=x.zfill(digitos)
    coordenada.insert(1,x)
    for j in range(N):
        y=j+1
        y=str(y)
        y=y.zfill(digitos)
        coordenada.insert(2,y)
        coordenada=("").join(coordenada)
        jugador.insert(1,coordenada)
        c=eliminarcaracter(coordenada,p,digitos)
        coordenada=[]
        coordenada.insert(1,c)
        y=int(y)
    coordenada=[]
    x=int(x)
#Generacion de todas las posibles coordenadas en el tablero de tamaño N, con longitud de las coordenadas "digitos".
computadora=jugador.copy()
sinbarcosjugador=jugador.copy()
sinbarcoscomputadora=jugador.copy()
celdasasignacionjugador=jugador.copy()
celdasasignacioncomputadora=jugador.copy()
#Genero todas las listas a las que se les dara uso despues
barcostotales=ingresonumero("Ingrese la cantidad de barcos en juego por jugador: ")
barcostotales=int(barcostotales)
while barcostotales<=2 or barcostotales>N:
    barcostotales=ingresonumero(f"----------\nValor fuera de rango\nDebe ser mayor a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: ")
    barcostotales=int(barcostotales)
#Ingreso de la cantidad de barcos por jugdor

barcosjugador={}    #Diccionario en que se guardaran las coordenadas del jugador.
for i in range(barcostotales):
    coordenada=coordenadacentral(i,"")
    CBarco=orientacionf(i,coordenada,"")
    while validacioncasilla(CBarco)==False:
        coordenada=coordenadacentral(i,"Valor erroneo")
        CBarco=orientacionf(i,coordenada,"")
    par={}
    par.setdefault((i+1),CBarco)
    barcosjugador.update(par)
    for k in range(3):
            sinbarcosjugador.remove(CBarco[k])
    perimetro=perimetrodelbarco(CBarco,digitos)
    for k in range(len(perimetro)):
        x=perimetro[k]
        if celdasasignacionjugador.count(x)==0:
                None
        else:
            celdasasignacionjugador.remove(x)


print(barcosjugador)
print(celdasasignacionjugador)
print(sinbarcosjugador)