# Austin - Mario Animation
import pygame, sys, time
from pygame.locals import *

pygame.init()


fps = 40 # 30 fps
fpsClock = pygame.time.Clock() # clock

windowx = 1000 # window dimensions
windowy = 600

surface = pygame.display.set_mode((windowx, windowy), 0, 32)
pygame.display.set_caption("Mushroom Madness") #Mushroom Madnesssss!!!!

WHITE = (255, 255, 255)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
darkgreen = (0,128,0)
maroon = (128,0,0)
coolblue = (42,191,199)
darkpurple = (150,9,129)
gold = (250,214,7)
brown = (130,50,10)

#load all images
mariostareImg = pygame.image.load("mario_stare.png")
backgroundImg = pygame.image.load("new_mario_background.png")
mushroomImg = pygame.image.load("mario_mushroom.png")
marioImg = pygame.image.load("mario_hammer.png")
skullImg = pygame.image.load("skull_death.png")
#load all sounds
deathtrack = pygame.mixer.Sound("endgame_mariotrack_converted.wav")
cointrack = pygame.mixer.Sound("coin_mariotrack_converted.wav")
maintrack = pygame.mixer.Sound("main_mariotrack_converted.wav")















#in-game background
def draw_background():
   surface.blit(backgroundImg,(0,0))   
     

#start up creen
def start_screen():
   startscreen = True
   while startscreen == True:
      #create new screen with title
      pygame.draw.polygon(surface, gold,((0,0),(1000,0),(1000,600),(0,600)))
      titleFont = pygame.font.Font('freesansbold.ttf',40)
      titleSurface = titleFont.render('Mushroom Madness',True,red)
      titleRect = titleSurface.get_rect()
      titleRect.center = (500,200)
      surface.blit(titleSurface,titleRect)
      #extra images on start screen
      surface.blit(mariostareImg, (780,50))
      surface.blit(mushroomImg, (80, 100))
      #create a start button with text and rect
      start_button_Font = pygame.font.Font('freesansbold.ttf',21)
      start_button_surface = start_button_Font.render('Start',True,red)
      start_button_rect = (475,400,50,25)
      surface.blit(start_button_surface,start_button_rect)
      #create an exit button with text and rect
      exit_button_Font = pygame.font.Font('freesansbold.ttf',21)
      exit_button_surface = start_button_Font.render('Exit',True,red)
      exit_button_rect = (475,500,50,25)
      surface.blit(exit_button_surface,exit_button_rect)
      #get mouse position to see if hovering over buttons
      mousepos = pygame.mouse.get_pos()
      #if hovering over start button, show white button for player interaction
      if 475 < mousepos[0] < 525 and 400 < mousepos[1] < 425:
         pygame.draw.rect(surface,WHITE,(475,400,50,25))
         surface.blit(start_button_surface,start_button_rect)
      #if not hovering over start button, show black button
      else:
         pygame.draw.rect(surface,black,(475,400,50,25))
         surface.blit(start_button_surface,start_button_rect)
      #if hovering over exit button, show white button for player interaction
      if 475 < mousepos[0] < 525 and 500 < mousepos[1] < 525:
         pygame.draw.rect(surface,WHITE,(475,500,50,25))
         surface.blit(exit_button_surface,exit_button_rect)
      #if not hovering over exit button, show black button
      else:
         pygame.draw.rect(surface,black,(475,500,50,25))
         surface.blit(exit_button_surface,exit_button_rect)


      for event in pygame.event.get():

         if event.type == QUIT:

            pygame.quit()

            sys.exit()
         
         elif event.type == pygame.MOUSEBUTTONDOWN:
            #if player clicks in the start button location, advance into game
            if 475 < mousepos[0] < 525 and 400 < mousepos[1] < 450:
               stage_one()
            #if player clicks in the exit button location, exit game
            elif 475 < mousepos[0] < 525 and 500 < mousepos[1] < 550:
               pygame.quit()
               sys.exit()
             
             
          
       
             

      pygame.display.update()
      fpsClock.tick(fps)   
   
     
