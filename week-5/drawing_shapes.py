import pygame 
pygame.init()
screen = pygame.display.set_mode ( (400, 300))
screen.fill((255, 255, 255))
# Line
pygame.draw. line(screen, (255, 0, 0), (50, 50), (150, 50), 5)
# Circle
pygame. draw. circle(screen, (0, 255, 0), (200, 150), 40)
# Polygon (triangle)
pygame .draw.polygon(screen, (0, 0, 255), [(250, 100), (300, 200), (200, 200)])
pygame.display.flip()

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()