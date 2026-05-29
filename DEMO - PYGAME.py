import pygame
import sys
import math

pygame.init()

# Pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Cubo 3D")

clock = pygame.time.Clock()

# Vértices del cubo
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

# Aristas
edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# Posición del cubo
cube_x = 0
cube_y = 0
cube_z = 5

rot_x = 0
rot_y = 0

move_speed = 0.1
rot_speed = 0.05


def rotate_x(point, angle):
    x, y, z = point
    y2 = y * math.cos(angle) - z * math.sin(angle)
    z2 = y * math.sin(angle) + z * math.cos(angle)
    return [x, y2, z2]


def rotate_y(point, angle):
    x, y, z = point
    x2 = x * math.cos(angle) + z * math.sin(angle)
    z2 = -x * math.sin(angle) + z * math.cos(angle)
    return [x2, y, z2]


def project(point):
    x, y, z = point
    factor = 200 / (z + cube_z)
    x = x * factor + WIDTH / 2 + cube_x
    y = -y * factor + HEIGHT / 2 + cube_y
    return (int(x), int(y))


while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movimiento WASD
    if keys[pygame.K_a]:
        cube_x -= 5
    if keys[pygame.K_d]:
        cube_x += 5
    if keys[pygame.K_w]:
        cube_y -= 5
    if keys[pygame.K_s]:
        cube_y += 5

    # Profundidad
    if keys[pygame.K_q]:
        cube_z += move_speed
    if keys[pygame.K_e]:
        cube_z -= move_speed

    # Rotación con flechas
    if keys[pygame.K_LEFT]:
        rot_y -= rot_speed
    if keys[pygame.K_RIGHT]:
        rot_y += rot_speed
    if keys[pygame.K_UP]:
        rot_x -= rot_speed
    if keys[pygame.K_DOWN]:
        rot_x += rot_speed

    screen.fill((0, 0, 0))

    transformed = []

    for vertex in vertices:
        v = rotate_x(vertex, rot_x)
        v = rotate_y(v, rot_y)
        transformed.append(project(v))

    # Dibujar cubo
    for edge in edges:
        pygame.draw.line(
            screen,
            (0, 255, 255),
            transformed[edge[0]],
            transformed[edge[1]],
            2
        )

    pygame.display.flip()
