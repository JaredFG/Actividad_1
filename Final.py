import HCRfinal # Codigo de solucion 

import pygame # Libreria para manejo de animacion

# Crea un canvas para poder mostrar la animacion
def redrawGameWindow(Dir, p1, p2):
    global x, y, Side_A, Side_B
            
    win.blit(bg,(0,0))
    
    # Define pocisiones para todos los personajes del lado derecho
    ypos = 300
    for item in Side_A:
        win.blit(item,(5,ypos))
        ypos = ypos - 60

    #Define pocisiones para todos los personajes del lado zquierdo
    ypos = 300
    for item in Side_B:
        win.blit(item,(450,ypos))
        ypos = ypos - 60

    # Direcciona bote y pocisiona personajes
    if p1 != 'Unknown':
        if right:
            win.blit(BoatRight,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))           
        elif left:
            win.blit(BoatLeft,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(char,(x, y))
    pygame.display.update() # Actualiza

def get_characters(d, p1, p2):
    
    #Define el segundo personaje; quien va con el granjero
    if p2 == 'Zorro':
        character = fox
    elif p2 == 'Maiz':
        character = corn
    elif p2 == 'Ganso':
        character = duck
    else:
        character = farmer
    return (d, farmer, character)

def Embark_characters(B, p1, p2):
    
    #Cambia pocision de personajes de costa a barco
    if p1 in B:
        B.remove(p1)     
    if p2 in B:
        B.remove(p2)
 
def Disembark_characters(A, p1, p2):
    
    #Cambia pocision de personajes de barco a costa
    if p1 not in A:
        A.append(p1)
    if p2 not in A:
        A.append(p2)
    
def HCR_animacion(P):
    global x, y, left, right, vel
    global Side_A, Side_B
    
    # Establece valores iniciales
    clock = pygame.time.Clock()
    run = True
    move = 0
    
    # Corre simulacion
    while run:
        clock.tick(27)
        
        # Cierra el programa cuando recibe el evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Corre embarque viaje hacia la izquierda y desembarca
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2]) # Establece direccion y personajes
                Embark_characters(Side_B, p1, p2) # Embarca
                for step in range(65): # Mueve las imagenes
                    x -= vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2) # Desembarca
        
        # Corre embarque viaje hacia la derecha y desembarca
        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2]) # Establece direccion y personajes
                Embark_characters(Side_A, p1, p2) # Embarca
                for step in range(65): # Mueve imagenes
                    x += vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_B, p1, p2) # Desembarca
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown') # Estado idle
        

    pygame.quit()

# Recupera solucion del sistema
def Busca_solucion():
    P = HCRfinal.HCR() 
    while len(P) > 22:
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCRfinal.HCR()
    print (P)
    print (len(P))
    print ('\n =====> Solución encontrada:')
    return (P)

 
            
P = Busca_solucion() # Encuantra solucion
print ('Aquí su animación')

pygame.init()

win = pygame.display.set_mode((500,500)) # Establece canvas
pygame.display.set_caption("How to Cross the River")

# Establece imagenes
BoatRight   = pygame.image.load('BoteRight.jpg')
BoatLeft    = pygame.image.load('BoteLeft.jpg')
bg          = pygame.image.load('seaL.jpg')
char        = pygame.image.load('BoteRight.jpg')
fox         = pygame.image.load('fox.png')
corn        = pygame.image.load('corn.jpg')
duck        = pygame.image.load('duck.jpg')
farmer      = pygame.image.load('farmer.jpg')

# Resize imagenes
BoatRight = pygame.transform.scale(BoatRight, (50, 70))
BoatLeft = pygame.transform.scale(BoatLeft, (50, 70))
char = pygame.transform.scale(char, (50, 70))
fox = pygame.transform.scale(fox, (50, 70))
corn = pygame.transform.scale(corn, (50, 70))
duck = pygame.transform.scale(duck, (50, 70))
farmer = pygame.transform.scale(farmer, (50, 70))

# Establece imagenes
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

Side_A = [farmer, fox, duck, corn]
Side_B = []

HCR_animacion(P)

