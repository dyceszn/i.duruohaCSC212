import pygame 
pygame. init()
screen = pygame.display.set_mode((400, 300))
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
surface.fill((255, 0, 0, 128)) # Semi-transparent red
# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()