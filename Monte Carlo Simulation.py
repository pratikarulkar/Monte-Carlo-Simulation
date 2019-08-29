
##function to get next position for an ant
def updatingpos(x,y):
    if random.randint(1,2)==1:
        x+=[1 if random.randint(1,2)==1 else -1][0] 
        y+=0
    else:
        y+=[1 if random.randint(1,2)==1 else -1][0]
        x+=0
    return x,y



                
##main function to get the probability of an ant reaching to point B    
def antproblem(n,numberofsimulation):
    reached=0
    notreached=0
    c=0
    for i in range(numberofsimulation):
        a=np.zeros((n,n))
        x,y=0,0
        a[x,y]=1
        for i in range(n*n):
            x0,y0=updatingpos(x,y)
##Not allowing ant to move out of the grid and to the same place from where it has moved already
            if ((x0<0 or x0>(n-1)) or (y0<0 or y0>(n-1))) or a[x0,y0]==1: 
                c=0
                while ((x0<0 or x0>(n-1)) or (y0<0 or y0>(n-1))) or a[x0,y0]==1:
                    x0,y0=updatingpos(x,y)
                    c+=1
                    if c>10:
                        break

            if c<10:
                a[x0,y0]=1
                x,y=x0,y0
            else:
                pass
    
        if a[(n-1),(n-1)]==1:
            reached+=1
        else:
            notreached+=1
    return print("probability that it will reach at the end is",reached/numberofsimulation)