import pygame 
pygame. init()
screen = pygame.display.set_mode((400, 300))

frames = [img1, img2, img3]
index = (index + 1) % len(frames)
screen. blit (frames[index], (x, y))

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()