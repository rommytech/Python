import pygame
import sys
import random
from bomber import Bomberman
from vehiculo import Aereo

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BUBBLE_COLOR = (0, 0, 0)
BUBBLE_HEIGHT = 36
# Crear la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bomberman")

# Lista de bombermans
bombermans = []

# Función para crear e instanciar bombermans
def create_bomberman(name, x, y):
    bomberman = Aereo("Boing", "Blanco", "Air", "3434", 45, "45", "454", "15:00", "16:00", name, x, y)
    bombermans.append(bomberman)


create_bomberman("Bichito", 100, 100)

# Bucle principal
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for bomberman in bombermans[:]:
                if bomberman.is_clicked(pos):
                    bombermans.remove(bomberman)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:  # Presionar 'n' para ingresar el nombre en la terminal
                # Pausar el juego y pedir el nombre en la terminal
                pygame.display.set_caption("Ingrese el nombre del Bomberman en la terminal...")
                name = input("Ingrese el nombre: ")
                #Ingrese apellido
                apellido = input("Ingrese apellido: ")

                x = random.randint(50, 750)
                y = random.randint(50, 550)
                create_bomberman(name + " " + apellido, x, y)
    
    for bomberman in bombermans:
        bomberman.falling()
        bomberman.move_to_right()
        bomberman.draw(screen)

    pygame.display.set_caption(f"{len(bombermans)} Bombermans")

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()