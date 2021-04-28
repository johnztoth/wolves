# wolves
 
In this model we have two types of agents; sheep and wolves.
The grass (environment) has a uniform length to start with.
The sheep randonly move by +/- 1 unit at a time.
When they move they eat 1 unit of grass where they land. 
They are not sick and there is no sharing.
As they eat the grass, their store increases.
The wolves randonly move by +/- 2 units at a time.
If a wolf gets within eating_range of a sheep it eats the sheep.
The wolf gets the sheep's store and the sheep agent is removed.

To run type> python wolf.py
