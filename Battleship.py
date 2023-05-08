#####DECLARING OBJECTS AND LOOPS#####
player1Win=0
player1Loss=0
player2Win=0
player2Loss=0
Loops = True
#####DECLARING OBJECTS AND LOOPS#####





#####MAKES THE GUESSING BOARDS AND VARIABLES TO DECIDE WHO WINS#####
while Loops:
     global guessingboard1
     guessingboard1=[[" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "]]
     global guessingboard2
     guessingboard2=[[" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "],
                     [" "," "," "," "," "," "," "," "," "," "]]
     checkboard1 = 0
     checkboard2 = 0
#####MAKES THE GUESSING BOARDS AND VARIABLES TO DECIDE WHO WINS#####
     
     
     
     
     
#####OUR CLASS TO CHECK TO MAKE SURE THE USER TYPES IN A VALID INPUT#####
     class CheckInput:
     
          @staticmethod
          def getCorrectInput(listOfAnswers,question):
               c=""
               while not (c in listOfAnswers):
                    c = input(question)
               return int(c) 
#####OUR CLASS TO CHECK TO MAKE SURE THE USER TYPES IN A VALID INPUT#####



     
     
#####CLASS TO PRINT PLAYER1'S BOARD#####
     def player1board():
          
          #creats the 10 by 10 board
          def printBoard(board):
               for r in range(10):
                    print(board[r][0]+"|"+board[r][1]+"|"+board[r][2]+"|"+board[r][3]+"|"+board[r][4]+"|"+board[r][5]+"|"+board[r][6]+"|"+board[r][7]+"|"+board[r][8]+"|"+board[r][9])
          
          
          #returns a true or false value on whether we can choose that spot
          def chooseSpot(r,c,symbol,board):
               #if the spot is open
               if board[r][c] == " ":
                    #add the symbol and return true
                    board[r][c]=symbol
                    return True    
               return False
     
          #List that will use the function above to turn into a playing board
          global board
          board=[[" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "],
                 [" "," "," "," "," "," "," "," "," "," "]]
          
          #Boat symbol
          symbol="O"
     
          #Code repeats 5 times
          for i in range(5):
               printBoard(board)
               print("\n")
               print("Place your ships 1-10")
               #place player 1 ships
               r=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Player 1 Place your ship row: ")-1
               c=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Plater 1 Place your ship column: ")-1
               printBoard(board)
               print("\n")    
               
               #If you choose a spot you already chose before, It will ask you again
               if (not chooseSpot(r,c,symbol,board)):
                              print("Spot Taken")
          printBoard(board)
#####CLASS TO PRINT PLAYER1'S BOARD#####
     
     
     
     
#####FUNCTION TO PRINT OUT PLAYER2'S BOARD#####
     def player2board():
          #Prints out the board
          def printBoard2(board2):
               for r in range(10):
                    print(board2[r][0]+"|"+board2[r][1]+"|"+board2[r][2]+"|"+board2[r][3]+"|"+board2[r][4]+"|"+board2[r][5]+"|"+board2[r][6]+"|"+board2[r][7]+"|"+board2[r][8]+"|"+board2[r][9])
     
          #returns a true or false value on whether we can choose that spot
          def chooseSpot2(r,c,symbol,board2):
               #if the spot is open
               if board2[r][c] == " ":
                    #add the symbol and return true
                    board2[r][c]=symbol
                    return True    
               return False
     
          global board2
          board2=[[" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "],
                  [" "," "," "," "," "," "," "," "," "," "]]
          symbol="O"
          
          for i in range(5):
               printBoard2(board2)
               print("\n")
               print("Place your ships 1-10")
               #place player 2 ship
               r=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Player 2 Place your ship row: ")-1
               c=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Player 2 Place your ship column: ")-1
               #print player 2 board
               printBoard2(board2)
               print("\n")    
               if (not chooseSpot2(r,c,symbol,board2)):
                              print("Spot Taken")
          printBoard2(board2)
#####FUNCTION TO PRINT OUT PLAYER2'S BOARD#####
     
     
     
     
     
#####CHECKS THE GUESSING OF PLAYER 1 TO FIND WHERE PLAYER 2'S SHIPS ARE#####
     def playersguessing():
          
          def guessingboard(guessingboard1):
               for r in range(10):
                    print(guessingboard1[r][0]+"|"+guessingboard1[r][1]+"|"+guessingboard1[r][2]+"|"+guessingboard1[r][3]+"|"+guessingboard1[r][4]+"|"+guessingboard1[r][5]+"|"+guessingboard1[r][6]+"|"+guessingboard1[r][7]+"|"+guessingboard1[r][8]+"|"+guessingboard1[r][9])
     
     
          
     
          symbol = "X"
          symbol2 = "O"
          print(""" if o = missed \nif x mean you hit a ship""")
          r=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Where is player2's ship? row: ")-1
          c=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Where is player2's ship? column: ")-1
          if board2[r][c] == "O":
          #add the symbol and return true
               guessingboard1[r][c]=symbol
               global checkboard1
               checkboard1 += 1
               
          elif guessingboard1[r][c] == " ":
                    #add the symbol and return true
                    guessingboard1[r][c]=symbol2
                    
                    
                    
          guessingboard(guessingboard1) 
          return True
#####CHECKS THE GUESSING OF PLAYER 1 TO FIND WHERE PLAYER 2'S SHIPS ARE#####
     
     
     
     
     
