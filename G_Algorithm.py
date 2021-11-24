import random 
import numpy as np
import heapq

def g_algo(fitness, weights):
    f_values = []
    for i in range(len(fitness)):
        summ = 0
        for j in range(len(fitness)):
            if(fitness[i][j] == 1):
                summ = summ + 1
        f_values.append(summ)

#    print("weight")
#    print(weights)
#    print("fitness")
#    print(f_values)
#    print("fitness Length: "+str(len(fitness)))
#    print()
        
    #Removing minimum half
    counter = 0
#    print("Counter Start: "+str(counter))
    for i in range(int(len(fitness)/2)):
#        print(f_values)
        counter = counter + 1
        minimum = np.min(f_values)
        index = f_values.index(minimum)
        f_values.remove(minimum)
        #weights.remove(weights[index].any())
        del weights[index]
#    print("Counter After Remove: "+str(counter))
#    print("After removing minimum")
#    print("Length")
#    print(len(weights))
#    print("fitness")
#    print(f_values)
#    print()
#    
    #Crossover
    for i in range(int(len(fitness)/4)+1):
#        print(f_values)
        max1, max2 = heapq.nlargest(2, f_values)
        
        index1 = f_values.index(max1)
        index2 = f_values.index(max2)
        
        parent1 = weights[index1]
        parent2 = weights[index2]
#        print("Par1: "+str(len(parent2)))
        
        w1 = []
        w2 = []
        ran = random.randint(0, (len(parent1)))
        for i in range(len(parent1)):
            if (i <= ran):
                w1.append(parent1[i])
                w2.append(parent2[i])
            else:
                w1.append(parent2[i])
                w2.append(parent2[i])
        
        #Mutation
        for i in range(int(len(parent1) * 0.1)):
            ran1 = random.randint(0, (len(parent1) - 1))
            ran2 = random.uniform(-1,1)
            ran3 = random.randint(0, (len(parent1) - 1))
            ran4 = random.uniform(-1,1)
            w1[ran1] = ran2
            w2[ran3] = ran4
        
        weights.append(w1)
        counter = counter - 1
#        print("Counter: "+str(counter))
        weights.append(w2)
        counter = counter - 1
#        print("Counter: "+str(counter))
    
#    print("Counter After Crossover "+str(counter))
#    print("Length")
#    print(len(weights))
    #Crossover and Mutation if....
   
    if(counter != 0):
        length = len(weights)
        del weights[length-1]
        counter = counter + 1
        
    return (weights)


###############################################################################

# =============================================================================
# fitness = []
# for i in range(9):
#     lst = []
#     for j in range(9):
#         ran = random.randint(-1,1)
#         lst.append(ran)
#     fitness.append(lst)
# 
# weights = []
# for i in range(9):
#     w =[]
#     for j in range(9):
#         w.append(random.randint(-1,1))
#     weights.append(w)
#     
# =============================================================================

