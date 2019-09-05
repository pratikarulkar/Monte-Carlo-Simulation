import numpy as np
import math
import random
import pandas as pd
import matplotlib.pyplot as plt

##Creating a function to get the point on a circle whose centre is (0,0) and having radius of 1.
def generating_points_on_perimeter_circle():
    k=random.choices([1,0,2])[0]
    if k==1:
        x=random.uniform(-1,1)
        y =math.sqrt(1-(x**2))
    elif k==0:
        y=random.uniform(-1,1)
        x =math.sqrt(1-(y**2))
    else:
        y=random.uniform(-1,1)
        x =math.sqrt(1-(y**2))
        if y>0:
            y=-1*y
        if x>0:
            x=-1*x
    return x,y

###To check whether 10000 number of simulation are enough to cover all the points on perimeter of circle...
z=pd.DataFrame(index=range(10000),columns=["x","y"])
for i in range(10000):
    z.loc[i,"x"],z.loc[i,"y"]=generating_points_on_perimeter_circle()
plt.scatter(z["x"],z["y"])


def func(simulation=10000):
    z=[]
    acute_triangle=0
    for i in range(simulation):
        a=generating_points_on_perimeter_circle()
        b=generating_points_on_perimeter_circle()
        c=generating_points_on_perimeter_circle()

        z1= (math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)**2+math.sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)**2)<math.sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)**2
        z2= (math.sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)**2+math.sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)**2)<math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)**2
        z3= (math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)**2+math.sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)**2)<math.sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)**2
        

        if z1 or z2 or z3:
            acute_triangle+=1
    
    return print("The probability of getting an acute angle is ",acute_triangle/simulation)
    
    
func()


         
