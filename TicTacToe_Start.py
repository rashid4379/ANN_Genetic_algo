import random
import numpy as np
import TicTacToe as tc
import G_Algorithm
import matplotlib.pyplot as plt

global flag
flag = True
global board



###############################################################################
def one():
    global flag
    global turn
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def two():
    global flag
    global turn
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def three():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def four():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def five():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def six():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def seven():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def eight():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

def nine():
    global turn
    global flag
    if(flag and turn == 'computer'):
        flag = False
        turn = 'player'
    else:
        flag = True
        turn = 'computer'

###############################################################################
def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

###############################################################################
global w_comp
global w_player


def play_game(board, rand1, rand2):
    global w_comp
    global w_player
    w_comp = False
    w_player = False
    board1= np.ones(shape=(3,3))
    middle_layer = tc.NeuralNetworks.funct(board1, rand1)
    output_layer = tc.NeuralNetworks.funct(middle_layer, rand2)
    
    for i in range(9):
#        print("Iteration : "+str(i))
#        print()
        dic = {}
        if(turn == 'computer'):         
#            print("Computer Turn: X")
            board_copy = tc.NeuralNetworks.getBoardCopy(board)
            loop = 0
            for j in range(len(board)):
                for k in range(len(board)):
                    if(board_copy[j][k] == 0):
                        dic1 = {loop:board_copy[j][k]}
                        dic.update(dic1)
                    loop = loop +1

            
            arr = output_layer

            arr1 = np.zeros(shape = (3,3))
            for i in dic.keys():
                if(i == 0):
                    arr1[0][0] = arr[0][0]
                elif(i == 1):
                    arr1[0][1] = arr[0][1]
                elif(i == 2):
                    arr1[0][2] = arr[0][2]
                elif(i == 3):
                    arr1[1][0] = arr[1][0]
                elif(i == 4):
                    arr1[1][1] = arr[1][1]
                elif(i == 5):
                    arr1[1][2] = arr[1][2]
                elif(i == 6):
                    arr1[2][0] = arr[2][0]
                elif(i == 7):
                    arr1[2][1] = arr[2][1]
                elif(i == 8):
                    arr1[2][2] = arr[2][2]

            i,j = np.unravel_index(arr1.argmax(), arr1.shape)
#            print("["+str(i)+"]["+str(j)+"]")

            if(i == 0 and j == 0):
                board[0][0] = 1
                one()
            elif(i == 0 and j == 1):
                board[0][1] = 1
                two()
            elif(i == 0 and j == 2):
                board[0][2] = 1
                three()
            elif(i == 1 and j == 0):
                board[1][0] = 1
                four()
            elif(i == 1 and j == 1):
                board[1][1] = 1
                five()
            elif(i == 1 and j == 2):
                board[1][2] = 1
                six()
            elif(i == 2 and j == 0):
                board[2][0] = 1
                seven()
            elif(i == 2 and j == 1):
                board[2][1] = 1
                eight()
            elif(i == 2 and j == 2):
                board[2][2] = 1
                nine()
        else:
#            print("Player's Turn: O")
            tick = None
            board_copy = tc.NeuralNetworks.getBoardCopy(board)
            loop = 0
            
            for j in range(3):
                for k in range(3):
                    if(board_copy[j][k] == 0):
                        dic1 = {loop:board_copy[j][k]}
                        dic.update(dic1)
                    loop = loop +1

            
            if(len(dic) > 1):
                tick, value = random.choice(list(dic.items()))
            elif(len(dic) == 1):
                tick = list(dic.keys())[0]

            if(tick != None):
                if(tick == 0):
                    board[0][0] = -1
                    one()
                elif(tick == 1):
                    board[0][1] = -1
                    two()
                elif(tick == 2):
                    board[0][2] = -1
                    three()
                elif(tick == 3):
                    board[1][0] = -1
                    four()
                elif(tick == 4):
                    board[1][1] = -1
                    five()
                elif(tick == 5):
                    board[1][2] = -1
                    six()
                elif(tick == 6):
                    board[2][0] = -1
                    seven()
                elif(tick == 7):
                    board[2][1] = -1
                    eight()
                elif(tick == 8):
                    board[2][2] = -1
                    nine()

        w_comp = tc.NeuralNetworks.comp_winner(board)
        w_player = tc.NeuralNetworks.player_winner(board)
        if(w_comp or w_player):
            break
