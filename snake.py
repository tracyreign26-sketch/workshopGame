import pygame
import random

# Start Pygame
pygame.init()

# Create the game window
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Create the snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Create the food
food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
)

score = 0
running = True
game_over = False

# Main game loop
while running:

    # Handle keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)

                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)

                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)

                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

            if game_over and event.key == pygame.K_r:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (CELL_SIZE, 0)
                food = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )
                score = 0
                game_over = False

    # Move the snake
    if not game_over:
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        snake.insert(0, new_head)

        # Check if the snake eats food
        if new_head == food:
            score += 1

            while True:
                food = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )
                if food not in snake:
                    break
        else:
            snake.pop()

        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT):
            game_over = True

        # Check collision with the snake's body
        if new_head in snake[1:]:
            game_over = True

    # Draw everything
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display game over message
    if game_over:
        message = font.render("Game Over!! Press R to Restart", True, WHITE)
        screen.blit(
            message,
            (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2)
        )

    pygame.display.update()
    clock.tick(10)

# Close the game
pygame.quit()