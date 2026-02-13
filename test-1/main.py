import pygame
import sys
import math

def rotate_and_scale_continuous(image_path):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rotating and Pulsing Logo")

    # Load image
    image = pygame.image.load(image_path).convert_alpha()
    width, height = image.get_size()

    clock = pygame.time.Clock()
    angle = 0
    time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Increase rotation angle
        angle += 2
        if angle >= 360:
            angle = 0

        # Use sine wave for pulsing scale effect (between 1.0 and 1.5)
        scale_factor = 1.25 + 0.25 * math.sin(time)
        time += 0.05

        # Scale and rotate
        scaled = pygame.transform.smoothscale(image, (int(width * scale_factor), int(height * scale_factor)))
        rotated = pygame.transform.rotate(scaled, angle)
        rect = rotated.get_rect(center=(400, 300))

        # Draw
        screen.fill((255, 255, 255))
        screen.blit(rotated, rect)
        pygame.display.flip()

        # Limit FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()

# === Usage ===
png_file = "logo.png"  # Your PNG logo path
rotate_and_scale_continuous(png_file)