import pygame
import random

# Připravíme PyGame
pygame.init()
pygame.display.set_caption("   Turtle Game")
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (200, 200, 200)
turtle = pygame.image.load("turtle.png")
turtle = pygame.transform.scale(turtle, (40, 40))
pineapple = pygame.image.load("pineapple.png")
pineapple = pygame.transform.scale(pineapple, (40, 40))

WIDTH = 8
HEIGHT = 7

turtle_x = 2
turtle_y = 1

def game_to_screen(x, y):
    return (x * 45 + 10, y * 45 + 10)

def move_turtle(nx, ny):
    global turtle_x, turtle_y

    duration = 1000
    t = 0
    # Obrazovkove souradnice
    sx, sy = game_to_screen(turtle_x, turtle_y)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        new = t / duration  # 0...1
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        draw_scene()
        screen.blit(rotated_turtle, (x, y))
        pygame.display.update()
        t = t + clock.tick()

    turtle_x = nx
    turtle_y = ny

    check_pineapples()

pa_x = 0
pa_y = 0
pineapples = [(0, 0), (5, 1), (0, 2)]
score = 0

def draw_scene():
    screen.fill(background)
    for x in range(WIDTH):
        for y in range(HEIGHT):                    
            color = (255, 255, 255)
            rect = (game_to_screen(x, y), (40, 40))
            pygame.draw.rect(screen, color, rect)
    for pa in pineapples:
        pa_x, pa_y = pa
        screen.blit(pineapple, game_to_screen(pa_x, pa_y))

    font = pygame.font.Font(None, 42) # presunout na zacatek
    text = font.render(f"Score: {score}", True, (0, 0, 0), (0, 255, 0))
    screen.blit(text, (20, 300))

countdown = 5

def check_pineapples():
    global pineapples
    global score
    global countdown
    new = []
    for pa in pineapples:
        if pa == (turtle_x, turtle_y):
            score = score + 10
        else:
            new.append(pa)
    pineapples = new
    countdown = countdown - 1
    if countdown == 0:
        rx = random.randrange(0, WIDTH)
        ry = random.randrange(0, HEIGHT)
        pineapples.append((rx, ry))
        countdown = 5

rotated_turtle = pygame.transform.rotate(turtle, 0)
while True:

    
    # Vykreslíme
    draw_scene()
    screen.blit(rotated_turtle, game_to_screen(turtle_x, turtle_y))
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            rotated_turtle = pygame.transform.rotate(turtle, 0)
            if turtle_x < WIDTH - 1:
                move_turtle(turtle_x + 1, turtle_y)
        elif event.key == pygame.K_UP:
            rotated_turtle = pygame.transform.rotate(turtle, 90)
            if turtle_y > 0:
                move_turtle(turtle_x, turtle_y - 1)
        elif event.key == pygame.K_LEFT:
            rotated_turtle = pygame.transform.rotate(turtle, 180)
            if turtle_x > 0:
                move_turtle(turtle_x - 1, turtle_y)
        elif event.key == pygame.K_DOWN:
            rotated_turtle = pygame.transform.rotate(turtle, 270)
            if turtle_y < HEIGHT - 1:
                move_turtle(turtle_x, turtle_y + 1)

    if (turtle_x, turtle_y) == (pa_x, pa_y):
        pa_x = random.randrange(0, WIDTH)
        pa_y = random.randrange(0, HEIGHT)