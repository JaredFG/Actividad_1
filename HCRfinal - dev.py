
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
    global Lado_A, Lado_B, Path
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
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
    P = HCR()# se llama a la funcion HCR la cual asigna el path a recorrer
    while len(P) > 22:#se hace un ciclo repitiendo los path posibles hasta encontrar el minimo optimo
        reiniciar_sistema()# se reinicia el juego poniendo a los animales al inicio
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))#se imprime la solcion y su tamaño de pasos
        P = HCR()#se repite el proceso para encontrar un nuevo path
    print (P)#se imprime el path con el mejor numero de pasos
    print (len(P))#se imprime el tamaño del path
            
main()#se llama a la funcion main que inicia el programa

  
