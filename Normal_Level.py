#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,random
# Global variables
Screen_Width = 890
Screen_Height = 476
Jump_Speed = 8
Fps = 24
Distance = 0
Highest_y = 145
Lowest_y = 370
Scores = 0
Barriers_Time = 0 
Barriers_List = []
Run_State = False

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
        Screen.blit(pygame.image.load(self.Background_Image).convert_alpha(),(self.x, self.y))

# The role of the game
class Game_Role():
    def __init__(self,Role_Image) :  
        self.rect = pygame.Rect(10,Lowest_y,0,0)
        self.Role_Image = Role_Image
        self.Jump_Height = Highest_y
        self.Jump_Start_Position = Lowest_y
        self.Jump_Control = False
        self.Image = (pygame.image.load(self.Role_Image[0]).convert_alpha(),pygame.image.load(self.Role_Image[1]).convert_alpha(),pygame.image.load(self.Role_Image[2]).convert_alpha())
        self.rect.size = self.Image[0].get_size()
        self.Jump_Control_Twist = False
        # self.Index = 0
        # self.IndexGen = itertools.cycle([0, 1, 2])
    
    def Jump(self):
        Jump_Sound.play()
        self.Jump_Control = True
    
    def Action_Move(self) : 
        if self.Jump_Control == True and self.Jump_Control_Twist == False :
            self.rect.y -= Jump_Speed
            if self.rect.y <= self.Jump_Height :
                self.Jump_Control = False
                self.Jump_Control_Twist = True
        elif self.Jump_Control_Twist == True :
            self.rect.y += (Jump_Speed - 2)
            if self.rect.y >= self.Jump_Start_Position :
                self.Jump_Control_Twist = False
            
    def Draw_Role(self,i) :
        # self.Index = next(self.IndexGen)
        if self.Jump_Start_Position <= self.rect.y :
            Screen.blit(self.Image[i],(self.rect.x, self.rect.y))  
        else  :
            Screen.blit(self.Image[2],(self.rect.x, self.rect.y))
            
# The barriers of the game
class Barriers() :
    def __init__(self,Barriers_Images) :   
        self.rect = pygame.Rect(800,0,0,0)  
        self.Barriers_Images = Barriers_Images
        Random_Number =  random.randint(0,3)
        if Random_Number == 0 :         
            self.Image = (pygame.image.load(self.Barriers_Images[0][0]).convert_alpha(),pygame.image.load(self.Barriers_Images[0][1]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = (pygame.image.load(self.Barriers_Images[1][0]).convert_alpha(),pygame.image.load(self.Barriers_Images[1][1]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 2 :
            self.Image = (pygame.image.load(self.Barriers_Images[2][0]).convert_alpha(),pygame.image.load(self.Barriers_Images[2][1]).convert_alpha())
            self.rect.y = Highest_y + 10
        elif Random_Number == 3 :
            self.Image = (pygame.image.load(self.Barriers_Images[3][0]).convert_alpha(),pygame.image.load(self.Barriers_Images[3][1]).convert_alpha())
            self.rect.y = Highest_y + 10
        self.rect.size = self.Image[0].get_size()
        self.Score = 1
 
    def Move(self) :
        self.rect.x -= 10
        
    def Draw_Barriers(self,i) :
        Screen.blit(self.Image[i], (self.rect.x, self.rect.y))
        
    def getScore(self):
        Temporary_Score = self.Score
        if Temporary_Score == 1 :
            Get_Score.play()
        self.Score = 0
        return Temporary_Score
                       
# Initialising pygame
pygame.init()
pygame.mixer.init()
# The sounds of the game
Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
Game_Run_Sound = pygame.mixer.Sound("Sounds/Normal_Bgm.mp3")
Get_Score = pygame.mixer.Sound("Sounds/Get_Score.wav")
Game_Over = ""
# Creat the display with Screen_Width and Screen_Height
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
# Set the title of the game
pygame.display.set_caption("CWG's Game")
# The images of the game
Role_Image_Action = ["Images/Role_Run_1.png","Images/Role_Run_2.png","Images/Role_Jump.png"]
Barriers_Images = [["Images/Barrier_Bottom_1.gif","Images/Barrier_Bottom_1.gif"],["Images/Barrier_Bottom_2_1.png","Images/Barrier_Bottom_2_2.png"],["Images/Barrier_Top_1_1.png","Images/Barrier_Top_1_2.gif"],["Images/Barrier_Top_2_1.png","Images/Barrier_Top_2_2.png"]]
Award_Item_Images = ["Images/Item_1.png","Images/Item_2.png"] 

Role = Game_Role(Role_Image_Action)
Fps_Flash = pygame.time.Clock()
Bg = Game_Map(0,0,"Images/Game_Background.png")
# Show the score and distance on the left top
def Show(Text,x,y) :
    Font = pygame.font.SysFont(pygame.font.get_default_font(),40)
    surf = Font.render(Text,False,(255,255,255))
    Screen.blit(surf,(x,y))


Game_Run_Sound.play(-1,0)
Game_Over = False 
while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()# for the rest of the people with windows or Linux
            os._exit(0) # for Mac users.
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                Role.Jump()
    if Game_Over == False :   
        Distance += 1
        Run_State = not Run_State
        Bg.Map_Move()
        Role.Action_Move()  
        if Run_State == True :
            Role.Draw_Role(0)
        else :
            Role.Draw_Role(1)
        if Barriers_Time >= 1000 :
            r=random.randint(0,100)
            if r <= 30 :
                Barrier = Barriers(Barriers_Images)
                Barriers_List += [Barrier]
                Barriers_Time = 0
        for i in range(len(Barriers_List)) :
            Barriers_List[i].Move()
            if Run_State == True :
                Barriers_List[i].Draw_Barriers(0)
            else :
                Barriers_List[i].Draw_Barriers(1)
            if pygame.sprite.collide_rect(Role,Barriers_List[i]) :
                Game_Over = True 
                Show("Dead",Screen_Width/2,Screen_Height/2)  
            elif (Barriers_List[i].rect.x + Barriers_List[i].rect.size[0]) < Role.rect.x :
                    Scores += Barriers_List[i].getScore()
    Show(f"Distance = {Distance} , Scores = {Scores}",0,0)             
    Barriers_Time += 20           
    pygame.display.flip()      
    Fps_Flash.tick(Fps)
    
