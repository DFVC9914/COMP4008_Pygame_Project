#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,sys,random

Images_Path = os.getcwd()
# Global variables
Screen_Width = 1000
Screen_Height = 443
Fps = 20

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
    def __init__(self,Role_Image) :  
        self.rect=pygame.Rect(10,250,0,0)
        self.Role_Image = Role_Image
        self.Jump_Height = 150
        self.Jump_Start_Position = 250
        self.Jump_Control = False
        Screen.blit(pygame.image.load(os.path.join(self.Role_Image[0])).convert_alpha(), (self.rect.x,self.rect.y))
        pygame.display.flip()
    
    def Jump(self):
        Jump_Sound.play()
        self.Jump_Control = True
    
    def Move(self) :   
        Screen.blit(pygame.image.load(os.path.join(self.Role_Image[0])).convert_alpha(), (self.rect.x, self.rect.y))
        if self.Jump_Control == True:
            self.rect.y -= 5
            if self.rect.y == self.Jump_Height :
                self.Jump_Control = False
        if self.Jump_Control == False and self.rect.y != self.Jump_Start_Position :
            self.rect.y += 5
            if self.rect.y == self.Jump_Start_Position :
                return self.rect.y

class Barriers() :
    def __init__(self,Barriers_Images):
        self.rect = pygame.Rect(800, 260, 0, 0)  
        self.Barriers_Images = Barriers_Images
        Random_Number =  random.randint(0, 1)
        if Random_Number == 0 :  
            self.Image = pygame.image.load(self.Barriers_Images[0]).convert_alpha()
        else:
            self.Image = pygame.image.load(self.Barriers_Images[1]).convert_alpha()

    def Move(self):
        self.rect.x -= 10
        Screen.blit(self.Image, (self.rect.x, self.rect.y))
        
# Initialising pygame
pygame.init()
pygame.mixer.init()
# The sounds of the game
Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
Game_Run_Sound = pygame.mixer.Sound("Sounds/Game_Run.mp3")
# creating the display with WIDTH and HEIGHT
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
# Set the title of the game
pygame.display.set_caption("CWG's Game")


Role_Image_Action = ["Images/222.png"]
Barriers_Images = ["Images/Barrier_1.png","Images/Barrier_2.png"]
Role = Game_Role(Role_Image_Action)
Fps_Flash = pygame.time.Clock()
Bg = Game_Map(0,0,"Images/Game_Background.jpg")


Barriers_Time = 0 
List = []
Game_Run_Sound.play()
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
                
    if Barriers_Time>=1000:
        r=random.randint(0,100)
        if r == 70:
            Barrier = Barriers(Barriers_Images)
            List.append(Barrier)
            Barriers_Time = 0
    for i in range(len(List)):
        List[i].Move()  # 出现的障碍物移动
    Barriers_Time += 20                
    pygame.display.flip()      
    Fps_Flash.tick(Fps)