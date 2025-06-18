import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
x = 50
running = True
while running:
	pygame.time.delay(30)
	screen.fill((255, 255, 255))  # Clear screen
	pygame.draw.circle(screen, (0, 0, 255), (x, 200), 30)
	x += 5
	if x > 400:
		x = 0
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False