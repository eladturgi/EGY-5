import pygame, time, random

#------------4 in a row Photos------------

# Game board of 4 in a row
RowBoard = pygame.image.load('Photos/4ROWboard.jpg')
REDtoken = pygame.image.load('Photos/token_red.png')
YELLOWtoken = pygame.image.load('Photos/yellow.png')
playerLogo = pygame.image.load('Photos/playerLogo.png')
computerLogo = pygame.image.load('Photos/computerLogo.png')
blank = pygame.image.load('Photos/blank.jpg')
playerWins = pygame.image.load('Photos/playerWins.png')
computerWins = pygame.image.load('Photos/computerWins.png')
TIE = pygame.image.load('Photos/Tie.png')
###

NumberGames4inRow=0
empty = None
GoUp = 71  # Move up one row
MAX_height = 170  # End of the board

reset_list_running=False
wins=[0,0]
delay = 3

#-----------wins list and file input&output----------
def update_wins_list():
    filename='data2.txt'
    file=open(filename,"r")
    x=[]
    for line in file:
        x=line
        
    file.close()
    
    
    
    wins[0]=int(x[0])
    wins[1]=int(x[2])

def update_wins_file():
    fh = open("data2.txt", "w")
    fh.writelines(str(wins[0])+" "+str(wins[1]))
    fh.close()

def reset_wins_file():
    global reset_list_running
    reset_list_running=True
    fh = open("data2.txt", "w")
    fh.writelines(str(0)+" "+str(0))
    fh.close()
 
update_wins_list()
#reset_wins_file() 

#-----------------end wins list and file----------------

def winner(column , color , row , stop , Board):
    
      row -= 1  # Board[column]["Revenue"] =  to the row +1!!
            
      #----Column wins-------------------------------------------------------
      sequence, temp_row = 0, 0
      while temp_row < 6 :  # row index 5 is the end of the board!

        if Board[column][temp_row] == color:
          sequence += 1
          if sequence == stop:  # WIN!
            
            #This is part of the conditions of artificial intelligence*******
            if stop != 4:
              x = 4 - stop + temp_row
              if x < 6:
                # break # is breaking the big loop ("Why ? -> Because there is not enough room for a sequence )
                while x > 0:
                  if Board[column][x] == empty or Board[column][x] == color:
                      x -= 1
                  else:
                    sequence = 0
                    x = 0
              else:
                sequence = 0
            #****************************************************************
            if sequence != 0:      
              return True
          
          temp_row += 1
          
        else:
          sequence = 0
          temp_row += 1
          
      #----END Column wins---------------------------------------------------
      
      #----Row wins----------------------------------------------------------
      sequence, temp_column = 0, 0
      while temp_column < 7 :  # column index 6 is the end of the board!
        
        if Board[temp_column][row] == color:
          sequence += 1
          
          if sequence == stop:  # WIN!
            
            #This is part of the conditions of artificial intelligence*******
            if stop != 4:
              x = 4 - stop + temp_column
              if x < 7:
                # break # is breaking the big loop ("Why ? -> Because there is not enough room for a sequence )
                while x > 0:
                  if Board[x][row] == empty or Board[x][row] == color:
                      x -= 1
                  else:
                    sequence = 0
                    x = 0
              else:
                sequence = 0
            #****************************************************************
                
            if sequence != 0:      
              return True

          temp_column += 1
          
        else:
          sequence = 0
          temp_column += 1
      #----END Row wins------------------------------------------------------
           #----DiagonalUP wins---------------------------------------------------
      if True:  # dead zone
        temp_column, temp_row, sequence = column, row, 0
        
        # Go down to the first square of the diagonal
        while temp_column > 0 and temp_row > 0:
          temp_row -= 1
          temp_column -= 1
          
        # Now temp_column and temp_row are indexes of the first cell in the diagonal
        while temp_column < 7 and temp_row < 6:
          if Board[temp_column][temp_row] == color:
            sequence += 1
            temp_row += 1
            temp_column += 1
            if sequence == stop:  # WIN!
              return True
          else:
            sequence = 0
            temp_row += 1
            temp_column += 1
      #----END DiagonalUP wins-----------------------------------------------
            
      #----Diagonal DOWN wins------------------------------------------------
      if True:  # dead zone
        temp_column, temp_row, sequence = column, row, 0
        
        # Go down to the first square of the diagonal
        while temp_column < 6 and temp_row > 0:
          temp_row -= 1
          temp_column += 1
          
        # Now temp_column and temp_row are indexes of the first cell in the diagonal
        while temp_column >= 0 and temp_row < 6:
          if Board[temp_column][temp_row] == color:
            sequence += 1
            temp_row += 1
            temp_column -= 1
            if sequence == stop:  # WIN!
              return True
          else:
            sequence = 0
            temp_row += 1
            temp_column -= 1
      #----END Diagonal DOWN wins--------------------------------------------
      
      return False  # if we dont have a winner 
     #~~~~~~~~~~~~~~~~~~~~~~~END WINNER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
         #~~~~~~~~~~~~~~~~~~~~~~ALL Artificial intelligence function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

     
