import pygame
import asyncio
import math
import random

from setting import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1500, 1000))
clock = pygame.time.Clock()

pygame.mixer.music.load("assets/manu2.ogg")

custom_font = pygame.font.Font("assets/custum_font.ttf", 50)

rocket_1_image = pygame.image.load("assets/rocket_2.png").convert_alpha()
player_1_image = pygame.image.load("assets/player3.png").convert_alpha()
trash_pile = pygame.image.load("assets/trash_pile.png").convert_alpha()
#alien_crowd = pygame.image.load("assets/alien_crowd.png").convert_alpha()
bg_image = pygame.image.load("assets/bg.png").convert_alpha()
planet_image = pygame.image.load("assets/planet.png").convert_alpha()
astroid_image1 = pygame.image.load("assets/astriod1.png").convert_alpha()
astroid_image2 = pygame.image.load("assets/astroid2.png").convert_alpha()
shop_sell_image = pygame.image.load("assets/shop_sell.png").convert_alpha()
shop_buy_image = pygame.image.load("assets/shop_buy.png").convert_alpha()
icon1_image = pygame.image.load("assets/icon1.png").convert_alpha()
icon2_image = pygame.image.load("assets/icon2.png").convert_alpha()
icon3_image = pygame.image.load("assets/icon3.png").convert_alpha()
icon4_image = pygame.image.load("assets/icon4.png").convert_alpha()
icon5_image = pygame.image.load("assets/icon5.png").convert_alpha()
icon6_image = pygame.image.load("assets/icon6.png").convert_alpha()
icon7_image = pygame.image.load("assets/icon7.png").convert_alpha()
icon8_image = pygame.image.load("assets/icon8.png").convert_alpha()
icon9_image = pygame.image.load("assets/icon9.png").convert_alpha()
icon10_image = pygame.image.load("assets/icon10.png").convert_alpha()
titlescreenimg = pygame.image.load("assets/Untitled_Artwork-1(2).png").convert_alpha()
title_monster = pygame.image.load("assets/Untitled_Artwork-2(1).png").convert_alpha()
play_image = pygame.image.load("assets/Untitled_Artwork-3(1).png").convert_alpha()


player_sprite = pygame.transform.smoothscale(player_1_image, (300, 300))
trash_pile_sprite = pygame.transform.smoothscale(trash_pile, (300, 300))
#alien_crowd_sprite = pygame.transform.smoothscale(alien_crowd, (900, 900))
rocket_1_sprite = pygame.transform.smoothscale(rocket_1_image, (400, 400))
bg_sprite = pygame.transform.smoothscale(bg_image, (1400, 1400))
plamet_sprite = pygame.transform.smoothscale(planet_image, (800, 800))
astroid_sprite1 = pygame.transform.smoothscale(astroid_image1, (800, 800))
astroid_sprite2 = pygame.transform.smoothscale(astroid_image2, (1300, 1300))
shop_sell_sprite = pygame.transform.smoothscale(shop_sell_image, (1000, 1000))
shop_buy_sprite = pygame.transform.smoothscale(shop_buy_image, (1000, 1000))
icon1_sprite = pygame.transform.smoothscale(icon1_image, (100, 100))
icon2_sprite = pygame.transform.smoothscale(icon2_image, (100, 100))
icon3_sprite = pygame.transform.smoothscale(icon3_image, (100, 100))
icon4_sprite = pygame.transform.smoothscale(icon4_image, (100, 100))
icon5_sprite = pygame.transform.smoothscale(icon5_image, (100, 100))
icon6_sprite = pygame.transform.smoothscale(icon6_image, (100, 100))
icon7_sprite = pygame.transform.smoothscale(icon7_image, (100, 100))
icon8_sprite = pygame.transform.smoothscale(icon8_image, (100, 100))
icon9_sprite = pygame.transform.smoothscale(icon9_image, (100, 100))
icon10_sprite = pygame.transform.smoothscale(icon10_image, (100, 100))
titlescreensprite = pygame.transform.smoothscale(titlescreenimg, (1500, 1000))
title_monster_sprite = pygame.transform.smoothscale(title_monster, (1000, 1000))
play_sprite = pygame.transform.smoothscale(play_image, (800, 800))

def start_screen_draw():
    screen.blit(titlescreensprite, (0,0))
    screen.blit(title_monster_sprite, (0,0))
    screen.blit(play_sprite, (400, 50))

    #pygame.draw.rect(screen, (0, 0, 0), [650, 600, 200, 100])
    #pygame.draw.rect(screen, (0, 0, 0), [650, 800, 200, 100])

    #pygame.draw.rect(screen, (200, 200, 200), [450, 200, 600, 300])

    #pygame.draw.rect(screen, (100, 100, 100), [640, option_y, 220, 10])
    #pygame.draw.rect(screen, (100, 100, 100), [640, option_y+110, 220, 10])
    #pygame.draw.rect(screen, (100, 100, 100), [640, option_y, 10, 120])
    #pygame.draw.rect(screen, (100, 100, 100), [640+210, option_y, 10, 120])

