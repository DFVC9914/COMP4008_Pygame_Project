# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:09:30 2020

@author: 90730
"""

import pygame,sys,os
pygame.init()
Width,Height = (780,366)
Orange = (255,89,0)
White = (255,255,255)
Blue = (0,238,255)
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("How_to_play")
background = pygame.image.load("Images/555.png")
font = pygame.font.Font(pygame.font.get_default_font(), 25)
screen.blit(background, (0,0))
pygame.display.update()

class Button():
    
    def __init__(self, text, color, x=None, y=None, **kwargs):

        self.surf = font.render(text, True, color)
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()
    
        if 'center_x' in kwargs and kwargs['center_x']:                    
            self.x = Width // 2 - self.WIDTH // 2
        else:
            self.x = x
    
        if 'center_y' in kwargs and kwargs['center_y']:
            self.y = Height // 2 - self.HEIGHT // 2
        else:
            self.y = y
    
    def display(self):
    	screen.blit(self.surf, (self.x, self.y))
    
    def check_click(self, position):  
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT
        
        if x_match and y_match:
            return True
        else:
            return False
        
def How_screen():
    b1x,b1y=None,5

    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')

    title = font.render('CWG-RUNNING GAME', True, White)
    screen.blit(title, (Width//2 - title.get_width()//2, 10))
    
    play_button = Button('Start Game', Orange, b1x, b1y, center_x=True)
    play_button.display()
    pygame.display.update() 
       
    while True:
        
        if not (play_button.check_click(pygame.mouse.get_pos())):
                
            pygame.mixer.music.play()
              
        if play_button.check_click(pygame.mouse.get_pos()):  
            
            play_button = Button('Start Game', Blue, b1x, b1y, center_x=True) 
                       
        else:            
            play_button = Button('Start Game', Orange, b1x, b1y, center_x=True)
        
        play_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    os.quit
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):
                
                import Main_Game.py
                pygame.quit()
                sys.exit()
                os.quit
                break
How_screen()
