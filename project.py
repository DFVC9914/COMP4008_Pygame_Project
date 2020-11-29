#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame
import os
Images_Path = os.getcwd()
# Global variables
Screen_Width = 1000
Screen_Height = 443
Fps = 20


#    
# The background of the game
class Game_Map() :
    def __init__(self,x,y,Background_Image):
        self.x = x
        self.y = y
        self.Background_Image = Background_Image

    def Map_Move(self):
        if self.x < -(Screen_Width-10) :  
            self.x = 0   
        else:
            self.x -= 10  
        Screen.blit(pygame.image.load(os.path.join(self.Background_Image)).convert_alpha(), (self.x, self.y))

#  
class Game_Role():
    def __init__(self,x,y,Role_Image) :  
        # self.rect=pygame.Rect(0,0,0,0)
        self.x = x
        self.y = y
        self.Role_Image = Role_Image
        self.Jump_Height = 150
        self.Jump_Control = False
        Screen.blit(pygame.image.load(os.path.join(self.Role_Image[0])).convert_alpha(), (self.x, self.y))
        pygame.display.flip()
    
    def Jump(self):
        Jump_Sounds.play()
        self.Jump_Control = True
    
    def Move(self) :   
        Screen.blit(pygame.image.load(os.path.join(self.Role_Image[0])).convert_alpha(), (self.x, self.y))
        if self.Jump_Control == True:
            self.y -= 5
            if self.y == self.Jump_Height :
                self.Jump_Control = False
        if self.Jump_Control == False and self.y != 250 :
            self.y += 5
            if self.y == 250 :
                return self.y
# Initialising pygame
pygame.init()
pygame.mixer.init()
# The sounds of the game
Jump_Sounds = pygame.mixer.Sound("Sounds/Jump.mp3")
# creating the display with WIDTH and HEIGHT
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
# Set the title of the game
pygame.display.set_caption("CWG's Game")


Role_Image_Action = ["Images/222.png"]
Role = Game_Role(10,250,Role_Image_Action)
Fps_Flash = pygame.time.Clock()
Bg = Game_Map(0,0,"Images/background.jpg")

event = pygame.event.poll()
while True:
    Bg.Map_Move()
    Role.Move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()# for the rest of the people with windows or Linux
            os._exit(0) # for Mac users.
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                Role.Jump()
    pygame.display.flip()      
    Fps_Flash.tick(Fps)