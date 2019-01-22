from IPython.display import clear_output
import random

def assign_side():
    global mark1
    global mark2
    mark1 = str(input("Player1 please choose your side:"))
    if mark1 == 'X':
        mark2 = 'O'
        print("Player2 you will play O")
    elif mark1 == 'O':
        mark2='X'
        print("Player2 you will play X")
    else:
        mark1 = input("You've writen a wrong symbol. Please choose between X or O    ")
        if mark1 == 'X':
            mark2 = 'O'
            print("Player2 you will play O")
        elif mark1 == 'O':
            mark2='X'
            print("Player2 you will play X")

def display_board(board):
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print(f"___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print(f"___|___|___")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print(f"   |   |   ")

def addposition(marker,board):
    position = 0
    while position not in range(1,10) or board[position] != " ":
        position = int(input("Add a position from one to nine:   "))
        if position not in range(1,10):
            print("Position is out of range")
        if position in range(1,10) and board[position] != " ":
            print("This cell has been filled already")
          
    board[position]=marker
    
def checking(marker,board):
    checksum = 0
    for x in board:
        if x == "X" or x == "O":
            checksum+=1
    if checksum == 9:
        return "Draw"
    elif board[1]==board[2]==board[3]==marker or board[4]==board[5]==board[6]==marker or board[7]==board[8]==board[9]==marker or board[1]==board[4]==board[7]==marker or board[2]==board[5]==board[8]==marker or board[3]==board[6]==board[9]==marker or board[7]==board[5]==board[3]==marker or board[1]==board[5]==board[9]==marker:
        return "Win"
    else:
        return "Continue"
    
def defineturn():
    if random.randint(0,10)>4:
        return "Player2"
    else:
        return "Player1"
        
def regame():
    plinput = " "
    while plinput != "Y" and plinput !="N":
        plinput = str(input("Do you want to play again Y/N:"))
    if plinput == "Y":
        Game_on = True
    elif plinput == "N":
        Game_on = False    


Game_on = True
while Game_on == True:
    boardlst = ["#"," "," "," "," "," "," "," "," "," "]
    assign_side()
    defineturn()
    checking(mark1,boardlst)
    checking(mark2,boardlst)
    if defineturn() == "Player1":
        while checking(mark1,boardlst) == "Continue" and checking(mark2,boardlst) == "Continue":
        
            clear_output()
            display_board(boardlst)
            print('Player1 turn')
            addposition(mark1,boardlst)
            if checking(mark1,boardlst) == "Continue":
                clear_output()
                display_board(boardlst)
                print('Player2 turn')
                addposition(mark2,boardlst)
    elif defineturn() == "Player2":            
        while checking(mark1,boardlst) == "Continue" and checking(mark2,boardlst) == "Continue":
            
            clear_output()
            display_board(boardlst)
            print('Player2 turn')
            addposition(mark2,boardlst)
            
            if checking(mark2,boardlst) == "Continue":
                clear_output()
                display_board(boardlst)
                print('Player1 turn')
                addposition(mark1,boardlst)
                
    if checking(mark1,boardlst) == "Win":
        clear_output()
        print("Player1 you are winner")
        regame()
        continue
    elif checking(mark2,boardlst) == "Win":
        clear_output()
        print("Player2 you are winner")
        regame()
        continue
    elif checking(mark1,boardlst) == "Draw" or checking(mark2,boardlst) == "Draw":
        clear_output()
        print("Draw")
        regame()
        continue
