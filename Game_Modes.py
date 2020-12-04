# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: NANDI GUO
"""
import pygame,sys,os
pygame.init()
Width,Height = (780,366)
Orange = (119,0,255)
White = (255,255,255)
Blue = (0,238,255)
screen = pygame.display.set_mode((Width, Height))

pygame.display.set_caption("Game Modes")
background = pygame.image.load("Images/Start2_Background.png")
font = pygame.font.Font(pygame.font.get_default_font(), 25)
screen.blit(background, (0,0))
pygame.display.update()

bgm2_sound = pygame.mixer.Sound("Sounds/bgm2.mp3")
bgm2_sound.play()

class Button():
    
    def __init__(self, text, color, x=None, y=None):

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
        
        if x_match and y_match:
            return True
        else:
            return False
        
def Modes_Screen():
    
    b1x,b1y=70,250
    b2x,b2y=340,250
    b3x,b3y=620,250

    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    Easy,Normal,Hard='Easy','Normal','Hard'
    play_button = Button(Easy, White, b1x, b1y)
    play2_button = Button(Normal, White, b2x, b2y)
    play3_button = Button(Hard, White, b3x, b3y)
    
    play_button.display()
    play2_button.display()
    play3_button.display()
    pygame.display.update() 
       
    while True:
        
        if not (play_button.check_click(pygame.mouse.get_pos()) or \
                play2_button.check_click(pygame.mouse.get_pos() or \
                play3_button.check_click(pygame.mouse.get_pos()))):                
            pygame.mixer.music.play() 
             
        if play_button.check_click(pygame.mouse.get_pos()):              
            play_button = Button(Easy, Blue, b1x, b1y)                        
        else:            
            play_button = Button(Easy, White, b1x, b1y)
            
        if play2_button.check_click(pygame.mouse.get_pos()):              
            play2_button = Button(Normal, Blue, b2x, b2y)                        
        else:            
            play2_button = Button(Normal, White, b2x, b2y)
            
        if play3_button.check_click(pygame.mouse.get_pos()):              
            play3_button = Button(Hard, Blue, b3x, b3y)                        
        else:            
            play3_button = Button(Hard, White, b3x, b3y)
        
        play_button.display()
        play2_button.display()
        play3_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    os.quit
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                import Main_Game
                pygame.quit()                
                os.quit
                break
            
            if play2_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                import Normal_Level
                pygame.quit()                
                os.quit
                break
            
            if play3_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                import Hard_Level
                pygame.quit()                
                os.quit
                break
Modes_Screen()