def main_screen_draw():
    screen.blit(bg_sprite, (50,50))
    screen.blit(plamet_sprite, (50, 150))
    screen.blit(astroid_sprite1, (650, 150))
    screen.blit(astroid_sprite2, (150, 50))
    pygame.draw.rect(screen, (100, 100, 100), [0, 0, 1500, 50])
    pygame.draw.rect(screen, (100, 100, 100), [0, 950, 1500, 50])
    pygame.draw.rect(screen, (100, 100, 100), [0, 0, 50, 1000])
    pygame.draw.rect(screen, (100, 100, 100), [1450, 0, 50, 1000])

    #pygame.draw.rect(screen, (100, 100, 100), [1340, 400, 100, 200])
    screen.blit(rocket_1_sprite, (1340-200, 400-350))
    #pygame.draw.rect(screen, (255, 0, 255), [950, 425, 300, 300])
    screen.blit(trash_pile_sprite, (1000, 425-250))
    #screen.blit(alien_crowd_sprite, (50, 50))
    #pygame.draw.rect(screen, (255, 0, 255), [100, 700, 200, 200])
    screen.blit(shop_sell_sprite, (50, 100))
    #pygame.draw.rect(screen, (255, 0, 255), [1250, 725, 200, 200])
    screen.blit(shop_buy_sprite, (550, 50))

    screen.blit(player_sprite, (player_x, player_y))

    #pygame.draw.rect(screen, (255, 0, 255), [950+50, 425+50, 300-100, 1]) 
    #pygame.draw.rect(screen, (255, 0, 255), [950+50, 425+50, 1, 300-100]) 
    #pygame.draw.rect(screen, (255, 0, 255), [950+50, 724-50, 300-100, 1]) 
    #pygame.draw.rect(screen, (255, 0, 255), [1249-50, 425+50, 1, 300-100])

    #pygame.draw.rect(screen, (255, 0, 255), [200, 50, 1, 900])

