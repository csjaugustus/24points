# 24 Game Solver

This is a solver for the [24 Game](https://en.wikipedia.org/wiki/24_Game), in which the objective is to find a way to manipulate four integers so that the end result is 24. 
Instead of just solving 4 numbers, this program also accepts inputs such as "J,Q,K,A" as the game is often played as a card game in which 4 cards are picked and players try to come up with possible solutions. "A" is counted as "1" while "J,Q,K" can either be "1" or respectively "11, 12, 13". The program takes into account all the different possible combinations and returns all possible solutions.

⋅⋅* **24.py** is the main file for the solver.
⋅⋅* **countpos.py** is just a dependency of the main solver file.
⋅⋅* **usergame.py** is the game itself, which gives the user 4 random cards and prompts the user to solve it before giving a solution.
