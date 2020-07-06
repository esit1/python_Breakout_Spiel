#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Displays the Game Over window. The points and the level reached are displayed. There is a button to play again.
"""

# Import
import pygame
import sys
from pygame import *
from pygame.sprite import *
from settings import Settings
import game_loop as game


def game_over(level, points):
    """
    Displays the Game Over window.
    :param level: Reached level
    :param points: Reached points
    """
    # Initialization
    pygame.init()
    settings = Settings()

    # Display configuration
    pygame.mouse.set_visible(1)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Anleitung - Breakout")
    font = pygame.font.SysFont("comicsansms", 20)
    image_background_menu = pygame.image.load("images/background_menu.png")

    # Text
    text_heading = font.render('Game Over', True, settings.ORANGE)
    text_back = font.render('Spiel erneut spielen', True, settings.BLACK)
    text_level = font.render('Level: ' + str(level) + ' erreicht', True, (0, 128, 0))
    text_points = font.render('Punkte: ' + str(points) + ' erreicht', True, (0, 128, 0))

    # Button
    button_back = pygame.Rect(200, 100, 400, 50)

    # Assign Variables
    manual_loop = True
    fps_clock = pygame.time.Clock()
    click = False

    # Menu Loop
    while manual_loop:
        # Timer
        fps_clock.tick(30)

        mouse_x_position, mouse_y_position = pygame.mouse.get_pos()

        # Event Handling
        # Event Handling,check Mouse pointer hit the button
        if button_back.collidepoint(mouse_x_position, mouse_y_position):
            if click:
                # Starts the game
                game.game()

        click = False

        # Event Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Redisplay
        screen.fill(settings.WHITE)
        screen.blit(image_background_menu, (0, 0))

        # Draw the Button
        pygame.draw.rect(screen, settings.ORANGE, button_back)

        # Draw the Text
        screen.blit(text_heading, (350, 10))
        screen.blit(text_back, (300, 100))
        screen.blit(text_level, (300, 200))
        screen.blit(text_points, (300, 300))

        pygame.display.update()

    pygame.quit()
    quit()
