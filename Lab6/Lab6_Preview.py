import numpy as np

def knapsack(capacity,weight,value,n):
    # print("capacity:", capacity, ", n:", n)
    if capacity == 0 or n == 0:
        return 0
    if len(weight) != len(value):
        return 0
    if weight[n-1] > capacity:
        return knapsack(capacity,weight,value,n-1)
    else:
        return max(value[n-1] + knapsack(capacity-weight[n-1], weight, value, n-1), knapsack(capacity, weight, value,n-1))

def randomized_knapsack(capacity, numitems, tries=10):
    largest_value, pos = -2302, 0
    perm, sack = [], []
    for i in range(tries):
        weight = np.random.permutation(numitems)
        values = np.random.permutation(numitems)
        perm.append(values)
        sack.append(knapsack(capacity,weight,values,len(values)))
    # print(sack)
    for i in range(len(sack)):
        if sack[i] > largest_value:
            largest_value, pos = sack[i], i
    # print(largest_value,pos)
    for j in range(len(perm)):
        # print(perm[j])
        if j == pos:
            return largest_value, perm[j]

wt = [1,2,3,4]
val = [2,2,6,7]
maxValue = GreedyKnapsack()

'''
weight = [1, 2, 3, 4]
value = [2, 2, 6, 7]
print("Exercise 1")
print("highest-value load:", knapsack(3,weight,value,len(value)))
print("")
print("Exercise 3")
print("permutation that resulted in the largest value: ",randomized_knapsack(15, 5, 10))
'''


'''
#Exercise 3
f1 = 'x*x + x - 12'
f2 = 'x*x + x + 12'
print(equal(f1,f2,10, 0.0001))
'''
