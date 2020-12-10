# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: CHAO CUI, HAO WU, NANDI GUO
"""
import pygame,os,Game_Modes,Start_Screen


Orange = (119,0,255)
White = (255,255,255)
Blue = (0,238,255)
Width,Height = (781,482)


def Con_Screen():
    global screen,font
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))  
    pygame.display.set_caption("Congratulation!")
    background = pygame.image.load("Images/Backgrounds/Congratulation_1.png")
    screen.blit(background, (0,0))
    cong = pygame.mixer.Sound("Sounds/happy.mp3")
    cong.play()
    
    b1x,b1y=670,400
    back_button = Start_Screen.Button('Back', Orange, b1x, b1y)
    back_button.display()
    pygame.display.update()
    
    while True:
        if not back_button.check_click(pygame.mouse.get_pos()):                
            pygame.mixer.music.play()
            
        if back_button.check_click(pygame.mouse.get_pos()):              
            back_button = Start_Screen.Button('Back', Blue, b1x, b1y)                        
        else:            
            back_button = Start_Screen.Button('Back', Orange, b1x, b1y)

        back_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        os._exit(0)

        if pygame.mouse.get_pressed()[0]:            
                         
            if back_button.check_click(pygame.mouse.get_pos()):
                cong.stop()
                Start_Screen.Firstscreen()
                pygame.quit()                
                os._exit(0)
                break
