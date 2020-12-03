#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,random

# Global variables
Screen_Width = 1000
Screen_Height = 443
Jump_Speed = 6
Fps = 20
Distance = 0
Lives = 0
Scores = 0
Game_Over = False 

# The background of the game
class Game_Map() :
    def __init__(self,x,y,Background_Image) :
        self.x = x
        self.y = y
        self.Background_Image = Background_Image

    def Map_Move(self):
        if self.x < -(Screen_Width-10) :  
            self.x = 0   
        else:
            self.x -= 10  
        Screen.blit(pygame.image.load(os.path.join(self.Background_Image)).convert_alpha(), (self.x, self.y))

# The role of the game
class Game_Role():
    def __init__(self,Role_Image) :  
        self.rect = pygame.Rect(10,250,0,0)
        self.Role_Image = Role_Image
        self.Jump_Height = 120
        self.Jump_Start_Position = self.rect.y
        self.Jump_Control = False
        self.Image = pygame.image.load(self.Role_Image[0]).convert_alpha()
        self.rect.size = self.Image.get_size()
    def Jump(self):
        Jump_Sound.play()
        self.Jump_Control = True
    
    def Move(self) :   
        Screen.blit(self.Image , (self.rect.x, self.rect.y))
        if self.Jump_Control == True :
            self.rect.y -= Jump_Speed
            if self.rect.y <= self.Jump_Height :
                self.Jump_Control = False
        if self.Jump_Control == False and self.rect.y != self.Jump_Start_Position :
            self.rect.y += Jump_Speed
            if self.rect.y == self.Jump_Start_Position :
                return self.rect.y
# The barriers of the game
class Barriers() :
    def __init__(self,Barriers_Images) :
        self.rect = pygame.Rect(800, 260, 0, 0)  
        self.Barriers_Images = Barriers_Images
        Random_Number =  random.randint(0, 1)
        if Random_Number == 0 :  
            self.Image = pygame.image.load(self.Barriers_Images[0]).convert_alpha()
        else:
            self.Image = pygame.image.load(self.Barriers_Images[1]).convert_alpha()
        self.rect.size = self.Image.get_size()
    
    def Move(self) :
        self.rect.x -= 10
        Screen.blit(self.Image, (self.rect.x, self.rect.y))
        

# Initialising pygame
pygame.init()
pygame.mixer.init()
# The sounds of the game
Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
Game_Run_Sound = pygame.mixer.Sound("Sounds/Game_Run.mp3")
Game_Over = ""
# Creat the display with Screen_Width and Screen_Height
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
# Set the title of the game
pygame.display.set_caption("CWG's Game")
# The images of the game
Role_Image_Action = ["Images/Role_1.png"]
Barriers_Images = ["Images/Barrier_1.png","Images/Barrier_2.png"]

Role = Game_Role(Role_Image_Action)
Fps_Flash = pygame.time.Clock()
Bg = Game_Map(0,0,"Images/Game_Background.jpg")
# Show the score and distance on the left top
def Show(Text) :
    Font = pygame.font.SysFont(pygame.font.get_default_font(),40)
    surf = Font.render(Text,False,(0,0,0))
    Screen.blit(surf,(0,0))

def Get_Scores(a) :
    global Scores
    if a == 1 :
        Scores += 1
        a = 0
    return Scores  

Barriers_Time = 0 
Barriers_List = []
Game_Run_Sound.play(-1,0)

while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()# for the rest of the people with windows or Linux
            os._exit(0) # for Mac users.
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                Role.Jump()
    if Game_Over == False :   
        Distance  += 1  
        Bg.Map_Move()
        Role.Move()   
        if Barriers_Time >= 1000 :
            r=random.randint(0,100)
            if r <= 10 :
                Barrier = Barriers(Barriers_Images)
                Barriers_List.append(Barrier)
                Barriers_Time = 0
        for i in range(len(Barriers_List)) :
            Barriers_List[i].Move()  
            if pygame.sprite.collide_rect(Role,Barriers_List[i]) :
                Game_Over = True
            else :
                if(Barriers_List[i].rect.x + Barriers_List[i].rect.size[0]) <= Role.rect.size[0] :
                    Lives = 1
                    Get_Scores(Lives)
        Show(f"Distance = {Distance} , Scores = {Scores}")             
        Barriers_Time += 20                
        pygame.display.flip()      
        Fps_Flash.tick(Fps)
    