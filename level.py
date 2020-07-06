#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Class contains the individual levels. Depending on the level, the stone are arranged differently and have different lives.
"""

# Import
from pygame import *
from pygame.sprite import *
import pygame
import sys
from settings import Settings
from stone import Stone


class Level(Sprite):
    """
    Class contains the individual levels.
    """

    def __init__(self, *groups):
        """
        Initializes the level
        :param groups: Group of Spites
        """
        super().__init__(*groups)
        self.settings = Settings()

        # All Spite
        self.all_sprite_group = pygame.sprite.Group()

        # Starts at level 1
        self.currentLevel = 1

    def level01(self):
        """
        Level 1
        three rows of stone with 14 stone each, row one with 1 life, row two with 2 lives,
        Row 3 with 3 lives.

        :return: all sprites
        """
        for i in range(14):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  40, 20, 3, 40 + i * 50, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               2, 40 + i * 50, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40, 20,
                                1, 40 + i * 50, 140)

            # add stone to sprite liste
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        return self.all_sprite_group

    def level02(self):
        """
        Level 2
        three rows of stone with 16 stone each, row one with 3 life, row two with 3 lives,
        Row 3 with 3 lives.

        :return: all sprites
        """
        stone_live = 3
        for i in range(16):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  40, 20, stone_live, 40 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 40 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40, 20,
                                stone_live, 40 + i * 45, 140)

            # add stone to sprite list
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        return self.all_sprite_group

    def level03(self):
        """
        Level 3
        4 rows of stone with 16 stone each. Each stone has 3 lives.

        :return: all sprites
        """
        stone_live = 3
        for i in range(16):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  40, 20, stone_live, 40 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 40 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40, 20,
                                stone_live, 40 + i * 45, 140)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png', 40,
                                 20,
                                 stone_live, 40 + i * 45, 180)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        return self.all_sprite_group

    def level04(self):
        """
        Level 4
        4 rows of stone. Each stone has 3 lives.

        :return: all sprites
        """
        stone_live = 3
        for i in range(5):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png',
                                  'images/stone/yellow3.png',
                                  40, 20, stone_live, 40 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 40 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40,
                                20,
                                stone_live, 40 + i * 45, 140)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20,
                                 stone_live, 40 + i * 45, 180)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        for i in range(5):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png',
                                  'images/stone/yellow3.png',
                                  40, 20, stone_live, 550 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 550 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40,
                                20,
                                stone_live, 550 + i * 45, 140)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20,
                                 stone_live, 550 + i * 45, 180)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        return self.all_sprite_group

    def level05(self):
        """
        Level 5
        5 rows of stone. Each stone has 3 lives.

        :return: all sprites
        """
        stone_live = 3
        for i in range(16):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  40, 20, stone_live, 40 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 40 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40, 20,
                                stone_live, 40 + i * 45, 140)

            # add stone to sprite list
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        for i in range(5):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png',
                                  'images/stone/purple3.png', 40,
                                  20, stone_live, 40 + i * 45, 180)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20, stone_live, 40 + i * 45, 220)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_purple)

        for i in range(5):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png',
                                  'images/stone/purple3.png', 40,
                                  20, stone_live, 550 + i * 45, 180)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20, stone_live, 550 + i * 45, 220)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_purple)

        return self.all_sprite_group

    def level06(self):
        """
        Level 6
        4 rows of stone. Each stone has 3 lives. Small stone

        :return: all sprites
        """
        stone_live = 3
        for i in range(10):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png',
                                  'images/stone/purple3.png', 30,
                                  10, stone_live, 40 + i * 75, 80)

            # add stone to sprite list
            self.all_sprite_group.add(stone_purple)

        for i in range(19):
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 30 + i * 40, 120)
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 30 + i * 40, 140)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 30 + i * 40, 160)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        return self.all_sprite_group

    def level07(self):
        """
        Level 7
        5 rows of stone. Each stone has 3 lives. Small stone
        25 stone in a row.

        :return: all sprites
        """
        stone_live = 3
        for i in range(25):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 15 + i * 31, 71)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 15 + i * 31, 81)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 15 + i * 31, 91)
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 15 + i * 31, 101)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 15 + i * 31, 111)

            # add stone to sprite list
            self.all_sprite_group.add(stone_purple)
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)
            self.all_sprite_group.add(stone_blue)

        return self.all_sprite_group

    def level08(self):
        """
        Level 8
        5 rows of stone. Each stone has 3 lives.

        :return: all sprites
        """

        stone_live = 3
        for i in range(16):
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  40, 20, stone_live, 40 + i * 45, 60)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png', 40, 20,
                               stone_live, 40 + i * 45, 100)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png', 40, 20,
                                stone_live, 40 + i * 45, 140)

            # add stone to sprite list
            self.all_sprite_group.add(stone_blue)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)

        for i in range(5):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png',
                                  'images/stone/purple3.png', 40,
                                  20, stone_live, 40 + i * 45, 180)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20, stone_live, 40 + i * 45, 220)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_purple)

        for i in range(5):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png',
                                  'images/stone/purple3.png', 40,
                                  20, stone_live, 550 + i * 45, 180)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 40, 20, stone_live, 550 + i * 45, 220)

            # add stone to sprite list
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_purple)

        return self.all_sprite_group

    def level09(self):
        """
        Level 9
        15 rows of stone. Each stone has 3 lives. Small stone
        1 stone in a row.

        :return: all sprites
        """
        stone_live = 3

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 20, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 40, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 60, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 80, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 100, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 120, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 140, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 160, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 180, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 200, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 220, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 240, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 260, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 280, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 300, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 320, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 340, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 360, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 380, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 400, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 420, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 440, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 460, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 480, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 500, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 520, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 540, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 560, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 580, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 600, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 620, 71)
        stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 640, 81)
        stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 660, 91)
        stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 680, 101)
        stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 700, 111)

        # add stone to sprite list
        self.all_sprite_group.add(stone_purple)
        self.all_sprite_group.add(stone_green)
        self.all_sprite_group.add(stone_red)
        self.all_sprite_group.add(stone_yellow)
        self.all_sprite_group.add(stone_blue)

        return self.all_sprite_group

    def level10(self):
        """
        Level 10
        15 rows of stone. Each stone has 3 lives. Small stone
        25 stone in a row.

        :return: all sprites
        """
        stone_live = 3
        for i in range(25):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 15 + i * 31, 71)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 15 + i * 31, 81)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 15 + i * 31, 91)
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 15 + i * 31, 101)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 15 + i * 31, 111)

            # add stone to sprite list
            self.all_sprite_group.add(stone_purple)
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)
            self.all_sprite_group.add(stone_blue)

        for i in range(25):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 15 + i * 31, 121)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 15 + i * 31, 131)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 15 + i * 31, 141)
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 15 + i * 31, 151)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 15 + i * 31, 161)

            # add stone to sprite list
            self.all_sprite_group.add(stone_purple)
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)
            self.all_sprite_group.add(stone_blue)

        for i in range(25):
            stone_purple = Stone('images/stone/purple1.png', 'images/stone/purple2.png', 'images/stone/purple3.png',
                                  30, 10, stone_live, 15 + i * 31, 171)
            stone_red = Stone('images/stone/red1.png', 'images/stone/red2.png', 'images/stone/red3.png',
                               30, 10, stone_live, 15 + i * 31, 181)
            stone_blue = Stone('images/stone/blue1.png', 'images/stone/blue2.png', 'images/stone/blue3.png',
                                30, 10, stone_live, 15 + i * 31, 191)
            stone_yellow = Stone('images/stone/yellow1.png', 'images/stone/yellow2.png', 'images/stone/yellow3.png',
                                  30, 10, stone_live, 15 + i * 31, 201)
            stone_green = Stone('images/stone/green1.png', 'images/stone/green2.png', 'images/stone/green3.png',
                                 30, 10, stone_live, 15 + i * 31, 211)

            # add stone to sprite list
            self.all_sprite_group.add(stone_purple)
            self.all_sprite_group.add(stone_green)
            self.all_sprite_group.add(stone_red)
            self.all_sprite_group.add(stone_yellow)
            self.all_sprite_group.add(stone_blue)

        return self.all_sprite_group
