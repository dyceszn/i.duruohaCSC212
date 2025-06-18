import pygame

pygame. init()
screen = pygame.display.set_mode ( (500, 300))
clock = pygame.time.Clock()

x, y = 50, 150
velocity = 3

running = True
while running:
    screen.fill((255, 255, 255))

    x += velocity
    if x > 500:
        x = -30 # Reset to left if it moves off screen
pygame .draw.circle(screen, (255, 0, 0), (x, y), 30) 
pygame.display.update()
clock.tick(60)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False