#if mario eats the mushroom    
def mush_death():
   #stop the main mario track
   maintrack.stop()
   deathscreen = True
   while deathscreen == True:
      #create a new screen for death, with a skull background image
      pygame.draw.polygon(surface, red,((0,0),(1000,0),(1000,600),(0,600)))
      surface.blit(skullImg, (320,90))
      #text ("YOU DIED!")
      titleFont = pygame.font.Font('freesansbold.ttf',40)
      titleSurface = titleFont.render('YOU DIED!',True,red)
      titleRect = titleSurface.get_rect()
      titleRect.center = (500,200)
      surface.blit(titleSurface,titleRect)

      #create a restart button with rect
      start_button_Font = pygame.font.Font('freesansbold.ttf',14)
      start_button_surface = start_button_Font.render('Restart',True,red)
      start_button_rect = (475,400,50,25)
      surface.blit(start_button_surface,start_button_rect)
      #create an exit button with rect
      exit_button_Font = pygame.font.Font('freesansbold.ttf',21)
      exit_button_surface = start_button_Font.render('Exit',True,red)
      exit_button_rect = (475,500,50,25)
      surface.blit(exit_button_surface,exit_button_rect)
      #get mouse position to see if player is hovering over a button
      mousepos = pygame.mouse.get_pos()
      #if hovering over restart button, color change to white
      if 475 < mousepos[0] < 525 and 400 < mousepos[1] < 425:
         pygame.draw.rect(surface,WHITE,(475,400,50,25))
         surface.blit(start_button_surface,start_button_rect) 
      #color stays black
      else:
         pygame.draw.rect(surface,black,(475,400,50,25))
         surface.blit(start_button_surface,start_button_rect)
      #if hovering over exit button, color change to white
      if 475 < mousepos[0] < 525 and 500 < mousepos[1] < 525:
         pygame.draw.rect(surface,WHITE,(475,500,50,25))
         surface.blit(exit_button_surface,exit_button_rect)
      #color stays black
      else:
         pygame.draw.rect(surface,black,(475,500,50,25))
         surface.blit(exit_button_surface,exit_button_rect)

      for event in pygame.event.get():

         if event.type == QUIT:

            pygame.quit()

            sys.exit()
         
         elif event.type == pygame.MOUSEBUTTONDOWN:
            #if player clicks on restart button, game restarts at stage one
            if 475 < mousepos[0] < 525 and 400 < mousepos[1] < 450:
               stage_one()
            #if player clicks on exit button, game exits
            elif 475 < mousepos[0] < 525 and 500 < mousepos[1] < 550:
               pygame.quit()
               sys.exit()
             
             
          
       
             

      pygame.display.update()
      fpsClock.tick(fps)




#stage one
def stage_one():
   #play main mario track in-game
   maintrack.play(3)
   initialmushroomx = 750 #mushroom starting x
   initialmushroomy = 400 #mushroom starting y

   mushroom_rectx = initialmushroomx #set mushroom rect coords equal to mushroom
   mushroom_recty = initialmushroomy
   #create the mushroom rect
   mushroom_rect = pygame.Rect(mushroom_rectx,mushroom_recty,92,92)
   #start the mushroom speed at 0
   move_mushroomx = 0
   move_mushroomy = 0
   #mushroom x value begins at 750
   mushroomx = initialmushroomx
   #mushroom y value begins at 400
   mushroomy = initialmushroomy
   #total coins collected starts at 0
   s1totalcoins = 0
### Coin 1 ####
   coin1 = True
   coin1Img = pygame.image.load("mario_coin.png") # load coin pic 25x25
   coin1x = 30 #x value
   coin1y = 550#y value
   coin1_rect = pygame.Rect(coin1x, coin1y, 25, 25)
###############

### Coin 2 ####
   coin2 = True
   coin2Img = coin1Img
   coin2x = 30 #x value
   coin2y = 25 #y value
   coin2_rect = pygame.Rect(coin2x, coin2y, 25, 25)
###############

### Coin 3 ####
   coin3 = True
   coin3Img = coin1Img
   coin3x = 945 #x value
   coin3y = 25 #y value
   coin3_rect = pygame.Rect(coin3x, coin3y, 25, 25)

### Coin 4 ####
   coin4 = True
   coin4Img = coin1Img
   coin4x = 488 #x value
   coin4y = 288 #y value
   coin4_rect = pygame.Rect(coin4x, coin4y, 25, 25)

   #useless boundary rect
   boundary_rect = pygame.Rect(80, 80, 820, 420)
   
   initialmariox = 250 #mario x value begins at 250
   initialmarioy = 250 #mario y value begins at 250
   
   mariox = initialmariox #initial x
   marioy = initialmarioy #initial y 


   mariochangex = 10 #mario x value speed
   mariochangey = 10 #mario y value speed

   mario_rect = pygame.Rect(initialmariox,initialmarioy,142,192) #mario rect
   #initial coin, mario, and mushroom image blitting
   surface.blit(coin1Img, (coin1x, coin1y))
   surface.blit(coin2Img, (coin2x, coin2y))
   surface.blit(coin3Img, (coin3x, coin3y))
   surface.blit(coin4Img, (coin4x, coin4y))
   surface.blit(marioImg, (mariox, marioy)) # blit mario image
   surface.blit(mushroomImg, (mushroomx, mushroomy)) # blit mushroom image 
   

   while True: # game logic
      #redraw background in-game
      draw_background()
    
