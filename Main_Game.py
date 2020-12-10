#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: Chao Cui
"""

import pygame,os,random,Game_Modes,Start_Screen,itertools 

# The background of the game
class Game_Map() :
    def __init__(self,x,y,Background_Image) :
        self.x = x
        self.y = y
        self.Background_Image = Background_Image

    def Map_Move(self):
        if self.x < -(Screen_Width-8) :  
            self.x = 0   
        else:
            self.x -= 8  
        Screen.blit(pygame.image.load(self.Background_Image).convert_alpha(),(self.x, self.y))

# The role of the game
class Game_Role():
    def __init__(self,Role_Image) :  
        self.rect = pygame.Rect(10,Lowest_y,0,0)
        self.Role_Image = Role_Image
        self.Jump_Height = Highest_y
        self.Jump_Start_Position = Lowest_y
        self.Jump_Control = False
        self.Image = (pygame.image.load(self.Role_Image[0]).convert_alpha()\
                      ,pygame.image.load(self.Role_Image[1]).convert_alpha()\
                          ,pygame.image.load(self.Role_Image[2]).convert_alpha()\
                              ,pygame.image.load(self.Role_Image[3]).convert_alpha()\
                                  ,pygame.image.load(self.Role_Image[4]).convert_alpha()\
                                     , pygame.image.load(self.Role_Image[5]).convert_alpha())
        self.rect.size = self.Image[0].get_size()
        self.rect.width -= 30
        self.rect.height -= 30
        self.Jump_Control_Twist = False
        self.jumpValue = 0
    
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
        if self.Jump_Start_Position <= self.rect.y :
            Screen.blit(self.Image[i],(self.rect.x, self.rect.y))  
        else  :
            Screen.blit(self.Image[5],(self.rect.x, self.rect.y))
            
# The barriers of the game
class Barriers() :
    def __init__(self,Barriers_Images) :   
        self.rect = pygame.Rect(800,0,0,0)  
        self.Barriers_Images = Barriers_Images
        Random_Number =  random.randint(0,3)
        if Random_Number == 0 :         
            self.Image = (pygame.image.load(self.Barriers_Images[0][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[0][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[0][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[0][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[0][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = (pygame.image.load(self.Barriers_Images[1][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[1][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[1][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[1][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[1][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 2 :
            self.Image = (pygame.image.load(self.Barriers_Images[2][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[2][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[2][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[2][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[2][4]).convert_alpha())
            self.rect.y = Highest_y 
        elif Random_Number == 3 :
            self.Image = (pygame.image.load(self.Barriers_Images[3][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[3][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[3][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[3][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[3][4]).convert_alpha())
            self.rect.y = Highest_y 
        self.rect.size = self.Image[0].get_size()
        self.rect.width -= 60
        self.rect.height -= 50
        self.Barriers_Index = itertools.cycle([0,1,2,3,4])
        self.Score = 1
 
    def Move(self) :
        self.rect.x -= 8
        
    def Draw_Barriers(self) :
        Index = next(self.Barriers_Index)
        Screen.blit(self.Image[Index], (self.rect.x, self.rect.y))
    
class Gems():
    def __init__(self,Gems_Images) :   
        self.rect = pygame.Rect(750,0,0,0)  
        self.Gems_Images = Gems_Images
        self.active = True  
        Random_Number =  random.randint(0,1)
        if Random_Number == 0 :         
            self.Image = pygame.image.load(self.Gems_Images).convert_alpha()
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = pygame.image.load(self.Gems_Images).convert_alpha()
            self.rect.y = Highest_y + 10
        self.rect.size = self.Image.get_size()
        self.Score = 1   
        
    def Draw_Gem(self) :
        if self.Gems_Images == "Images/Barriers/Nothing_1.png" :
            pass
        else :
            Screen.blit(self.Image, (self.rect.x, self.rect.y))
    
    def Move(self) :
        self.rect.x -= 8
    
    def getScore(self):
        Temporary_Score = self.Score
        self.Score = 0
        return Temporary_Score

def Game_Main(P_Fps,P_Screen_Width,P_Screen_Height,P_Highest_y,P_Lowest_y,P_Background,P_Background_Sound,P_Barriers_Images,P_Gems_Images,Mode):
    global  Screen_Width,Screen_Height,Jump_Speed,Highest_y,Lowest_y,Jump_Sound,\
        Game_Run_Sound,Get_Score,Screen,Background_Images,Role,Barriers_List
    Screen_Width = P_Screen_Width
    Screen_Height = P_Screen_Height
    Highest_y = P_Highest_y
    Lowest_y = P_Lowest_y    
    # Local variables
    Jump_Speed = 8  
    Gems_number = 0
    Distance = 0
    Gem_Lists = []
    Barriers_Time = 0 
    Barriers_List = []
    Gem_Time = 0
    Role_Image_Time = -1
    # Initialising pygame
    pygame.init()
    pygame.mixer.init() 
    # The sounds of the game
    Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
    Game_Run_Sound = pygame.mixer.Sound(P_Background_Sound)
    Get_Score = pygame.mixer.Sound("Sounds/Get_Score.wav")
    Dead_Bgm = pygame.mixer.Sound("Sounds/Dead.mp3")
    # The images of the game
    Role_Image_Action = ["Images/Roles/Role_Run_1.png","Images/Roles/Role_Run_2.png","Images/Roles/Role_Run_3.png"\
                         ,"Images/Roles/Role_Run_4.png","Images/Roles/Role_Run_5.png","Images/Roles/Role_Jump.png"]
    Game_Over_Image = pygame.image.load("Images/Game_Over.png").convert_alpha()
    Return_Button = Start_Screen.Button("Play Again", (255,255,255), Screen_Width/2 , Lowest_y)
    # Creat the display with Screen_Width and Screen_Height
    Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
    # Set the title of the game
    pygame.display.set_caption("CWG's Game")   
    Role = Game_Role(Role_Image_Action)
    Fps_Flash = pygame.time.Clock()
    Bg = Game_Map(0,0,P_Background)  
    Game_Run_Sound.play(-1,0)
    Game_Over = False  
    
    while True : 
        if Game_Over == False : 
            Distance += 1
            Role_Image_Time += 1
            Bg.Map_Move()
            Role.Action_Move()  
            if Role_Image_Time == 0 :
                Role.Draw_Role(0)
            elif Role_Image_Time == 1 :
                Role.Draw_Role(1)
            elif Role_Image_Time == 2 :
                Role.Draw_Role(2)
            elif Role_Image_Time == 3 :
                Role.Draw_Role(3)
            elif Role_Image_Time == 4 :
                Role.Draw_Role(4)
                Role_Image_Time = -1         
            #########################################        
            if Gem_Time >= 800 :
                r=random.randint(0,100)
                if r <= 10 :
                    Gem = Gems(P_Gems_Images) 
                    Gem_Lists += [Gem]
                    Gem_Time = 0
                    
            for i in range(len(Gem_Lists)) :   
                Gem_Lists[i].Move() 
                Gem_Lists[i].Draw_Gem()
                if pygame.sprite.collide_rect(Role,Gem_Lists[i]):
                    Get_Score.play()
                    Gem_Lists[i] = Gems("Images/Barriers/Nothing_1.png")
                    Gems_number += Gem_Lists[i].getScore()
                    Start_Screen.Show(Screen,"Gem + 1",Role.rect.x + 15 , Role.rect.y - 10)  
                      
            if Barriers_Time >= 1000 :
                r=random.randint(0,100)
                if r <= 40 :
                    Barrier = Barriers( P_Barriers_Images)
                    Barriers_List += [Barrier]
                    Barriers_Time = 0              
            for i in range(len(Barriers_List)) :
                Barriers_List[i].Move() 
                Barriers_List[i].Draw_Barriers()              
                if pygame.sprite.collide_rect(Role,Barriers_List[i]) :
                    Game_Over = True
                    Game_Run_Sound.stop()
                    Dead_Bgm.play()
                    Start_Screen.Show(Screen,f"You ran {Distance} meters and got {Gems_number} gems",0,0)
                    if Mode == 0 :
                        Game_Modes.Gem_easy += Gems_number
                    elif Mode == 1 :
                        Game_Modes.Gem_normal += Gems_number
                    elif Mode == 2 :
                        Game_Modes.Gem_hard += Gems_number
                    elif Mode == 3 :
                        Game_Modes.Gem_ultimate += Gems_number
                    Screen.blit(Game_Over_Image,((Screen_Width/2 - Game_Over_Image.get_width()/2),(Screen_Height/2 - Game_Over_Image.get_height()/2)))
                    pygame.draw.rect(Screen, (0,0,0),[Screen_Width/2, Lowest_y, 130, 40])
                    Return_Button.display()
                    break    
        #########################################                
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit() # For the rest of the people with windows or Linux
                os._exit(0) # For Mac users.
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                    Role.Jump()                   
        ######################################
        if pygame.mouse.get_pressed()[0]:            
            if Return_Button.check_click(pygame.mouse.get_pos()):
                Game_Run_Sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()                
                os._exit(0)    
        Barriers_Time += 20
        Gem_Time += 30            
        pygame.display.flip()      
        Fps_Flash.tick(P_Fps)
        
