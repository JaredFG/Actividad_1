#Utilizamos la libreria random 
import random

#iniciamos las variables de ambos lados del rio  
Lado_A = ['Granjero', 'Zorro', 'Ganso', 'Maiz']
Lado_B = []
Path = []

#funcion que escoje una variable aleatoria de la lista que entra  
def seleccion(L):
    #seleccion aleatoria de la entrada L
    op = random.randint(0,len(L)-1)
    #regresamos el valor que se escogio de manera aleatoria 
    return (L[op])

#funcion que mueve el elemento de la lista de la fuente al destino 
def Viaje(F, D):
    #tomamos un valor aleatorio de la fuente
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    #si el valor es distinto a granjero, movemos el elemento de la fuente al destino
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)
    #si solo esta el granjero, lo movemos de la fuente al destino 
    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    #regresamos wl valor de granjero junto con el otro elemento de la lista  
    return ('Granjero',p1)

#Validamos que las dos condiciones impuestas por el juego para perder no se cumplan
def valida_estado(L):
    #checamos la lista de entrada para ver si estan juntos el ganso y el maiz 
    if 'Maiz' in L and 'Ganso' in L and len(L) == 2:
        #si se cumple la condicion, se levanta la bandera False y se reinicia  
        return False
     #checamos la lista de entrada para ver si estan juntos el zorro y el ganso
    elif 'Zorro' in L and 'Ganso' in L and len(L) == 2:
        #si se cumple la condicion, se levanta la bandera False y se reinicia 
        return False
    #si no se cumplen  las condiciones, se levanta l bandera True y el juego continua
    return True

def reiniciar_sistema():
    '''
    Funcion que reinicia las variables del codigo. 
    No tiene parametros y no devuelve nada.
    Se llama cuando ocurre un estado invalido o se llega a una solucion insficiente.
    Implica que todos los personajes esten en el origen, y nadie en el destino, sin
    ningun movimiento en el path.
    '''

    global Lado_A, Lado_B, Path     # variables origen y destino globales
    


def HCR():
    '''
    Funcion que lleva a cabo la dinamica de la situacion hasta una conclusion.
    No tiene parametros.
    Devuelve el camino de la solucion encontrada.
    Inicializa las variables e itera hasta obtener una solucion.
    Reinicia el sistema si es que encuentra un estado invalido. 
    '''

    # inicia variables
    F = Lado_A              # variable lado origen
    D = Lado_B              # variable lado destino
    # mientras el lado destino no contenga a los 4 personjes, itera, pues no ha encontrado solucion
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)        # primer viaje
        # valida estados de ambos lados
        if valida_estado (F) and valida_estado (D):
            # estado valido, continua
            if F == Lado_A:                 # si es lado origen, el movimiento fue de origen a destino
                Path.append('A->B :')       # añade movimiento a la lista
            else:                           # sino, es lado destino, movimiento destino a origen
                Path.append('B->A :')       # añade movimiento a la lista
            # añade personajes del origen y del destino
            Path.append(p1)
            Path.append(p2)
            
            # swap de lados; origen swap destino
            Temp = F
            F = D
            D = Temp
        else:
            # sstado inválido, reinicia sistema
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    # devuelve el camino de la solucion obtenida
    return (Path)


def main():

    P = HCR()# se llama a la funcion HCR la cual asigna el path a recorrer
    while len(P) > 22:#se hace un ciclo repitiendo los path posibles hasta encontrar el minimo optimo
        reiniciar_sistema()# se reinicia el juego poniendo a los animales al inicio
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))#se imprime la solcion y su tamaño de pasos
        P = HCR()#se repite el proceso para encontrar un nuevo path
    print (P)#se imprime el path con el mejor numero de pasos
    print (len(P))#se imprime el tamaño del path
            
main()#se llama a la funcion main que inicia el programa

