import pygame 
pygame. init()
screen = pygame.display.set_mode((400, 300))

image = pygame.image.load('image.png')  # Load an image
scaled_image = pygame.transform.scale(image, (200, 200))

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()