def tickPlayers(px, py, pxv, pyv, pspeed, up, down, left, right):
    #player controls
    key = pygame.key.get_pressed()
    if key[pygame.K_w]and up == True:
        pyv -= pspeed*dt

    elif key[pygame.K_s] and down == True:
        pyv += pspeed*dt

    if key[pygame.K_a] and left == True:
        pxv -= pspeed*dt

    elif key[pygame.K_d]and right == True:
        pxv += pspeed*dt

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
    global trash_list
    global player_take_timer
    global player_take_time
    global player_inventory
    global dt
    global trash
    global trash_time
    global trash_timer
    global trash_score_x
    global trash_score_y
    global player_sell_timer
    global player_sell_time
    global money_player
    global money_text_true
    global money_timer
    global money_time
    global skill_number
    global skill_limit
    global common_trash_price
    global spawn_time
    skill_number_t = 0

    skill_3_count = 0

    skill_done = []

    player_x_pre = 0
    player_y_pre = 0

    skip = False
    pygame.mixer.music.play(-1)
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
                            pygame.mixer.music.load("assets/Background_Game.ogg")
                            pygame.mixer.music.play(-1)
                            

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

                if event.type == pygame.QUIT:
                    pygame.quit()

            screen.fill((200, 200, 200))

            main_screen_draw()
            player_capacity_text_surface = custom_font.render(f"{number_trash_player}/{trash_capacity_player}", True, (150, 150, 150))
            player_money_text = custom_font.render(f"{money_player} money", True, (255, 255, 0))
            screen.blit(player_capacity_text_surface, (player_x+120, player_y+70))
            screen.blit(player_money_text, (60, 60))

            player_x, player_y, player_xv, player_yv = tickPlayers(player_x, player_y, player_xv, player_yv, player_speed, up, down, left, right)

            player_rect = pygame.Rect(player_x+120, player_y+120, player_w-133, player_h-119)
            wall_top = pygame.Rect(0, 45, 1500, 5)
            wall_left = pygame.Rect(45, 0, 5, 1000)
            wall_down = pygame.Rect(0, 955, 1500, 5)
            wall_right = pygame.Rect(1455, 0, 5, 1000)

            trash_top = pygame.Rect(1050, 475-250, 300-100, 1)
            trash_left = pygame.Rect(1050, 475-250, 1, 300-100)
            trash_down = pygame.Rect(1050, 684-250, 300-100, 1)
            trash_right = pygame.Rect(1249, 475-250, 1, 300-100)

            trash_pile_area = pygame.Rect(950+30, 425-250, 300, 300)
            sell_area = pygame.Rect(100, 700, 200, 200)
            buy_area = pygame.Rect(1250, 725, 200, 200)

            top_rect_group = [wall_top, trash_down]
            left_rect_group = [wall_left, trash_right]
            down_rect_group = [wall_down, trash_top]
            right_rect_group = [wall_right, trash_left]
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
                    trash_list.append(common_trash_price)


                ##print(number_trash)
                spawn_timer = 0
                


                
            if player_rect.colliderect(trash_pile_area) and number_trash > 0:
                player_take_timer += dt

                if player_take_timer >= player_take_time and number_trash_player < trash_capacity_player:
                    player_inventory.append(trash_list[0])
                    trash_list.pop(0)
                    number_trash -= 1
                    number_trash_player += 1
                    #print(player_inventory)
                    #print(trash_list)
                    player_take_timer = 0
                    trash = 1                                                                               
                    trash_timer = 3                                                          
                    trash_time = 0                                                                          
                    trash_text_surface = custom_font.render(f"+{common_trash_price}", True, (255, 255, 255))

                    trash_score_x = random.randint(math.floor(player_x+50), math.floor(player_x+100))
                    trash_score_y = random.randint(math.floor(player_y+50), math.floor(player_y+100))

            if trash == 1:                                                     
                trash_time += dt                                               
                screen.blit(trash_text_surface, (trash_score_x, trash_score_y))
                if trash_time >= trash_timer:
                    trash=0
                    trash_time = 0

            if player_rect.colliderect(sell_area) and number_trash_player > 0:
                player_sell_timer += dt
                if player_sell_timer >= player_sell_time:
                    number_trash_player -= 1
                    money_player += player_inventory[0]
                    player_inventory.pop(0)
                    player_sell_timer=0
                    #print(money_player)

                    money_text_surface = custom_font.render(f"+{common_trash_price}", True, (255, 255, 0))
                    money_score_x = random.randint(math.floor(player_x+50), math.floor(player_x+100))
                    money_score_y = random.randint(math.floor(player_y+50), math.floor(player_y+100))

                    money_text_true = True

            if money_text_true == True:
                money_timer += dt
                screen.blit(money_text_surface, (money_score_x, money_score_y))
                if money_timer >= money_time:
                    money_text_true = False
                    money_timer = 0

            if buy_area.colliderect(player_rect):
                key = pygame.key.get_pressed()

                if key[pygame.K_RETURN]:
                    screen_phase = 3
                    player_x_pre = player_x
                    player_y_pre = player_y

                    player_x = 800
                    player_y = 800

            
                    

        ##print(dt)

        if screen_phase == 3:
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screen_phase = 2
                        player_x = player_x_pre
                        player_y = player_y_pre
                        skip = True


                    if event.key == pygame.K_RIGHT:
                        skill_number += 1

                    if event.key == pygame.K_LEFT:
                        skill_number-=1

                    if skill_number_t == 1:
                        if event.key == pygame.K_RETURN and  1 not in skill_done:
                            if money_player >= 1:
                                skill_limit.append(2)
                                skill_limit.append(3)
                                money_player -= 1
                                skill_done.append(1)

                    if skill_number_t == 2:
                        if event.key == pygame.K_RETURN and 2 not in skill_done:
                            if money_player >= 2:
                                common_trash_price *= 2
                                skill_limit.append(4)
                                skill_limit.append(5)
                                money_player -= 2    
                                skill_done.append(2) 

                    if skill_number_t == 3:
                        if event.key == pygame.K_RETURN and 3 not in skill_done:
                            if money_player >= 5:
                                skill_3_count += 1

                                if skill_3_count == 1:
                                    skill_limit.append(6)
                                    skill_limit.append(7)
                                
                                money_player -= 5
                                spawn_time -= 0.5

                                if skill_3_count == 5:
                                    skill_done.append(3)
 

            screen.fill((255, 255, 255))
            skill_number_t = skill_limit[skill_number]
            if skill_number_t == 1 and skip == False:
                player_x = 800
                player_y= 800

            player_x, player_y, player_xv, player_yv = tickPlayers(player_x, player_y, player_xv, player_yv, player_speed, up, down, left, right)
            skill_x = (player_x -  1500// 2 + 77 // 2)
            skill_y = (player_y - 1000// 2 + 81// 2)

            screen.blit(icon1_sprite, (800-skill_x, 800-skill_y))
            text_surface = custom_font.render(f"unlcoks skill tree (1 money)", True, (0, 0, 0))
            screen.blit(text_surface, (800-skill_x, 900-skill_y))

            player_money_text = custom_font.render(f"{money_player} money", True, (0, 0, 0))
            screen.blit(player_money_text, (60, 60))

            for index in skill_limit:
                if index == 2:
                    if skill_number_t == 2 and skip == False:
                        player_x = 100
                        player_y= 850
                    pygame.draw.rect(screen, (0, 0, 0), [150-skill_x, 850-skill_y, 675, 5])
                    screen.blit(icon3_sprite, (100-skill_x, 800-skill_y))
                    text_surface = custom_font.render(f"double value of common trash (2 money)", True, (0, 0, 0))
                    screen.blit(text_surface, (100-skill_x, 900-skill_y))

                if index == 3:
                    if skill_number_t == 3 and skip == False:
                        player_x = 1500
                        player_y = 850

                    pygame.draw.rect(screen, (0, 0, 0), [875-skill_x, 850-skill_y, 675, 5])                      
                    screen.blit(icon3_sprite, (1500-skill_x, 800-skill_y))                                        
                    text_surface = custom_font.render(f"speeds up trash production (5 gold)", True, (0, 0, 0))
                    screen.blit(text_surface, (1500-skill_x, 900-skill_y))


            

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        #print(player_x, player_y, player_x_pre, player_y_pre)
        await asyncio.sleep(0)

asyncio.run(main())