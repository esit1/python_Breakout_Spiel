#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""
This class represents the player figure. this class contains methods of movement
"""

# Import
import pygame
import sys
from pygame import *
from pygame.sprite import *
from settings import Settings

class Player(Sprite):
    """
    This class represents the player figure.
    """
    def __init__(self):
        Sprite.__init__(self)
        self.settings = Settings()

        # speed
        self.speed = 15

        # size and width
        self.size_width = 200
        self.size_height = 20

        # image
        self.image = image.load('images/player/bar.png')
        self.image = pygame.transform.scale(self.image, (self.size_width, self.size_height))
        self.rect = self.image.get_rect()

        # sound
        self.sound = pygame.mixer.Sound('sounds/bounce.wav')

        # start position
        self.rect.x = 300
        self.rect.y = 550

    def player_move_right(self):
        """
        Moves the character to the right
        """
        if self.rect.x < self.settings.SCREEN_WIDTH - self.size_width:
            self.rect.x += self.speed

    def player_move_left(self):
        """
        Moves the character to the left
        """
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def player_move_up(self):
        """
        Moves the character up
        """
        if self.rect.y > 500:
            self.rect.y -= self.speed

    def player_move_down(self):
        """
        Moves the character down
        """
        if self.rect.y < self.settings.SCREEN_HEIGHT - 20:
            self.rect.y += self.speed

    def player_x_position_left(self):
        """
        get position left
        :return: position left
        """
        return self.rect.left

    def player_x_position_right(self):
        """
        get position right
        :return: position right
        """
        return self.rect.right

    def player_x_position_center(self):
        """
        get position center
        :return: position center
        """
        return self.rect.centerx

    def make_bigger(self):
        """
        make the player bigger
        """
        if self.size_width <= 400:
            self.size_width += 50

        self.size_width = 200

    def make_smaller(self):
        """
        make the player smaller
        """
        if self.size_width > 60:
            self.size_width -= 50

    def update(self):
        self.image = pygame.transform.scale(self.image, (self.size_width, self.size_height))