# when animation begins, mario begins moving at the initial speed and direction
# assigned by the variables (mariochangex, mariochangey) from the initial x and
# y coordinates given by the variables (mariox, marioy).
      mariox += mariochangex 
      marioy += mariochangey
# if mario image hits the bottom of the window (400pi) or the top of the window
# (0pi), the variable (mariochangey) changes sign, essentially sending mario
# the opposite direction on the y axis. 
      if marioy > 399 or marioy < 1:
         mariochangey = mariochangey * -1
# if mario image hits the right side of the window (1000pi) or the left side of
# window (0pi), the variable (mariochangex) changes sign, essentially sending
# mario the opposite direction on the x axis.
      if mariox > 849 or mariox < 1:
         mariochangex = mariochangex * -1
# once the variables change for mario, then blit his image in the new
# location
      surface.blit(marioImg, (mariox, marioy))
      mario_rect = pygame.Rect(mariox,marioy,120,150)

            
      # if mario hits the mushroom, the death screen will appear      
      if mario_rect.colliderect(mushroom_rect):
         mush_death() #death screen
       
        
    
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()

         elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
               move_mushroomx = -4 #mush speed changing
            elif event.key == pygame.K_RIGHT:
               move_mushroomx = 4
            elif event.key == pygame.K_UP:
               move_mushroomy = -4
            elif event.key == pygame.K_DOWN:
               move_mushroomy = 4
            
                
         elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT:
               move_mushroomx = 0 #mush speed returns to zero when key is up
            elif event.key == pygame.K_RIGHT:
               move_mushroomx = 0
            elif event.key == pygame.K_UP:
               move_mushroomy = 0
            elif event.key == pygame.K_DOWN:
               move_mushroomy = 0
            elif event.key == pygame.K_SPACE:
               move_mushroomy = 0

      mushroomx += move_mushroomx #x-speed is added to current mushroom x value
    
      mushroomy += move_mushroomy #y-speed is added to current mushroom y value
    

      if mushroomx < 0: #left boundary
         mushroomx = 0
      if mushroomx > 900: #right boundary
         mushroomx = 900
      if mushroomy < 0: #top boundary
         mushroomy = 0
      if mushroomy > 500: #bottom boundary
         mushroomy = 500


      #blit mushroom at new x,y location with its assigned rect
      surface.blit(mushroomImg, (mushroomx, mushroomy))
      mushroom_rect = pygame.Rect(mushroomx,mushroomy,70,70)


      #coin grabbing
      if mushroom_rect.colliderect(coin1_rect):
         cointrack.play()
         coin1 = False
         coin1_rect = pygame.Rect(-5000, -5000, 1, 1)
         s1totalcoins += 1   
      elif coin1 == True:
         surface.blit(coin1Img, (coin1x, coin1y))
      #coin grabbing
      if mushroom_rect.colliderect(coin2_rect):
         cointrack.play()
         coin2 = False
         coin2_rect = pygame.Rect(-5002, -5000, 1, 1)
         s1totalcoins += 1
      elif coin2 == True:
         surface.blit(coin2Img, (coin2x, coin2y))
      #coin grabbing
      if mushroom_rect.colliderect(coin3_rect):
         cointrack.play()
         coin3 = False
         coin3_rect = pygame.Rect(-5004, -5000, 1, 1)
         s1totalcoins += 1
      elif coin3 == True:
         surface.blit(coin3Img, (coin3x, coin3y))
        
      if mushroom_rect.colliderect(coin4_rect):
         cointrack.play()
         coin4 = False
         coin4_rect = pygame.Rect(-5006, -5000, 1, 1)
         s1totalcoins += 1
      elif coin4 == True:
         surface.blit(coin4Img, (coin4x, coin4y))

      #if all the coins are collected, maintrack stops, and returned to start
      if s1totalcoins == 4:
         maintrack.stop()
         start_screen()
    
      pygame.display.update()
      fpsClock.tick(fps)
#stage set to 0
stage = 0
#initializes the game
while True:
   if stage == 0:
      start_screen()

 

           

 





