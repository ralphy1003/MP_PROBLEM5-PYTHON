#PROBLEM 5-PYTHON
import matplotlib.pylab as plot
import numpy as np
n=np.linspace(0,199,200)       
def x(n): 
    a=eval(FCT)  
    return a 
FCT=(input("Please input an equation for x(n):"))   
for i in range(0,200):
    if i==0:
        y=(-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2))
    elif i > 0 & i <= 198:
        y= (0.5*x(n+1))-(0.5*x(n-1))
    else:
        y=(1.5*x(n))-(2*x(n-1))+(0.5*x(n-2))
plot.title("Plot of x(n) and y(n)")
plot.plot(x(n),label = "x(n)")
plot.plot(y,linestyle="dashed",label = "y(n)")
plot.grid()
plot.xlabel('x-axis')
plot.ylabel('y-axis')
plot.legend()
plot.show