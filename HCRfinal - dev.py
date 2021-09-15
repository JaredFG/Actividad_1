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
    global Lado_A, Lado_B, Path
    
    Lado_A = ['Granjero', 'Zorro', 'Ganso', 'Maiz']
    Lado_B = []
    Path = []
    

def HCR():
    F = Lado_A
    D = Lado_B
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        if valida_estado (F) and valida_estado (D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)
            
            Temp = F
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
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

  
