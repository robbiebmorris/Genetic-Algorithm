import random
import numpy
#https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/


#create a population of random bitstrings
def createPopulation(bits, size):
    arr = []
    for p in range(size):
        num = []
        for x in range(bits):
            num.append(random.randint(0, 1))
        arr.append(num)

    return arr

#get a score for any given child
def generateScore(child):
    return 10

#choose best parrent out of k possible parents
def selection(population, scoreList, k):

    index = random.randint(0, len(population) - 1)
    
    for a in range(k):
        newIndex = random.randint(0, len(population) - 1)
        #smaller score is more desirable - subject to change
        if (scoreList[newIndex] < scoreList[index]):
            index = newIndex

    return population[index]


def breed(parent1, parent2, pCross):
    child1 = parent1
    child2 = parent2

    if (random.random() < pCross):
        #choose point not at the end of list
        pointer = random.randint(1, len(parent1) - 2)
        child1 = parent1[:pointer] + parent2[pointer:]
        child2 = parent2[:pointer] + parent1[pointer:]

    return [child1, child2]

def mutate(input, pMutation):
    for i in range(len(input)):
        if (random.random() < pMutation):
            #bit flip logic: change
            input[i] = 1 - input[i]

#some cool machine learning stuff different from what I've done before
#iterations:
#popSize
#k: number of comparisons in selection function

def geneticAlgorithm(iterations, popSize, k, pMutation):
    
    population = createPopulation(5, popSize)
    
    bestIndex = 0
    bestScore = generateScore(population[0])

    for generation in range(iterations):
        scores = []
        for parent in population:
            tempScore = generateScore(parent)
            scores.append(tempScore)
            #note: smaller is better still
            if (tempScore < bestScore):
                bestIndex = tempScore
                bestScore = generateScore(population[bestIndex])
        print(scores)


        parents = []
        for parent in population:
            parents.append(selection(population, scores, k))
        print(parents)

        children = []
        for i in range(0, popSize, 2):
            tempChildList = breed(parents[i], parents[i + 1])
            for child in tempChildList:
                mutate(child, pMutation)
                children.append(child)

        population = children

    return bestScore


#print(createPopulation(4, 10))
geneticAlgorithm(1, 10, 2)
