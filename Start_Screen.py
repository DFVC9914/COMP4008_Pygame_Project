
import pygame,os,Game_Modes,How_to_play

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:24:39 2020
@author: NANDI GUO
"""

pygame.init()
Width,Height = (780,366)
Orange = (255,145,0)
White = (255,255,255)
Blue = (0,238,255)
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Start Screen")
background = pygame.image.load("Images/Backgrounds/Start1_Background.png")
how_to_play = pygame.image.load("Images/Backgrounds/how.png")
font = pygame.font.Font(pygame.font.get_default_font(), 32)
bgm_sound = pygame.mixer.Sound("Sounds/Start_Bgm.mp3")
bgm_sound.play()

class Button():
    def __init__(self, text, color, x=None, y=None, **kwargs):
        self.surf = font.render(text, True, color)
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()
        self.x = x
        self.y = y

    def display(self):
    	screen.blit(self.surf, (self.x, self.y))

    def check_click(self, position):  
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if (x_match) and (y_match):
            return True
        else:
            return False

def Firstscreen():
    b1x,b1y=360,100
    b2x,b2y=360,160 
    b3x,b3y=310,220  
    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')

    def Ourname():
        global font
        aut = pygame.font.Font(pygame.font.get_default_font(), 16)
        author = aut.render('Creators: CHAO CUI, NANDI GUO, HAO WU                                                                    \
                Version 1.0', True, White)
        screen.blit(author, (10, 340))

    title = font.render('CWG-Ultimate Running', True, White)
    screen.blit(title, (Width//2 - title.get_width()//2, 25))

    play_button = Button('Play', Orange, b1x, b1y)
    exit_button = Button('Quit', Orange, b2x, b2y)
    introduction_button = Button('How to play', Orange, b3x, b3y)

    play_button.display()
    exit_button.display()
    introduction_button.display()
    Ourname()
    pygame.display.update()

    while True:
        if not (play_button.check_click(pygame.mouse.get_pos()) or\
            exit_button.check_click(pygame.mouse.get_pos()) or\
            introduction_button.check_click(pygame.mouse.get_pos())):
                pygame.mixer.music.play()

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', Blue, b1x, b1y)                        
        else:            
            play_button = Button('Play', Orange, b1x, b1y)
            
        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Quit', Blue, b2x, b2y)
        else:           
            exit_button = Button('Quit', Orange, b2x, b2y)

        if introduction_button.check_click(pygame.mouse.get_pos()):
            introduction_button = Button('How to play', Blue, b3x, b3y)                        
        else:            
            introduction_button = Button('How to play', Orange, b3x, b3y)

        play_button.display()
        exit_button.display()
        introduction_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                bgm_sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()
                os._exit(0)
                break

            if exit_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                os._exit(0)
                break

            if introduction_button.check_click(pygame.mouse.get_pos()):
                bgm_sound.stop()
                How_to_play.How_screen()
                os._exit(0)
                break            
Firstscreen()
