import pygame 
pygame. init()
screen = pygame.display.set_mode((400, 300))
# Solid red (opaque)
red = (255, 0, 0, 255)

# Red at 50% opacity
red_50 = (255, 0, 0, 128)

# Blue with 30% opacity
blue_30 = (0, 0, 255, int(0.3 * 255))

# Fully transparent black
transparent_black = (0, 0, 0, 0)

screen.fill((0, 128, 255)) # Fill screen with blue
pygame.draw.circle(screen, (255, 0, 0), (150, 150), 50) # Red circle

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()