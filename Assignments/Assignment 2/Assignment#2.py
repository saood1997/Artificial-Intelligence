import random
class TSP:
    
    def __init__(self,matrix):
        self.mtx = matrix
        self.populationSize = len(matrix)
        
    # Step 1: Generating Population
    def generatePopulation(self):
        population = []
        for _ in range(0,self.populationSize):
            chromosome = self.generateChromosome()
            population.append(chromosome)
        return population
    
    
    #For Generating Poulation ,need to generate the Chromosome
    def generateChromosome(self):
        count = 0
        chromosome = []
        i = 100
        while i != 0:
            num = random.randrange(0,self.populationSize)
            if num not in chromosome and count != self.populationSize:
                chromosome.append(num)
                count+=1
            elif count == self.populationSize:
                break
        return chromosome
                
    #Geneate a whole trip path in which last and first city are same and passes through 
    # all the cities
    def generateTripPath(self,population):
        tripPath = []
        for chromosome in population:
            tempLis = []
            for gene in chromosome:
                tempLis.append(gene)
            tempLis.append(chromosome[0])
            tripPath.append(tempLis)
        return tripPath
    
    
    # Fitness Function , which is sum of all the diatance between two cityes in the trip path
    def fitnessFunction(self,tripPath):
        distance_list = []
        row = 0
        for chromosome in tripPath:
            col = 0
            distance = 0
            for gene in chromosome:
                if len(chromosome)-1 == col:
                    break
                else:
                    city1 = tripPath[row][col]
                    city2 = tripPath[row][col+1]
                    dst = self.calculateDistance(city1,city2)
                    distance += dst
                    col += 1
            distance_list.append(distance)
            row += 1
        return distance_list
    
    
    def calculateDistance(self,city1,city2):
        return self.mtx[city1][city2]
    
    
    #Step 2 : Selection
    # This function return the index of selected chromosome
    def selctionParents(self,tripPath,fitnessValues):
        totalFitness = sum(fitnessValues)
        rand_val = random.randrange(0,totalFitness)
        partial_sum = 0
        count = 0
        for i in fitnessValues:
            partial_sum += i
            if partial_sum >= rand_val:
                return count
            count += 1
        return -1
    
    # Step : 3
    # Modification
    
    def createChilderns(self,parent1,parent2):
        random_index = random.randrange(0,self.populationSize-1)
        childerns  = []
        child1 = []
        child2 = []
        temp_lis = []
        count1 = 0
        count2 = 0 
        count3 = 0
        
        for gene in parent1:
            if count1 != random_index:
                child1.append(gene)
                count1 += 1
            else:
                temp_lis.append(gene)
                
        for gene in parent2:
            if count2 != random_index:
                child2.append(gene)
                count2 += 1
            else:
                child1.append(gene)
                child2.append(temp_lis[count3])
                count3 += 1
        childerns.append(child1)
        childerns.append(child2)
        return childerns
    
    def mutation(self,population):
        fix_num = 63
        forward_count = 0
        for chromosome in population:
            random_num = random.randrange(0,100)
            if fix_num == random_num:
                    temp = chromosome[forward_count]
                    chromosome[forward_count]=chromosome[3]
                    forward_count += 1
                    continue
            forward_count += 1
            if forward_count >= 4:
                     break
        return population

    
    def modify(self,parent1,parent2):
        new_population = []
        childerns = self.createChilderns(parent1,parent2)
        new_population.append(parent1),new_population.append(parent2)
        for i in childerns:
            new_population.append(i)
        
        population = self.mutation(new_population)
        return new_population
    
    
matrix = [
             [0,66,21,300,500,26,77,69,125,650],
             [66,0,35,115,36,65,85,90,44,54],
             [21,35,0,450,448,846,910,47,11,145],
             [300,115,450,0,65,478,432,214,356,251],
             [500,36,448,65,0,258,143,325,125,39],
             [26,65,846,478,258,0,369,256,345,110],
             [77,85,910,432,143,369,0,45,120,289],
             [69,90,47,214,325,256,45,0,325,981],
             [125,44,11,356,125,345,120,325,0,326],
             [650,54,145,251,39,110,289,981,326,0]
             ]



tsp = TSP(matrix)
# Step : 1
pop_matrix = tsp.generatePopulation()  #Generating population
tripPath = tsp.generateTripPath(pop_matrix) #Generating a whole trip in which first and last city are same
fitnessValues = tsp.fitnessFunction(tripPath) # calculating the fitness of each chromosome

# Step : 2
# select two the parents randomly 
# randomnes depend on the fitness of chromosome
select_chrom = 2
selected_chromosomes = []
count = 100
while count != 0:
    lis = []
    chromosome_index = tsp.selctionParents(tripPath,fitnessValues)
    if chromosome_index == -1:
        continue
    elif len(selected_chromosomes) != select_chrom and chromosome_index not in lis: 
        selected_chromosomes.append(tripPath[chromosome_index])
        lis.append(chromosome_index)
    else:
        break

# Step : 3
# Modification
parent1 = selected_chromosomes[0]
parent2 = selected_chromosomes[1]
matrix = tsp.modify(parent1,parent2)


fitnessValues = tsp.fitnessFunction(matrix)
val = max(fitnessValues)
count = 0
index = None
for i in fitnessValues:
    if i == val:
        index = count
    count+=1

best_path = matrix[index]

        
        
    
    
