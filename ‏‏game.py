import pygame,sys,time,random
from tkinter import *
import tkinter.messagebox


#tkinter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#the username and password
Username='None'
Password='None'
ValidUser=False

def LoginWindow(sort):
  Tpassword='1234'
  Epassword='4321'

  def show_entry_fields():
    global Username,Password,ValidUser
    User=e1.get()
    Pass=e2.get()
    if sort == 'T':
      if Pass!=Tpassword:
        tkinter.messagebox.showinfo("Warning","Bad Password!")
        ValidUser=False
          
      else:
        Username,Password=User,Pass
        ValidUser=True
        window.destroy()
    elif sort == 'E':
      if Pass!=Epassword:
        tkinter.messagebox.showinfo("Warning","Bad Password!")
        ValidUser=False

      else:
        Username,Password=User,Pass
        ValidUser=True
        window.destroy()
        
  window = Tk()
  window.title("Login") #title
  
  #window.minsize(width=200,height=0) #force window size if needed  
  #size and location of window
  #size
  w = 200 # width for the window
  h = 80 # height for the window
  #location
  '''
  #side position
  #x = 625
  #y = 120
  '''
  x=400
  y=300

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
  window.call('wm', 'attributes', '.', '-topmost', '1') #make the window on top of pygame window
 
  mainloop()
#-----------------------------------------
#end of tkinter window
  

###########################PYGAME INITIATION####################  
pygame.init()

#screen
screen_width=800
screen_length=600

screen=pygame.display.set_mode((screen_width,screen_length))

#Global Game counters
NumberGames4inRow=0
NumberGamesSankesAndLadders=0
#~~~~~~~~~~~Technician~~~~~~~~~~ 
def TechLogin():
  LoginWindow('T')
  if ValidUser:
    while True:
      #screen color
      screen.fill([255,255,255])
      #text message
      pygame.font.init() 
      myfont = pygame.font.SysFont('Arial Black', 50)
      #print Tech name
      text='Technician: ' +str(Username)
      textsurface = myfont.render(text, False, (0, 0, 0))
      screen.blit(textsurface,(0,0))
      #print errors
      text2='Number of errors: 0'
      textsurface2 = myfont.render(text2, False, (0, 0, 0))
      screen.blit(textsurface2,(0,100))
      pygame.display.update()
      
      for event in pygame.event.get():
        #Exit case
        if event.type == pygame.QUIT:
          return True
   
  else:
    return True

#~~~~~~~~~~Educator~~~~~~~~~~
def EducLogin(): 
  LoginWindow('E')
  if ValidUser:
    while True:
      
      #screen color
      screen.fill([255,255,255])
      #text message
      pygame.font.init() 
      myfont = pygame.font.SysFont('Arial Black', 50)
      myfont2 = pygame.font.SysFont('Arial Black', 30)
      #print educator name
      text='Educator: ' +str(Username)
      textsurface = myfont.render(text, False, (0, 0, 0))
      screen.blit(textsurface,(0,0))
      #print game statistics
      text2='Number of games in 4 in row: '+str(NumberGames4inRow)
      textsurface2 = myfont2.render(text2, False, (0, 0, 0))
      screen.blit(textsurface2,(0,100))
      text3='Number of games in snakes and laaders: '+str(NumberGamesSankesAndLadders)
      textsurface3 = myfont2.render(text3, False, (0, 0, 0))
      screen.blit(textsurface3,(0,300))
      pygame.display.update()

      for event in pygame.event.get():
        #Exit case
        if event.type == pygame.QUIT:
          return True
   
  else:
    return True
  

#Load Images-----------------------------------------

#1
User_input=pygame.image.load('input.jpg')
#2
User_ID=pygame.image.load('ID.jpg')
#3
menu=pygame.image.load('Menu.jpg')
#4
intro=pygame.image.load('intro.jpg')#!!! delete educator and technician!!!

#5-The board of ladders and snakes 
Board=pygame.image.load('Board.jpg')
#5.1- players figures
person1=pygame.image.load('1.png')
person2=pygame.image.load('2.png')

#5.2 -players logos
logo1=pygame.image.load('player1.png')
logo2=pygame.image.load('player2.png')

#players win message
Win1=pygame.image.load('player1Wins.png')
Win2=pygame.image.load('Player2Wins.png')

#5.3 -cubes
cube1=pygame.image.load('cube1.png')
cube2=pygame.image.load('cube2.png')
cube3=pygame.image.load('cube3.png')
cube4=pygame.image.load('cube4.png')
cube5=pygame.image.load('cube5.png')
cube6=pygame.image.load('cube6.png')
cubes={1:cube1,2:cube2,3:cube3,4:cube4,5:cube5,6:cube6}