#####CHECKS THE GUESSING OF PLAYER 2 TO FIND WHERE PLAYER 1'S SHIPS ARE#####
     def playersguessing2():
          
          def secondplayerguessingboard(guessingboard2):
               for r in range(10):
                    print(guessingboard2[r][0]+"|"+guessingboard2[r][1]+"|"+guessingboard2[r][2]+"|"+guessingboard2[r][3]+"|"+guessingboard2[r][4]+"|"+guessingboard2[r][5]+"|"+guessingboard2[r][6]+"|"+guessingboard2[r][7]+"|"+guessingboard2[r][8]+"|"+guessingboard2[r][9])
     
          
          # X=hit O=miss
          symbol = "X"
          symbol2 = "O"
          print(""" if o = missed \nif x mean you hit a ship""")
          r=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Where is player1's ship? row: ")-1
          c=CheckInput.getCorrectInput(["1","2","3","4","5","6","7","8","9","10"],"Where is player1's ship? column: ")-1
          if board2[r][c] == "O":
          #add the symbol and return true
               guessingboard2[r][c]=symbol
               global checkboard2
               checkboard2 += 1
          elif guessingboard2[r][c] == " ":
                    #add the symbol and return true
                    guessingboard2[r][c]=symbol2
          secondplayerguessingboard(guessingboard2) 
#####CHECKS THE GUESSING OF PLAYER 2 TO FIND WHERE PLAYER 1'S SHIPS ARE#####         
     
     
     
     
#####WHERE ALL OF THE FUNCTIONS AND CLASSES RUN, PRINTS THE BOARD, AND CHECKS THE BOARDS FOR SYMBOLS#####

     #Uses the board print out functions
     
     #The title page ascii art
     print('''
From: Charles Shannon Hendrix 
                                                    Rats... my recruiter
                                              _     said I'd be on a sub
                                      /    _,'|     in the South Pacific...
                                     /_ _,'   |     
                                    $$;'     _;     
                    ,-'-._    ,-'. ,-'    _.'
                    \     `-,'  ,-'    _,'
   _od8PP8booo   ,....       ;,'    ,,'  _____
 d8P''         ,'     \   _,'    ,-' ,oo8P"""Y8.
 `'             `-.    i,'    ,-',odPP''      8b
                   `-,'    ,-',o8P'          ,8P
                .',-'   ,-',o8P'             d8
             .'.-'  _,-',o8P'               ,8P
           ',-'  _,' _o8P'                  dP
8bo,     _,'  _,'  ,dP'                    d8
  Y8'    \ ,,'  ,o8P'                    _op'                     _,d8P
  dP      '  ,o8P'                     ,o8'                   ,oo8P"'
  Yb     _oo8P'                      ,dP'                 ,odPP''
   Ybooo8P''                       ,dP'              _,odPP'
     ''                           o8'            _oo8P"'
                                ,8P         _,odPP''
                               d8'    __,odPP"'
                               Y8oooo8PP"'
                                ~~~~~~
           ''')
     
     
     player1board()
     print("""
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~oo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 o o
                                 o ooo
                                   o oo
                                      o o      |   #)
                                       oo     _|_|_#_    -Scott Mason-
                                         o   | 751   |
    __                    ___________________|       |_________________
   |   -_______-----------                                              \
  >|    _____                                                   --->     )
   |__ -     ---------_________________________________________________ /
           """)
         
     player2board()
     # print('####\n,\n,\n,\n,\n,\n,\n')
     print("""
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~oo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 o o
                                o ooo
                                   o oo
                                      o o      |   #)
                                       oo     _|_|_#_    -Scott Mason-
                                         o   | 751   |
    __                    ___________________|       |_________________
   |   -_______-----------                                              \
  >|    _____                                                   --->     )
   |__ -     ---------_________________________________________________ /
           """)
     
     #Checks to see who won
     loop = 0
     while loop == 0:
          playersguessing()
          if checkboard1 == 5:
               loop = 1
               print("player1")
               break
          if checkboard2 == 5:
               loop = 1
               print("player2")
               break
          
          
          playersguessing2()
          if checkboard1 == 5:
               loop = 1
          if checkboard2 == 5:
               loop = 1
     #Keeps track of how many wins and losses player1 and player2 has. Players have the option to play again, reset scores, or stop playing.
     if checkboard1 == 5:
          print("Player1 wins!")
          player1Win+=1
          player2Loss+=1
          print(f"Player1 Wins:{player1Win} loss:{player1Loss}")
          print(f"Player2 Wins:{player2Win} loss:{player2Loss}")
          ui = input("Want to play again 1 for yes 2 for reset score 3 for quit")
          if ui == "2":
               player1Win=0
               player1Loss=0
               player2Win=0
               player2Loss=0
          elif ui == "3":
               break
          else:
               continue
     if checkboard2 == 5:
          print("Player2 Wins!")
          player1Loss+=1
          player2Win+=1
          print(f"Player1 Wins:{player1Win} loss:{player1Loss}")
          print(f"Player2 Wins:{player2Win} loss:{player2Loss}")
          ui = input("Want to play again 1 for yes 2 for reset score 3 for quit")
          if ui == "2":
               player1Win=0
               player1Loss=0
               player2Win=0
               player2Loss=0
          elif ui == "3":
               break
          else:
               continue
#####WHERE ALL OF THE FUNCTIONS AND CLASSES RUN, PRINTS THE BOARD, AND CHECKS THE BOARDS FOR SYMBOLS#####
     
               
          
     
     
     
     
     