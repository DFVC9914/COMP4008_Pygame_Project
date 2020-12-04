# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: NANDI GUO
"""
import pygame,os,Main_Game

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

bgm2_sound = pygame.mixer.Sound("Sounds/Modes_Bgm.mp3")
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
    
    b1x,b1y=155,155
    b2x,b2y=550,155
    b3x,b3y=155,320
    b4x,b4y=510,320
    

    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    Easy,Normal,Hard,Ultimate = 'Easy','Normal','Hard','Coming soon'
    play_button = Button(Easy, White, b1x, b1y)
    play2_button = Button(Normal, White, b2x, b2y)
    play3_button = Button(Hard, White, b3x, b3y)
    play4_button = Button(Ultimate, White, b4x, b4y)
    
    play_button.display()
    play2_button.display()
    play3_button.display()
    play4_button.display()
    pygame.display.update() 
       
    while True:
        
        if not (play_button.check_click(pygame.mouse.get_pos()) or \
                play2_button.check_click(pygame.mouse.get_pos()) or \
                play3_button.check_click(pygame.mouse.get_pos()) or \
                play4_button.check_click(pygame.mouse.get_pos())):                
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
            
        if play4_button.check_click(pygame.mouse.get_pos()):              
            play4_button = Button(Ultimate, Blue, b4x, b4y)                        
        else:            
            play4_button = Button(Ultimate, White, b4x, b4y)
        
        play_button.display()
        play2_button.display()
        play3_button.display()
        play4_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
# =============================================================================
#                 Screen_Width = 890
#                 Screen_Height = 476
#                 Fps = 24
#                 Highest_y = 200
#                 Lowest_y = 370
# =============================================================================
                Main_Game.Game_Main(890,476,200,370,"Images/Game_Background.png","Sounds/Normal_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play2_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                Main_Game.Game_Main(890,476,180,370,"Images/Game_Background.png","Sounds/Normal_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play3_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
# =============================================================================
#                 Screen_Width = 850
#                 Screen_Height = 476
#                 Fps = 40
#                 Highest_y = 145
#                 Lowest_y = 305
# =============================================================================
                Main_Game.Game_Main(850,476,145,305,"Images/Road_Background.png","Sounds/Hard_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play4_button.check_click(pygame.mouse.get_pos()):
                pass
                
Modes_Screen()