def add_artificial_token(column, color,Board):
         
         Board[column][Board[column]["Revenue"]] = color
         Board[column]["Revenue"] += 1

    
def Remove_artificial_token(column,Board):
         
         Board[column]["Revenue"] -= 1
         Board[column][Board[column]["Revenue"]] = empty


def Artificial_intelligence(color , stop , Board):
         
         column = 0
         while column < 7:
             if Board[column]["Revenue"] < 6:
                 add_artificial_token(column, color,Board)
        
                 if winner(column, color, Board[column]["Revenue"], stop,Board):
                     Remove_artificial_token(column,Board)
                     return column
            
                 Remove_artificial_token(column,Board)
             column += 1
      
         return None


def Artificial_intelligence2(color , stop,Board):
         
         column = 0
         while column < 7:
             if Board[column]["Revenue"] < 6:
                 add_artificial_token(column, color,Board)
        
                 if color == "red":
                     if winner(column, color, Board[column]["Revenue"], stop,Board):
                         Remove_artificial_token(column,Board)
                         add_artificial_token(column, "yellow",Board)
                         if Artificial_intelligence("red" , 4,Board) == None:
                             Remove_artificial_token(column,Board)
                             return column
                         else:
                             Remove_artificial_token(column,Board)
                             add_artificial_token(column, color,Board)
                  
                 elif winner(column, color, Board[column]["Revenue"], stop,Board) and not Artificial_intelligence("red" , 4,Board):
                     Remove_artificial_token(column,Board)
                     return column
        
                 Remove_artificial_token(column,Board)
                 
             column += 1
      
         return None
     #~~~~~~~~~~~~~~~~~~END ALL Artificial intelligence function~~~~~~

     
def Insert_column(col, color, Image, screen,Board):
      
       
      #-----Update Photo-------      
      screen.blit(Image, (Board[col]["X"], Board[col]["Y"]))
      pygame.display.update()
            
      #-----Update Board-------
      Board[col][Board[col]["Revenue"]] = color
      Board[col]["Revenue"] += 1
      Board[col]["Y"] -= GoUp

def IsEmptyBoard(Board):
    temp_row=6
    temp_col=7
    for i in range(temp_row):
        for j in range(temp_col):
            if Board[j][i]!=empty:
                return False
    return True


