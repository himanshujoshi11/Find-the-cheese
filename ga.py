import maze
import maze_samples
import random
moves=['U','D','L','R']

test_case=1 #change TESTCASE here. test_case=0 for maze[0] and test_Case=1 for maze[1]
class ga:
  def __init__(self,fd):
    self.mutaterate=75 #This is the mutation Rate(0 to 100, higher the number-higher the chance of mutation)
    self.fd = fd
    self.new_generation=[]
    
    #Beginning of MonteCarlo provided in ga_logic
  def SetWeightsForMonteCarloSelection(self,values):
    normalized_values = [int(v/sum(values)*100+.5) for v in values]
    accum = 0
    selection_weights = []
    for w in normalized_values:
      accum += w
      selection_weights.append(accum)
    return selection_weights

  def MonteCarloSelection(self,selection_weights):
    selection = random.randint(0,selection_weights[-1])
    for i,w in enumerate(selection_weights):
      if selection <= w:
        return i
    #End of MonteCarlo Selection Code
      
  def call(self):    #Function that calls Montecarlo on a generation and crossbreeds the results
    population_size = len(self.fd.fitnessdata)
    S = self.SetWeightsForMonteCarloSelection(firstgen.fitnessdata)
    for i in range(population_size//2):
      p1 = self.MonteCarloSelection(S)
      p2 = self.MonteCarloSelection(S)
      result = self.crossbreed(p1,p2)
      self.new_generation.append(result[0])
      self.new_generation.append(result[1])
    
  def crossbreed(self,parent1,parent2): #Function that crossbreeds and two parents
          a = random.randint(0,len(firstgen.population[0])-1)
          parent1=firstgen.population[parent1]
          parent2=firstgen.population[parent2]
          individual1= parent1[:a] + parent2[a:]
          individual2= parent2[:a] + parent1[a:]
          
          return [individual1,individual2]
        
  def mutation(self,child1,child2):
    self.child1=child1
    self.child2=child2
    mutationprobab1=random.randint(0,99)
    mutationprobab2=random.randint(0,99)
    if mutationprobab1 < self.mutaterate:
      genex1=random.randint(0,len(firstgen.population[0])-1)
      selectnew_gene=random.randint(0,3)
      newgene=[moves[selectnew_gene]]
      child1[random.randint(0,len(firstgen.population[0])-1)]=moves[random.randint(0,3)]
      return self.child1

    if mutationprobab2<self.mutaterate: 
      genex2=random.randint(0,len(firstgen.population[0])-1)
      selectnew_gene2=random.randint(0,3)
      newgene2=moves[selectnew_gene2]
      self.child2[random.randint(0,len(firstgen.population[0])-1)]=newgene2
      return self.child2    
class individual:
    def __init__(self,population=[]):
        self.population=population
        self.fitnessdata=[]
        
    def createpopulation(self): #The first generation of randomly generated parents
        global moves, test_case
        self.i=0
        self.gene_count=0
        mouse=[]
        while self.i<100: #100 is current population, change this to change the POPULATION.
            if self.gene_count<maze_samples.string_length[test_case]: #Change test_case at the top
                r=random.randint(0,3)
                mouse.append(moves[r])
                self.gene_count +=1
            elif self.gene_count==maze_samples.string_length[test_case]:
                self.population.append(''.join(mouse))
                self.i +=1
                mouse=[]
                self.gene_count=0
 
    def fitness(self): #This function checks the fitness of a given population and returns a list of fitness scores at corresponding indices 
        
        global test_case
        current_maze=maze_samples.maze[test_case]
        self.number= 0 
        self.counter=0
        while self.number < len(self.population):
            
            gene=self.population[self.number]
            self.fitness_score=0

            for rows in current_maze:
                if 'M' in rows:
                    mousecurrent=[current_maze.index(rows),rows.index('M')]
                    
            for nextmove in gene:
        

                if nextmove == 'U': mousecurrent[0] += 1
                elif nextmove == 'L': mousecurrent[1] -= 1
                elif nextmove == 'R': mousecurrent[1] += 1
                elif nextmove == 'D': mousecurrent[0] -= 1
                
                if 0 <= mousecurrent[0] < len(current_maze) \
                and 0 <= mousecurrent[1] < len(current_maze[0]):
                    self.counter=self.counter+1
                    if current_maze[mousecurrent[0]][mousecurrent[1]]== 'M':
                        self.fitness_score +=1
                        
                    elif current_maze[mousecurrent[0]][mousecurrent[1]]== '-':
                        self.fitness_score +=1
                        
                    elif current_maze[mousecurrent[0]][mousecurrent[1]]== 'C' :
                        self.fitness_score += 1
                        
                        if self.counter==maze_samples.string_length[test_case]:
                            self.fitness_score += 1000
                            
                            self.number+=1
                            self.counter=0
                            
                            break
                    elif current_maze[mousecurrent[0]][mousecurrent[1]]== 'x':
                        
                        if nextmove == 'U': mousecurrent[0] -= 1
                        elif nextmove == 'L': mousecurrent[1] += 1
                        elif nextmove == 'R': mousecurrent[1] -= 1
                        elif nextmove == 'D': mousecurrent[0] += 1
                        
                        
                    if self.counter>=maze_samples.string_length[test_case]:
                        
                        self.fitnessdata.append(self.fitness_score)
                        self.number +=1
                        self.counter=0
                        break
   
                else:
                    
                    self.counter +=1
                    if nextmove == 'U': mousecurrent[0] -= 1
                    elif nextmove == 'L': mousecurrent[1] += 1
                    elif nextmove == 'R': mousecurrent[1] -= 1
                    elif nextmove == 'D': mousecurrent[0] += 1
       
firstgen=individual()
firstgen.createpopulation() #The population length can be changed in line57
firstgen.fitness()

bestalreadyfound=False
generations=10 #Change this value to edit the number of generations to iterate for.
for x in range(generations): 
    gen2=ga(firstgen)
    gen2.call()
    second_gen = individual(gen2.new_generation)
    second_gen.fitness()
    firstgen = second_gen
    if max(firstgen.fitnessdata)>500: #This takes the gene and stores it if the cheese is found in one of the indermidiate generations
      bestfound=firstgen.fitnessdata.index(max(firstgen.fitnessdata))
      bestalreadyfound=True
      
if bestalreadyfound==False:
  best= second_gen.fitnessdata.index(max(second_gen.fitnessdata))
  bestmouse=second_gen.population[best]
else:
  bestmouse=bestfound

def main():
  global test_case #To change the test case, go to line 5
  
  M = maze.Maze(maze_samples.maze[test_case])
  string_length = maze_samples.string_length[test_case]
  M.Visualize()
  M.RunMaze(bestmouse)
  x = input('ENTER to Try Another Series of Moves.')
  M.ResetMouse()
  M.RunMaze('RLUULLLDDDDL')
if __name__=='__main__' :
    main()
