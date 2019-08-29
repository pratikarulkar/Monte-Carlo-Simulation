# Monte-Carlo-Simulation  
##this problem is taken from https://brilliant.org/practice/monte-carlo/
Finding the probability of an ant who have started from point A and reached B using monte carlo simulation

the ant is trying to get from point A to point B in a grid. The coordinates of point A is (1,1) (this is top left corner), and the coordinates of point B is (n,n) (this is bottom right corner, n is the size of the grid).

Once ant starts moving, there are four options, it can go left, right, up or down (no diagonal movement allowed). If any of these four options satisfy the following:

    1.The new point should still be within the boundaries of the n×n grid
    2.The new point should not be visited previously.

If P is the probability of the ant reaching point B for a 6×6 grid, use Monte Carlo simulation to compute P.

Details and Assumptions

    Assume 10,000 simulations are sufficient enough to compute P.

#######################################################################################################################################

Result: With the increasing size of the grid it is unlikely that ant would be able to reach point B
(The python code for the same is provided in the same repository.)

        ￼gridsize(n)           Probability_of reaching_to_point_B
            1                                  1
            2                             0.9046
            3                             0.7207
            4                             0.5546
            5                             0.4254
            6                             0.3311
            7                             0.2581
            8                             0.1984
            9                             0.1566
           10                             0.1175
