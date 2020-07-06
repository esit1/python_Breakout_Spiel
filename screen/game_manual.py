#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This window shows the game instructions and controls. It contains a back button, if you click it the main menu is called up.
"""

# Import
import pygame
import sys
import main as main
from pygame import *
from pygame.sprite import *
from settings import Settings


def game_manual():
    """This window shows the game instructions and controls. It contains a back button, if you click it the main menu is called up."""

    # Initialization
    pygame.init()
    settings = Settings()

    # Display configuration
    pygame.mouse.set_visible(1)
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Anleitung - Breakout")
    font = pygame.font.SysFont("comicsansms", 20)
    image_background_menu = pygame.image.load("images/background_manual.png")

    # Text
    text_heading = font.render('Anleitung', True, settings.ORANGE)
    text_back = font.render(' zurück zum Hauptmenü', True, settings.BLACK)

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
                # Opens the main menu
                main.main()

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
        pygame.draw.rect(screen, settings.ORANGE, button_back)

        # Draw Text
        screen.blit(text_heading, (350, 10))
        screen.blit(text_back, (300, 110))

        pygame.display.update()

    pygame.quit()
    quit()
