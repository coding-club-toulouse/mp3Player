#!/usr/bin/python3
# -*- coding; utf-8 -*-

import pygame, time
from pygame.locals import *
from sort import *

def main():
    pygame.init()
    pygame.display.set_caption("mp3player")
    display_window = 1
    window = pygame.display.set_mode((640, 480))
    size = [640, 480]
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("fond.jpg").convert()
    continuer = 1
    button_l = pygame.Rect(230, 200, 200, 75)
    button_s = pygame.Rect(230, 300, 200, 75)
    while display_window:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                display_window = 0
        if key[K_ESCAPE]:
            display_window = 0
        window.blit(background, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button_l.collidepoint(mouse_pos):
                    print('button long was pressed at {0}'.format(mouse_pos))
                    find_music('./music/', 'long')
                elif button_s.collidepoint(mouse_pos):
                    print('button short was pressed at {0}'.format(mouse_pos))
                    find_music('./music/', 'short')
        pygame.draw.rect(screen, [255, 0, 0], button_l)
        pygame.draw.rect(screen, [0, 255, 0], button_s)
        pygame.display.update()
    pygame.quit()
main()