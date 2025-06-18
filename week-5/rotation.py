import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
angle = 0

while True:
	screen.fill((255, 255, 255))
	rect = pygame.Surface((100, 50))
	rect.fill((0, 128, 0))
	rotated = pygame.transform.rotate(rect, angle)
	screen.blit(rotated, (150, 175))
	pygame.display.update()
	angle += 1
	clock.tick(60)