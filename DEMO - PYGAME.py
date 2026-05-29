import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Demo PyGame - Movimiento y Rotación")


NEGRO = (0, 0, 0)
AZUL = (0, 150, 255)


x = ANCHO // 2
y = ALTO // 2
velocidad = 5
angulo = 0

tam = 80
cuadrado = pygame.Surface((tam, tam), pygame.SRCALPHA)
pygame.draw.rect(cuadrado, AZUL, (0, 0, tam, tam))

clock = pygame.time.Clock()


while True:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    # Movimiento con WASD
    if teclas[pygame.K_a]:
        x -= velocidad
    if teclas[pygame.K_d]:
        x += velocidad
    if teclas[pygame.K_w]:
        y -= velocidad
    if teclas[pygame.K_s]:
        y += velocidad

    # Rotación con flechas
    if teclas[pygame.K_LEFT]:
        angulo += 3
    if teclas[pygame.K_RIGHT]:
        angulo -= 3
    if teclas[pygame.K_UP]:
        angulo += 3
    if teclas[pygame.K_DOWN]:
        angulo -= 3

   
    pantalla.fill(NEGRO)

    cuadrado_rotado = pygame.transform.rotate(cuadrado, angulo)
    rect = cuadrado_rotado.get_rect(center=(x, y))
    pantalla.blit(cuadrado_rotado, rect)

    pygame.display.update()