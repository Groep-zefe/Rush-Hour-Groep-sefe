# Rush-Hour-Groep-zefe

Rush Hour is a puzzle game where the objective is to move vehicles on a board until the red car is able to escape. This program focuses on the ability to solve any board from the game automatically and specifically to do it in as fewest moves as possible using implemented algorithms.

## Installation

There are several steps needed to succesfully run the code:
1. Have Python installed on your computer (preferably Python 3).
2. Download the files from this repository to your computer.
3. Open the files in your application that is able to run these files (e.g. Visual Studio Code).
4. Run 'python main.py' in the terminal to run the game (use 'python3' instead of 'python' if you're running the later Python versions).
5. ***** omschrijving verschillende command line arguments
6. **** omschrijving hoe output uit te lezen


Some specifications to keep in mind is that by simply running 'main.py' in the terminal, the code automatically loads the first board. You can choose a different board by simply adding a number of the preferred board after 'main.py'. Furthermore once the code runs it will never stop, so to make it stop you'd have to perform a keyboard interrupt in the terminal.

## Specifics

This program loads a gameboard that you've selected in the terminal. The game will run on automatically, printing the amount of attemps it's done, as well as the fewest amount of moves needed for the fastest solution. Everytime a solution is found requiring the fewest amount of moves the program automatically makes a file saving the results in steps of which car was moved and 1 step in which direction. 
