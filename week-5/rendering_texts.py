import pygame 
pygame. init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont('Arial'
, 36)
text = font. render ("Welcome!", True, (255, 255, 0)) # Yellow text
screen.blit(text, (100, 50))
pygame.display.update()

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()