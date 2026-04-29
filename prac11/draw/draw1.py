import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLACK
radius = 5
drawing = False
mode = "paint"
fill = False

start_pos = None
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "paint"
            elif event.key == pygame.K_q:
                mode = "rect"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right triangle"
            elif event.key == pygame.K_l:
                mode = "equilateral triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"

            elif event.key == pygame.K_f:
                fill = not fill

            elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                radius += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                radius -= 1

            elif event.key == pygame.K_x:
                screen.fill(WHITE)

            radius = max(1, radius)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            canvas_copy = screen.copy()

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                x1, y1 = start_pos
                x2, y2 = event.pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))

                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                x1, y1 = start_pos
                x2, y2 = event.pos

                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)
            
            elif mode == "square":
                x1, y1 = start_pos
                x2, y2 = event.pos

                side = min(x2-x1, y2-y1)
                if (x2-x1) < 0:
                    x = x1-side
                else:
                    x = x1

                if (y2-y1) < 0:
                    y = y1 - side
                else:
                    y = y1

                square = pygame.Rect(x, y, side, side)
                width = 0 if fill else 2
                pygame.draw.rect(screen, (color), square, width)

            elif mode == "right triangle":
                x1, y1 = start_pos
                x2, y2 = event.pos

                points = [
                    (x1, y1),
                    (x1, y2),
                    (x2, y2)]
                
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)
            
            elif mode == "equilateral triangle":
                x1, y1 = start_pos
                x2, y2 = event.pos

                side = min(abs(x2-x1), abs(y2-y1))
                h = side * (math.sqrt(3)/2)

                if y2 >= y1:
                    p1 = (x1, y1)
                    p2 = (x1 + side, y1)
                    p3 = (x1 + side // 2, y1 - h)
                else:
                    p1 = (x1, y1)
                    p2 = (x1 + side, y1)
                    p3 = (x1 + side // 2, y1 + h)
            
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, [p1, p2, p3], width)

            elif mode == "rhombus":
                x1, y1 = start_pos
                x2, y2 = event.pos

                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                points = [(cx, y1),
                          (x2, cy),
                          (cx, y2),
                          (x1, cy)]
                
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos

            if mode == "paint":
                pygame.draw.line(screen, color, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "erase":
                pygame.draw.line(screen, WHITE, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "rect":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))

                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)
            
            elif mode == "square":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                
                side = min(x2-x1, y2-y1)
                if (x2-x1) < 0:
                    x = x1-side
                else:
                    x = x1

                if (y2-y1) < 0:
                    y = y1 - side
                else:
                    y = y1

                square = pygame.Rect(x, y, side, side)
                width = 0 if fill else 2
                pygame.draw.rect(screen, (color), square, width)
            
            elif mode == "right triangle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                points = [
                    (x1, y1),
                    (x1, y2),
                    (x2, y2)]
                
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)

            elif mode == "equilateral triangle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                side = min(abs(x2-x1), abs(y2-y1))
                h = side * math.sqrt(3)/2

                if y2 >= y1:
                    p1 = (x1, y1)
                    p2 = (x1 + side, y1)
                    p3 = (x1 + side // 2, y1 - h)
                else:
                    p1 = (x1, y1)
                    p2 = (x1 + side, x1)
                    p3 = (x1 + side // 2, y1 + h)
            
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, [p1, p2, p3], width)

            elif mode == "rhombus":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos

                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                points = [(cx, y1),
                          (x2, cy),
                          (cx, y2),
                          (x1, cy)]
                
                width = 0 if fill else 2
                pygame.draw.polygon(screen, color, points, width)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()