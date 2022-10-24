def Rosenbrock(x1,x2):
    # global minimum (1,1)
    return 100*(x2-x1**2)**2 + (1-x1)**2
    
def Beale(x, y):
    # global minimum (3,0.5)=0
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    
def Goldenstein(X,Y):
    # global minimum (0,-1)=3
    return (1+(X+Y+1)**2*(19-14*X+3*X**2-14*Y+6*X*Y+3*Y**2))*(30+(2*X-3*Y)**2*(18-32*X+12*X**2+48*Y-36*X*Y+27*Y**2)) 
    
def Booth(x,y):
    # global minimum (1,3)=0
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2
    
    
def Ackley(x, y):
    # global minimum (0,0) = 0
    pi = 3.1416
    e = 2.71
    return -20.0 * math.exp(-0.2 * math.sqrt(0.5 * (x**2 + y**2)))-math.exp(0.5 * (math.cos(2 * 
  pi * x)+math.cos(2 * pi * y))) + e + 20
  
  
  
def Easom(x,y):
    # global minimum (pi,pi) = 1
    pi = 3.1416
    return math.cos(x)*math.cos(y)*math.exp(-(x-pi)**2-(y-pi)**2)
    
    
def Eggholder(x1,x2):
    # global minimum (512,404.2319) = -959.6407
    a=math.sqrt(math.fabs(x2+x1/2+47))
    b=math.sqrt(math.fabs(x1-(x2+47)))
    c=-(x2+47)*math.sin(a)-x1*math.sin(b)
    return c
    
def Schaffer(x,y):                          
        # global minimum (0,0) = 0
        num = (np.sin((x**2 + y**2)**2)**2) - 0.5
        den = (1 + 0.001*(x**2 + y**2))**2 
        return 0.5 + num/den



