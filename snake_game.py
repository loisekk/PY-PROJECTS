import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SNAKE_SPEED = 7

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, GREEN)
    screen.blit(value, (10, 10))

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, (*block, BLOCK_SIZE, BLOCK_SIZE))

def message(msg, color):
    msg_surface = font_style.render(msg, True, color)
    screen.blit(msg_surface, (WIDTH // 6, HEIGHT // 3))

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = BLOCK_SIZE, 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press C to Play Again or Q to Quit", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            snake_list.pop(0)

        if snake_head in snake_list[:-1]:
            game_close = True

        draw_snake(snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT, BLOCK_SIZE)
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
