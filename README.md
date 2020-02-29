# Terminal-Tour
A programme which will solve the classic knight's tour problem for user specified board sizes (if possible) and print the resultant path to the user's terminal.

It takes advantage of Warnsdorff's algorithm to speed up search time.

Terminal Tour is now a functioning programme. I have hardcapped board sizes to be composed of less than 100 squares because after this amount the wait time becomes very long.

Unfortunately there is a bug in Terminal Tour. Regardless of the input starting square the knight will always begin from the bottom right corner of the board regardless of user input.
