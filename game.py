import pygame
import random
import math
import sys 
import os

#inicializamos pygame 
pygame.init ()

#establecemos el tamaño de la pantalla 
width = 800 #ancho 
height = 600  #alto
screen = pygame.display.set_mode((width,height))

#ruta de los recursos
def resource_path(ralative_path):
    try:
        base_path = sys ._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, ralative_path)
    
#cargar imagen de fondo 
asset_background = resource_path("assets/images/background.png")
background = pygame.image.load(asset_background)

#icono de ventana 
asset_icon = resource_path("assets/images/ufo.png")
icon = pygame.image.load(asset_icon)

#cargar sonido de fondo  
asset_sound = resource_path("assets/audio/background_music.mp3")
background_sound = pygame.mixer.music.load(asset_sound)

#imagen del jugador 
asset_playering = resource_path("assets/images/space-invaders.png")
playering = pygame.image.load(asset_playering)

#imagen de bala 
asset_bulleting = resource_path("assets/images/bullet.png")
bulleting = pygame.image.load(asset_bulleting)

#fuente para texto de game over 
asset_over_font = resource_path("assets/fonts/RAVIE.TTF")
over_font = pygame.font.Font(asset_over_font)

#puntaje
asset_font = resource_path("assets/fonts/comicbd.ttf")
font = pygame.font.Font(asset_font)

#ponemos titulo a nuestro juego 
pygame.display.set_caption("Space Invader")

#estabkecemos el icono de la ventana
pygame.display.set_icon(icon)

#reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#crear reloj para controlar la velocidad del juego 
clock = pygame.time.Clock()

#posicion inicial del jugador 
playerX = 370
PlayerY = 470
playerx_change = 0
playery_change = 0

#lista para almacenar posiciones de los enemigos 
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#Seinicia las variables para que los enemigos tengan posiciones 
for i in range(no_of_enemies):
    #se carga la imagen del enemigo 1
    enemy1=resource_path('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))
    #se carga la imagen del enemigo 2
    enemy2=resource_path('assets/images/enemy2.png')
    enemyimg.append(pygame.image.load(enemy2))
    
#se asigna una posicion aleatoria en x y Y para el enemigo 
enemyX.append(random.randint(0,736))
enemyY.append(random.randint(0,150))

#Se establece la velocidad de movimiento del enemigo x e y 
enemyX_change.append(5)
enemyY_change.append(20)

#se incializan las variables para guardar la posicion de la bala
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#inicializamos la puntuacion en 0
score = 0

# funcion que nos sirve para mostrar la puntuación 
def show_score():
    score_value = font.render("SCORE"+ str(score), True,(255, 255, 255))
    screen.blit(score_value,(10, 10))
    
# funcion que dibuja al jugador en la pantalla
def player(x,y):
    screen.blit(playering,(x, y))
    
#funcion para dibujar al enemigo en la pantalla 
def enemy  (x, y , i):
    screen.blit(enemyimg[i],(x,y))

#funcion para disparar la bala  
def fire_bullet(x,y):
    global bullet_state
    
    bullet_state = "fire"
    screen.blit(bulleting,(x+16 , y+10))

#colision entre bala y enemigo 
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +
                         (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False
    
#funcion de game over en la pantalla
def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    text_rect =over_text.get_rect(
        center=(int(width/2), int(height/2)))  
    screen.blit(over_text, text_rect)
    
#funcion principal del juego 
def gameloop():
    
    #declaramos las variables globales 
    global score
    global playerX
    global player_change
    global bulletX
    global bulletY
    global Collision
    global bullet_state
    
    in_game = True
    while in_game:
        #maneja y limpia la pantall 
        screen.fill(0,0,0)
        screen.blit(background,(0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                pygame.quit ()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                
                #maneja el movimiento del jugador y el disparo 
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                    
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                    
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = bulletX
                        fire_bullet(bulletX, bulletY)
                        
                if event.type == pygame.KEYUP:
                    playerx_change = 0
                    
        #se actualiza la posicion del jugador 
        playerX += playerx_change
                
        if playerX<=0:
            playerX=0
        elif playerX >= 736:
            playerX = 736
            
        #loop para cada enemigo 
        for i in range(no_of_enemies):
            if enemyY[i]>440:
                for j in range (no_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                
            enemyX[i]+= enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i]=5
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i]>=736:
                enemyX_change[i]=-5
                enemyY_change[i] += enemyY_change[i]
                                        
                        
            