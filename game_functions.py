#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains functions with different game functions
"""

# Import
import sys
import pygame
import sys
import pygame
import random
from random import randrange
from ball import Ball
from bonus_or_malus import Bonus_or_malus
from screen import game_over as over


def check_events(player):
    """
    Check key and mouse events
    :param player: Player object
    """
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        # mouse events
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                player.player_move_right()
            if event.rel[0] < 0:
                player.player_move_left()
            if event.rel[1] > 0:
                player.player_move_down()
            if event.rel[1] < 0:
                player.player_move_up()
    # key events
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.player_move_up()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.player_move_down()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.player_move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.player_move_right()


def check_level(level_nr, level):
    """
    :param level_nr: Level Nr
    :param level: object Level
    """
    global all_sprite_stones

    # select the Level, and returns the stones
    if level_nr == 1:
        all_sprite_stones = level.level01()
    elif level_nr == 2:
        all_sprite_stones = level.level02()
    elif level_nr == 3:
        all_sprite_stones = level.level03()
    elif level_nr == 4:
        all_sprite_stones = level.level04()
    elif level_nr == 5:
        all_sprite_stones = level.level05()
    elif level_nr == 6:
        all_sprite_stones = level.level06()
    elif level_nr == 7:
        all_sprite_stones = level.level07()
    elif level_nr == 8:
        all_sprite_stones = level.level08()
    elif level_nr == 9:
        all_sprite_stones = level.level09()
    elif level_nr == 10:
        all_sprite_stones = level.level10()
    elif level_nr > 10:
        all_sprite_stones = level.level_endless()
    else:
        print("Error, Level not found")

    return all_sprite_stones


def collide_player_vs_balls(player, all_sprite_balls):
    """
    Collision between player and balls,
    :param player: player
    :param all_sprite_balls: all balls
    """
    ball_collision_list = pygame.sprite.spritecollide(player, all_sprite_balls, False)
    for ball in ball_collision_list:
        # Calls a method that changes the direction of the ball.
        ball.bounce_player(player.player_x_position_left(), player.player_x_position_right(),
                           player.player_x_position_center())


def collide_balls_vs_stones(all_sprite_balls, all_sprite_stones):
    """
    Collision between balls and stones.
    :param all_sprite_balls: all balls
    :param all_sprite_stones: all stones
    """
    ball_collision_list = pygame.sprite.groupcollide(all_sprite_balls, all_sprite_stones, False, False)
    for ball in ball_collision_list:
        # Calls a method that changes the direction of the ball.
        ball.bounce_stone()


def collide_stones_vs_balls(all_sprite_stones, all_sprite_balls, bonus_or_malus_list, bonus, malus, all_sprite_group):
    """
    Collision between balls and stones. Creates a bonus or malus

    :param all_sprite_stones: all stones
    :param all_sprite_balls: all balls
    :param bonus_or_malus_list: list of bonus or malus sprite
    :param bonus: the name of the bonus
    :param malus: the name pf the malus
    :param all_sprite_group: all sprite
    """
    name_bonus = ('slowlyBall', 'newBall', 'biggerBall', 'biggerPlayer')
    name_malus = ('smallerBall', 'fasterBall', 'smallerPlayer')

    stones_collision_list = pygame.sprite.groupcollide(all_sprite_stones, all_sprite_balls, False, False)
    for stone in stones_collision_list:

        # Reduces the life of the stone
        stone.reduce_life()

        # Checks if there are more than 6 bonus or malus stones
        if bonus_or_malus_list.__len__() <= 6:

            # If the bonus counter is zero, a new bonus is created.
            if bonus == 0:
                # create new bonus
                bonus_sprite = Bonus_or_malus(stone.get_x_position(), stone.get_y_position(),
                                              name_bonus[randrange(0, len(name_bonus))])

                # add bonus to all sprites list and bonus or malus list
                bonus_or_malus_list.add(bonus_sprite)
                all_sprite_group.add(bonus_sprite)

            # If the malus counter is zero, a new malus is created.
            if malus == 0:
                # create new malus
                malus_sprite = Bonus_or_malus(stone.get_x_position(), stone.get_y_position(),
                                              name_malus[randrange(0, len(name_malus))])

                # add bonus to all sprites list and bonus or malus list
                bonus_or_malus_list.add(malus_sprite)
                all_sprite_group.add(malus_sprite)


def collide_player_vs_bonus_or_malus(player, all_sprite_bonus_or_malus, all_sprite_ball, all_sprite_group):
    """
    Collision between player and bonus or malus. Select the appropriate method

    :param player: player
    :param all_sprite_bonus_or_malus: bonus or malus list
    :param all_sprite_ball: all balls
    :param all_sprite_group: all sprite
    """
    bonus_or_malus_collision_list = pygame.sprite.spritecollide(player, all_sprite_bonus_or_malus, False)
    for bonus_or_malus in bonus_or_malus_collision_list:

        if bonus_or_malus.get_name() == 'newBall':
            # create new ball
            new_ball = Ball()
            # add ball to ball list and all sprite list
            all_sprite_ball.add(new_ball)
            all_sprite_group.add(new_ball)
        elif bonus_or_malus.get_name() == 'biggerBall':
            for ball in all_sprite_ball:
                # make ball bigger
                ball.make_bigger()
        elif bonus_or_malus.get_name() == 'smallerBall':
            for ball in all_sprite_ball:
                # make ball smaller
                ball.make_smaller()
        elif bonus_or_malus.get_name() == 'slowlyBall':
            for ball in all_sprite_ball:
                # make ball slowly
                ball.move_slower()
        elif bonus_or_malus.get_name() == 'fasterBall':
            for ball in all_sprite_ball:
                # make ball faster
                ball.move_faster()
        elif bonus_or_malus.get_name() == 'biggerPlayer':
            # make player bigger
            player.make_bigger()
        elif bonus_or_malus.get_name() == 'smallerPlayer':
            # make player smaller
            player.make_smaller()
        else:
            pass

        # deletes bonus or malus
        bonus_or_malus.kill()


def check_bonus_or_malus_null(number):
    """
    create random number between 3 and 8
    :param number:
    :return: random number
    """
    if number == 0:
        number = random.randint(3, 8)
    return number


def game_over(level, highscore):
    """
    Opens the Game over window
    :param level: current level
    :param highscore: current highscore
    """
    over.game_over(level, highscore)
