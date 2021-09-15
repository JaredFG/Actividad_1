
import random

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

def seleccion(L):
    op = random.randint(0,len(L)-1)
    return (L[op])

def Viaje(F, D):
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1)

def valida_estado(L):
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
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
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']     # variable lado origen
    Lado_B = []                                         # variable lado destino
    Path = []                                           # variable movimientos realizados
    

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
    P = HCR()
    while len(P) > 22:
        reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print (P)
    print (len(P))
            
main()

  
