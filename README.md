# Rush-Hour-Groep-zefe

Rush Hour is a puzzle game where the objective is to move vehicles on a board until the red car is able to escape. This program focuses on the ability to solve any board from the game automatically and specifically to do it in as fewest moves as possible using implemented algorithms. The first algorithm implemented was a random with archive algorithm, where random moves were made every turn and distinctive boards couldn't be repeated. The second algorithm implemented was a Breadth First algorithm, where every possible board combination is being visited until the program finds the solution requiring the fewest moves possible. 

## Information about the files

The files are neatly organized in different folders. There are 4 main folders in this project: boards, code, docs and solutions. Furthermore this project contains a README file, an init.py file and a main.py file.

The boards folder consists of the seven boards used for this project, but users can add more boards to this folder if they want to.

The 'code' folder represents the code needed to run this program. In here the 'classes' folder represents the different types of classes used for this program. The 'algorithms' folder represents the 2 different algorithms used for this program, depending on what the user wants to use.

The docs folder consists of the data structure for both the random and the Breadth First algorithm. Both the UML's for these algorithms can be found here.

The solutions folder consists of the csv-files that have been made when running the code.

## Installation

There are several steps needed to succesfully run the code:
1. Have Python installed on your computer (preferably Python 3).
2. Download the files from this repository to your computer. You can also clone the repository to your application using 'git clone '
3. Open the files in your application that is able to run these files (e.g. Visual Studio Code).
4. Run 'python main.py' in the terminal to run the game (use 'python3' instead of 'python' if you're running the later Python versions).
5. After the command 'python main.py' you have the option to choose a board (represented by a number) you want to be solved. Choosing no number results in the first board being selected automatically. After that you have the option to type in either 'random' or 'breadth' to choose the algorithm you want to use for solving the board.
6. The output in the terminal depends on using either the random algorithm or the Breadth First algorithm. By filling in 'random' or nothing at all, you get an output reading the number of tries the program has run through the board, as well as the fastest solution in terms of moves. By filling in 'breadth', you get an output reading the minimum amount of moves needed to solve the board, as well as the time it took for the program to solve the board.

## Specifics

Running this program not only gives an output in the terminal, but also creates a csv-file in the 'solutions' tab of this project. The csv-file displays the moves made for the particular boards that has been solved. The first line in the file displays which car is being moved for each move, which direction it went (either 1 or -1) and the amount of moves it took to solve the board. The next lines display the letter the car represents as well as the move that was made.

*Random and Archive algorithm*

When running the random and archive algorithm the terminal displays the amount of 
