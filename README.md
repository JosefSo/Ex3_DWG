# Ex3_DWG

This is the third assignment this semester in the course OOP, in this assignment we had to to implement directed weighted graph like in the last 
assignment but this time in python.
Like in the last one we implemented algorithms of Traveller Salesman Problem and Dijkstra.

link to the wiki: <br>
https://github.com/JosefSo/Ex3_DWG/wiki

## Pre-Work

We already implemented this algorithms so we used the same as in the previous assigment: <br>
https://github.com/SaliSharfman/Ex2_DirectedWeightedGraph.git


## Algorithms 

🔹Center: finding a central node (node with the minimal sum weight of edges that get out of it to all other nodes). Our algorithm for finding center is based on dijkstra unlike the previous time.

🔹Shortest path: finding the shortest path between two nodes and its length. Our algorithm for finding shortest path is based on Dijkstra algorithm.

🔹TSP:(not real tsp but very close to it): finding the shortest path between all given nodes on the graph. We've used ACO (Ant colony optimization) algorithm to solve this problem. ACO is a probabilistic technique for solving computational problems which can be reduced to finding good paths through graphs.<br> A little bit more about the algorithm:<br> Artificial ants stand for multi-agent methods inspired by the behavior of real ants. The pheromone-based communication of biological ants is often the predominant paradigm used.[2] Combinations of artificial ants and local search algorithms have become a method of choice for numerous optimization tasks involving some sort of graph, e.g., vehicle routing and internet routing.

As an example, ant colony optimization[3] is a class of optimization algorithms modeled on the actions of an ant colony.[4] Artificial 'ants' (e.g. simulation agents) locate optimal solutions by moving through a parameter space representing all possible solutions. Real ants lay down pheromones directing each other to resources while exploring their environment. The simulated 'ants' similarly record their positions and the quality of their solutions, so that in later simulation iterations more ants locate better solutions.[5] One variation on this approach is the bees algorithm, which is more analogous to the foraging patterns of the honey bee, another social insect.

## matplotlib

We used matplotlib to draw the graphs, here some screenshots of the results:

check 0, no pos so the pos is random between 0-100:  <br>

![image](https://user-images.githubusercontent.com/75334138/147599233-29f5bc5d-db32-4950-8639-035549e3ece8.png)
 
check1 (T0), no pos so the pos is random between 0-100: <br>

![image](https://user-images.githubusercontent.com/75334138/147599314-738e8289-4336-40bd-8cad-fcabe8dce715.png)

check2 (A5 after removing an edge) with pos: <br>

![image](https://user-images.githubusercontent.com/75334138/147599385-7693df7b-9a2d-41de-bee5-ff0d9931cb25.png)

check3 no pos so the pos is random between 0-100: <br>

![image](https://user-images.githubusercontent.com/75334138/147599517-3d353ebe-de48-4327-9046-38e8b4ba79a5.png)



## UML

link to UML: [UML_Ex3_DWG.pdf](https://github.com/JosefSo/Ex3_DWG/files/7786177/UML_Ex3_DWG.pdf)


![UML_Ex3_DWG](https://user-images.githubusercontent.com/77780368/147602367-65ecc9f8-69cf-4975-b8e3-3e6bc1983ebb.jpeg)


## How To Run

In order to run the program you will have to install matplotlib library. to install it in the terminal pip install matplotlib.

![image](https://user-images.githubusercontent.com/75334138/147597429-72bb6735-c163-43cb-9165-899a96286178.png)

An exapmle of output like the required output of the main: <br>
![image](https://user-images.githubusercontent.com/75334138/147598653-ef875698-f9b2-4822-ab53-2d6fd3398ce5.png)






