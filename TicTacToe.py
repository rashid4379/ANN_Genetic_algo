import math as mt
import random
import numpy as np



class NeuralNetworks():
    def player_winner(board):
        if((board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1) or # across the top
        (board[1][0] == -1 and board[1][1] == -1 and board[1][2] == -1) or # across the middle
        (board[2][0] == -1 and board[2][1] == -1 and board[2][2] == -1) or # across the bottom
        (board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1) or # down the left side
        (board[0][1] == -1 and board[1][1] == -1 and board[2][1] == -1) or # down the middle
        (board[0][2] == -1 and board[1][2] == -1 and board[2][2] == -1) or # down the right side
        (board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1) or # diagonal
        (board[0][2] == -1 and board[1][1] == -1 and board[2][0] == -1)):
            return True
        else:
            return False
    ###########################################################################
    def comp_winner(board):
        if((board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or # across the top
        (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or # across the middle
        (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or # across the bottom
        (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or # down the left side
        (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or # down the middle
        (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or # down the right side
        (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or # diagonal
        (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1)):
            return True
        else:
            return False
    ############################################################################
    
    global sigmoid
    def sigmoid(x):
        return 1 / (1 + mt.exp(-x))
    ############################################################################
    
    def getBoardCopy(board):
        dupeBoard = []    
        for i in board:
            dupeBoard.append(i)    
        return dupeBoard
    
    
    def gen_random():
        rand = np.ndarray(shape = (1,81))
        for i in range(rand.shape[1]):
            rand[0,i] = random.uniform(-1,1)
        return rand
    
    def funct(board, rand):
        w=0
        lst=[]
        itr = 0
        for i in range(len(board)):
            for j in range(len(board)):
                for k in range(int((rand.size)/9)):
                    #print(board[i,j])
                    w = w + (board[i,j] * rand[0][itr])
                    itr = itr+1
                lst.append(w)
        
        arr = np.array(lst)
        arr = arr.reshape(3,3)
        for i in range(len(arr)):
            for j in range(len(arr)):
                arr[i][j] = sigmoid(arr[i][j])
        
        return arr
    
    