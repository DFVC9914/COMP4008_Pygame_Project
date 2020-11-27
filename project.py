import pygame,os,sys
print("hello world")
print("起始测试，Window10可以运行")

speed = [1,0]
Background = 255,255,255
width,height = 1200,400
FPS = 300

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('pygame test')

ball = pygame.image.load('konglong.gif','r')
ballrect = ball.get_rect()

pygame.mixer.init()
pygame.mixer.music.load('Time.mp3')
pygame.mixer.music.play()

fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            os.exit
                
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left<0 or ballrect.right > width:     
        speed[0] =-speed[0]
        
  
    screen.fill(Background)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(FPS)