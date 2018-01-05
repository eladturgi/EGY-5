import pygame, sys, time, random
from tkinter import *
import tkinter.messagebox
import connect_four
import LaddersAndSnakes

#tkinter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the username and password
Username = 'None'
Password = 'None'
ValidUser = False



def message_display(text,x,y,font_size,color):
    def text_objects(text, font,color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

    

def LoginWindow(sort):
  Tpassword = '1234'
  Epassword = '4321'

  def show_entry_fields():
    global Username, Password, ValidUser
    User = e1.get()
    Pass = e2.get()
    if sort == 'T':
      if Pass != Tpassword:
        tkinter.messagebox.showinfo("Warning", "Bad Password!")
        ValidUser = False
          
      else:
        Username, Password = User, Pass
        ValidUser = True
        window.destroy()
    elif sort == 'E':
      if Pass != Epassword:
        tkinter.messagebox.showinfo("Warning", "Bad Password!")
        ValidUser = False

      else:
        Username, Password = User, Pass
        ValidUser = True
        window.destroy()
        
  window = Tk()
  window.title("Login")  # title
  
  # window.minsize(width=200,height=0) #force window size if needed  
  # size and location of window
  # size
  w = 200  # width for the window
  h = 80  # height for the window
  # location
  '''
  #side position
  #x = 625
  #y = 120
  '''
  x = 400
  y = 300

  # set the dimensions of the screen 
  # and where it is placed
  window.geometry('%dx%d+%d+%d' % (w, h, x, y))
  
  Label(window, text="User Name").grid(row=0)
  Label(window, text="Password").grid(row=1)
  
  e1 = Entry(window)
  e2 = Entry(window)
  
  e1.grid(row=0, column=1)
  e2.grid(row=1, column=1)

  Button(window, text='Back', command=window.destroy).grid(row=3, column=0, sticky=W, pady=4)
  Button(window, text='Login', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
  window.call('wm', 'attributes', '.', '-topmost', '1')  # make the window on top of pygame window
 
  mainloop()
#-----------------------------------------
# end of tkinter window
  

###########################PYGAME INITIATION####################  



# screen
screen_width = 800
screen_length = 600

#Game is off

pygame.init()  
screen = pygame.display.set_mode((screen_width, screen_length))


# Global Game counters
NumberGames4inRow = 0
NumberGamesSankesAndLadders = 0



#~~~~~~~~~~~Technician~~~~~~~~~~ 
def TechLogin():
  LoginWindow('T')
  if ValidUser:
    while True:
        # screen color
        screen.fill([255, 255, 255])
        # text message
        pygame.font.init() 
        myfont = pygame.font.SysFont('Arial Black', 50)
        # print Tech name
        text = 'Technician: ' + str(Username)
        textsurface = myfont.render(text, False, (0, 0, 0))
        screen.blit(textsurface, (0, 0))
        # print errors
        text2 = 'Number of errors: 0'
        textsurface2 = myfont.render(text2, False, (0, 0, 0))
        screen.blit(textsurface2, (0, 100))
        pygame.display.update()
      
      
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                return True
   
  else:
    return True


#~~~~~~~~~~Educator~~~~~~~~~~
def EducLogin(): 
  def ShowAll():
    black=0,0,0
    white=255,255,255
    message_display("Ladders and Snakes correct answers report:",278,320,25,(0,100,100))
    message_display("Connect Four win report :",155,220,25,(0,100,100))
    Q=LaddersAndSnakes.Q
    wins=connect_four.wins
    message_display("PC wins: {0}    Player wins: {1}".format(wins[1],wins[0]),168,255,25,black)
     
    for i in range(1,10):
        message_display("question number {0}: {1}\{2} ".format(i,Q[i][1],Q[i][0],[1]),115,330+i*22,20,black)
    for i in range(10,16):
        message_display("question number {0}: {1}\{2} ".format(i,Q[i][1],Q[i][0],[1]),400,330+i*22-9*22,20,black)
        
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                return True


  LoginWindow('E')
  if ValidUser:
    #while True:
      # screen color
      screen.fill([255, 255, 255])
      message_display("current game:",107,80,30,(200,0,0))
      message_display("number of Connect Four games: "+str(NumberGames4inRow),247,120,30,(0,0,0))
      message_display("number of Snakes & Ladders games: "+str(NumberGamesSankesAndLadders),286,150,30,(0,0,0))
      message_display("total games:",92,185,30,(200,0,0))
      # text message
      pygame.font.init() 
      myfont = pygame.font.SysFont('Arial Black', 50)
      myfont2 = pygame.font.SysFont('Arial Black', 30)
      # print educator name
      text = 'Educator: ' + str(Username)
      textsurface = myfont.render(text, False, (0, 0, 0))
      screen.blit(textsurface, (0, 0))
      '''
      # print game statistics
      text2 = 'Number of games in 4 in row: ' + str(NumberGames4inRow)
      textsurface2 = myfont2.render(text2, False, (0, 0, 0))
      screen.blit(textsurface2, (0, 100))
      text3 = 'Number of games in snakes and laaders: ' + str(NumberGamesSankesAndLadders)
      textsurface3 = myfont2.render(text3, False, (0, 0, 0))
      screen.blit(textsurface3, (0, 150))
      '''
      pygame.display.update()
      return ShowAll()

   
  else:
    return True

#Load Images-----------------------------------------


# 1
User_input = pygame.image.load('Photos/input.jpg')
# 2
User_ID = pygame.image.load('Photos/ID.jpg')
# 3
menu = pygame.image.load('Photos/Menu.jpg')
# 4
intro = pygame.image.load('Photos/intro.jpg')  #!!! delete educator and technician!!!


instructions = pygame.image.load('Photos/instructions.jpg')
help_s = pygame.image.load('Photos/help_s.jpg')
help_4 = pygame.image.load('Photos/help_4.jpg')



# 4
def Intro(game):

    # show intro
    screen.blit(intro, (0, 0))
    pygame.display.update()

    while(True):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            
            pressed = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT :
                 return True
                        
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     return True      
                            
            if event.type == pygame.MOUSEBUTTONDOWN:
              x, y = pygame.mouse.get_pos()   
              if 170 < x < 586 and 43 < y < 129:
                  if game == 'LaddersAndSnakes&Ladders':
                    return LaddersAndSnakes.Snakes(screen)
                  elif game == '4InRow':
                    return connect_four.Start_Game(screen)
              if 138 < x < 625 and 215 < y < 300:
                  if game == 'LaddersAndSnakes&Ladders':
                    screen.fill([255, 255, 255])
                    screen.blit(help_s, (175, 100)) 
                    pygame.display.update()
                    time.sleep(0.5)
                    while True:
                            for event in pygame.event.get():
                              if pygame.mouse.get_pressed() == (1, 0, 0):
                                return
                  if game == '4InRow':
                    screen.fill([255, 255, 255])
                    screen.blit(help_4, (175, 20)) 
                    pygame.display.update()
                    time.sleep(0.5)
                    while True:
                            for event in pygame.event.get():
                              if pygame.mouse.get_pressed() == (1, 0, 0):
                                return

  
def UserSelection():
  global NumberGamesSankesAndLadders,NumberGames4inRow
  screen.blit(User_ID, (0, 0))
  pygame.display.update()
  Exit = False
 
  for event in pygame.event.get():  
        x, y = 0, 0
        # exit case
        if event.type == pygame.QUIT :
          return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # case preseed 'Player'
            if 182 < x < 543 and 29 < y < 154:
              while not Exit:
                Exit = Menu()
              NumberGamesSankesAndLadders=LaddersAndSnakes.NumberGamesSankesAndLadders
              NumberGames4inRow=connect_four.NumberGames4inRow

            # case pressed 'Technician'
            elif 92 < x < 648 and 209 < y < 341:
              while not Exit:
                Exit = TechLogin()
                          
            # case pressed 'Educator'  
            elif 118 < x < 632 and 384 < y < 517:
              while not Exit:
                Exit = EducLogin()


def Menu():
    screen.blit(menu, (0, 0))           
    pygame.display.update()
    for event in pygame.event.get():
         
        x, y = pygame.mouse.get_pos()
        
        pressed = pygame.mouse.get_pressed() 
         #~~~~~~~~~~~~~~EXIT~~~~~~~~~~~~
        if event.type == pygame.QUIT :
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
                    
        elif pressed == (1, 0, 0) and 306 < x < 467 and 490 < y < 560:
            return True
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

          #~~~~~~~~~~~~~Connect 4~~~~~~~~
        elif pressed == (1, 0, 0) and 230 < x < 575 and 260 < y < 320:
            return Intro("4InRow")
              
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    
          #~~~~~~~~~~~~~LaddersAndSnakes&Ladders~~~~
        elif pressed == (1, 0, 0) and 145 < x < 625 and 345 < y < 407:
          return Intro("LaddersAndSnakes&Ladders")
             
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def Game():
    Exit = False
    while not Exit:
      Exit = UserSelection()

    pygame.quit()


Game()

