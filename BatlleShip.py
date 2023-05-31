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
    if len(mensaje)==0:
        coordenada=int(input(f"Ingrese la Coordenada Central de su {i+1}°barco: "))
    else:
         coordenada=int(input(f"{mensaje}\nIngrese la Coordenada Central de su {i+1}°barco: "))
    coordenada=str(coordenada)
    coordenada=coordenada.zfill(digitos*2)
    if sinbarcosjugador.count(coordenada)==0:
        coordenada=int(input(f"----------\nCelda invalida\nIngrese de nuevo la Coordenada Central de su {i+1}°barco: "))
        coordenada=str(coordenada)
        coordenada=coordenada.zfill(digitos*2)
    return(coordenada)

N=int(input("Ingrese el tamaño del tablero: "))
while N<10 or N>1000:
    N=int(input("----------\nValor fuera de rango, debe ser mayor o igual a 10\nIngrese el tamaño del tablero: "))
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
computadora=jugador

barcostotales=int(input("Ingrese la cantidad de barcos en juego por jugador: "))
while barcostotales<=2 or barcostotales>N:
    barcostotales=int(input(f"----------\nValor fuera de rango\nDebe ser mayor a 2 y menor o igual a {N}\nIngrese la cantidad de barcos en juego por jugador: "))
#Ingreso de la cantidad de barcos por jugdor
barcosjugador={}    #Diccionario en que se guardaran las coordenadas del jugador.
sinbarcosjugador=jugador
for i in range(barcostotales):
    coordenada=coordenadacentral(i,"")
    orientacion=str(input(f"Ingrese la horientacion de su {i+1}°Barco(V o H): "))
    while orientacion !="V" and orientacion !="H":
        orientacion=str(input(f"----------\nValor erroneo, vuelva a ingresarlo\nIngrese la horientacion de su {i+1}°Barco(V o H): "))
    if orientacion == "V":
        CBarco=coordenadasverticales(coordenada,i)
        for j in range(len(CBarco)):
            while sinbarcosjugador.count(CBarco[j])==0:
                coordenada=coordenadacentral(i,"Valor erroneo")
        par={}
        par.setdefault((i+1),coordenadasverticales)
        barcosjugador.update(par)
        par.clear()
    if orientacion == "H":
        CBarco=coordenadashorizontales(coordenada,i)
        for j in range(len(CBarco)):
            while sinbarcosjugador.count(CBarco.get(j+1))==0:
                coordenada=coordenadacentral(i,"Valor erroneo")
        par={}
        par.setdefault((i+1),coordenadasverticales)
        barcosjugador.update(par)
        par.clear()
 
        #FALTA RESTRINGIR LA SELECCION DE CELDAS DEPENDIENDO DEL LUGAR
print(barcosjugador)
print(sinbarcosjugador)