import pygame,sys,os
pygame.init()
Width,Height = 780,366
Orange = 255,89,0
White = 255,255,255
Blue = 0,238,255
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Start Screen")
background = pygame.image.load("Images/Start_Background.jpg")
how_to_play = pygame.image.load("Images/555.png")
font = pygame.font.Font(pygame.font.get_default_font(), 32)
bgm_sound = pygame.mixer.Sound("Sounds/bgm1.mp3")
bgm_sound.play()


class Button():

    def __init__(self, text, color, x=None, y=None, **kwargs):

        self.surf = font.render(text, True, color)
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()

        if 'center_x' in kwargs and kwargs['center_x']:                    
            self.x = Width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'center_y' in kwargs and kwargs['center_y']:
            self.y = Height // 2 - self.HEIGHT // 2
        else:
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

def Secondscreen():
    screen2 = pygame.display.set_mode((Width, Height)) 
    screen2.blit(how_to_play, (0,0))

    pygame.display.set_caption("Game Introduction") 
    pygame.display.update()


def Firstscreen():
    b1x,b1y=None,90
    b2x,b2y=None,150 
    b3x,b3y=None,210
    #b4x,b4y=None,270
    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')

    def Ourname():
            global font
            aut = pygame.font.Font(pygame.font.get_default_font(), 15)
            author = aut.render('Creators: CHAO CUI, NANDI GUO, HAO WU\
                                                                    \
                        Version 1.0', True, White)
            screen.blit(author, (10, 340))

    title = font.render('CWG-RUNNING GAME', True, White)
    screen.blit(title, (Width//2 - title.get_width()//2, 10))

    play_button = Button('Play', Orange, b1x, b1y, center_x=True)
    exit_button = Button('Quit', Orange, b2x, b2y, center_x=True)
    introduction_button = Button('How to play', Orange, b3x, b3y, center_x=True)

    play_button.display()
    exit_button.display()
    introduction_button.display()
    Ourname()
    pygame.display.update()

    while True:

        if not (play_button.check_click(pygame.mouse.get_pos()) or\
            exit_button.check_click(pygame.mouse.get_pos()) or\
            introduction_button.check_click(pygame.mouse.get_pos())):
                pygame.mixer.music.play()

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', Blue, b1x, b1y, center_x=True)                        
        else:            
            play_button = Button('Play', Orange, b1x, b1y, center_x=True)
        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Quit', Blue, b2x, b2y, center_x=True)
        else:           
            exit_button = Button('Quit', Orange, b2x, b2y, center_x=True)

        if introduction_button.check_click(pygame.mouse.get_pos()):
            introduction_button = Button('How to play', Blue, b3x, b3y, center_x=True)                        
        else:            
            introduction_button = Button('How to play', Orange, b3x, b3y, center_x=True)

        play_button.display()
        exit_button.display()
        introduction_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                os.quit

        if pygame.mouse.get_pressed()[0]:

            if play_button.check_click(pygame.mouse.get_pos()):
                import Main_Game
                pygame.quit()
                break

            if exit_button.check_click(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
                os.quit
                break

            if introduction_button.check_click(pygame.mouse.get_pos()):            
                Secondscreen()
                #back_button = Button('Back', Orange, b4x, b4y, center_x=True)
                #back_button.display()

Firstscreen()