#5.4 - questions
#laddes questions
LQcorrect=pygame.image.load('LQcorrect.png')
LQincorrect=pygame.image.load('LQincorrect.png')
LQ1=pygame.image.load('LQ1.png')
LQ2=pygame.image.load('LQ2.png')
LQ3=pygame.image.load('LQ3.png')
LQ4=pygame.image.load('LQ4.png')
LQ5=pygame.image.load('LQ5.png')
LQ6=pygame.image.load('LQ6.png')
LQ7=pygame.image.load('LQ7.png')
LQ8=pygame.image.load('LQ8.png')
LQ9=pygame.image.load('LQ9.png')
LQ10=pygame.image.load('LQ10.png')
LQ11=pygame.image.load('LQ11.png')
LQ12=pygame.image.load('LQ12.png')
LQ13=pygame.image.load('LQ13.png')
LQ14=pygame.image.load('LQ14.png')
LQ15=pygame.image.load('LQ15.png')
LQuestions={1:(LQ1,False),2:(LQ2,True),3:(LQ3,True),4:(LQ4,True),5:(LQ5,False),6:(LQ6,False),7:(LQ7,False),8:(LQ8,True),9:(LQ9,False),
            10:(LQ10,True),11:(LQ11,False),12:(LQ12,False),13:(LQ13,True),14:(LQ14,False),15:(LQ15,True)}
#snake questions
SQcorrect=pygame.image.load('SQcorrect.png')
SQincorrect=pygame.image.load('SQincorrect.png')
SQ1=pygame.image.load('SQ1.png')
SQ2=pygame.image.load('SQ2.png')
SQ3=pygame.image.load('SQ3.png')
SQ4=pygame.image.load('SQ4.png')
SQ5=pygame.image.load('SQ5.png')
SQ6=pygame.image.load('SQ6.png')
SQ7=pygame.image.load('SQ7.png')
SQ8=pygame.image.load('SQ8.png')
SQ9=pygame.image.load('SQ9.png')
SQ10=pygame.image.load('SQ10.png')
SQ11=pygame.image.load('SQ11.png')
SQ12=pygame.image.load('SQ12.png')
SQ13=pygame.image.load('SQ13.png')
SQ14=pygame.image.load('SQ14.png')
SQ15=pygame.image.load('SQ15.png')
SQuestions={1:(SQ1,False),2:(SQ2,True),3:(SQ3,True),4:(SQ4,True),5:(SQ5,False),6:(SQ6,False),7:(SQ7,False),8:(SQ8,True),9:(SQ9,False),
            10:(SQ10,True),11:(SQ11,False),12:(SQ12,False),13:(SQ13,True),14:(SQ14,False),15:(SQ15,True)}


#------------4 in a row Photos------------
#Game board of 4 in a row
RowBoard=pygame.image.load('4ROWboard.jpg')

REDtoken=pygame.image.load('token_red.png')

YELLOWtoken=pygame.image.load('yellow.png')

playerLogo=pygame.image.load('playerLogo.png')
computerLogo=pygame.image.load('computerLogo.png')
blank=pygame.image.load('blank.jpg')
playerWins=pygame.image.load('playerWins.png')
computerWins=pygame.image.load('computerWins.png')

