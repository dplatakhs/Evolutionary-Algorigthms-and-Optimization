import random
from Functions import *

def decimalToBinary(n):
    # converting decimal to binary
    # and removing the prefix(0b)
    sampleInBin = []
    rBinList = list(bin(n).replace("0b", ""))
    if(n<0): rBinList.remove('-')
    for j in range(10-len(rBinList)):
        rBinList.insert(0, '0')
    if(n<0): rBinList.insert(0, '-')
    sampleInBin.append(listToString(rBinList))
    return listToString(sampleInBin)

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # return string  
    return (str1.join(s))

def population(n):
    # n: how many samples we have
    populInDecimal = []
    populInBin = []
    for i in range(n):
        sampleInDecimal = []
        sampleInBin = []
        r1 = random.randint(-1024, 1023)
        r2 = random.randint(-1024, 1023)
        sampleInDecimal.append(r1)
        sampleInDecimal.append(r2)
        #we try to make all bins to same length
        if(r1<0):
            #if it's negative, it has +1 length cause of '-' symbol
            rBinList = list(decimalToBinary(r1))
            rBinList.remove('-')
            for j in range(10-len(rBinList)):
                rBinList.insert(0, '0')
            rBinList.insert(0,'-')
            #beware, the length is 11!!!
        else:
            #now we have just want our length to be 10
            rBinList = list(decimalToBinary(r1))
            for j in range(10-len(rBinList)):
                rBinList.insert(0, '0')
        sampleInBin.append(listToString(rBinList))
        if(r2<0):
            #if it's negative, it has +1 length cause of '-' symbol
            rBinList = list(decimalToBinary(r2))
            rBinList.remove('-')
            for j in range(10-len(rBinList)):
                rBinList.insert(0, '0')
            rBinList.insert(0,'-')
            #beware, the length is 11!!!
        else:
            #now we have just want our length to be 10
            rBinList = list(decimalToBinary(r2))
            for j in range(10-len(rBinList)):
                rBinList.insert(0, '0')
        sampleInBin.append(listToString(rBinList))
        populInDecimal.append(sampleInDecimal)
        populInBin.append(sampleInBin)
        #print("Here we have a sample: ",sampleInDecimal)
    return populInDecimal,populInBin


def findValues(listOfDecimals):
    fitnessValues = []
    for i in range(len(listOfDecimals)):
        inputInFunction0 = listOfDecimals[i][0]
        inputInFunction1 = listOfDecimals[i][1]
        val = pow(inputInFunction0,2) + inputInFunction1
        fitnessValues.append(val)
    return fitnessValues



def findPsi(listOfValues):
    sum = 0
    listOfPsi = []
    for i in range(len(listOfValues)):
        sum += listOfValues[i]
    for i in range(len(listOfValues)):
        listOfPsi.append(1-listOfValues[i]/sum)
    return listOfPsi


def findParensRoulette(listOfPsi, numOfParents):
    #first we have to find the limits
    limits = []
    indexOfChosenParents = []
    sum = 0
    for i in range(len(listOfPsi)):
        sum += listOfPsi[i]
        limits.append(sum)
    #print("He are the limits: ",limits)
    for i in range(numOfParents):
        #r = random.randint(0, 1000)/1000
        r = random.random()
        for j in range(len(limits)):
            if(r<limits[j]):
                indexOfChosenParents.append(j)
                break
    return indexOfChosenParents


