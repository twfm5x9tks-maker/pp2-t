import pygame
import datetime
import os
import math

pygame.init()
screen = pygame.display.set_mode((1200, 700))
WHITE = (255, 255, 255)

base = r'C:\Users\serik\pp2-t\prac09\mickey_clock\images'
image_surface = pygame.image.load(os.path.join(base, 'clock.png')).convert_alpha()
mickey        = pygame.image.load(os.path.join(base, 'mUmrP.png')).convert_alpha()
hand_l        = pygame.image.load(os.path.join(base, 'hand_left.png')).convert_alpha()
hand_r        = pygame.image.load(os.path.join(base, 'hand_right.png')).convert_alpha()

resized_image = pygame.transform.scale(image_surface, (800, 600))
res_mickey    = pygame.transform.scale(mickey, (350, 350))
hand_l_base   = pygame.transform.scale(hand_l, (80, 80))  
hand_r_base   = pygame.transform.scale(hand_r, (100, 100))  

CLOCK_CENTER  = (600, 320)  
MICKEY_CENTER = (600, 320)   

def draw_hand(surface, image, angle_deg, pivot, length_ratio=0.5):
    
    rotated = pygame.transform.rotate(image, -angle_deg)
    rad = math.radians(angle_deg)
    h   = image.get_height()
    offset = h * length_ratio          
    cx = pivot[0] + offset * math.sin(rad)
    cy = pivot[1] - offset * math.cos(rad)
    rect = rotated.get_rect(center=(int(cx), int(cy)))
    surface.blit(rotated, rect)

clock = pygame.time.Clock()
done  = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
   
    seconds = (s/60) * 360
    minutes_angle = (m / 60) * 360 + (s / 60) * 6     

    screen.fill(WHITE)

    image_rect = resized_image.get_rect(center=(600, 340))
    screen.blit(resized_image, image_rect)

    mic_rect = res_mickey.get_rect(center=MICKEY_CENTER)
    screen.blit(res_mickey, mic_rect)

    draw_hand(screen, hand_r_base,minutes_angle ,   CLOCK_CENTER, length_ratio=0.45)  
    draw_hand(screen, hand_l_base, seconds, CLOCK_CENTER, length_ratio=0.50)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()