import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Blocking")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up sprite
sprite_width, sprite_height = 50, 50
sprite_color = (255, 0, 0)  # Red
sprite_x, sprite_y = width // 2, height // 2
sprite_speed = 5

sprite_rect = pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move sprite
    if keys[pygame.K_LEFT]:
        sprite_rect.x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += sprite_speed
    if keys[pygame.K_UP]:
        sprite_rect.y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite_rect.y += sprite_speed

    # Check if the sprite is on a black background
    background_color = screen.get_at((sprite_rect.x, sprite_rect.y))
    if background_color == black:
        # Block the sprite from moving further
        sprite_rect.x += sprite_speed  # Move back to the previous position
        sprite_rect.y += sprite_speed  # Move back to the previous position

    # Fill the screen with white
    screen.fill(white)

    # Draw the sprite
    pygame.draw.rect(screen, sprite_color, sprite_rect)

    pygame.display.flip()
