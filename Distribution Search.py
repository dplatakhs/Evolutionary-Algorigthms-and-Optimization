from scipy.stats import norm
import numpy as np
import math

def NormalRandomSearch(x1,x2,steps,N,chooseFunc):
    i = 0
    opts = []
    values = []
    #print("Steps:",steps)
    while(i<steps):
        # get all points (x1,x2) through normal distribution
        for j in range(N):
            opts.append([np.random.normal(x1, 0.01),np.random.normal(x2, 0.01)])
            #print(np.random.normal(x1, 0.01),np.random.normal(x2, 0.01))
        if(chooseFunc == 0):
            for j in range(N):
                values.append(Rosenbrock(opts[j][0],opts[j][1]))
        elif(chooseFunc == 1):
            for j in range(N):
                values.append(Beale(opts[j][0],opts[j][1]))
        elif(chooseFunc == 2):
            for j in range(N):
                values.append(Goldenstein(opts[j][0],opts[j][1]))
        elif(chooseFunc == 3):
            for j in range(N):
                values.append(Booth(opts[j][0],opts[j][1]))
        elif(chooseFunc == 4):
            for j in range(N):
                values.append(Ackley(opts[j][0],opts[j][1]))
        
        minValue = values.index(min(values))
        x1 = opts[minValue][0]
        x2 = opts[minValue][1]
        
        #print("Current Position:",opts[minValue][0],opts[minValue][1])
        
        #reset the lists
        values = []
        opts = []
        #increase i
        i+=1
    return x1,x2


def UniformRandomSearch(x1,x2,steps,N,chooseFunc):
    i = 0
    opts = []
    values = []
    #print("Steps:",steps)
    while(i<steps):
        # get all points (x1,x2) through normal distribution
        for j in range(N):
            opts.append([np.random.uniform(-100, 100),np.random.uniform(-100,100)])
            #print(np.random.uniform(-100, 100),np.random.uniform(-100,100))
        
        # Choose Rosenbrock
        if(chooseFunc == 0):
            for j in range(N):
                values.append(Rosenbrock(opts[j][0],opts[j][1]))
        # Choose Beale
        elif(chooseFunc == 1):
            for j in range(N):
                values.append(Beale(opts[j][0],opts[j][1]))
        elif(chooseFunc == 2):
            for j in range(N):
                values.append(Goldenstein(opts[j][0],opts[j][1]))
        elif(chooseFunc == 3):
            for j in range(N):
                values.append(Booth(opts[j][0],opts[j][1]))
        elif(chooseFunc == 4):
            for j in range(N):
                values.append(Ackley(opts[j][0],opts[j][1]))
        
        minValue = values.index(min(values))
        x1 = opts[minValue][0]
        x2 = opts[minValue][1]
        
        #print("Current Position:",opts[minValue][0],opts[minValue][1])
        
        #reset the lists
        values = []
        opts = []
        #increase i
        i+=1
    return x1,x2


def CombineRandomSearch(x1,x2,steps,N,chooseFunc):
    i = 0
    e = 10
    opts = []
    values = []
    #print("Steps:",steps)
    while(i<steps):
        # get all points (x1,x2) through normal distribution
        for j in range(N):
            opts.append([np.random.normal(x1, 0.01),np.random.normal(x2, 0.01)])
            opts.append([np.random.uniform(-100, 100),np.random.uniform(-100,100)])
            #print(np.random.normal(x1, 0.01),np.random.normal(x2, 0.01))
        if(chooseFunc == 0):
            for j in range(N):
                # -1.5 < x,y < 1.5
                if(opts[j][0]>1.5): opts[j][0]=1.5
                if(opts[j][0]<-1.5): opts[j][0]=-1.5
                if(opts[j][1]>1.5): opts[j][0]=1.5
                if(opts[j][1]<-1.5): opts[j][0]=-1.5
                values.append(Rosenbrock(opts[j][0],opts[j][1]))
        elif(chooseFunc == 1):
            for j in range(N):
                # -4.5 < x,y < 4.5
                if(opts[j][0]>1.5): opts[j][0]=4.5
                if(opts[j][0]<-1.5): opts[j][0]=-4.5
                if(opts[j][1]>1.5): opts[j][0]=4.5
                if(opts[j][1]<-1.5): opts[j][0]=-4.5
                values.append(Beale(opts[j][0],opts[j][1]))
        elif(chooseFunc == 2):
            for j in range(N):
                # -2 < x,y < 2
                if(opts[j][0]>1.5): opts[j][0]=2
                if(opts[j][0]<-1.5): opts[j][0]=-2
                if(opts[j][1]>1.5): opts[j][0]=2
                if(opts[j][1]<-1.5): opts[j][0]=-2
                values.append(Goldenstein(opts[j][0],opts[j][1]))
        elif(chooseFunc == 3):
            for j in range(N):
                values.append(Booth(opts[j][0],opts[j][1]))
        elif(chooseFunc == 4):
            for j in range(N):
                values.append(Ackley(opts[j][0],opts[j][1]))
        elif(chooseFunc == 5):
            for j in range(N):
                values.append(Easom(opts[j][0],opts[j][1]))
        elif(chooseFunc == 6):
            for j in range(N):
                values.append(Eggholder(opts[j][0],opts[j][1]))
        elif(chooseFunc == 7):
            for j in range(N):
                values.append(Schaffer(opts[j][0],opts[j][1]))
        
        
        minValue = values.index(min(values))
        x1 = opts[minValue][0]
        x2 = opts[minValue][1]
        #print("Current Position:",opts[minValue][0],opts[minValue][1])
        
        #reset the lists
        values = []
        opts = []
        #increase i
        i+=1
    return x1,x2

