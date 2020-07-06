#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class represents a ball. Contains methods, move faster, move slower, make bigger, make smaller, bounce player and bounce stone.
"""

# Import
from pygame import *
from pygame.sprite import *
from settings import Settings
import pygame
import sys


class Ball(Sprite):
    """
    This class represents a ball.
    """

    def __init__(self):
        """
        Initializes ball
        """
        Sprite.__init__(self)

        self.settings = Settings()

        # Start speed
        self.speed_x_position = 0
        self.speed_y_position = 2
        self.speed = 1

        # Size ball
        self.size = 10

        # Image ball
        self.image = image.load('images/ball/ball.png')
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()

        # Sound ball
        self.sound = pygame.mixer.Sound('sounds/bounce.wav')
        self.sound_player = pygame.mixer.Sound('sounds/player.wav')

        # Start Position ball
        self.rect.x = self.settings.SCREEN_WIDTH / 2
        self.rect.y = 150

    def bounce_stone(self):
        """
        Plays a sound. Changes the direction of the ball.
        """
        self.sound.play()
        self.speed_y_position *= -1

    def bounce_player(self, left_position_player, right_position_player, center_position_player):
        """
        Plays a sound. Changes the direction of the ball.
        :param left_position_player: Position Player left
        :param right_position_player: Position Player left
        :param center_position_player: Position Player left
        """
        # play sound
        self.sound_player.play()

        # Checks whether the ball comes from above
        if self.speed_y_position >= 0:

            # Changes the Y direction
            self.speed_y_position *= -1

            # Calculates half the size of the racket
            difference = (right_position_player - left_position_player) / 2

            # Checks whether the racket is hit to the right of the center
            if center_position_player <= self.rect.centerx:

                # Calculates what percentage is the center away.
                ten_percent = center_position_player + (difference * 0.1)
                thirty_percent = center_position_player + (difference * 0.3)
                fifty_percent = center_position_player + (difference * 0.5)
                seventy_percent = center_position_player + (difference * 0.7)
                ninety_percent = center_position_player + (difference * 0.9)

                # Checks in which area the ball is hit. The X speed is changed accordingly.
                # The closer to the center, the smaller the angle.
                if self.rect.centerx <= ten_percent:
                    # area 0 - 10 % from the center
                    self.speed_x_position = 2
                elif ten_percent < self.rect.centerx <= thirty_percent:
                    # area 10 - 30 % from the center
                    self.speed_x_position = 2.5
                elif thirty_percent < self.rect.centerx <= fifty_percent:
                    # area 30 - 50 % from the center
                    self.speed_x_position = 3
                elif fifty_percent < self.rect.centerx <= seventy_percent:
                    # area 50 - 70 % from the center
                    self.speed_x_position = 3.5
                elif seventy_percent < self.rect.centerx <= ninety_percent:
                    # area 70 - 90 % from the center
                    self.speed_x_position = 4
                elif self.rect.centerx > ninety_percent:
                    # area 90 - 100 % from the center
                    self.speed_x_position = 4.5

            # Checks whether the racket is hit to the left of the center
            elif center_position_player > self.rect.centerx:

                # Calculates what percentage is the center away.
                ten_percent = center_position_player - (difference * 0.1)
                thirty_percent = center_position_player - (difference * 0.3)
                fifty_percent = center_position_player - (difference * 0.5)
                seventy_percent = center_position_player - (difference * 0.7)
                ninety_percent = center_position_player - (difference * 0.9)

                # Checks in which area the ball is hit. The X speed is changed accordingly.
                # The closer to the center, the smaller the angle.
                if self.rect.centerx > ten_percent:
                    # area 0 - 10 % from the center
                    self.speed_x_position = -2
                elif ten_percent > self.rect.centerx >= thirty_percent:
                    # area 10 - 30 % from the center
                    self.speed_x_position = -2.5
                elif thirty_percent > self.rect.centerx >= fifty_percent:
                    # area 30 - 50 % from the center
                    self.speed_x_position = -2
                elif fifty_percent > self.rect.centerx >= seventy_percent:
                    # area 50 - 70 % from the center
                    self.speed_x_position = -3.5
                elif seventy_percent > self.rect.centerx >= ninety_percent:
                    # area 70 - 90 % from the center
                    self.speed_x_position = -4
                elif self.rect.centerx <= ninety_percent:
                    # area 90 - 100 % from the center
                    self.speed_x_position = -4.5

    def update(self):
        """
        update Ball
        """

        # speed
        self.rect.x += self.speed_x_position * self.speed
        self.rect.y += self.speed_y_position * self.speed

        # Selects the picture based on how much life is live.
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Changes direction when the ball hits a screen
        if self.rect.x >= self.settings.SCREEN_WIDTH - self.size or self.rect.x <= 0:
            self.speed_x_position *= -1

        # Changes direction when the ball hits the top of the screen
        if self.rect.y <= 0:
            self.speed_y_position *= -1

        # Deletes the ball as soon as the ball touches the bottom of the screen
        if self.rect.y >= self.settings.SCREEN_HEIGHT - self.size:
            #self.speed_y_position *= -1
            self.kill()

    def move_faster(self):
        """
        move the ball faster
        """
        self.speed += 0.4

    def move_slower(self):
        """
        move the ball slower
        """
        if self.speed > 1:
            self.speed -= 0.4

    def make_bigger(self):
        """
        make the ball bigger
        """
        if self.size <= 25:
            self.size += 4

    def make_smaller(self):
        """
        make the ball smaller
        """
        if self.size > 9:
            self.size -= 4
