#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains the game loop, in which the game runs.
The method contains different queries that check whether there has been a collision between objects.
"""

# Import
import pygame
import sys
import random
from pygame import *
from pygame.sprite import *
import game_functions as game_functions

from settings import Settings
from player import Player
from ball import Ball
from level import Level

def game():
    """
    This method includes the game loop.
    """

    # Initialization
    pygame.init()
    settings = Settings()

    # Display configuration
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout")
    pygame.mouse.set_visible(0)
    font = pygame.font.SysFont("comicsansms", 20)
    image_background = pygame.image.load("images/background.png")

    # Entities
    all_sprite_group = pygame.sprite.Group()
    all_sprite_bonus_or_malus = pygame.sprite.Group()
    all_sprite_stones = pygame.sprite.Group()
    all_sprite_balls = pygame.sprite.Group()

    # create a ball
    ball = Ball()

    #create the player
    player = Player()

    #create the first level
    level = Level()

    # Adds objects to the group
    all_sprite_group.add(ball)
    all_sprite_group.add(player)
    all_sprite_balls.add(ball)

    # level counter
    level_nr = 0

    # live counter
    live = 2

    # highscore counter
    highscore = 0

    # bonus counter
    bonus = random.randint(1, 5)

    # malus counter
    malus = random.randint(2, 5)

    # Assign Variables
    game_loop = True
    fps_clock = pygame.time.Clock()

    # Game Loop
    while game_loop:
        # Timer
        fps_clock.tick(60)

        # Event Handling
        game_functions.check_events(player)

        # Checks whether stones are still present. If there are only zero stones, a new level is started.
        if all_sprite_stones.__len__() == 0:

            # If level 10 is reached do not increase
            if level_nr != 10:
                level_nr += 1
            else:
                pass

            live += 1

            # new level, add stones to sprites
            all_sprite_stones = game_functions.check_level(level_nr, level)
            all_sprite_group.add(all_sprite_stones)

        # Checks whether there are any balls left. If there are no balls, a new ball is created.
        if all_sprite_balls.__len__() == 0:

            # new ball, add ball to sprites
            new_ball = Ball()
            all_sprite_balls.add(new_ball)
            all_sprite_group.add(new_ball)

            # Life is reduced by one.
            live -= 1

        # Checks if there was a collision between player and balls.
        if pygame.sprite.spritecollide(player, all_sprite_balls, False):
            game_functions.collide_player_vs_balls(player, all_sprite_balls)

        # Checks if there was a collision balls player and stones.
        if pygame.sprite.groupcollide(all_sprite_balls, all_sprite_stones, False, False):
            game_functions.collide_balls_vs_stones(all_sprite_balls, all_sprite_stones)
            highscore += 10

        # Checks if there was a collision between stones and balls.
        if pygame.sprite.groupcollide(all_sprite_stones, all_sprite_balls, False, False):
            game_functions.collide_stones_vs_balls(all_sprite_stones, all_sprite_balls, all_sprite_bonus_or_malus, bonus,
                                                   malus, all_sprite_group)


            # Checks whether the bonus is less than zero, if so the function returns a new number
            bonus = game_functions.check_bonus_or_malus_null(bonus)

            # Checks whether the malus is less than zero, if so the function returns a new number
            malus = game_functions.check_bonus_or_malus_null(malus)

            bonus -= 1
            malus -= 1

            # Checks whether bonus and malus are equal
            if bonus == malus:
                malus = +2

        # Checks if there was a collision between player and bonus or malus.
        if pygame.sprite.spritecollide(player, all_sprite_bonus_or_malus, False):
            game_functions.collide_player_vs_bonus_or_malus(player, all_sprite_bonus_or_malus, all_sprite_balls,
                                                            all_sprite_group)
        # Checks if life is zero
        if live <= 0:
            game_functions.game_over(level_nr, highscore)

        # draw text, Current level
        text_level = font.render('Level: ' + str(level_nr), True, settings.ORANGE)

        # draw text, Current live
        text_live = font.render('Leben: ' + str(live), True, settings.ORANGE)

        # draw text, Current highscore
        text_highscore = font.render('Punkte: ' + str(highscore), True, settings.ORANGE)

        # Redisplay
        screen.fill(settings.WHITE)
        screen.blit(image_background, (0, 0))
        screen.blit(text_level, (10, 5))
        screen.blit(text_live, (350, 5))
        screen.blit(text_highscore, (settings.SCREEN_WIDTH - 150, 5))
        all_sprite_group.update()
        all_sprite_group.draw(screen)

        pygame.display.flip()

    pygame.quit()
    quit()
