import pygame
import sys
import random 
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

score = 0
speed = 4
coins = 0

width = 400
height = 600

coinr = {
    "x": random.randint(0, width - 40),
    "y":-50,
    "value":random.randint(1,10)}

#Font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

pygame.mixer.init()

background = pygame.image.load("AnimatedStreet.png")
player = pygame.transform.scale(pygame.image.load("Player.png"), (60,100))
enemy = pygame.transform.scale(pygame.image.load("Enemy.png"),(60,100))
coin = pygame.transform.scale(pygame.image.load("coiin.png"), (30,30))

crash = pygame.mixer.Sound("crash.wav")

playerrect = player.get_rect()
playerrect.center = (160,520)

enemyrect = enemy.get_rect()
enemyrect.center = (random.randint(40, width - 40),0)

coinrect = coin.get_rect()
coinrect.center = (random.randint(40, width - 40), -100)



def move_player():
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] and playerrect.left > 0:
        playerrect.move_ip(-5,0)

    if pressed_keys[K_RIGHT] and playerrect.right < width:
        playerrect.move_ip(5,0)

def move_enemy():
    global score
    enemyrect.move_ip(0, speed)

    if enemyrect.top > height:
        score += 1
        enemyrect.center = (random.randint(40, width - 40), 0)

def move_coin():
    global coins
    global coinr
    global text
    global speed
    coinrect.move_ip(0, speed-2)

    if coinrect.top > height:
        coinr = {
            "x": random.randint(0, width - 40),
            "y":-50,
            "value":random.randint(1,10)}
        coinrect.center = (coinr["x"], coinr["y"])


    if playerrect.colliderect(coinrect):
        coins += coinr["value"]
        if coins % 5 == 0:
            speed += 1

        coinr = {
            "x": random.randint(0, width - 40),
            "y":-50,
            "value":random.randint(1,10)}
        coinrect.center = (coinr["x"], coinr["y"])


backgroundsound = pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        
    screen.blit(background, (0,0))

    scoretext = font_small.render("Score: " + str(score), True, black)
    screen.blit(scoretext, (10,10))

    coin_text = font_small.render("Coins: " + str(coins), True, black)
    screen.blit(coin_text, (280,10))

    move_player()
    move_enemy()
    text = font_small.render(str(coinr["value"]), True, black)
    text_rect = text.get_rect(center=(coinrect.centerx, coinrect.centery - 25))
    screen.blit(text, text_rect)
    move_coin()

    screen.blit(player, playerrect)
    screen.blit(enemy, enemyrect)
    screen.blit(coin, coinrect)


    if playerrect.colliderect(enemyrect):
        pygame.mixer.music.pause()
        crash.play()

        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()
        
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)     