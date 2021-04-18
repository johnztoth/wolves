""" sheepclass.py """

import random

class Sheep():

    def __init__ (self,grass):
        
        """ find no. of rows and columns in the environment list """
        self.rows=len(grass)
        self.cols=len(grass[0])
                
        """ initialise the sheep object with a randon position """
        self.x = random.randint(0,self.rows-1)
        self.y = random.randint(0,self.cols-1)
        self.grass = grass
        self.store = 0 
        
         
    def move(self):
        """ randonly move the sheep by one unit in x and y direction """
        """ keeping within boundaries """
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows
        else:
            self.y = (self.y - 1) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols


    def graze(self):
        """ graze 1 unit of the environment """
        if self.grass[self.y][self.x] > 0:
            self.grass[self.y][self.x] -= 1
            self.store +=1
        

    def __str__(self) :
        """ override print to print sheep location and store """
        """ PS this works in the iPython console but not in the command shell? """
        return ("y= " + str(self.y) + " x= " + str(self.x)\
                + " store= " + str(self.store))


    
    
    