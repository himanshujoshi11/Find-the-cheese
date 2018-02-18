# About
This an automated program that creates a *genetic algorithm* approach for *evolving* a "mouse" to successfully navigate a maze to find the "cheese." This was created using *Python 3* and the visualization was done using *Turtle graphics*.  
**Professor: Dr. Amy Larson**.  
**CSCI 1133 at UMN, Twin Cities**.  

## How was Genetic Algorithm implemented?
An individual was defined by some string meant to represent genes. The individual was *tested* in a given environment that resulted in a fitness value for that individual. For this project, the genes were the possible moves in the maze.

The GA started with a population of individuals. For the next evolved generation, a new population was formed by *selecting* 2 parents (selection was biased to choose those more fit), and combined (i.e. *cross breed*) those 2 individuals by combining their genes to form a new individual. There was also a chance that the genes will undergo a *mutation*.

Populations evolved over a number of generations (or until a solution was found) and the hope was that an individual will converge on the solution.
