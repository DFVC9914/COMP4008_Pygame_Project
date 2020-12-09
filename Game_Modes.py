# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: NANDI GUO
"""
import pygame,os,Main_Game,How_to_play,Start_Screen

Orange = (119,0,255)
White = (255,255,255)
Blue = (0,238,255)
Width,Height = (780,366)
  
def Modes_Screen():
    global screen,font,Best_Score
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))  
    pygame.display.set_caption("Game Modes")
    background = pygame.image.load("Images/Backgrounds/Start2_Background.png")
    background1 = pygame.image.load("Images/Backgrounds/p.png")
    screen.blit(background, (0,0))
    bgm2_sound = pygame.mixer.Sound("Sounds/Modes_Bgm.mp3")
    bgm2_sound.play()
    b1x,b1y=155,155
    b2x,b2y=550,155
    b3x,b3y=155,320
    b4x,b4y=550,320
    b5x,b5y=350,165   
    if Main_Game.Scores <= 3 :
        screen.blit(background, (0,0))
    else :
        screen.blit(background1, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    Easy,Normal,Hard,Ultimate,Back = 'Easy','Normal','Hard','Locked','Back'
    play_button = Start_Screen.Button(Easy, White, b1x, b1y)
    play2_button = Start_Screen.Button(Normal, White, b2x, b2y)
    play3_button = Start_Screen.Button(Hard, White, b3x, b3y)
    play4_button = Start_Screen.Button(Ultimate, White, b4x, b4y)
    back_button = Start_Screen.Button(Back, Orange, b5x, b5y)
    
    play_button.display()
    play2_button.display()
    play3_button.display()
    play4_button.display()
    back_button.display()
    pygame.display.update() 
    Start_Screen.Show(screen,f"Best Score = {Main_Game.Scores}",0,0) 
    
    while True:  
        if not (play_button.check_click(pygame.mouse.get_pos()) or \
                play2_button.check_click(pygame.mouse.get_pos()) or \
                play3_button.check_click(pygame.mouse.get_pos()) or \
                play4_button.check_click(pygame.mouse.get_pos()) or\
                back_button.check_click(pygame.mouse.get_pos())):                
            pygame.mixer.music.play() 
             
        if play_button.check_click(pygame.mouse.get_pos()):              
            play_button = Start_Screen.Button(Easy, Blue, b1x, b1y)                        
        else:            
            play_button = Start_Screen.Button(Easy, White, b1x, b1y)
            
        if play2_button.check_click(pygame.mouse.get_pos()):              
            play2_button = Start_Screen.Button(Normal, Blue, b2x, b2y)                        
        else:            
            play2_button = Start_Screen.Button(Normal, White, b2x, b2y)
            
        if play3_button.check_click(pygame.mouse.get_pos()):              
            play3_button = Start_Screen.Button(Hard, Blue, b3x, b3y)                        
        else:            
            play3_button = Start_Screen.Button(Hard, White, b3x, b3y)
            
        if play4_button.check_click(pygame.mouse.get_pos()):              
            play4_button = Start_Screen.Button(Ultimate, Blue, b4x, b4y)                        
        else:            
            play4_button = Start_Screen.Button(Ultimate, White, b4x, b4y)
        
        if back_button.check_click(pygame.mouse.get_pos()):              
            back_button = Start_Screen.Button(Back, Blue, b5x, b5y)                        
        else:            
            back_button = Start_Screen.Button(Back, Orange, b5x, b5y)
            
        play_button.display()
        play2_button.display()
        play3_button.display()
        play4_button.display()
        back_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                Barriers = [["Images/Barriers/Barrier_Bottom_1_1.png","Images/Barriers/Barrier_Bottom_1_2.png","Images/Barriers/Barrier_Bottom_1_3.png","Images/Barriers/Barrier_Bottom_1_4.png","Images/Barriers/Barrier_Bottom_1_5.png"]\
                             ,["Images/Barriers/Barrier_Bottom_2_1.png","Images/Barriers/Barrier_Bottom_2_2.png","Images/Barriers/Barrier_Bottom_2_3.png","Images/Barriers/Barrier_Bottom_2_4.png","Images/Barriers/Barrier_Bottom_2_5.png"]\
                                 ,["Images/Barriers/Barrier_Top_1_1.png","Images/Barriers/Barrier_Top_1_2.png","Images/Barriers/Barrier_Top_1_3.png","Images/Barriers/Barrier_Top_1_4.png","Images/Barriers/Barrier_Top_1_2.png"]\
                                     ,["Images/Barriers/Barrier_Top_2_1.png","Images/Barriers/Barrier_Top_2_2.png","Images/Barriers/Barrier_Top_2_3.png","Images/Barriers/Barrier_Top_2_4.png","Images/Barriers/Barrier_Top_2_5.png"]]
                Gem = "Images/Barriers/Green.png"
# =============================================================================
#                 Easy
#                 Screen_Width = 890
#                 Screen_Height = 476
#                 Fps = 24
#                 Highest_y = 200
#                 Lowest_y = 370
# =============================================================================
                Main_Game.Game_Main(850,476,150,305,"Images/Backgrounds/Snow_Background.jpg","Sounds/Normal_Bgm.mp3",Barriers,Gem)
                pygame.quit()                
                os._exit(0)
                break
            
            if play2_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                Barriers = [["Images/Barriers/Normal_bot1_1.png","Images/Barriers/Normal_bot1_2.png","Images/Barriers/Normal_bot1_3.png","Images/Barriers/Normal_bot1_4.png","Images/Barriers/Normal_bot1_5.png"]\
                             ,["Images/Barriers/Normal_bot2_1.png","Images/Barriers/Normal_bot2_2.png","Images/Barriers/Normal_bot2_3.png","Images/Barriers/Normal_bot2_4.png","Images/Barriers/Normal_bot2_5.png"]\
                                 ,["Images/Barriers/Normal_top1_1.png","Images/Barriers/Normal_top1_2.png","Images/Barriers/Normal_top1_3.png","Images/Barriers/Normal_top1_4.png","Images/Barriers/Normal_top1_5.png"]\
                                     ,["Images/Barriers/Normal_top2_1.png","Images/Barriers/Normal_top2_2.png","Images/Barriers/Normal_top2_3.png","Images/Barriers/Normal_top2_4.png","Images/Barriers/Normal_top2_5.png"]]
                Gem = "Images/Barriers/Blue.png"
# =============================================================================
#                 Normal 
#                 Screen_Width = 890
#                 Screen_Height = 476
#                 Fps = 24
#                 Highest_y = 120
#                 Lowest_y = 370
# =============================================================================
                Main_Game.Game_Main(890,476,120,370,"Images/Backgrounds/Game_Background.png","Sounds/Normal_Bgm.mp3",Barriers,Gem)
                pygame.quit()                
                os._exit(0)
                break
            
            if play3_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                Barriers = [["Images/Barriers/Hard_bot1_1.png","Images/Barriers/Hard_bot1_2.png","Images/Barriers/Hard_bot1_3.png","Images/Barriers/Hard_bot1_4.png","Images/Barriers/Hard_bot1_5.png"]\
                             ,["Images/Barriers/Hard_bot1_1.png","Images/Barriers/Hard_bot2_2.png","Images/Barriers/Hard_bot1_3.png","Images/Barriers/Hard_bot1_4.png","Images/Barriers/Hard_bot1_5.png"]\
                                 ,["Images/Barriers/Hard_top1_1.png","Images/Barriers/Hard_top1_2.png","Images/Barriers/Hard_top1_3.png","Images/Barriers/Hard_top1_4.png","Images/Barriers/Hard_top1_5.png"]\
                                     ,["Images/Barriers/Hard_top2_1.png","Images/Barriers/Hard_top2_2.png","Images/Barriers/Hard_top2_3.png","Images/Barriers/Hard_top2_4.png","Images/Barriers/Hard_top2_5.png"]]
                Gem = "Images/Barriers/Red.png"
# =============================================================================
#                 Hard
#                 Screen_Width = 850
#                 Screen_Height = 476
#                 Fps = 40
#                 Highest_y = 120
#                 Lowest_y = 305
# =============================================================================
                Main_Game.Game_Main(850,476,120,305,"Images/Backgrounds/Road_Background.png","Sounds/Hard_Bgm.mp3",Barriers,Gem)
                pygame.quit()                
                os._exit(0)
                break
            
            if play4_button.check_click(pygame.mouse.get_pos()):

                if Main_Game.Scores < 3 :
                    Start_Screen.Show(screen,"Your scores are not enought!",b4x-50,b4y+20)                   
                else :
                    bgm2_sound.stop()
                    Barriers = [["Images/Barriers/Ultimate_bot1_1.png","Images/Barriers/Ultimate_bot1_2.png","Images/Barriers/Ultimate_bot1_3.png","Images/Barriers/Ultimate_bot1_4.png","Images/Barriers/Ultimate_bot1_5.png"]\
                             ,["Images/Barriers/Ultimate_bot2_1.png","Images/Barriers/Ultimate_bot2_2.png","Images/Barriers/Ultimate_bot2_3.png","Images/Barriers/Ultimate_bot2_4.png","Images/Barriers/Ultimate_bot2_5.png"]\
                                 ,["Images/Barriers/Ultimate_top1_1.png","Images/Barriers/Ultimate_top1_2.png","Images/Barriers/Ultimate_top1_3.png","Images/Barriers/Ultimate_top1_4.png","Images/Barriers/Ultimate_top1_5.png"]\
                                     ,["Images/Barriers/Ultimate_top2_1.png","Images/Barriers/Ultimate_top2_2.png","Images/Barriers/Ultimate_top2_3.png","Images/Barriers/Ultimate_top2_4.png","Images/Barriers/Ultimate_top2_5.png"]]
                    Gem = "Images/Barriers/Yellow.png"
                    Main_Game.Game_Main(880,476,145,320,"Images/Backgrounds/Red_Background.png","Sounds/Hard_Bgm.mp3",Barriers,Gem)
                    pygame.quit()                
                    os._exit(0)
                    break
                
            if back_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()                
                How_to_play.How_screen()
                pygame.quit()                
                os._exit(0)
                break
                    

