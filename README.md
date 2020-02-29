# Terminal-Tour
A programme which will solve the classic knight's tour problem for user specified board sizes (if possible) and print the resultant path to the user's terminal.

It takes advantage of Warnsdorff's algorithm to speed up search time. This is a depth first search algorithm which determines which node to move to at each step based on which of the possible nodes has the least number of edges out of it.

Terminal Tour is now a functioning programme. I have hardcapped board sizes to be composed of less than 101 squares because after this amount the wait time becomes very long. On my laptop it was around 45 seconds wait time worst case for a 10x10 board.

To use Terminal Tour run the programme Terminal_Tour_Recursive.py in your terminal using python3.
