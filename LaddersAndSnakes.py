import pygame, time, random

# 5-The board of ladders and snakes 
Board = pygame.image.load('Photos/Board.jpg')
# 5.1- players figures
person1 = pygame.image.load('Photos/1.png')
person2 = pygame.image.load('Photos/2.png')

# 5.2 -players logos
logo1 = pygame.image.load('Photos/player1.png')
logo2 = pygame.image.load('Photos/player2.png')

# players win message
Win1 = pygame.image.load('Photos/player1Wins.png')
Win2 = pygame.image.load('Photos/Player2Wins.png')

# 5.3 -cubes
cube1 = pygame.image.load('Photos/cube1.png')
cube2 = pygame.image.load('Photos/cube2.png')
cube3 = pygame.image.load('Photos/cube3.png')
cube4 = pygame.image.load('Photos/cube4.png')
cube5 = pygame.image.load('Photos/cube5.png')
cube6 = pygame.image.load('Photos/cube6.png')
cubes = {1:cube1, 2:cube2, 3:cube3, 4:cube4, 5:cube5, 6:cube6}

# 5.4 - questions
# ladders questions
LQcorrect = pygame.image.load('Photos/LQcorrect.png')
LQincorrect = pygame.image.load('Photos/LQincorrect.png')
LQ1 = pygame.image.load('Photos/LQ1.png')
LQ2 = pygame.image.load('Photos/LQ2.png')
LQ3 = pygame.image.load('Photos/LQ3.png')
LQ4 = pygame.image.load('Photos/LQ4.png')
LQ5 = pygame.image.load('Photos/LQ5.png')
LQ6 = pygame.image.load('Photos/LQ6.png')
LQ7 = pygame.image.load('Photos/LQ7.png')
LQ8 = pygame.image.load('Photos/LQ8.png')
LQ9 = pygame.image.load('Photos/LQ9.png')
LQ10 = pygame.image.load('Photos/LQ10.png')
LQ11 = pygame.image.load('Photos/LQ11.png')
LQ12 = pygame.image.load('Photos/LQ12.png')
LQ13 = pygame.image.load('Photos/LQ13.png')
LQ14 = pygame.image.load('Photos/LQ14.png')
LQ15 = pygame.image.load('Photos/LQ15.png')
LQuestions = {1:(LQ1, False), 2:(LQ2, True), 3:(LQ3, True), 4:(LQ4, True), 5:(LQ5, False), 6:(LQ6, False), 7:(LQ7, False), 8:(LQ8, True), 9:(LQ9, False),
            10:(LQ10, True), 11:(LQ11, False), 12:(LQ12, False), 13:(LQ13, True), 14:(LQ14, False), 15:(LQ15, True)}
# snake questions
SQcorrect = pygame.image.load('Photos/SQcorrect.png')
SQincorrect = pygame.image.load('Photos/SQincorrect.png')
SQ1 = pygame.image.load('Photos/SQ1.png')
SQ2 = pygame.image.load('Photos/SQ2.png')
SQ3 = pygame.image.load('Photos/SQ3.png')
SQ4 = pygame.image.load('Photos/SQ4.png')
SQ5 = pygame.image.load('Photos/SQ5.png')
SQ6 = pygame.image.load('Photos/SQ6.png')
SQ7 = pygame.image.load('Photos/SQ7.png')
SQ8 = pygame.image.load('Photos/SQ8.png')
SQ9 = pygame.image.load('Photos/SQ9.png')
SQ10 = pygame.image.load('Photos/SQ10.png')
SQ11 = pygame.image.load('Photos/SQ11.png')
SQ12 = pygame.image.load('Photos/SQ12.png')
SQ13 = pygame.image.load('Photos/SQ13.png')
SQ14 = pygame.image.load('Photos/SQ14.png')
SQ15 = pygame.image.load('Photos/SQ15.png')
SQuestions = {1:(SQ1, False), 2:(SQ2, True), 3:(SQ3, True), 4:(SQ4, True), 5:(SQ5, False), 6:(SQ6, False), 7:(SQ7, False), 8:(SQ8, True), 9:(SQ9, False),
            10:(SQ10, True), 11:(SQ11, False), 12:(SQ12, False), 13:(SQ13, True), 14:(SQ14, False), 15:(SQ15, True)}

