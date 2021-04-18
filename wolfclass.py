""" wolfclass.py """

import random

class Wolf():

    def __init__ (self, grass):
        
        """ find no. of rows and columns in the environment list """
        self.rows=len(grass)
        self.cols=len(grass[0])
                
        """ initialise the wolf object with a randon position """
        self.x = random.randint(0,self.rows-1)
        self.y = random.randint(0,self.cols-1)
        self.store = 0 
        
         
    def move(self):
        """ randonly move the wolves by two units in x and y direction """
        """ keeping within boundaries """
        if random.random() < 0.5:
            self.y = (self.y + 2) % self.rows
        else:
            self.y = (self.y - 2) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 2) % self.cols
        else:
            self.x = (self.x - 2) % self.cols


    def __str__(self) :
        """ override print to print wolf location and store """
        """ PS this works in the iPython console but not in the command shell? """
        return ("y= " + str(self.y) + " x= " + str(self.x)\
                + " store= " + str(self.store))


    
    
    