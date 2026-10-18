import pygame

pygame.init()

running = True

player_x = 500
player_y = 500
player_w = 200
player_h = 200

player_xv = 0
player_yv = 0

player_speed = 1

up = True
down = True
left = True
right = True

screen_phase = 1
menu_option = 1

option_y = 590

spawn_timer = 0
spawn_time = 5

trash_type = -1

number_trash = 0
number_trash_player = 0
trash_capacity = 10
trash_capacity_player = 3