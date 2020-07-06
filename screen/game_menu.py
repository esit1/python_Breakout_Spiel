#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Displays the main menu. The following buttons are available, play, manual and quit.
If the user presses the play button, a new game is started. If the user presses the Manual button,
the menu with the manual is called up. If the player presses the Exit button, the window is closed."""


# Import
import pygame
import sys
from pygame import *
from pygame.sprite import *
from screen import game_manual as manual
from settings import Settings
import game_loop as game


def game_menu():
    """Represents the main menu. With three buttons play, instructions and quit."""

    # Initialization
    pygame.init()
    settings = Settings()

    # Display configuration
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.mouse.set_visible(1)
    pygame.display.set_caption("Menü - Breakout")
    font = pygame.font.SysFont("comicsansms", 20)
    image_background_menu = pygame.image.load("images/background_menu.png")

    # Text
    text_menu = font.render('Hauptmenü ', True, settings.ORANGE)
    text_play = font.render('Spielen ', True, settings.BLACK)
    text_manual = font.render('Anleitung ', True, settings.BLACK)
    text_exit = font.render('Beenden ', True, settings.BLACK)

    # Buttons
    button_play = pygame.Rect(200, 100, 400, 50)
    button_manual = pygame.Rect(200, 200, 400, 50)
    button_exit = pygame.Rect(200, 300, 400, 50)

    # Assign Variables
    menu_loop = True
    fps_clock = pygame.time.Clock()
    click = False

    # Menu Loop
    while menu_loop:
        # Timer
        fps_clock.tick(30)

        mouse_x_position, mouse_y_position = pygame.mouse.get_pos()

        # Event Handling
        # Event Handling,check Mouse pointer hit the button
        if button_play.collidepoint(mouse_x_position, mouse_y_position):
            if click:
                # Starts the game
                game.game()
        if button_manual.collidepoint(mouse_x_position, mouse_y_position):
            if click:
                # Opens the instructions
                manual.game_manual()
        if button_exit.collidepoint(mouse_x_position, mouse_y_position):
            if click:
                # Closes the window
                sys.exit()

        click = False

        # Event Handling, Qquit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Redisplay
        screen.fill(settings.WHITE)
        screen.blit(image_background_menu, (0, 0))

        # Draw the Buttons
        pygame.draw.rect(screen, settings.ORANGE, button_play)
        pygame.draw.rect(screen, settings.ORANGE, button_manual)
        pygame.draw.rect(screen, settings.ORANGE, button_exit)

        # Draw the Text
        screen.blit(text_menu, (350, 10))
        screen.blit(text_play, (350, 110))
        screen.blit(text_manual, (350, 210))
        screen.blit(text_exit, (350, 310))

        pygame.display.update()

    pygame.quit()
    quit()