def Start_Game(screen):
            
          Board = [{0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":154, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":226, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":298, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":370, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":442, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":514, "Revenue":0},
                     {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":586, "Revenue":0}]
          PC_choice = None
          Human_turn = True
          screen.blit(RowBoard, (0, 0))
          global NumberGames4inRow
          NumberGames4inRow+=1
          
          
          while(True):
            screen.blit(blank, (0, 0))
            if Human_turn:
              screen.blit(playerLogo, (0, 0))
              pygame.display.update()
            else:
              screen.blit(computerLogo, (0, 0))
              pygame.display.update()
              time.sleep(0.5)
        
            #The player's turn to play---------------------------------
            if Human_turn:
              for event in pygame.event.get():
                  # Exit case
                  if event.type == pygame.QUIT:
                    return True
        
                  if event.type == pygame.MOUSEBUTTONDOWN and Human_turn:
                    x, y = pygame.mouse.get_pos()
                  
                    # user function
                    if 644 < x < 675 and 18 < y < 55:
                      return True
                    if 691 < x < 724 and 16 < y < 55:
                      return Start_Game(screen)
                    #------------Column 1----------------------
                    if 156 < x < 211 and y > 172 and Board[0]["Y"] > MAX_height:
                      Insert_column(0, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(0, "red", Board[0]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                      
                    #------------Column 2------------------------
                    if 227 < x < 286 and y > 172 and Board[1]["Y"] > MAX_height:
                      Insert_column(1, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(1, "red", Board[1]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        return
                      
                    #------------Column 3----------------------
                    if 298 < x < 357 and y > 172 and Board[2]["Y"] > MAX_height:
                      Insert_column(2, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(2, "red", Board[2]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                      
                    #------------Column 4----------------------
                    if 371 < x < 427 and y > 172 and Board[3]["Y"] > MAX_height:
                      Insert_column(3, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(3, "red", Board[3]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                      
                    #------------Column 5----------------------
                    if 443 < x < 501 and y > 172 and Board[4]["Y"] > MAX_height:
                      Insert_column(4, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(4, "red", Board[4]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                      
                    #------------Column 6----------------------
                    if 516 < x < 573 and y > 172 and Board[5]["Y"] > MAX_height:
                      Insert_column(5, "red", REDtoken, screen,Board)
                      Human_turn = False
                      if winner(5, "red", Board[5]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                      
                    #------------Column 7----------------------
                    if 588 < x < 644 and y > 172 and Board[6]["Y"] > MAX_height:
                      Insert_column(6, "red", REDtoken, screen,Board)
                      Human_turn = False
                      
                      if winner(6, "red", Board[6]["Revenue"], 4,Board):
                        wins[0]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(playerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay+2)
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
                        
                      Human_turn = False
                      
                #(PC)The computer's turn to play-------------------------------     
            else:
                  #Artificial intelligence~~~~~~~~~~~~~~~~~~~~~
                  """
                  Artificial intelligence to choose where
                  it is best to put a token into the board
                  """
                  # Priority1
                  print("A1")
                  PC_choice = Artificial_intelligence("yellow", 4,Board)
                  if PC_choice != None:  # Priority1  work!
                    Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
                  
                  else:  # #go to Priority2 (if Priority1 not work)
                    # Priority2
                    print("A2")
                    PC_choice = Artificial_intelligence("red", 4,Board)
                    
                    if PC_choice != None:  # Priority2  work!
                      Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
                    
                    else:  # go to Priority3 (if Priority2 not work)
                      # Priority3
                      print("A3")
                      PC_choice = Artificial_intelligence2("yellow", 3,Board)
                      
                      if PC_choice != None:  # Priority3  work!
                        Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
                        
                      else:  # go to Priority4 (if Priority3 not work)
                        # Priority4
                        print("A4")
                        PC_choice = Artificial_intelligence2("red", 3,Board)
                        
                        if PC_choice != None:  # Priority3  work!
                          Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
        
                        else:  # go to Priority3 (if Priority2 not work)
                          # Priority5
                          print("A5")
                          PC_choice = Artificial_intelligence2("yellow", 2,Board)
                          
                          if PC_choice != None:  # Priority3  work!
                            Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
        
                          else:
                            print("A6")
                            PC_choice = Artificial_intelligence2("red", 2,Board)
                            
                            if PC_choice != None:  # Priority3  work!
                              Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
                            
                            else:  # go to random!!! (if Priority4 not work)

                              #!Randomm!!!
                              def B(col,Board):
                                add_artificial_token(col, "yellow",Board)
                                if Artificial_intelligence("red" , 4,Board) != None:
                                  Remove_artificial_token(col,Board)
                                  return True
                                else:
                                  Remove_artificial_token(col,Board)
                                  return False
                                
                              PC_choice = random.randrange(0, 7)
                          
                              while Board[PC_choice]["Revenue"] == 6 or B(PC_choice,Board): 
                                PC_choice = random.randrange(0, 7)
                          
                              Insert_column(PC_choice, "yellow", YELLOWtoken, screen,Board)
                      
                  if winner(PC_choice, "yellow", Board[PC_choice]["Revenue"], 4,Board):
                        wins[1]+=1
                        update_wins_file()
                        screen.blit(blank, (0, 0))
                        screen.blit(computerWins, (0, 0)) 
                        pygame.display.update()
                        time.sleep(delay)
                        while True:
                                for event in pygame.event.get():
                                  if pygame.mouse.get_pressed() == (1, 0, 0):
                                    return
              
                  # TIE CHECK                
                  Tie = True     
                  for i in range(7):
                    if Board[i]["Revenue"] != 6:
                      Tie = False
                      
                  if Tie:
                    screen.blit(blank, (0, 0))
                    screen.blit(TIE, (0, 0)) 
                    pygame.display.update()
                    time.sleep(delay)
                    while True:
                      for event in pygame.event.get():
                        if pygame.mouse.get_pressed() == (1, 0, 0):
                          return
          
                  Human_turn = True
                  PC_choice = None
        
 #-------------------------------------------------------
 # end 4 in row game
     
