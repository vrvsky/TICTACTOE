import os
import time
def print_game(board):
    for i in range(0,9,3):
        print(board[i]+"|"+board[i+1]+"|"+board[i+2])
        if i!=6:
            print("-----")

def playercharchoice():
    player1_choice = 'XO'
    while player1_choice not in ['x','o']:
        player1_choice = input('Enter choice of x and o for player-1: ')
        player1_choice = player1_choice.lower()
        if player1_choice not in ['x','o']:
            print('Please enter either x or o ')
        
    if player1_choice=='x':
        player2_choice = 'o'
    else:
        player2_choice = 'x'
    return [player1_choice,player2_choice]
    
def results(gamefin):
    if gamefin==1:
        print("Game results in draw")
    elif gamefin==2:
        print("Player 1 won")
    else:
        print("Player 2 won")

def playerpos(playernum):
    position = 0
    while position not in ['1','2','3','4','5','6','7','8','9']:
        print("Enter player{} position: ".format(playernum+1),end="")
        position = input()
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('Please enter valid number in [1-9]')
        elif game_board[int(position)-1] in l:
            print('The position is already filled! ')
            position = 0
    return position
    
def game_result(board):
    horz1 = board[0]+board[1]+board[2]
    horz2 = board[3]+board[4]+board[5]
    horz3 = board[6]+board[7]+board[8]
    vert1 = board[0]+board[3]+board[6]
    vert2 = board[1]+board[4]+board[7]
    vert3 = board[2]+board[5]+board[8]
    cross1 = board[0]+board[4]+board[8]
    cross2 = board[2]+board[4]+board[6]
    resultlist = [horz1,horz2,horz3,vert1,vert2,vert3,cross1,cross2]
    if 'xxx' in resultlist:
        return 2
    elif 'ooo' in resultlist:
        return 3
    elif ' ' not in board:
        return 1
    else:
        return 0
print("Rules are as follows:\nPlayer 1 chooses X or O and the opposite is assigned to 2nd player")
print("Players positions are from 1 to 9 starting from top left and ending at bottom right")
print("1st player to get x or o 3 times horizontally or vertically or criss cross wins")
print("Sample board")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")
print("Loading game ")
time.sleep(10)
    
play_again = 'p'
while play_again!='n':
    game_board = [' ']*9
    os.system('cls')
    #os.system('clear') #[linux]
    i=0
    game_finished = 0
    l = playercharchoice()
    while game_finished==0:
        os.system('cls')
        print("Player 1 {} Player 2 {}\n".format(l[0],l[1]))
        #os.system('clear') #[linux]
        print_game(game_board)
        position = playerpos(i)
        game_board[int(position)-1] = l[i]
        i = (i+1)%2
        game_finished = game_result(game_board)
    os.system('cls')
    #os.system('clear') #[linux]
    print("Player 1 {} Player 2 {}\n".format(l[0],l[1]))
    print_game(game_board)
    results(game_finished)
    play_again = 'p'
    while play_again not in ['y','n']:
        play_again = input("Do you want to play again? Y or N: ")
        play_again = play_again.lower()
        if play_again not in ['y','n']:
            print("Enter either y or n only")
    
        
    
        
        
        
        
    
    
    
    
