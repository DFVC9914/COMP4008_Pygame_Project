#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,random,Game_Modes


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

class Button(): 
    def __init__(self, text, color, x=None, y=None):
        font = pygame.font.SysFont(pygame.font.get_default_font(),40)
        self.surf = font.render(text, True, color)
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()   
        self.x = x    
        self.y = y
    
    def display(self):
    	Screen.blit(self.surf, (self.x, self.y))
    
    def check_click(self, position):  
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT
        
        if x_match and y_match:
            return True
        else:
            return False
        
# Show the score and distance on the left top
def Show(Text,x,y) :
    Font = pygame.font.SysFont(pygame.font.get_default_font(),40)
    surf = Font.render(Text,False,(255,255,255))
    Screen.blit(surf,(x,y))


def Game_Main(P_Screen_Width,P_Screen_Height,P_Highest_y,P_Lowest_y,P_Background,P_Background_Sound):
    global  Screen_Width,Screen_Height,Jump_Speed,Highest_y,Lowest_y,Jump_Sound,Game_Run_Sound,Get_Score,Screen,Background_Images
    Screen_Width = P_Screen_Width
    Screen_Height = P_Screen_Height
    Jump_Speed = 8  
    Highest_y = P_Highest_y
    Lowest_y = P_Lowest_y    
    # Local variables
    Fps = 24
    Distance = 0
    Scores = 0
    Barriers_Time = 0 
    Barriers_List = []
    Run_State = False
    Return_Button = Button("Return", (255,255,255), Screen_Width, Screen_Height) 
    # Initialising pygame
    pygame.init()
    pygame.mixer.init() 
    # The sounds of the game
    Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
    Game_Run_Sound = pygame.mixer.Sound(P_Background_Sound)
    Get_Score = pygame.mixer.Sound("Sounds/Get_Score.wav")
    Game_Over = ""   
    # The images of the game
    Role_Image_Action = ["Images/Roles/Role_Run_1.png","Images/Roles/Role_Run_2.png","Images/Roles/Role_Jump.png"]
    Barriers_Images = [["Images/Barriers/Barrier_Bottom_1.gif","Images/Barriers/Barrier_Bottom_1.gif"],["Images/Barriers/Barrier_Bottom_2_1.png","Images/Barriers/Barrier_Bottom_2_2.png"],["Images/Barriers/Barrier_Top_1_1.png","Images/Barriers/Barrier_Top_1_2.gif"],["Images/Barriers/Barrier_Top_2_1.png","Images/Barriers/Barrier_Top_2_2.png"]]
    Background = P_Background
    # Creat the display with Screen_Width and Screen_Height
    Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
    # Set the title of the game
    pygame.display.set_caption("CWG's Game")   
    Role = Game_Role(Role_Image_Action)
    Fps_Flash = pygame.time.Clock()
    Bg = Game_Map(0,0,Background)
    Return_Button.display()
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
                    
        if pygame.mouse.get_pressed()[0]:            
            if Return_Button.check_click(pygame.mouse.get_pos()):
                Game_Modes.Modes_Screen()
                pygame.quit()                
                os._exit(0)
            
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
        