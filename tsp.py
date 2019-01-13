#CS486 Assignment2 Question1.2
#20559425 Ye Wang

###This is a python implementation of tsp problem(hill climbing)
###To compile the program use command python3 tsp.py
###Then copy the instance to the command line and followed by the cost of the alternative solution (from piazza) to test the program

from scipy.spatial import distance
from random import shuffle
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
    global n
    lowest_cost = float("inf")
    i = 0
    while i < n :
        j = i + 1
        while j < n:
            temp_state = swap_elem(i,j,state)
            #print("neighbor after applying neighbor relation: ", temp_state)
            temp_cost = cost_cal(temp_state)
            #print("cost of this neignbor: ", temp_cost)
            if temp_cost <= lowest_cost:
                #print("this cost is <= the lowest cost neignbor(",lowest_cost,") we have so far.")
                lowest_cost = temp_cost
                temp_lowest_neighbor = temp_state
            j += 1
        i += 1
    #print("found the lowest cost neighbor with cost: ", temp_lowest_neighbor)
    return temp_lowest_neighbor

#hill_climbing algorithm implementation
def hill_climbing():
    global current_state,step_counter
    while True:
        #print("current state: ",current_state)
        next_neighbor = get_best_neighbor(current_state)
        cost = cost_cal(current_state)
        if cost <= cost_cal(next_neighbor):
            #print("found local optimal!")
            break
        current_state = next_neighbor
        #print("swaped to: ",next)
        #print("The neighbor ",next_neighbor," has lower cost than current state,make it the current state.")
        step_counter += 1
    return current_state

#take # of cities from command line
n = int(input())
#build the map
my_map = make_map(n)

#take the cost of the best solution from command line
best_cost = float(input())
print("data received. Calculating the 100 repititions now.")
#randomize the initial state
#current_state = state_initializer()
step_counter = 0
total_cost = 0
hit_counter = 0 #hit_counter increased if the solution hit with the best solution
temp_lowest_neighbor = []
i = 0
while i < 100:
    current_state = state_initializer()
    #print("my initial random state: ",current_state)
    if current_state == []:
        exit()
    final_state = hill_climbing()
    cost = cost_cal(final_state)
    #print("final state is: ",final_state)
    #print("cost of final state is: ",cost)
    total_cost += cost
    if cost >= best_cost-0.05 and cost <= best_cost+0.05:
        hit_counter += 1
    i += 1
#print("final result: ",final_state)
print("Average steps(100 repititions): ",step_counter/100)
print("Average cost(100 repititions): ",total_cost/(best_cost*100))
print("Toatl hit(100 repititions): ",hit_counter)
    

