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

N=ingresonumero("Ingrese el tamaño del tablero: ")
while N<10 or N>1000:
    N=ingresonumero("----------\nValor fuera de rango, debe ser mayor o igual a 10 y menor o igual a 1000\nIngrese el tamaño del tablero: ")

matriz(N)