def crossOver(chosenParentsDecimal,chosenParentsBin,chanceToCross):
    nextGenDecimal = []
    nextGenBin = []
    for i in range(len(chosenParentsDecimal)):
        if((i%2) != 0): continue
        #print(i)
        r = random.randint(0, 1000)/1000
        if(r>chanceToCross):
            # No crossOver is about to happen :(
            nextGenDecimal.append(chosenParentsDecimal[i])
            nextGenBin.append(chosenParentsBin[i])
            nextGenDecimal.append(chosenParentsDecimal[i+1])
            nextGenBin.append(chosenParentsBin[i+1])
            continue
        # we are supposed to have even number of parents...
        # first parent 1
        # x1
        x1parent1 = chosenParentsDecimal[i][0]
        x1parent1Bin = decimalToBinary(x1parent1)
        if x1parent1<0:
            # we turn the bin to list in order to remove the '-'
            x1parent1BinList = list(x1parent1Bin)
            x1parent1BinList.remove('-')
            x1parent1Bin = listToString(x1parent1BinList)
        # x2
        x2parent1 = chosenParentsDecimal[i][1]
        x2parent1Bin = decimalToBinary(x2parent1)
        if x2parent1<0:
            # we turn the bin to list in order to remove the '-'
            x2parent1BinList = list(x2parent1Bin)
            x2parent1BinList.remove('-')
            x2parent1Bin = listToString(x2parent1BinList)
            #x2parent1Bin.replace('-', '')
        
        # then parent 2
        # x1
        x1parent2 = chosenParentsDecimal[i+1][0]
        x1parent2Bin = decimalToBinary(x1parent2)
        if x1parent2<0:
            #print(x1parent2)
            x1parent2BinList = list(x1parent2Bin)
            #print(x1parent2Bin)
            x1parent2BinList.remove('-')
            x1parent2Bin = listToString(x1parent2BinList)
            #x1parent2Bin.replace('-', '')
        # x2
        x2parent2 = chosenParentsDecimal[i+1][1]
        x2parent2Bin = decimalToBinary(x2parent2)
        if x2parent2<0:
            x2parent2BinList = list(x2parent2Bin)
            x2parent2BinList.remove('-')
            x2parent2Bin = listToString(x2parent2BinList)
            #x2parent2Bin.replace('-', '')
        #print("Binary parent1 x1,x2: ",x1parent1Bin,x2parent1Bin)
        #print("Binary parent2 x1,x2: ",x1parent2Bin,x2parent2Bin)
        #print("Decimal parent1 x1,x2: ",x1parent1,x2parent1)
        #print("Decimal parent2 x1,x2: ",x1parent2,x2parent2)
        
        # ~~~~~~~~~~Time to implement the crossover~~~~~~~~~~~~~~
        crossPoint = random.randint(0, len(x1parent1Bin))
        # First we do x1s
        # Parent 1, x1!
        x1parent1BinList = list(x1parent1Bin)
        x1parent1BinListLeft = x1parent1BinList[:crossPoint]
        x1parent1BinListRight = x1parent1BinList[crossPoint:]
        # Parent 2, x1!
        x1parent2BinList = list(x1parent2Bin)
        x1parent2BinListLeft = x1parent2BinList[:crossPoint]
        x1parent2BinListRight = x1parent2BinList[crossPoint:]
        # Time to join the two halfs to make 2 kids
        # first kid, parent1 left x1 with parent2 right x1
        firstKidx1 = x1parent1BinListLeft + x1parent2BinListRight
        # second kid, parent2 left x1 with parent1 right x1
        secondKidx1 = x1parent2BinListLeft + x1parent1BinListRight
        
        # Then we do x2s
        # Parent 1, x2!
        x2parent1BinList = list(x2parent1Bin)
        x2parent1BinListLeft = x2parent1BinList[:crossPoint]
        x2parent1BinListRight = x2parent1BinList[crossPoint:]
        # Parent 2, x2!
        x2parent2BinList = list(x2parent2Bin)
        x2parent2BinListLeft = x2parent2BinList[:crossPoint]
        x2parent2BinListRight = x2parent2BinList[crossPoint:]
        # Time to join the two halfs to make 2 kids
        # first kid, parent1 left x2 with parent2 right x2
        firstKidx2 = x2parent1BinListLeft + x2parent2BinListRight
        # second kid, parent2 left x2 with parent1 right x2
        secondKidx2 = x2parent2BinListLeft + x2parent1BinListRight
        
        # now let's say parent1 x1 is negative and parent2
        if(x1parent1<0 and x1parent2<0):
            firstKidx1.insert(0,'-')
        elif(x1parent1<0 or x1parent2<0):
            neg = random.random()
            if(neg<0.5): firstKidx1.insert(0,'-')
        
        if(x2parent1<0 and x2parent2<0):
            firstKidx2.insert(0,'-')
        elif(x2parent1<0 or x2parent2<0):
            neg0 = random.random()
            if(neg0<0.5): firstKidx2.insert(0,'-')
        
        if(x1parent1<0 and x1parent2<0):
            secondKidx1.insert(0,'-')
        elif(x1parent1<0 or x1parent2<0):
            neg2 = random.random()
            if(neg2<0.5): secondKidx1.insert(0,'-')
        
        if(x2parent1<0 and x2parent2<0):
            secondKidx2.insert(0,'-')
        elif(x2parent1<0 or x2parent2<0):
            neg3 = random.random()
            if(neg3<0.5): secondKidx2.insert(0,'-')
        
        
        # connect x1 and x2
        firstKid = []
        firstKid.append(listToString(firstKidx1))
        firstKid.append(listToString(firstKidx2))
        
        # connect x1 and x2
        secondKid = []
        secondKid.append(listToString(secondKidx1))
        secondKid.append(listToString(secondKidx2))
        
        nextGenBin.append(firstKid)
        nextGenBin.append(secondKid)
        # WARNING, WE STILL HAVENT CHANGED THE DECIMAL VALUES OF THE KIDS, OF THE NEXT GEN
        
    return nextGenBin



