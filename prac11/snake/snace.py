import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 600
TILE = 20

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // TILE
                        col = x // TILE
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, TILE, TILE))
                        x += TILE
                y += TILE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
GRAY = (100,100,100)
GOLD = (255,215,0)

font = pygame.font.SysFont("Arial", 34)


def generate_walls(level):
    walls = []
    f = open("levels/level{}.txt".format(level), "r")
    row = -1
    col = -1
    for line in f:
        row = row + 1
        col = -1
        for c in line:
            col = col + 1
            if c == '#':
                walls.append((col * TILE, row * TILE))
    f.close()

    return walls


def generate_food(snake, walls):
    while True:
        x = random.randrange(0, WIDTH, TILE)
        y = random.randrange(0, HEIGHT, TILE)

        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

def disappering_food(snake, walls, food):
    while True:
        x = random.randrange(0, WIDTH, TILE)
        y = random.randrange(0, WIDTH, TILE)

        disfood = {"pos":(x, y),
                   "value":5,
                   "color":GOLD,
                   "spawn time":pygame.time.get_ticks()}

        if (x, y) not in snake and (x, y) not in walls and (x, y) not in food:
            return disfood

def reset_game():
    snake = [(100,100), (80,100), (60,100)]
    dx, dy = TILE, 0
    level = 1
    walls = generate_walls(level)
    food = generate_food(snake, walls)
    disfood = disappering_food(snake, walls, food)
    score = 0
    speed = 5
    return snake, dx, dy, food, score, level, speed, walls, disfood

snake, dx, dy, food, score, level, speed, walls, disfood = reset_game()
game_over = False

food_lifetime = 5000
last_food_change = pygame.time.get_ticks()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -TILE
            if event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, TILE
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -TILE, 0
            if event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = TILE, 0
    current_time = pygame.time.get_ticks()

    if current_time - last_food_change >= food_lifetime:
        disfood = disappering_food(snake, walls, food)
        last_food_change = current_time

    if not game_over:
        head = (snake[0][0] + dx, snake[0][1] + dy)


        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            game_over = True

        if head in snake:
            game_over = True

        if head in walls:
            game_over = True

        snake.insert(0, head)
        value = random.randint(1,3)
        if head == food:
            score += value

            if score != 0 and score % 2 == 0:
                level += 1
                speed += 1
                walls = generate_walls(level)

            food = generate_food(snake, walls)
        if head == disfood["pos"]:
            score += disfood["value"]

            if score != 0 and score % 2 == 0:
                level += 1
                speed += 1
                walls = generate_walls(level)
            
            disfood = disappering_food(snake, walls, food)
        else:
            snake.pop()
        create_background(screen, 600,600)


    for s in snake:
        pygame.draw.rect(screen, GREEN, (*s, TILE, TILE))

    pygame.draw.rect(screen, RED, (*food, TILE, TILE))
    pygame.draw.rect(screen, disfood["color"], (*disfood["pos"], TILE, TILE))

    for w in walls:
        pygame.draw.rect(screen, GRAY, (*w, TILE, TILE))

    text = font.render(f"Score: {score} Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    if game_over:
        screen.fill(RED)
        over = font.render("GAME OVER! Press R FOR RESTART", True, BLACK)
        screen.blit(over, (70, 260))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            snake, dx, dy, food, score, level, speed, walls = reset_game()
            game_over = False

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()