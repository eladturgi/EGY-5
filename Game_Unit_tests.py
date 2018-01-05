import Game
import connect_four
import LaddersAndSnakes
import unittest

#help board for unit test connect 4
empty=None
Board = [{0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":154, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":226, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":298, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":370, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":442, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":514, "Revenue":0},
                    {0:empty, 1:empty, 2:empty, 3:empty, 4:empty, 5:empty, "Y":534, "X":586, "Revenue":0}]

 
class Test(unittest.TestCase):
    
    #help function check snakes and ladders dictionaries and verify that all the 15 question are inside
    def is_all_question_in_dict(self,dictName):
        for i in range(1,16):
            if i not in dictName:
                return False
            return True 
        
    def test_ladders_questions_dictionary(self):
        result=self.is_all_question_in_dict(LaddersAndSnakes.LQuestions)
        self.assertTrue(result, "error!not all ladders questions are inside his dictionary!")
        
    def test_snakes_questions_dictionary(self):
        result=self.is_all_question_in_dict(LaddersAndSnakes.SQuestions)
        self.assertTrue(result, "error!not all snakes questions are inside his dictionary!")
        
    def test_roll_dice(self):
        #testing if cube dice roll will give answer between 1-6
        answer=LaddersAndSnakes.roll()
        self.assertTrue(1<=answer<=6, "wrong dice number! not between 1-6")
        
    def test_fix_index_player1(self):
        #testing the ability of fixing index of player in the game
        X1location,X2location=20,100
        self.assertEqual(LaddersAndSnakes.FixIndex(X1location,X2location), (17,128), "wrong index fixing! player1 or player2 index is not fixed!")
    
    def test_empty_board(self):
         #testing case that the board is empty
         self.assertTrue(connect_four.IsEmptyBoard(Board),"problem! the board is ready but the function does not recognize it!")
    
    def test_NotEmpty_board(self):
        #testing case that we allready inserted 1 token
        connect_four.add_artificial_token(0, "red",Board) #insert the new token
        self.assertFalse(connect_four.IsEmptyBoard(Board),"problem! the board is not empty but the function does not recognize it!")
        connect_four.Remove_artificial_token(0,Board) #remove the token
        
    
    def test_insert_function(self):
        #testing if insert function really inserts token
        connect_four.add_artificial_token(3, "yellow",Board) #insert the new token
        self.assertFalse(connect_four.IsEmptyBoard(Board), "error! insert function does not inserts any token!")
        
        
    def test_remove_function(self):
       #testing if insert function really removes token
        connect_four.Remove_artificial_token(3,Board)   #insert the new token
        self.assertTrue(connect_four.IsEmptyBoard(Board), "error! remove function does not removes the necessary token!")
        
        
    def test_artificial_intelligence(self):
        #testing the ability of the pc to find suitable move to play
        PC_choice = connect_four.Artificial_intelligence2("red", 1,Board) # 1-means sequence length
        self.assertIsNotNone( PC_choice, "error! the pc cannot find suitable location for insert token!")
    
    def test_artificial_intelligence_win(self):
        #testing the ability of the pc to find suitable move to win the game
        #insert tokens for creation of suitable case
        connect_four.add_artificial_token(3, "yellow",Board) #insert the new token
        connect_four.add_artificial_token(3, "yellow",Board) #insert the new token
        connect_four.add_artificial_token(3, "yellow",Board) #insert the new token  
        #-----------------------------------------------------------------------------
        
        #TEST:
        PC_choice = connect_four.Artificial_intelligence2("yellow", 4,Board) #4means sequence length
        self.assertEqual(PC_choice,3, "error! the pc cannot recognize situation to win the game (col number 3)!")
        
        #remove all tokens
        connect_four.Remove_artificial_token(3,Board) #remove the token
        connect_four.Remove_artificial_token(3,Board) #remove the token
        connect_four.Remove_artificial_token(3,Board) #remove the token
        #--------------------------------------------------------------   
        
    def test_winner_function1(self):
        #testing the ability of winner function to recognize if player or pc won the game
        connect_four.add_artificial_token(1, "red",Board) #insert the new token ,col=1
        connect_four.add_artificial_token(2, "red",Board) #insert the new token ,col=2
        connect_four.add_artificial_token(3, "red",Board) #insert the new token ,col=3
        
        result=connect_four.winner(3 , "red" , 1 , 4 , Board) #col=3,color=red,row-1=1,SeqLen=4
        
        self.assertFalse(result, "error! winner function return True for win situation in mistake!")
        
    def test_winner_function2(self):
          #testing the ability of winner function to recognize if player or pc won the game
          
        connect_four.add_artificial_token(4, "red",Board) #insert the new token, col=4
          
        #TEST:
        result=connect_four.winner(3 , "red" , 1 , 4 , Board) #col=3,color=red,row-1=1,SeqLen=4 
        self.assertTrue(result, "error! winner function does not recognize win situation!")
        
        #remove all tokens
        connect_four.Remove_artificial_token(1,Board) #remove the token
        connect_four.Remove_artificial_token(2,Board) #remove the token
        connect_four.Remove_artificial_token(3,Board) #remove the token
        connect_four.Remove_artificial_token(4,Board) #remove the token
        
    def test_reset_ladders_and_snakes_not_running(self):
        #testing that reset dictionary questions function is not working
        self.assertFalse(LaddersAndSnakes.reset_running, "error! reset questions function has been activated!")
        
    def test_reset_connect_four_not_running(self):
        #testing that reset winning listfunction is not working
        self.assertFalse(connect_four.reset_list_running, "error! reset questions function has been activated!")    
    
    def test_initial_2players_right_answers_is_zero(self):
        #testing that the initial amount of right answers for both players is zero
        result=LaddersAndSnakes.PlayersInfo[1][1]+LaddersAndSnakes.PlayersInfo[2][1]
        self.assertEqual(result, 0, "error! 2 players initial number of right answers is not zero!")
            
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

