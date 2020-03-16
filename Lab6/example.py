"""
CS 2302 - Data Structures
Instructor: Dr. Olac Fuentes
TA: Ismael Villanueva-Miranda
Lab 6: Algorithm Design Techniques
Author: Dilan Ramirez
Description:
    Experiment with three algorithm design techniques applied to the solution of three
    version of the knapsack problem.
Last Modification: Aug 5, 2019
Lab Report Link: https://drive.google.com/open?id=1wcU7CfshxBHe9ar8VkP4BzOiLi1qKi8V
"""

from datetime import datetime
start = datetime.now()
import numpy as np


'''
• Implement a backtracking algorithm that solves the optimization 0-1 knapsack problem. Instead of
deciding whether we can take items worth a predefined amount of money, as described in class, in
this version of the problem you need to find the highest-value load that can fit in the knapsack.

'''
def knapsack_Backtracking(capacity,weight,value,n):
    if capacity == 0 or n == 0: # if the capacity of the bag is 0 or there are no items to steal, so it returns 0
        return 0
    if len(weight) != len(value): #if the lenght of the lists are different, they cannot be compared so it returns 0
        return 0
    if weight[n-1] > capacity: # if it is not the case, the length of teh weight list is decresed by 1
        return knapsack_Backtracking(capacity,weight,value,n-1) # it returns a recursive call wich will decrese the length of the length of the values list
    else:
        return max(value[n-1] + knapsack_Backtracking(capacity-weight[n-1], weight, value, n-1), knapsack_Backtracking(capacity, weight, value,n-1)) #finally if it is not the case, it returns the max item


'''
 Implement a greedy algorithm that solves the optimization continuous knapsack problem. This
problem is identical the previous one, except that in this case we can take fractions of items. For
example, if we take 3/4 of an item that has value 2 and weight 3, the value of the fraction would be
3/2 and its weight would be 9/4
'''
def knapsack_Greedy(capacity, weight, values):
        items = []
        for i in range(len(weight)):
            items.append((weight[i], values[i], i)) # It creates a list with all the information from the weight, values and index.
        sorted(items, reverse=True) # This list is sorted to make it easier
        highest_value = 0
        for i in items: 
            curWeight = int(i[0]) #the first item of the first list is stored to then being compared
            curValue = int(i[1]) #the second item of the first list is stored to then being compared
            if capacity - curWeight >= 0: # we check if the capacity of the knapsack minus the current weight is greater to zero
                capacity -= curWeight # to then substract the current weight to the capacity of the snapsack to know that an item was taken and stored
                highest_value += curValue # the Highest value is stored
            else:
                fraction = capacity / curWeight # it it is not the case, so 
                highest_value += curValue * fraction # the highest value is multiplied by the faction which contains the capacity of the bag between the weight of the item
                capacity = int(capacity-(curWeight * fraction)) 
        return highest_value # returns the highest value found
    
'''
Implement a randomized algorithm that solves the optimization 0-1 knapsack problem. You should
generate many random permutations (you can use the numpy np.random.permutation(n)function)
of the items and, for every permutation, add the items to the knapsack one by one until the capacity
is reached. At the end, return the permutation that resulted in the largest value.
'''    
def knapsack_randomized_Backtracking(capacity, numitems, tries=10):
    highest_value, pos = -2302, 0
    perm, sack = [], []
    for i in range(tries):
        weight = np.random.permutation(numitems) # creates random permutations to find the highest value load
        values = np.random.permutation(numitems)
        perm.append(values) # the permutations are stored to then return the one that contains the highest value load
        sack.append(knapsack_Backtracking(capacity,weight,values,len(values))) # the backtracking algorithm is used to look for the highest value
    for i in range(len(sack)): # it looks for the index of the highest values and stores the highest value and its position
        if sack[i] > highest_value: 
            highest_value, pos = sack[i], i
    for j in range(len(perm)):  # finds the permutation that contains the highest values load
        if j == pos:
            return highest_value, perm[j] # returns the highest value load
        
