"""
Wolf

In this model we have two types of agents; sheep and wolves.
The grass (environment) has a uniform length to start with.
The sheep randonly move by +/- 1 unit at a time.
When they move they eat 1 unit of grass where they land. 
They are not sick and there is no sharing.
As they eat the grass their store increases.
The wolves randonly move by +/- 2 units at a time.
If a wolf gets within eating_range of a sheep it eats the sheep.
The wolf gets the sheep's store and the sheep agent is removed.
"""

import matplotlib.pyplot
import random
import sheepclass
import wolfclass
import numpy as np


num_of_sheep = 10
num_of_wolves = 2
num_of_iterations = 1000
eating_range = 10
grass_length = 100

""" sheep list and wolf list, and the store totals for graphing"""
sheep = []
wolves = []
shuffled = []
sheep_store = np.zeros(num_of_iterations, dtype=int)
wolf_store = np.zeros((num_of_iterations,num_of_wolves), dtype=int)

""" create flat grass """
grass=[]
no_rows=300
no_cols=300

for i in range(1, no_rows):    
    rowlist=[]
    for j in range(1, no_cols):  
        rowlist.append(grass_length)     
    grass.append(rowlist)

""" distance between wolf and sheep """
def distance_between(wolf,sheep):
    dy=wolf.y-sheep.y
    dx=wolf.x-sheep.x
    return((dx**2+dy**2)**0.5)

""" Make the sheep using the Sheep class """
for i in range(num_of_sheep):        
    sheep.append(sheepclass.Sheep(grass))

""" Make the wolves using the Wolf class """
for i in range(num_of_wolves):        
    wolves.append(wolfclass.Wolf(grass))

""" time steps """
for step in range(num_of_iterations):
    
    """ move the sheep and graze the grass """
    for i in range(num_of_sheep):
        sheep[i].move()
        sheep[i].graze()
    
    """ update the total sheep store """
    for i in range(num_of_sheep):
        sheep_store[step] += sheep[i].store

    """ move the wolves """
    for i in range(num_of_wolves):
        wolves[i].move()

    """ wolves eat the sheep if the sheep get too close """
    """ shuffle wolves so each wolf gets first chance to eat sheep """
    shuffled = random.sample(wolves,len(wolves)) 
    for i in range(num_of_wolves):
        sheep_temp=sheep[:]    # temporary list for calculating distances
        eaten=0 
        for j in range(num_of_sheep):
            distance=distance_between(shuffled[i],sheep_temp[j])
            if distance <= eating_range:
                del sheep[j-eaten]   # remove sheep from real list
                print("iteration",step,"sheep eaten by wolf")
                eaten += 1
                shuffled[i].store += sheep_temp[j].store
        num_of_sheep -= eaten
    
    """ update the wolf store for each wolf """
    for i in range(num_of_wolves):
        wolf_store[step,i]=wolves[i].store

    """ break from iterations if no sheep left """
    if num_of_sheep == 0:
        print("zero sheep left")
        break


""" plot the sheep store """
matplotlib.pyplot.figure(1)
matplotlib.pyplot.plot(sheep_store, color='blue')
for i in range(num_of_wolves):
    matplotlib.pyplot.plot(wolf_store[:,i])
matplotlib.pyplot.xlabel("no of iterations")
matplotlib.pyplot.ylabel("units stored")
matplotlib.pyplot.show()

""" plot the sheep, wolves and grass """
matplotlib.pyplot.figure(2)
matplotlib.pyplot.xlim(0, no_cols)
matplotlib.pyplot.ylim(0, no_rows)
matplotlib.pyplot.imshow(grass)
for i in range(num_of_sheep):
    matplotlib.pyplot.scatter(sheep[i].x,sheep[i].y,color="blue")
for i in range(num_of_wolves):
    matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y,color="red")
matplotlib.pyplot.show()







