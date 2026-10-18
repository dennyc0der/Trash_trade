import pygame
import asyncio
import math
import random

from setting import *

pygame.init()

screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()

rocket_1_image = pygame.image.load("assets/rocket_1.png").convert_alpha()
player_1_image = pygame.image.load("assets/player1.png").convert_alpha()
trash_pile = pygame.image.load("assets/trash_pile.png").convert_alpha()

player_sprite = pygame.transform.smoothscale(player_1_image, (100, 100))
trash_pile_sprite = pygame.transform.smoothscale(trash_pile, (300, 300))

def start_screen_draw():
    pygame.draw.rect(screen, (0, 0, 0), [650, 600, 200, 100])
    pygame.draw.rect(screen, (0, 0, 0), [650, 800, 200, 100])

    pygame.draw.rect(screen, (200, 200, 200), [450, 200, 600, 300])

    pygame.draw.rect(screen, (100, 100, 100), [640, option_y, 220, 10])
    pygame.draw.rect(screen, (100, 100, 100), [640, option_y+110, 220, 10])
    pygame.draw.rect(screen, (100, 100, 100), [640, option_y, 10, 120])    
    pygame.draw.rect(screen, (100, 100, 100), [640+210, option_y, 10, 120])

def main_screen_draw():
    pygame.draw.rect(screen, (100, 100, 100), [0, 0, 1500, 50])
    pygame.draw.rect(screen, (100, 100, 100), [0, 950, 1500, 50])
    pygame.draw.rect(screen, (100, 100, 100), [0, 0, 50, 1000])
    pygame.draw.rect(screen, (100, 100, 100), [1450, 0, 50, 1000])

    #pygame.draw.rect(screen, (100, 100, 100), [1340, 400, 100, 200])
    screen.blit(rocket_1_image, (1340, 400))
    screen.blit(player_sprite, (player_x, player_y))
    screen.blit(trash_pile_sprite, (1050, 425))

def tickPlayers(px, py, pxv, pyv, pspeed, up, down, left, right):
    #player controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w]and up == True:
        pyv -= pspeed

    elif key[pygame.K_s] and down == True:
        pyv += pspeed

    if key[pygame.K_a] and left == True:
        pxv -= pspeed

    elif key[pygame.K_d]and right == True:
        pxv += pspeed

    #update velocities
    pyv =  0.85 * pyv
    pxv = 0.85 * pxv

    #update player positions
    py += pyv
    px += pxv

    return px, py,pxv, pyv

async def main():

    global player_x
    global player_y
    global screen_phase
    global option_y
    global menu_option
    global up
    global down
    global left
    global right
    global player_xv
    global player_yv
    global player_speed
    global spawn_timer
    global spaawn_time
    global trash_type
    global number_trash
    global number_trash_player
    global trash_capacity
    global trash_capacity_player

    while running == True:
        if screen_phase == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        option_y = 790

                    if event.key == pygame.K_UP:
                        menu_option -= 1
                        option_y = 590

                    if event.key == pygame.K_RETURN:
                        if menu_option == 1:
                            screen_phase = 2

                        if menu_option == 2:
                            screen_phase = 3

            screen.fill((255, 255, 255))
            if menu_option == 3:
                menu_option = 1
                option_y = 590

            elif menu_option == 0:
                menu_option = 2
                option_y = 790

            start_screen_draw()
                
        if screen_phase == 2:
            for event in pygame.event.get():    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screen_phase = 1

            screen.fill((200, 200, 200))

            main_screen_draw()

            player_x, player_y, player_xv, player_yv = tickPlayers(player_x, player_y, player_xv, player_yv, player_speed, up, down, left, right)

            player_rect = pygame.Rect(player_x+15, player_y-5, player_w-130, player_h-90)
            wall_top = pygame.Rect(0, 45, 1500, 5)  
            wall_left = pygame.Rect(45, 0, 5, 1000)     
            wall_down = pygame.Rect(0, 955, 1500, 5)
            wall_right = pygame.Rect(1455, 0, 5, 1000)
            
                           

            top_rect_group = [wall_top]
            left_rect_group = [wall_left]
            down_rect_group = [wall_down]
            right_rect_group = [wall_right]
            for rect in top_rect_group:
                if rect.colliderect(player_rect):
                    up = False
                    player_yv = 0
                    break
                up = True

            for rect in left_rect_group:
                if rect.colliderect(player_rect):
                    left = False
                    player_xv = 0
                    break
                left = True

            for rect in down_rect_group:
                if rect.colliderect(player_rect):
                    down = False
                    player_yv = 0
                    break
                down = True

            for rect in right_rect_group:
                if rect.colliderect(player_rect):
                    right = False
                    player_xv = 0
                    break

                right = True

            spawn_timer += dt

            if spawn_timer >= spawn_time:
                if number_trash < trash_capacity:
                    trash_type = random.randint(1, 101)
                    number_trash += 1

                print(number_trash)
                spawn_timer = 0

        if screen_phase == 3:
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screen_phase = 1

            screen.fill((0, 255, 0))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

        await asyncio.sleep(0)

asyncio.run(main())