'''
Implement a randomized algorithm that solves the optimization 0-1 knapsack problem. You should
generate many random permutations (you can use the numpy np.random.permutation(n)function)
of the items and, for every permutation, add the items to the knapsack one by one until the capacity
is reached. At the end, return the permutation that resulted in the largest value.
'''    
def knapsack_randomized_Greedy(capacity, numitems, tries=200):
    highest_value, pos = -2302, 0
    perm, sack = [], []
    for i in range(tries):
        weight = np.random.permutation(numitems) # creates random permutations to find the highest value load
        values = np.random.permutation(numitems)
        perm.append(values) # the permutations are stored to then return the one that contains the highest value load
        sack.append(knapsack_Greedy(capacity, weight, values)) # the Greedy algorithm is used to look for the highest value
    for i in range(len(sack)): # it looks for the index of the highest values and stores the highest value and its position
        if sack[i] > highest_value: 
            highest_value, pos = sack[i], i
    for j in range(len(perm)):  # finds the permutation that contains the highest values load
        if j == pos:
            return highest_value, perm[j] # returns the highest value load
    
'''
Implement a dynamic programming algorithm that solves the optimization integer knapsack problem.
In this case, the thief can take multiple instances of an item. As before, you need to find the highestvalue load that can fit in the knapsack. Hint: This problem is similar to the minimum coin problem
described in class.
'''    
def knapsac_Dynamic_Programming(numitems, weight, values, total):
    knapsack = [0 for i in range(numitems + 1)] # creates a list storing as many zeros as the length of the num of items that the knapsack can store 
    for i in range(numitems + 1): 
        for j in range(total):
            if weight[j] <= i:
                knapsack[i] = max(knapsack[i], knapsack[i-weight[j]] + values[j]) #searches for the max value stored in the weight and values
    return knapsack[numitems] # returns the highest value that the thief can steal


if __name__ == "__main__":
    weight = [10, 20, 35, 5, 20] 
    value = [200, 100, 120, 80, 90]
    Capacity = 5
    
    '''
    print("Exercise 1")
    Capacity = 8
    maxValueBacktracking = knapsack_Backtracking(Capacity,weight,value,len(value))
    print("weight: ", weight)
    print("value: ", value)
    print("Capacity:", Capacity)
    print("highest-value load:", maxValueBacktracking)
    backtracking_end = datetime.now() # finish time
    print('It took: {} seconds'.format(backtracking_end - start))
    print("")

    print("Exercise 2")
    maxValueGreedy = knapsack_Greedy(Capacity, weight, value)
    print("weight: ", weight)
    print("value: ", value)
    print("Capacity:", Capacity)
    print("Highest-value load that can fit in the knapsack using a Greedy Algorithm:", maxValueGreedy)
    Greedy_end = datetime.now()
    print('It took: {} seconds'.format(Greedy_end - start))
    print("")
    
    print("Exercise 3")
    maxValue_randomized_Backtracking = knapsack_randomized_Backtracking(15, 10, 50)
    print("weight: ", weight)
    print("value: ", value)
    print("Capacity:", 12)
    print("permutation that resulted in the largest value using Backtracking Algorithm: ",maxValue_randomized_Backtracking)
    randomized_Backtracking_end = datetime.now()
    print('It took: {} seconds'.format(randomized_Backtracking_end - start))
    print("")
    
    
    print("weight: ", weight)
    print("value: ", value)
    print("Capacity:", Capacity)
    print("Exercise 3")
    maxValue_randomized_Greedy = knapsack_randomized_Greedy(Capacity, 10, 50)
    print("permutation that resulted in the largest value using Greedy Algorithm: ", maxValue_randomized_Greedy)
    randomized_Greedy_end = datetime.now()
    print('It took: {} seconds'.format(randomized_Greedy_end - start))
    print("")
    
    '''
    print("Exercise 4")
    print("weight: ", weight)
    print("value: ", value)
    print("Capacity:", 2)
    maxValueDynamic = knapsac_Dynamic_Programming(Capacity, weight, value, len(value))
    print("Highest-value load that can fit in the knapsack using a Dynamic Programming Algorithm:", maxValueDynamic)
    Dynamic_end = datetime.now()
    print('It took: {} seconds'.format(Dynamic_end - start))
    