def mutation(population,mut):
    sum = 0
    # if <mut we mutate
    for i in range(len(population)):
        x1 = population[i][0]
        x2 = population[i][1]
        x1List = list(x1)
        x2List = list(x2)
        for j in range(len(x1List)):
            r1 = random.random()
            if(x1List[j] == '-'): continue
            if(r1<mut):
                sum += 1
                # change it 0->1, 1->0
                x1List[j] = str(1-int(x1List[j]))
        for j in range(len(x2List)):
            r1 = random.random()
            if(x2List[j] == '-'): continue
            if(r1<mut):
                sum += 1
                # change it 0->1, 1->0
                x2List[j] = str(1-int(x2List[j]))
        population[i][0] = listToString(x1List)
        population[i][1] = listToString(x2List)
    #print("We had",sum,"mutations!")
    return population


def mutatedPopulBinToDecimal(mutatedPopulationBin):
    mutatedPopulationDecimal = []
    for i in range(len(mutatedPopulationBin)):
        sample = []
        samplex1 = binaryToDecimal(mutatedPopulationBin[i][0])
        samplex2 = binaryToDecimal(mutatedPopulationBin[i][1])
        sample.append(samplex1)
        sample.append(samplex2)
        mutatedPopulationDecimal.append(sample)
    return mutatedPopulationDecimal


def binaryToDecimal(n):
    if(int(n)>0):
        return int(n,2)
    noNegative = n.replace('-', '')
    y = int(noNegative,2)
    n = -y
    return n

