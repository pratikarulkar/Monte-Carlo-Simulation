# Monte-Carlo-Simulation  
##this problem is taken from https://brilliant.org/practice/monte-carlo/
Finding the probability of an ant who have started from point A and reached B using monte carlo simulation

the ant is trying to get from point A to point B in a grid. The coordinates of point A is (1,1) (this is top left corner), and the coordinates of point B is (n,n) (this is bottom right corner, n is the size of the grid).

Once ant starts moving, there are four options, it can go left, right, up or down (no diagonal movement allowed). If any of these four options satisfy the following:

    The new point should still be within the boundaries of the n×nn \times nn×n grid
    The new point should not be visited previously.

If P is the probability of the ant reaching point B for a 6×6 grid, use Monte Carlo simulation to compute P.

Details and Assumptions

    Assume 10,00010,00010,000 simulations are sufficient enough to compute PPP.
