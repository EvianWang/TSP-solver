#CS486 Assignment2 Question1.5
#20559425 Ye Wang

###This is a python implementation of tsp problem(hill climbing with random restarts)
###To compile the program use command python3 tsp_randomrestarts.py
###Then copy the instance to the command line and followed by the cost of the alternative solution (from piazza) and the number of restars to test the program

from scipy.spatial import distance
from random import shuffle
import copy
import time
#helper function stores the cities' coordinates
def make_map(n):
	my_map = []
	i = 0
	while i < n:
		s = input()
		temp = s.split(" ")
		map_entry = (temp[0],int(temp[1]),int(temp[2]))
		my_map.append(map_entry)
		i += 1
	return my_map

#helper function for calculating the euclidean distance
def euc_dist(entry1,entry2):
	coord1 = (entry1[1],entry1[2])
	coord2 = (entry2[1],entry2[2])
	dist = distance.euclidean(coord1,coord2)
	return dist

#helper function for generating a random initial state
def state_initializer():
    global n
    if n == 14:
        initial_state = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
        shuffle(initial_state)
        return initial_state
    elif n == 15:
        initial_state = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        shuffle(initial_state)
        return initial_state
    elif n == 16:
        initial_state = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
        shuffle(initial_state)
        return initial_state
    elif n == 5:
        initial_state = ['A','B','C','D','E']
        shuffle(initial_state)
        return initial_state
    elif n == 6:
        initial_state = ['A','B','C','D','E','F']
        shuffle(initial_state)
        return initial_state
    elif n == 7:
        initial_state = ['A','B','C','D','E','F','G']
        shuffle(initial_state)
        return initial_state

    elif n == 36:
        initial_state = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ']
        shuffle(initial_state)
        return initial_state
    else:
        print("The number of cities is not supported by the program")
        return []

#helper function for find the entry in the map based on the city name
def find_entry(name):
    global my_map,n
    i = 0
    while i < n:
        if my_map[i][0] == name:
            return my_map[i]
        i += 1

#helper function for calculating total cost of a state
def cost_cal(state):
    global my_map,n
    cost = 0
    i = 0
    while i < n-1:
        entry1 = find_entry(state[i])
        entry2 = find_entry(state[i+1])
        temp = euc_dist(entry1,entry2)
        cost += temp
        i += 1
    entry_start = find_entry(state[0])
    entry_end = find_entry(state[n-1])
    temp = euc_dist(entry_start,entry_end)
    cost += temp
    return cost

#helper function for swapping two elements in the state
def swap_elem(ind1,ind2,state):
    state_copy = state.copy()
    temp = state_copy.pop(ind1)
    state_copy.insert(ind2,temp)
    temp = state_copy.pop(ind2-1)
    state_copy.insert(ind1,temp)
    return state_copy

#helper function for finding the best neighbor of current node
def get_best_neighbor(state):
    global n,temp_lowest_neighbor
    lowest_cost = float("inf")
    i = 0
    while i < n :
        j = i + 1
        while j < n:
            temp_state = swap_elem(i,j,state)
            temp_cost = cost_cal(temp_state)
            if temp_cost <= lowest_cost:
                lowest_cost = temp_cost
                temp_lowest_neighbor = temp_state
            j += 1
        i += 1
    return temp_lowest_neighbor

#hill_climbing algorithm implementation
def hill_climbing():
    global current_state,step_counter,total_restarts,restarts_counter,temp_lowest_neighbor,current_optima
    while restarts_counter < total_restarts+1:
        next_neighbor = get_best_neighbor(current_state)
        temp_lowest_neighbor = []
        cost = cost_cal(current_state)
        if cost <= cost_cal(next_neighbor):
            current_state_copy = copy.deepcopy(current_state)
            if cost < current_optima[1]:
                current_optima = (current_state_copy,cost)
            current_state = state_initializer()
            step_counter += 1
            restarts_counter += 1
            #break
        else:
            current_state = next_neighbor
            step_counter += 1
    restarts_counter = 0
    return current_optima[0]

start_time = time.time()
#take # of cities from command line
n = int(input())
#build the map
my_map = make_map(n)

#take the cost of the best solution from command line
best_cost = float(input())
#take the number of restarts from command line
total_restarts = int(input())

print("data received. Calculating the 100 repititions now.")
#randomize the initial state
#current_state = state_initializer()
step_counter = 0
total_cost = 0
hit_counter = 0 #hit_counter increased if the solution hit with the best solution
restarts_counter = 0

current_optima = (None,float("inf"))
temp_lowest_neighbor = []
i = 0
while i < 100:
    current_state = state_initializer()
    if current_state == []:
        exit()
    final_state = hill_climbing()
    current_optima = (None,float("inf"))
    cost = cost_cal(final_state)
    #print("final state is: ",final_state)
    #print("cost of final state is: ",cost)
    total_cost += cost
    if cost >= best_cost-0.05 and cost <= best_cost+0.05:
        hit_counter += 1
    i += 1

print("Average steps(100 repititions): ",step_counter/100)
print("Average cost(100 repititions): ",total_cost/(best_cost*100))
print("Toatl hit(100 repititions): ",hit_counter)
print("--- %s seconds ---" % (time.time() - start_time))
    