global finalMin, finalMinSample
finalMinSample = 0
finalMin = 100000000
#global minValueNew,minValueIndexNew,minSampleNew
def produceNextGen(populInDecimal,populInBin,flagP):
    global finalMin,finalMinSample
    vals = findValues(populInDecimal)
    if(flagP==1): print("The values of the functions through the population: ",vals)
    # Step 3: find the psi values through the FITNESS function
    psi = findPsi(vals)
    if(flagP==1): print("Here we have the values of each psi throught the fitness function: ",psi)
    # Step 4: get the index of the parents you are about to choose
    indexOfChosenParents = findParensRoulette(psi, len(populInDecimal))
    chosenParentsDecim = []
    chosenParentsBin = []
    # Step 5: get the chosen parents from the population
    for i in indexOfChosenParents:
        chosenParentsDecim.append(populInDecimal[i])
        chosenParentsBin.append(populInBin[i])
    if(flagP==1): print("Chosen parents that are about to crossover in decimal:",chosenParentsDecim)
    if(flagP==1): print("Chosen parents that are about to crossover in bin:",chosenParentsBin)
    # Step 6: do the crossover
    kids = crossOver(chosenParentsDecim,chosenParentsBin,11)
    if(flagP==1): print("The crossoverd population: \n",kids)
    # Step 7: do the mutation on the kids
    mutatedPopulationBin = mutation(kids,0.3)
    if(flagP==1): print("The mutated population in binary: \n",mutatedPopulationBin)
    mutatedPopulationDecimal = mutatedPopulBinToDecimal(mutatedPopulationBin)
    if(flagP==1): print("~~~The population before and after~~~")
    if(flagP==1): print("The population before: \n", populInDecimal)
    if(flagP==1): print("The population after mutation: \n",mutatedPopulationDecimal)
    # Step 8: Compare old and new function values
    valsNew = findValues(mutatedPopulationDecimal)
    if(flagP==1): print("~~~Values of the function before and after~~~")
    # 'vals' are the values of the old population
    if(flagP==1): print("The values before: \n",vals)
    if(flagP==1): print("The values after: \n",valsNew)
    # Lowest sample and value in old
    minValue = min(vals)
    minValueIndex = vals.index(minValue)
    minSample = populInDecimal[minValueIndex]
    # Lowest sample and value in new
    minValueNew = min(valsNew)
    minValueIndexNew = valsNew.index(minValueNew)
    minSampleNew = mutatedPopulationDecimal[minValueIndexNew]
    
    #finalMin = minValue
    #finalMinSample = minSample
    #finalMinIndex = minValueIndex
    if(finalMin > minValueNew):
        finalMin = minValueNew
        finalMinSample = minSampleNew
        #finalMinIndex = minValueIndexNew
    print("The lowest value: ", minValue)
    #print("At index: ",finalMinIndex)
    return mutatedPopulationDecimal,mutatedPopulationBin, finalMin, finalMinSample


def howManyGens(gens,flagP):
    if(gens<=0): return
    if(gens == 1):
        popDec, popBin, minValue, minSample = produceNextGen(populInDecimal,populInBin,0)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("The lowest value we encountered: ",minValue)
        print("Using x1 and x2: ", minSample)
        return
    tempMin = 100000000000000000
    minSampleTmp = 0
    print("~~~~~~~Generation 1~~~~~~~")
    popDec, popBin, minValue, minSample = produceNextGen(populInDecimal,populInBin,flagP)
    if(minValue < tempMin):
        tempMin = minValue
        minSampleTmp = minSample
    for i in range(gens-1):
        print("~~~~~~~Generation ",i+2,"~~~~~~~")
        popDec, popBin, minValue, minSample = produceNextGen(popDec, popBin,flagP)
        if(minValue < tempMin):
            tempMin = minValue
            minSampleTmp = minSample
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The lowest value we encountered: ",tempMin)
    print("Using x1 and x2: ", minSample)


#print("Here we have again the population in binary",populInBin)



print("How much population do you want to have? MUST BE EVEN NUMBER")
y = input()
# take all the functions as black boxes!!!
populInDecimal = []
populInBin = []
# Step 1: produce the first population you need.
# Dont forget, we have to have even population.
populInDecimal,populInBin = population(int(y))
print("Here we have the population in decimal",populInDecimal)
# Step 2: find the values through the given function
popDec, popBin, minValue, minSample = produceNextGen(populInDecimal,populInBin,0)
print("How mant generations do you want to produce?")
x = int(input())
if(x<=0):
	print("Enter greater than 0")
else:
	print("Do you want to print the info of each Generation? 1 for YES, 0 for NO")
	z = int(input())
	howManyGens(x,z)



