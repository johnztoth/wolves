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

num_of_sheep = 10
num_of_wolves = 6
num_of_iterations = 1000
eating_range = 10
grass_length = 100

""" sheep list and wolf list """
sheep = []
wolves = []

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
    
    """ move the wolves """
    for i in range(num_of_wolves):
        wolves[i].move()

    """ wolves eat the sheep if the sheep get too close """
    """ shuffle wolves so each wolf gets first chance to eat sheep """
    random.shuffle(wolves)
    for i in range(num_of_wolves):
        sheep_temp=sheep[:]
        eaten=0 
        for j in range(num_of_sheep):
            distance=distance_between(wolves[i],sheep_temp[j])
            if distance <= eating_range:
                del sheep[j-eaten]
                print("sheep eaten by wolf")
                eaten += 1
                wolves[i].store += sheep_temp[j].store
        num_of_sheep -= eaten
    
    """ break from iterations if no sheep left """
    if num_of_sheep == 0:
        print("zero sheep left")
        break

""" plot the sheep, wolves and grass """
matplotlib.pyplot.xlim(0, no_cols)
matplotlib.pyplot.ylim(0, no_rows)
matplotlib.pyplot.imshow(grass)
for i in range(num_of_sheep):
    matplotlib.pyplot.scatter(sheep[i].x,sheep[i].y,color="blue")
for i in range(num_of_wolves):
    matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y,color="red")
matplotlib.pyplot.show()