NumberGamesSankesAndLadders=0

Q={1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0],7:[0,0],8:[0,0],9:[0,0],10:[0,0],11:[0,0],12:[0,0],13:[0,0],14:[0,0],15:[0,0]}
PlayersInfo={1:[0,0],2:[0,0]}
#~~~~~~~~~~~~~~Game Snakes & Ladders~~~~~~~~~~~~~~~~~~~~


X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
cube_width = 80
cube_length = 48
Player1_Index = 1
Player2_Index = 1
Right1 = True  # flag indicate which side player1 should go
Right2 = True  # flag indicate which side player2 should go
reset_running=False
# Begin the game "ladders and snakes"
logo = logo1  # logo
TurnPlayer1 = True  # indicate whose turn is now
#-----------------------------------------------------
#---------------question data input&output----------
def update_data_dict():
    filename = "data.txt"
    file = open(filename, "r")
    x=""
    for line in file:
       x+=line
    
    file.close()


    x=x.split('\n')
    x=list(map(lambda x:x.split(),x))
    
    for i in range(1,16):
        Q[i][0]=int(x[i-1][0])
        Q[i][1]=int(x[i-1][1])
        
    
def update_data_file():
    fh = open("data.txt", "w")
    lines_of_text=[]
    for i in range(1,16):
        lines_of_text+= str(Q[i][0])+" "+ str(Q[i][1])+"\n"
    fh.writelines(lines_of_text)
    fh.close()

def reset_data_file():
    global reset_not_running
    reset_running=True
    fh = open("data.txt", "w")
    lines_of_text=[]
    for i in range(1,16):
        lines_of_text+= str(0)+" "+ str(0)+"\n"
    fh.writelines(lines_of_text)
    fh.close()

update_data_dict()
#reset_data_file()

#----------------end data file and dict--------------


