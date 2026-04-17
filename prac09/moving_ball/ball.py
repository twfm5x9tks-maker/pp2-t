import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ball Game")
pygame.key.set_repeat(100, 50)
done = False
clock = pygame.time.Clock()

x = 300
y = 200
radius = 30
speed = 20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed

        if x - radius < 0:
            x = radius
        if x + radius > 600:
            x = 600 - radius
        if y - radius < 0:
            y = radius
        if y + radius > 400:
            y = 400 - radius
        
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
        pygame.display.update()