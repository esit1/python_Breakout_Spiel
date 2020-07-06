#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Class represents a single stone. Contains methods that reduce the life of the stone and return the position.
"""

# Import
from pygame import *
from pygame.sprite import *
from settings import Settings


class Stone(Sprite):
    """
    Class represents a single stone.
    """
    def __init__(self, stone_image1, stone_image2, stone_image3, width, height, live, x_position, y_position):
        """
        Initializes a single stone
        :param stone_image1: Picture, stone with life 1
        :param stone_image2: Picture, stone with life 2
        :param stone_image3: Picture, stone with life 3
        :param width: width Stone
        :param height: height Stone
        :param live: Number of lives
        :param x_position: Starting position X
        :param y_position: Starting position Y
        """
        super(Stone, self).__init__()

        self.settings = Settings()

        # width and heigth
        self.size_width = width
        self.size_height = height

        # live
        self.live = live

        # Pictures of the stone
        self.images = []
        self.images.append(pygame.image.load(stone_image1))
        self.images.append(pygame.image.load(stone_image2))
        self.images.append(pygame.image.load(stone_image3))
        self.image = self.images[self.live - 1]

        self.image = pygame.transform.scale(self.image, (self.size_width, self.size_height))
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = x_position
        self.rect.y = y_position

    def reduce_life(self):
        """
        Reduces the life of the stone, but only if it is not indestructible.
        """
        if self.live != 'indestructible':
            self.live -= 1

    def update(self):
        """
        Erase the stone as soon as life is zero. Changes the picture
        """
        if self.live == 0:
            self.kill()

        self.image = self.images[self.live - 1]
        self.image = pygame.transform.scale(self.image, (self.size_width, self.size_height))

    def get_x_position(self):
        """
        Get X Position
        :return: X Position
        """
        return self.rect.x

    def get_y_position(self):
        """
        Get Y Position
        :return: Y Position
        """
        return self.rect.y
