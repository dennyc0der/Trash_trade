import pygame

pygame.init()

running = True

player_x = 500
player_y = 500
player_w = 200
player_h = 200

player_xv = 0
player_yv = 0

player_speed = 60

dt = 0

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

trash_list = []
player_inventory = []

common_trash_price = 1
uncommon_trash_price = 2
rare_trash_price = 4

player_take_timer = 0
player_take_time = 4

player_sell_timer = 0
player_sell_time = 5

trash = 0
trash_timer = 1
trash_time = 0

trash_score_x = 0
trash_score_y = 0

money_player = 0
money_text_true = False

money_timer = 0
money_time = 1

skill_number = 0

skill_limit = [1]