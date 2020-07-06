#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Goal:
Destroy all stones with a ball. You have to keep the ball coming from above with your racket from falling. If all stones are destroyed, the level is done.
Control:
Move racket to the right: button D or arrow to the right
Move racket to the left: button A or arrow to the left
To move the racket up: W button or up arrow
Move racket down: button D or arrow down
Alternatively, the racket can be moved with the mouse.
"""


__author__ = "Christine Dall"

# import
import pygame
import sys
import screen.game_menu as menu


def main():
    """ Main method, starting point of the game. The main menu is called in the main method."""
    menu.game_menu()


if __name__ == '__main__':
    main()
