import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Move the Circle")
x, y = 250, 200
radius = 20
speed = 5
running = True

while running:
	screen.fill((0, 0, 0))  # Black background
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x -= speed
	if keys[pygame.K_RIGHT]:
		x += speed
	if keys[pygame.K_UP]:
		y -= speed
	if keys[pygame.K_DOWN]:
		y += speed

	pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)
	pygame.display.flip()
	pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()