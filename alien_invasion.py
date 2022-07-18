# -*- coding: utf-8 -*-
#外星人入侵游戏
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """初始化PGGAME、设置、屏幕"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_Invasion")

    #创建一艘飞船、一个子弹的编组和一个外星人的编组
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()