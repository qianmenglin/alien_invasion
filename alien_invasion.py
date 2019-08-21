# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_status import GameStats
from button import  Button
from scoreboard import  ScoreBoard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion for you')

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)


    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets, sb)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)



if __name__ == '__main__':
    run_game()