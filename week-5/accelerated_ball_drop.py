import pygame
pygame.init()
# Screen
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
# Ball properties
x, y = 200, 0
velocity = 0
acceleration = 0.5 # Gravity
clock = pygame.time.Clock()
running = True
while running:
	clock.tick(60)
	# 60 FPS
	screen.fill((255, 255, 255)) # Clear screen
	# Update velocity and position
	velocity += acceleration
	y += velocity
	# Collision with ground
	if y > height - 30:
		y = height - 30
		velocity *= -0.7 # Bounce with energy loss
	# Draw ball
	pygame.draw.circle(screen, (0, 0, 255), (x, int(y)), 30)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False