import pygame 
import math

pygame .init()
screen = pygame.display.set_mode ((500, 300))

clock = pygame.time.clock()
t = 0

running = True
while running:
    screen.fill((255, 255, 255))
    # Oscillation using sine
    x = 250 + 100 * math. sin(t)
    pygame.draw.circle(screen, (0, 0, 255), (int(x), 150), 30)
    t+= 0.05
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame. QUIT:
            running = False