def message_display(text,x,y,font_size,color,screen):
    def text_objects(text, font,color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

#------------------------

#///////////Ladders Question function//////// 
def LadderQuestion(playerNumber,screen):
    global X1,X2
    if playerNumber ==1:
      logo=logo1
    else:
      logo=logo2
    PlayersInfo[playerNumber][0]+=1
    #show the updated position of the players
    screen.blit(Board,(0,0)) #place board
    screen.blit(logo,(0,0)) #place logo #1
    X1,X2=FixIndex(X1,X2)
    screen.blit(person1,(X1,Y1)) #place person1
    screen.blit(person2,(X2,Y2)) #place person2
    message_display("player1 questions:{0}\{1}".format(PlayersInfo[1][1],PlayersInfo[1][0]), 400, 8, 20, (0,0,0), screen)
    message_display("player2 questions:{0}\{1}".format(PlayersInfo[2][1],PlayersInfo[2][0]), 400, 40, 20, (0,0,0), screen)
    pygame.display.update()
    time.sleep(0.3)
    
    #random question
    question_number = random.randrange(1,16)                       #random ladder question
    Q[question_number][0]+=1
    update_data_file()
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
              Q[question_number][1]+=1
              PlayersInfo[playerNumber][1]+=1
              update_data_file()
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
                Q[question_number][1]+=1
                PlayersInfo[playerNumber][1]+=1
                update_data_file()
                return True
              else:
                screen.blit(LQincorrect,(120,138))
                pygame.display.update()
                time.sleep(1.5)
                return False
  #-------------------------------------------
  # ///////////Snakes Question function////////            
def SnakeQuestion(playerNumber,screen):
    global X1, X2
    if playerNumber == 1:
      logo = logo1
    else:
      logo = logo2
    
    PlayersInfo[playerNumber][0]+=1
    # show the updated position of the players
    screen.blit(Board, (0, 0))  # place board
    screen.blit(logo, (0, 0))  # place logo #1
    X1,X2=FixIndex(X1,X2)
    screen.blit(person1, (X1, Y1))  # place person1
    screen.blit(person2, (X2, Y2))  # place person2
    pygame.display.update()
    time.sleep(0.3)
    
    # random question
    question_number = random.randrange(1, 16)  # random snake question
    Q[question_number][0]+=1
    update_data_file()
    # question picture
    Question = SQuestions[question_number][0]
    # question answer
    RightAnswer = SQuestions[question_number][1]
    # place and update
    screen.blit(Question, (120, 138))
    screen.blit(logo, (300, 100))  # place logo  #2
    message_display("player1 questions:{0}\{1}".format(PlayersInfo[1][1],PlayersInfo[1][0]), 400, 8, 20, (0,0,0), screen)
    message_display("player2 questions:{0}\{1}".format(PlayersInfo[2][1],PlayersInfo[2][0]), 400, 40, 20, (0,0,0), screen)
    pygame.display.update()
    while(True):
      for event in pygame.event.get():
          x, y = pygame.mouse.get_pos()  
          pressed = pygame.mouse.get_pressed()
                  
          # pressed 'True'
          if pressed == (1, 0, 0) and 461 < x < 581 and 358 < y < 410:
            if RightAnswer == True:
              screen.blit(SQcorrect, (120, 138))
              pygame.display.update()
              time.sleep(1.5)
              Q[question_number][1]+=1
              PlayersInfo[playerNumber][1]+=1
              update_data_file()
              return True
            else:
              screen.blit(SQincorrect, (120, 138))
              pygame.display.update()
              time.sleep(1.5)
              return False
          # pressed 'False'
          elif pressed == (1, 0, 0) and 70 < x < 308 and 358 < y < 410:
              if RightAnswer == False:
                screen.blit(SQcorrect, (120, 138))
                pygame.display.update()
                time.sleep(1.5)
                Q[question_number][1]+=1
                PlayersInfo[playerNumber][1]+=1
                update_data_file()
                return True
              else:
                screen.blit(SQincorrect, (120, 138))
                pygame.display.update()
                time.sleep(1.5)
                return False




  #------------------------------------------            
  # roll dice function
def roll():
    return random.randrange(1, 7)

  #------------------------------
  
  # correction of players location function
def FixIndex(X1,X2):
    # correction of location
    # cube 1
    if 0 < X1 < 80:
      X1 = 17
    if 0 < X2 < 80:
      X2 = 48
    # cube 2
    if 80 < X1 < 160:
      X1 = 17 + cube_width
    if 80 < X2 < 160:
      X2 = 48 + cube_width
    # cube 3
    if 160 < X1 < 240:
      X1 = 17 + cube_width * 2
    if 160 < X2 < 240:
      X2 = 48 + cube_width * 2
    # cube 4
    if 240 < X1 < 320:
      X1 = 17 + cube_width * 3
    if 240 < X2 < 320:
      X2 = 48 + cube_width * 3
    # cube 5
    if 320 < X1 < 400:
      X1 = 17 + cube_width * 4
    if 320 < X2 < 400:
      X2 = 48 + cube_width * 4
    # cube 6
    if 400 < X1 < 480:
      X1 = 17 + cube_width * 5
    if 400 < X2 < 480:
      X2 = 48 + cube_width * 5
    # cube 7
    if 480 < X1 < 560:
      X1 = 17 + cube_width * 6
    if 480 < X2 < 560:
      X2 = 48 + cube_width * 6
    # cube 8
    if 560 < X1 < 640:
      X1 = 17 + cube_width * 7
    if 560 < X2 < 640:
      X2 = 48 + cube_width * 7
    # cube 9
    if 640 < X1 < 720:
      X1 = 17 + cube_width * 8
    if 640 < X2 < 720:
      X2 = 48 + cube_width * 8
    # cube 10
    if 720 < X1 < 800:
      X1 = 17 + cube_width * 9
    if 720 < X2 < 800:
      X2 = 49 + cube_width * 9
    return X1, X2

#-----------------------------------------------------------------------

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GAME LOOP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Snakes(screen):
    global logo,X1,X2,Y1,Y2,Player1_Index,Player2_Index,TurnPlayer1,Right1,Right2,NumberGamesSankesAndLadders
    NumberGamesSankesAndLadders+=1
    update_data_dict()
    while(True):
        message_display("player1 questions:{0}\{1}".format(PlayersInfo[1][1],PlayersInfo[1][0]), 400, 8, 20, (0,0,0), screen)
        message_display("player2 questions:{0}\{1}".format(PlayersInfo[2][1],PlayersInfo[2][0]), 400, 40, 20, (0,0,0), screen)
        
        Change = False  # Change player flag
        screen.blit(logo, (0, 0))  # place logo 
        screen.blit(person1, (X1, Y1))  # place person1
        screen.blit(person2, (X2, Y2))  # place person2
        cube_answer = 0  # cube answer
        pygame.display.update()
        screen.blit(Board, (0, 0))  # place board
        for event in pygame.event.get():
          
          #print(pygame.mouse.get_pos())                              #print the x,y !@#!@#!@#!@#!@#@!213
          x, y = pygame.mouse.get_pos()
          
          # Exit case
          if event.type == pygame.QUIT or Player1_Index == 100:
            X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
            X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
            Player1_Index = 1
            Player2_Index = 1
            Right1 = True  # flag indicate which side player1 should go
            Right2 = True  # flag indicate which side player2 should go
            logo=logo1
            PlayersInfo[1][0]=PlayersInfo[1][1]=PlayersInfo[2][0]=PlayersInfo[2][1]=0
            return True
          
           #-----cheats-----
          if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
              pass
              #LadderQuestion(1,screen)

            #-------------
          #-------------------Game Options----------------------
          if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 644 < x < 675 and 18 < y < 55:
                X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
                X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
                Player1_Index = 1
                Player2_Index = 1
                Right1 = True  # flag indicate which side player1 should go
                Right2 = True  # flag indicate which side player2 should go
                logo=logo1
                PlayersInfo[1][0]=PlayersInfo[1][1]=PlayersInfo[2][0]=PlayersInfo[2][1]=0
                return True
            if 691 < x < 724 and 16 < y < 55:
                X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
                X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
                Player1_Index = 1
                Player2_Index = 1
                Right1 = True  # flag indicate which side player1 should go
                Right2 = True  # flag indicate which side player2 should go
                logo=logo1
                PlayersInfo[1][0]=PlayersInfo[1][1]=PlayersInfo[2][0]=PlayersInfo[2][1]=0
                return Snakes(screen)
            #-------------------ROLL DICE CASE----------------------
            if 6 < x < 791 and 538 < y < 596:
              cube_answer = roll()
              # cube_answer=1                                               ######################force cube
              screen.blit(person1, (X1, Y1))
              screen.blit(person2, (X2, Y2))
              message_display("player1 questions:{0}\{1}".format(PlayersInfo[1][1],PlayersInfo[1][0]), 400, 8, 20, (0,0,0), screen)
              message_display("player2 questions:{0}\{1}".format(PlayersInfo[2][1],PlayersInfo[2][0]), 400, 40, 20, (0,0,0), screen)
              screen.blit(cubes[cube_answer], (400, 300))  # show the suitable cube
              pygame.display.update()
              time.sleep(0.8)  ##########cube time delay
              # change player flag=True
              Change = True
            
              #~~~~~~~~~~~~~PLAYER 1 TURN~~~~~~~~~~~~~~
              if TurnPlayer1:
                # update x and y coordinates
                Player1_Index += cube_answer
                # in case we move right
                if(Right1):
                  # if we stuck at right wall
                  if X1 + cube_answer * cube_width >= 10 * cube_width:
                    delta1 = X1 + cube_answer * cube_width - 800
                    X1 = 800 - delta1
                    Y1 = Y1 - cube_length  # Rise line
                    Right1 = False
                  else:
                    X1 += cube_answer * cube_width
                # in case we move left
                else:
                  # if we stuck at left wall
                  if X1 - cube_answer * cube_width < 0:
                    X1 = cube_answer * cube_width - X1
                    Y1 = Y1 - cube_length  # Rise line
                    Right1 = True
                    
                    # $$$$PLAYER 1 WIN CASE!$$$$
                    if Y1 <= 62:
                      X1 = 17
                      Y1 = 494 - 9 * cube_length
                      screen.blit(Board, (0, 0))  # place board
                      screen.blit(person1, (X1, Y1))  # place person1
                      screen.blit(person2, (X2, Y2))  # place person2
                      screen.blit(Win1, (120, 138))
                      pygame.display.update()
                      time.sleep(3)
                      X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
                      X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
                      Player1_Index = 1
                      Player2_Index = 1
                      Right1 = True  # flag indicate which side player1 should go
                      Right2 = True  # flag indicate which side player2 should go
                      logo=logo1
                      PlayersInfo[1][0]=PlayersInfo[1][1]=PlayersInfo[2][0]=PlayersInfo[2][1]=0
                      while True:
                          for event in pygame.event.get():
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                                return 
                      
                  else:
                     X1 -= cube_answer * cube_width

                #Snakes--------------------------------------------
                if Player1_Index == 17 and not SnakeQuestion(1,screen):
                  Player1_Index = 5
                  X1 += cube_width
                  Y1 += cube_length  # Going down
                  Right1 = True
                
                elif Player1_Index == 11 and not SnakeQuestion(1,screen) :
                  Player1_Index = 9
                  X1 -= cube_width
                  Y1 += cube_length  # Going down
                  Right1 = True
                    
                elif Player1_Index == 58 and not SnakeQuestion(1,screen):
                  Player1_Index = 18
                  Y1 += cube_length * 4  # Going down
                    
                elif Player1_Index == 34 and not SnakeQuestion(1,screen):
                  Player1_Index = 13
                  X1 += cube_width
                  Y1 += cube_length * 2  # Going down

                elif Player1_Index == 53 and not SnakeQuestion(1,screen):
                  Player1_Index = 49
                  X1 += 2 * cube_width
                  Y1 += cube_length  # Going down
                  Right1 = True
                    
                elif Player1_Index == 87 and not SnakeQuestion(1,screen):
                  Player1_Index = 66
                  X1 -= cube_width
                  Y1 += cube_length * 2  # Going down
                    
                elif Player1_Index == 98 and not SnakeQuestion(1,screen):
                  Player1_Index = 76
                  X1 += 2 * cube_width
                  Y1 += cube_length * 2  # Going down
                    
                elif Player1_Index == 92 and not SnakeQuestion(1,screen):
                  Player1_Index = 90
                  X1 += cube_width
                  Y1 += cube_length  # Going down
                  Right1 = True
                #END Snakes----------------------------------------
                
                #Ladders-------------------------------------------
                if Player1_Index == 6 and LadderQuestion(1,screen):
                  Player1_Index = 26
                  Y1 -= cube_length * 2  # Going up
                elif Player1_Index == 16 and LadderQuestion(1,screen):
                  Player1_Index = 36
                  Y1 -= cube_length * 2  # Going up
                elif Player1_Index == 21 and LadderQuestion(1,screen):
                  Player1_Index = 41
                  Y1 -= cube_length * 2  # Going up
                elif Player1_Index == 30 and LadderQuestion(1,screen):
                  Player1_Index = 51
                  Y1 -= cube_length * 3  # Going up
                  Right1 = False
                elif Player1_Index == 45 and LadderQuestion(1,screen):
                  Player1_Index = 76
                  Y1 -= cube_length * 3  # Going up
                  Right1 = False
                elif Player1_Index == 42 and LadderQuestion(1,screen):
                  Player1_Index = 82
                  Y1 -= cube_length * 4  # Going up
                elif Player1_Index == 68 and LadderQuestion(1,screen):
                  Player1_Index = 88
                  Y1 -= cube_length * 2  # Going up
                #END Ladders---------------------------------------
              
              #~~~~~~~~~~~~~PLAYER 2 TURN~~~~~~~~~~~~~~
              elif not TurnPlayer1:
                # update x and y coordinates
                Player2_Index += cube_answer
                
                # in case we move right
                if(Right2):
                  # if we stuck at right wall
                  if X2 + cube_answer * cube_width >= 10 * cube_width:
                    delta2 = X2 + cube_answer * cube_width - 800
                    X2 = 800 - delta2
                    Y2 = Y2 - cube_length  # Rise line+fix
                    Right2 = False
                  else:
                    X2 += cube_answer * cube_width
                # in case we move left
                else:
                  # if we stuck at left wall
                  if X2 - cube_answer * cube_width < 0:
                    X2 = cube_answer * cube_width - X2
                    Y2 = Y2 - cube_length  # Rise line+fix
                    Right2 = True

                    # $$$$PLAYER 2 WIN CASE!$$$$
                    if Y2 <= 62:
                      X2 = 17
                      Y2 = 494 - 9 * cube_length
                      screen.blit(Board, (0, 0))  # place board
                      screen.blit(person1, (X1, Y1))  # place person1
                      screen.blit(person2, (X2, Y2))  # place person2
                      screen.blit(Win2, (120, 138))
                      pygame.display.update()
                      time.sleep(3)
                      X1, Y1 = 17, 494  # The initial coordinates in the Board -player1
                      X2, Y2 = 48, 494  # The initial coordinates in the Board -player2
                      Player1_Index = 1
                      Player2_Index = 1
                      Right1 = True  # flag indicate which side player1 should go
                      Right2 = True  # flag indicate which side player2 should go
                      logo=logo1
                      PlayersInfo[1][0]=PlayersInfo[1][1]=PlayersInfo[2][0]=PlayersInfo[2][1]=0
                      while True:
                          for event in pygame.event.get():
                            if pygame.mouse.get_pressed() == (1, 0, 0):
                              return 
                  else:
                    X2 -= cube_answer * cube_width                

              #Snakes--------------------------------------------
                if Player2_Index == 17 and not SnakeQuestion(2,screen):
                  Player2_Index = 5
                  X2 += cube_width
                  Y2 += cube_length  # Going down
                  Right2 = True
                
                elif Player2_Index == 11 and not SnakeQuestion(2,screen) :
                  Player2_Index = 9
                  X2 -= cube_width
                  Y2 += cube_length  # Going down
                  Right2 = True
                    
                elif Player2_Index == 58 and not SnakeQuestion(2,screen):
                  Player2_Index = 18
                  Y2 += cube_length * 4  # Going down
                    
                elif Player2_Index == 34 and not SnakeQuestion(2,screen):
                  Player2_Index = 13
                  X2 += cube_width
                  Y2 += cube_length * 2  # Going down

                elif Player2_Index == 53 and not SnakeQuestion(2,screen):
                  Player2_Index = 49
                  X2 += 2 * cube_width
                  Y2 += cube_length  # Going down
                  Right2 = True
                    
                elif Player2_Index == 87 and not SnakeQuestion(2,screen):
                  Player2_Index = 66
                  X2 -= cube_width
                  Y2 += cube_length * 2  # Going down
                    
                elif Player2_Index == 98 and not SnakeQuestion(2,screen):
                  Player2_Index = 76
                  X2 += 2 * cube_width
                  Y2 += cube_length * 2  # Going down
                    
                elif Player2_Index == 92 and not SnakeQuestion(2,screen):
                  Player2_Index = 90
                  X2 += cube_width
                  Y2 += cube_length  # Going down
                  Right2 = True
                #END Snakes----------------------------------------
                
                #Ladders-------------------------------------------
                if Player2_Index == 6 and LadderQuestion(2,screen):
                  Player2_Index = 26
                  Y2 -= cube_length * 2  # Going up
                elif Player2_Index == 16 and LadderQuestion(2,screen):
                  Player2_Index = 36
                  Y2 -= cube_length * 2  # Going up
                elif Player2_Index == 21 and LadderQuestion(2,screen):
                  Player2_Index = 41
                  Y2 -= cube_length * 2  # Going up
                elif Player2_Index == 30 and LadderQuestion(2,screen):
                  Player2_Index = 51
                  Y2 -= cube_length * 3  # Going up
                  Right2 = False
                elif Player2_Index == 45 and LadderQuestion(2,screen):
                  Player2_Index = 76
                  Y2 -= cube_length * 3  # Going up
                  Right2 = False
                elif Player2_Index == 42 and LadderQuestion(2,screen):
                  Player2_Index = 82
                  Y2 -= cube_length * 4  # Going up
                elif Player2_Index == 68 and LadderQuestion(2,screen):
                  Player2_Index = 88
                  Y2 -= cube_length * 2  # Going up
                #END Ladders---------------------------------------
              
            #END Case of throwing a cube-----------------------------------------------------
            
            #~~~~~~~~~~~~~~~~~~~~~~
            if Change:
              Change = False
              # change gamer
              if TurnPlayer1:
                TurnPlayer1 = False
              else:
                TurnPlayer1 = True
              
              # change logo of gamer
              if logo == logo2:
                logo = logo1
              else:
                logo = logo2
              
          # Fixing the Plyaers Locations indexs
          X1,X2=FixIndex(X1,X2)
#---------------------------------------------------------------------
# end game snakes & ladders
