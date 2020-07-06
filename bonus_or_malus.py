#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class provides bonus or malus stones.
"""
# Import
from pygame import *
from pygame.sprite import *
import pygame
import sys
from settings import Settings


class Bonus_or_malus(Sprite):
    """
    This class provides bonus or malus stones.
    """
    def __init__(self, x_position, y_position, name):
        """
        Bonus_or_malus , initialization
        :param x_position: X Start Position
        :param y_position: Y Start Position
        :param name: Name of the bonus or malus
        """
        Sprite.__init__(self)

        self.settings = Settings()

        # Greatness of the bonus or malus
        self.size_width = 40
        self.size_height = 20

        # Speed
        self.speed_y_position = 2

        # Image
        self.name = name
        self.image = image.load('images/BonusOrMalus/' + name + '.png')
        self.image = pygame.transform.scale(self.image, (self.size_width, self.size_height))
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = x_position
        self.rect.y = y_position

    def get_name(self):
        """
        Get the Name of the bonus or malus
        :return: Name of the bonus or malus
        """
        return self.name

    def update(self):
        """
        Move the bonus or malus. Erase the bonus or malus as soon as it leaves the screen.
        """

        self.rect.y += self.speed_y_position

        if self.rect.y > self.settings.SCREEN_HEIGHT:
            self.kill()