###############################################################################       

def N_Average(lists):
    avg = []
    for i in range(len(lists)):
        a = 0
        summ = 0
        for j in range(len(lists)):
            if(lists[i][j] == 1):
                summ = summ + 1
        a = ((summ) / len(lists))
        avg.append(a)
    return avg

###############################################################################
def WinTime(ch):
    s = []
    for i in range(len(ch)):
        summ = 0
        for j in range(len(ch)):
            if(ch[i][j] == 1):
                summ = summ + 1
        s.append(summ)
    return s

###############################################################################
def learning(weights1, weights2):
    ch = []
    for i in range(len(weights1)):
        w1 = np.array(weights1[i])
        w2 = np.array(weights2[i])
        w1 = w1.reshape(1, w1.size)
        w2 = w2.reshape(1, w2.size)
        
        won = 0
        tie = 0
        won1 = 0
        ch1 = []
        for j in range(10):
            board = np.zeros(shape = (3,3))
            play_game(board, w1, w2)
            if(w_comp):
                won = won + 1
                ch1.append(1)
            elif(w_player):
                ch1.append(-1)
                won1 = won1 + 1
            else:
                ch1.append(0)
                tie = tie + 1
#                chrom1.append(0)
                #print("Tie")
        ch.append(ch1)
        print("Every 10 Games:")
        print("Comp: "+str(won))
        print("Pla: "+str(won1))
        print("Tie: "+str(tie))
        print()
    
    return ch


###############################################################################
global turn
turn = whoGoesFirst()

chromosom = []
weights = []

for j in range(10):
    rand = []
    won = 0
    tie = 0
    won1 = 0
    r1 = list(tc.NeuralNetworks.gen_random())
    r2 = list(tc.NeuralNetworks.gen_random())
    rand.append(r1)
    rand.append(r2)
    
    rand1 = np.array(r1)
    rand2 = np.array(r2)
    rand1 = rand1.reshape(1,rand1.size)
    rand2 = rand2.reshape(1,rand2.size)
    
    weights.append(rand)
    
#    print(weights)
    chrom1 = []
    for i in range(10):
        board = np.zeros(shape = (3,3))
        play_game(board, rand1, rand2)
        if(w_comp):
            won = won + 1
            #print("Computer")
            chrom1.append(1)
        elif(w_player):
            won1 = won1 + 1
            #print("Player")
            chrom1.append(-1)
        else:
            tie = tie + 1
            chrom1.append(0)
                #print("Tie")
    chromosom.append(chrom1)
    print("Comp: "+str(won))
    print("Pla: "+str(won1))
    print("Tie: "+str(tie))
    print()
###############################################################################
print()
print("#######################################################################")



final_ch = []
#Training the Neural Network  
for i in range(20):
    w1 = G_Algorithm.g_algo(chromosom, weights)
    fst = []
    scnd = []
    
    for j in range(len(w1)):
        fst.append(w1[j][0])
        scnd.append(w1[j][1])
    
    ch = learning(fst, scnd)
    s = WinTime(ch)
    final_ch.append(s)
    weights = w1
    chromosom = ch

#print(final_ch)
ch_avg = []
for i in range(len(final_ch)):
    a = sum(final_ch[i]) / float(len(final_ch[i]))
    ch_avg.append(a)


#print(final_ch)
print("########################################################")
#print(ch_avg)
#plt.plot(ch_avg)