#~~~~~~~~~~~~~~Game 4 in row~~~~~~~~~~~~~~~~~~~~~~~~~~
def Four_in_row():
  
  screen.blit(RowBoard,(0,0))
  pygame.display.update()
  
  empty=None
  GoUp=71#Move up one row
  MAX_height=170#End of the board
  PC_choice=None
  Human_turn=True
  PC_priority=None
  delay=3
  
  Board=[{0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":154,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":226,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":298,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":370,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":442,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":514,"Revenue":0},
          {0:empty,1:empty,2:empty,3:empty,4:empty,5:empty,"Y":534,"X":586,"Revenue":0}]
  
  #~~~~~~~~~~~~~~~~~~~~~~~WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def winner(column ,color ,row ,stop ):
      nonlocal Board
      row-=1 #Board[column]["Revenue"] =  to the row +1!!

      #----DiagonalUP wins---------------------------------------------------
      if True:#dead zone
        temp_column,temp_row,sequence=column,row,0
        
        #Go down to the first square of the diagonal
        while temp_column>0 and temp_row>0:
          temp_row-=1
          temp_column-=1
          
        #Now temp_column and temp_row are indexes of the first cell in the diagonal
        while temp_column<7 and temp_row<6:
          if Board[temp_column][temp_row] == color:
            sequence+=1
            temp_row+=1
            temp_column+=1
            if sequence == stop:#WIN!
              return True
          else:
            sequence=0
            temp_row+=1
            temp_column+=1
      #----END DiagonalUP wins-----------------------------------------------

            
      #----Diagonal DOWN wins------------------------------------------------
      if True:#dead zone
        temp_column,temp_row,sequence=column,row,0
        
        #Go down to the first square of the diagonal
        while temp_column<6 and temp_row>0:
          temp_row-=1
          temp_column+=1
          
        #Now temp_column and temp_row are indexes of the first cell in the diagonal
        while temp_column>=0 and temp_row<6:
          if Board[temp_column][temp_row] == color:
            sequence+=1
            temp_row+=1
            temp_column-=1
            if sequence == stop:#WIN!
              return True
          else:
            sequence=0
            temp_row+=1
            temp_column-=1
      #----END Diagonal DOWN wins--------------------------------------------
            
      #----Column wins-------------------------------------------------------
      sequence,temp_row=0,0
      
      while temp_row<6 :#row index 5 is the end of the board!

        if Board[column][temp_row] == color:
          sequence+=1
  
          if sequence == stop:#WIN!
            
            #This is part of the conditions of artificial intelligence*******
            if stop != 4:
              x=4-stop + temp_row
              if x<6:
                #break # is breaking the big loop ("Why ? -> Because there is not enough room for a sequence )
                while x>0:
                  if Board[column][x] == empty or Board[column][x] == color:
                      x-=1
                  else:
                    sequence=0
                    x=0
              else:
                sequence=0
            #****************************************************************
            if sequence!=0:      
              return True
          
          temp_row+=1
          
        else:
          sequence=0
          temp_row+=1
          
      #----END Column wins---------------------------------------------------
      
      #----Row wins----------------------------------------------------------
      sequence,temp_column=0,0
      while temp_column<7 :#column index 6 is the end of the board!
        
        if Board[temp_column][row] == color:
          sequence+=1
          
          if sequence == stop:#WIN!
            
            #This is part of the conditions of artificial intelligence*******
            if stop != 4:
              x=4-stop + temp_column
              if x<7:
                #break # is breaking the big loop ("Why ? -> Because there is not enough room for a sequence )
                while x>0:
                  if Board[x][row] == empty or Board[x][row] == color:
                      x-=1
                  else:
                    sequence=0
                    x=0
              else:
                sequence=0
            #****************************************************************
                
            if sequence!=0:      
              return True

          temp_column+=1
          
        else:
          sequence=0
          temp_column+=1
      #----END Row wins------------------------------------------------------
      
      return False#if we dont have a win 
  #~~~~~~~~~~~~~~~~~~~~~~~END WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    


 #~~~~~~~~~~~~~~~~~~~~~~ALL Artificial intelligence function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  def add_artificial_token(column,color ):
    nonlocal Board
    Board[column][Board[column]["Revenue"]]=color
    Board[column]["Revenue"]+=1
    
  def Remove_artificial_token(column ):
    nonlocal Board
    Board[column]["Revenue"]-=1
    Board[column][Board[column]["Revenue"]]=empty

  def Artificial_intelligence(color , stop):
    nonlocal Board
    column=0
    while column<7:
      if Board[column]["Revenue"]<6:
        add_artificial_token(column,color )
        
        if winner(column,color,Board[column]["Revenue"],stop ):
          Remove_artificial_token(column )
          return column
        
        Remove_artificial_token(column)
      column+=1
      
    return None
  #~~~~~~~~~~~~~~~~~~END ALL Artificial intelligence function~~~~~~
  
  def Insert_column(col,color,Image):
      nonlocal Board 
      #-----Update Photo-------      
      screen.blit(Image,(Board[col]["X"],Board[col]["Y"]))
      pygame.display.update()
            
      #-----Update Board-------
      Board[col][Board[col]["Revenue"]]=color
      Board[col]["Revenue"]+=1
      Board[col]["Y"]-=GoUp
  
  
  #The Game Loop
  #logo
  while(True):
    screen.blit(blank,(0,0))
    if Human_turn:
      screen.blit(playerLogo,(0,0))
      pygame.display.update()
    else:
      screen.blit(computerLogo,(0,0))
      pygame.display.update()
      time.sleep(0.5)

    #The player's turn to play---------------------------------
    if Human_turn:
      for event in pygame.event.get():
          #Exit case
          if event.type == pygame.QUIT:
            return True

          if event.type == pygame.MOUSEBUTTONDOWN and Human_turn:
            x,y = pygame.mouse.get_pos()
          
             
            #------------Column 1----------------------
            if 156<x<211  and Board[0]["Y"]>MAX_height:
              Insert_column(0,"red",REDtoken)
              Human_turn=False
              if winner(0,"red",Board[0]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
              
            #------------Column 2------------------------
            if 227<x<286  and Board[1]["Y"]>MAX_height:
              Insert_column(1,"red",REDtoken)
              Human_turn=False
              if winner(1,"red",Board[1]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
              
            #------------Column 3----------------------
            if 298<x<357  and Board[2]["Y"]>MAX_height:
              Insert_column(2,"red",REDtoken)
              Human_turn=False
              if winner(2,"red",Board[2]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
              
            #------------Column 4----------------------
            if 371<x<427  and Board[3]["Y"]>MAX_height:
              Insert_column(3,"red",REDtoken)
              Human_turn=False
              if winner(3,"red",Board[3]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
              
            #------------Column 5----------------------
            if 443<x<501  and Board[4]["Y"]>MAX_height:
              Insert_column(4,"red",REDtoken)
              Human_turn=False
              if winner(4,"red",Board[4]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
              
            #------------Column 6----------------------
            if 516<x<573  and Board[5]["Y"]>MAX_height:
              Insert_column(5,"red",REDtoken)
              Human_turn=False
              if winner(5,"red",Board[5]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return
                
              
            #------------Column 7----------------------
            if 588<x<644  and Board[6]["Y"]>MAX_height:
              Insert_column(6,"red",REDtoken)
              Human_turn=False
              
              if winner(6,"red",Board[6]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(playerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                if pygame.mouse.get_pressed()==(1,0,0):
                  return

            Human_turn=False
                
              
        #(PC)The computer's turn to play-------------------------------     
    else:
          #Artificial intelligence~~~~~~~~~~~~~~~~~~~~~
          """
          Artificial intelligence to choose where
          it is best to put a token into the board
          """
          #Priority1
          print("A1")
          PC_choice = Artificial_intelligence("yellow", 4)
          if PC_choice != None:#Priority1  work!
            Insert_column(PC_choice,"yellow",YELLOWtoken)
            
          
          else:##go to Priority2 (if Priority1 not work)
            #Priority2
            print("A2")
            PC_choice = Artificial_intelligence("red",4)
            
            if PC_choice != None:#Priority2  work!
              Insert_column(PC_choice,"yellow",YELLOWtoken)
              
            
            else:#go to Priority3 (if Priority2 not work)
              #Priority3
              print("A3")
              PC_choice = Artificial_intelligence("yellow",3)
              
              if PC_choice != None:#Priority3  work!
                Insert_column(PC_choice,"yellow",YELLOWtoken)
                
              else:#go to Priority4 (if Priority3 not work)
                #Priority4
                print("A4")
                PC_choice = Artificial_intelligence("red",3)
                
                if PC_choice != None:#Priority3  work!
                  Insert_column(PC_choice,"yellow",YELLOWtoken)


                else:#go to Priority3 (if Priority2 not work)
                  #Priority5
                  print("A5")
                  PC_choice = Artificial_intelligence("yellow",2)
                  
                  if PC_choice != None:#Priority3  work!
                    Insert_column(PC_choice,"yellow",YELLOWtoken)
 
                    
                  else: #go to random!!! (if Priority4 not work)
                    #!Randomm!!!
                    print("R")
                    PC_choice=random.randrange(0,7)
                
                    while Board[PC_choice]["Revenue"]==6: 
                      PC_choice=random.randrange(0,7)
                
                    Insert_column(PC_choice,"yellow",YELLOWtoken)
                

              
          if winner(PC_choice,"yellow",Board[PC_choice]["Revenue"],4):
                screen.blit(blank,(0,0))
                screen.blit(computerWins,(0,0)) 
                pygame.display.update()
                time.sleep(delay)
                while True:
                        for event in pygame.event.get():
                          if pygame.mouse.get_pressed()==(1,0,0):
                            return
      
          #TIE CHECK                
          Tie=True     
          for i in range(6):
            if Board[i]["Revenue"]!= 6:
              Tie=False
              
          if Tie:
            print("TIE")
                
  
          Human_turn=True
          PC_choice=None

#-------------------------------------------------------
#end 4 in row game

#~~~~~~~~~~~~~~Game Snakes & Ladders~~~~~~~~~~~~~~~~~~~~
def Snakes():
  X1,Y1=17,494 #The initial coordinates in the Board -player1
  X2,Y2=48,494    #The initial coordinates in the Board -player2
  screen.blit(Board,(0,0)) #loading the Board
  cube_width=80
  cube_length=48
  Player1_Index=1
  Player2_Index=1
  Right1=True #flag indicate which side player1 should go
  Right2=True #flag indicate which side player2 should go
  
  #Begin the game "ladders and snakes"
  logo=logo1  #logo
  TurnPlayer1=True #indicate whose turn is now

  #-----------------------------------------------------
  #///////////Ladders Question function//////// 
  def LadderQuestion(logo):
    nonlocal X1,X2
    if logo ==1:
      logo=logo1
    else:
      logo=logo2
    #show the updated position of the players
    screen.blit(Board,(0,0)) #place board
    screen.blit(logo,(0,0)) #place logo #1
    X1,X2=FixIndex(X1,X2)
    screen.blit(person1,(X1,Y1)) #place person1
    screen.blit(person2,(X2,Y2)) #place person2
    pygame.display.update()
    time.sleep(0.3)
    
    #random question
    question_number = random.randrange(1,16)                       #random ladder question
    #question picture
    Question=LQuestions[question_number][0]
    #question answer
    RightAnswer=LQuestions[question_number][1]
    #place and update
    screen.blit(Question,(120,138))
    screen.blit(logo,(300,100)) #place logo  #2
    pygame.display.update()
    while(True):
      for event in pygame.event.get():
          x,y = pygame.mouse.get_pos()  
          pressed = pygame.mouse.get_pressed()
                  
          #pressed 'True'
          if pressed ==(1,0,0) and 461<x<581 and 358<y<410:
            if RightAnswer == True:
              screen.blit(LQcorrect,(120,138))
              pygame.display.update()
              time.sleep(1.5)
              return True
            else:
              screen.blit(LQincorrect,(120,138))
              pygame.display.update()
              time.sleep(1.5)
              return False
          #pressed 'False'
          elif pressed ==(1,0,0) and 70<x<308 and 358<y<410:
              if RightAnswer == False:
                screen.blit(LQcorrect,(120,138))
                pygame.display.update()
                time.sleep(1.5)
                return True
              else:
                screen.blit(LQincorrect,(120,138))
                pygame.display.update()
                time.sleep(1.5)
                return False
  #-------------------------------------------
  #///////////Snakes Question function////////            
  def SnakeQuestion(logo):
    nonlocal X1,X2
    if logo ==1:
      logo=logo1
    else:
      logo=logo2
    #show the updated position of the players
    screen.blit(Board,(0,0)) #place board
    screen.blit(logo,(0,0)) #place logo #1
    X1,X2=FixIndex(X1,X2)
    screen.blit(person1,(X1,Y1)) #place person1
    screen.blit(person2,(X2,Y2)) #place person2
    pygame.display.update()
    time.sleep(0.3)
    
    #random question
    question_number = random.randrange(1,16)                       #random snake question
    #question picture
    Question=SQuestions[question_number][0]
    #question answer
    RightAnswer=SQuestions[question_number][1]
    #place and update
    screen.blit(Question,(120,138))
    screen.blit(logo,(300,100)) #place logo  #2
    pygame.display.update()
    while(True):
      for event in pygame.event.get():
          x,y = pygame.mouse.get_pos()  
          pressed = pygame.mouse.get_pressed()
                  
          #pressed 'True'
          if pressed ==(1,0,0) and 461<x<581 and 358<y<410:
            if RightAnswer == True:
              screen.blit(SQcorrect,(120,138))
              pygame.display.update()
              time.sleep(1.5)
              return True
            else:
              screen.blit(SQincorrect,(120,138))
              pygame.display.update()
              time.sleep(1.5)
              return False
          #pressed 'False'
          elif pressed ==(1,0,0) and 70<x<308 and 358<y<410:
              if RightAnswer == False:
                screen.blit(SQcorrect,(120,138))
                pygame.display.update()
                time.sleep(1.5)
                return True
              else:
                screen.blit(SQincorrect,(120,138))
                pygame.display.update()
                time.sleep(1.5)
                return False
  #------------------------------------------            
  #roll dice function
  def roll():
    return random.randrange(1,7)
  #------------------------------
  #correction of players location function
  def FixIndex(X1,X2):
    #correction of location
    #cube 1
    if 0<X1<80:
      X1=17
    if 0<X2<80:
      X2=48
    #cube 2
    if 80<X1<160:
      X1=17+cube_width
    if 80<X2<160:
      X2=48+cube_width
    #cube 3
    if 160<X1<240:
      X1=17+cube_width*2
    if 160<X2<240:
      X2=48+cube_width*2
    #cube 4
    if 240<X1<320:
      X1=17+cube_width*3
    if 240<X2<320:
      X2=48+cube_width*3
    #cube 5
    if 320<X1<400:
      X1=17+cube_width*4
    if 320<X2<400:
      X2=48+cube_width*4
    #cube 6
    if 400<X1<480:
      X1=17+cube_width*5
    if 400<X2<480:
      X2=48+cube_width*5
    #cube 7
    if 480<X1<560:
      X1=17+cube_width*6
    if 480<X2<560:
      X2=48+cube_width*6
    #cube 8
    if 560<X1<640:
      X1=17+cube_width*7
    if 560<X2<640:
      X2=48+cube_width*7
    #cube 9
    if 640<X1<720:
      X1=17+cube_width*8
    if 640<X2<720:
      X2=48+cube_width*8
    #cube 10
    if 720<X1<800:
      X1=17+cube_width*9
    if 720<X2<800:
      X2=49+cube_width*9
    return X1,X2


  #-----------------------------------------------------------------------
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GAME LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  while(True):
        Change=False #Change player flag
        screen.blit(logo,(0,0)) #place logo 
        screen.blit(person1,(X1,Y1)) #place person1
        screen.blit(person2,(X2,Y2)) #place person2
        cube_answer=0 #cube answer
        pygame.display.update()
        screen.blit(Board,(0,0)) #place board
        for event in pygame.event.get():
          
          #print(pygame.mouse.get_pos())                              #print the x,y !@#!@#!@#!@#!@#@!213
          x,y = pygame.mouse.get_pos()
          
          #Exit case
          if event.type == pygame.QUIT or Player1_Index == 100:
            return True

          #-------------------ROLL DICE CASE----------------------
          if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if 6<x<791 and 538<y<596:
              cube_answer=roll()
              #cube_answer=1                                               ######################force cube
              screen.blit(person1,(X1,Y1))
              screen.blit(person2,(X2,Y2))
              screen.blit(cubes[cube_answer],(400,300)) #show the suitable cube
              pygame.display.update()
              time.sleep(0.8)                                              ##########cube time delay
              #change player flag=True
              Change=True
      
            
              #~~~~~~~~~~~~~PLAYER 1 TURN~~~~~~~~~~~~~~
              if TurnPlayer1:
                #update x and y coordinates
                Player1_Index+=cube_answer
                #in case we move right
                if(Right1):
                  #if we stuck at right wall
                  if X1+cube_answer*cube_width>=10*cube_width:
                    delta1=X1+cube_answer*cube_width-800
                    X1=800-delta1
                    Y1=Y1-cube_length#Rise line
                    Right1=False
                  else:
                    X1+=cube_answer*cube_width
                #in case we move left
                else:
                  #if we stuck at left wall
                  if X1-cube_answer*cube_width<0:
                    X1=cube_answer*cube_width-X1
                    Y1=Y1-cube_length#Rise line
                    Right1=True
                    
                    #$$$$PLAYER 1 WIN CASE!$$$$
                    if Y1<=62:
                      X1=17
                      Y1=494-9*cube_length
                      screen.blit(Board,(0,0)) #place board
                      screen.blit(person1,(X1,Y1)) #place person1
                      screen.blit(person2,(X2,Y2)) #place person2
                      screen.blit(Win1,(120,138))
                      pygame.display.update()
                      time.sleep(3)
                      while True:
                          for event in pygame.event.get():
                            if pygame.mouse.get_pressed()==(1,0,0):
                              return 
                      
                  else:
                     X1-=cube_answer*cube_width


                #Snakes--------------------------------------------
                if Player1_Index==17 and not SnakeQuestion(1):
                  Player1_Index=5
                  X1+=cube_width
                  Y1+=cube_length#Going down
                  Right1=True
                
                elif Player1_Index==11 and not SnakeQuestion(1) :
                  Player1_Index=9
                  X1-=cube_width
                  Y1+=cube_length#Going down
                  Right1=True
                    
                elif Player1_Index==58 and not SnakeQuestion(1):
                  Player1_Index=18
                  Y1+=cube_length*4#Going down
                    
                elif Player1_Index==34 and not SnakeQuestion(1):
                  Player1_Index=13
                  X1+=cube_width
                  Y1+=cube_length*2#Going down

                elif Player1_Index==53 and not SnakeQuestion(1):
                  Player1_Index=49
                  X1+=2*cube_width
                  Y1+=cube_length#Going down
                  Right1=True
                    
                elif Player1_Index==87 and not SnakeQuestion(1):
                  Player1_Index=66
                  X1-=cube_width
                  Y1+=cube_length*2#Going down
                    
                elif Player1_Index==98 and not SnakeQuestion(1):
                  Player1_Index=76
                  X1+=2*cube_width
                  Y1+=cube_length*2#Going down
                    
                elif Player1_Index==92 and not SnakeQuestion(1):
                  Player1_Index=90
                  X1+=cube_width
                  Y1+=cube_length#Going down
                  Right1=True
                #END Snakes----------------------------------------
                
                #Ladders-------------------------------------------
                if Player1_Index==6 and LadderQuestion(1):
                  Player1_Index=26
                  Y1-=cube_length*2#Going up
                elif Player1_Index==16 and LadderQuestion(1):
                  Player1_Index=36
                  Y1-=cube_length*2#Going up
                elif Player1_Index==21 and LadderQuestion(1):
                  Player1_Index=41
                  Y1-=cube_length*2#Going up
                elif Player1_Index==30 and LadderQuestion(1):
                  Player1_Index=51
                  Y1-=cube_length*3#Going up
                  Right1=False
                elif Player1_Index==45 and LadderQuestion(1):
                  Player1_Index=76
                  Y1-=cube_length*3#Going up
                  Right1=False
                elif Player1_Index==42 and LadderQuestion(1):
                  Player1_Index=82
                  Y1-=cube_length*4#Going up
                elif Player1_Index==68 and LadderQuestion(1):
                  Player1_Index=88
                  Y1-=cube_length*2#Going up
                #END Ladders---------------------------------------

              
              #~~~~~~~~~~~~~PLAYER 2 TURN~~~~~~~~~~~~~~
              elif not TurnPlayer1:
                #update x and y coordinates
                Player2_Index+=cube_answer
                
                #in case we move right
                if(Right2):
                  #if we stuck at right wall
                  if X2+cube_answer*cube_width>=10*cube_width:
                    delta2=X2+cube_answer*cube_width-800
                    X2=800-delta2
                    Y2=Y2-cube_length#Rise line+fix
                    Right2=False
                  else:
                    X2+=cube_answer*cube_width
                #in case we move left
                else:
                  #if we stuck at left wall
                  if X2-cube_answer*cube_width<0:
                    X2=cube_answer*cube_width-X2
                    Y2=Y2-cube_length#Rise line+fix
                    Right2=True

                    #$$$$PLAYER 2 WIN CASE!$$$$
                    if Y2<=62:
                      X2=17
                      Y2=494-9*cube_length
                      screen.blit(Board,(0,0)) #place board
                      screen.blit(person1,(X1,Y1)) #place person1
                      screen.blit(person2,(X2,Y2)) #place person2
                      screen.blit(Win2,(120,138))
                      pygame.display.update()
                      time.sleep(3)
                      while True:
                          for event in pygame.event.get():
                            if pygame.mouse.get_pressed()==(1,0,0):
                              return 
                  else:
                    X2-=cube_answer*cube_width                

              #Snakes--------------------------------------------
                if Player2_Index==17 and not SnakeQuestion(2):
                  Player2_Index=5
                  X2+=cube_width
                  Y2+=cube_length#Going down
                  Right2=True
                
                elif Player2_Index==11 and not SnakeQuestion(2) :
                  Player2_Index=9
                  X2-=cube_width
                  Y2+=cube_length#Going down
                  Right2=True
                    
                elif Player2_Index==58 and not SnakeQuestion(2):
                  Player2_Index=18
                  Y2+=cube_length*4#Going down
                    
                elif Player2_Index==34 and not SnakeQuestion(2):
                  Player2_Index=13
                  X2+=cube_width
                  Y2+=cube_length*2#Going down

                elif Player2_Index==53 and not SnakeQuestion(2):
                  Player2_Index=49
                  X2+=2*cube_width
                  Y2+=cube_length#Going down
                  Right2=True
                    
                elif Player2_Index==87 and not SnakeQuestion(2):
                  Player2_Index=66
                  X2-=cube_width
                  Y2+=cube_length*2#Going down
                    
                elif Player2_Index==98 and not SnakeQuestion(2):
                  Player2_Index=76
                  X2+=2*cube_width
                  Y2+=cube_length*2#Going down
                    
                elif Player2_Index==92 and not SnakeQuestion(2):
                  Player2_Index=90
                  X2+=cube_width
                  Y2+=cube_length#Going down
                  Right2=True
                #END Snakes----------------------------------------
                
                #Ladders-------------------------------------------
                if Player2_Index==6 and LadderQuestion(2):
                  Player2_Index=26
                  Y2-=cube_length*2#Going up
                elif Player2_Index==16 and LadderQuestion(2):
                  Player2_Index=36
                  Y2-=cube_length*2#Going up
                elif Player2_Index==21 and LadderQuestion(2):
                  Player2_Index=41
                  Y2-=cube_length*2#Going up
                elif Player2_Index==30 and LadderQuestion(2):
                  Player2_Index=51
                  Y2-=cube_length*3#Going up
                  Right2=False
                elif Player2_Index==45 and LadderQuestion(2):
                  Player2_Index=76
                  Y2-=cube_length*3#Going up
                  Right2=False
                elif Player2_Index==42 and LadderQuestion(2):
                  Player2_Index=82
                  Y2-=cube_length*4#Going up
                elif Player2_Index==68 and LadderQuestion(2):
                  Player2_Index=88
                  Y2-=cube_length*2#Going up
                #END Ladders---------------------------------------
              
            #END Case of throwing a cube-----------------------------------------------------
            
            #~~~~~~~~~~~~~~~~~~~~~~
            if Change:
              Change=False
              #change gamer
              if TurnPlayer1:
                TurnPlayer1=False
              else:
                TurnPlayer1=True
              
              #change logo of gamer
              if logo==logo2:
                logo=logo1
              else:
                logo=logo2
            
              
          #Fixing the Plyaers Locations indexs
          X1,X2=FixIndex(X1,X2)
#---------------------------------------------------------------------
#end game snakes & ladders
              
            
            
     

#4
def Intro(game):

    #show intro
    screen.blit(intro,(0,0))
    pygame.display.update()

    while(True):
        for event in pygame.event.get():
            x,y = pygame.mouse.get_pos()
            
            pressed = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT :
                 return True
                        
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     return True      
                            
                
            if pressed ==(1,0,0) and 170<x<586 and 43<y<129:
                if game=='Snakes&Ladders':
                  return Snakes()
                elif game=='4InRow':
                  return Four_in_row()
            if pressed ==(1,0,0) and 138<x<625 and 215<y<300:
                if game=='snakes':
                  print('snakes Instructions')
                else:
                  print('4inrow Instructions')
                

  
def UserSelection():
  screen.blit(User_ID,(0,0))
  pygame.display.update()
  Exit =False
 
  for event in pygame.event.get():  
        x,y=0,0
        #exit case
        if event.type == pygame.QUIT :
          return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            #case preseed 'Player'
            if 182<x<543 and 29<y<154:
              while not Exit:
                Exit=Menu()

            #case pressed 'Technician'
            elif 92<x<648 and 209<y<341:
              while not Exit:
                Exit=TechLogin()
                
                          
            #case pressed 'Educator'  
            elif 118<x<632 and 384<y<517:
              while not Exit:
                Exit=EducLogin()
      


def Menu():
    screen.blit(menu,(0,0))           
    pygame.display.update()
    global NumberGames4inRow,NumberGamesSankesAndLadders
    for event in pygame.event.get():
         
        x,y = pygame.mouse.get_pos()
        
        pressed = pygame.mouse.get_pressed() 
         #~~~~~~~~~~~~~~EXIT~~~~~~~~~~~~
        if event.type == pygame.QUIT :
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
                    
        elif pressed ==(1,0,0) and 306<x<467 and 490<y<560:
            return True
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

          #~~~~~~~~~~~~~Connect 4~~~~~~~~
        elif pressed ==(1,0,0) and 230<x<575 and 260<y<320:
            NumberGames4inRow+=1
            return Intro("4InRow")
           
              
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    
          #~~~~~~~~~~~~~Snakes&Ladders~~~~
        elif pressed == (1,0,0) and 145<x<625 and 345<y<407:
          NumberGamesSankesAndLadders+=1
          return Intro("Snakes&Ladders")
             
          #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def Game():
    Exit =False
    while not Exit:
      Exit=UserSelection()

    pygame.quit()

Game()



        

