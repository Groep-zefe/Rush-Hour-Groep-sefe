# Rush-Hour-Groep-zefe

Rush Hour is a puzzle game where the objective is to move vehicles on a board until the red car is able to escape. This program focuses on the ability to solve any board from the game automatically and specifically to do it in as fewest moves as possible using implemented algorithms. The first algorithm implemented was a random with archive algorithm, where random moves were made every turn and distinctive boards couldn't be repeated. The second algorithm implemented was a Breadth First algorithm, where every possible board combination is being visited until the program finds the solution requiring the fewest moves possible. 

## Information about the files

The files are neatly organized in different folders. There are 4 main folders in this project: boards, code, docs and solutions. Furthermore this project contains a README file, an init.py file and a main.py file.

The 'boards' folder consists of the seven boards used for this project, but users can add more boards to this folder if they want to.

The 'code' folder represents the code needed to run this program. In here the 'classes' folder represents the different types of classes used for this program. The 'algorithms' folder represents the 2 different algorithms used for this program, depending on what the user wants to use.

The 'docs' folder consists of the data structure for both the random and the Breadth First algorithm. Both the UML's for these algorithms can be found here.

The 'solutions' folder consists of the csv-files that have been made when running the code.

## Installation

There are several steps needed to succesfully run the code:
1. Have Python installed on your computer (preferably Python 3).
2. Download the files from this repository to your computer. You can also clone the repository to your application using 'git clone https://github.com/Groep-zefe/Rush-Hour-Groep-sefe.git'
3. Open the files in your application that is able to run these files (e.g. Visual Studio Code).
4. Type 'python main.py' in the command bar in the terminal (use 'python3' instead of 'python' if you're running the later Python versions).
5. After the command 'python main.py' you also have the option to choose a board (represented by a number) you want to be solved. Choosing no number results in the first board being selected automatically. After that you have the option to type in either 'random' or 'breadth' to choose the algorithm you want to use for solving the board. typing neither of these will result in running the random and archive algorithm. A full command in the terminal looks like this for example: 
python main.py 2 breadth
This is an example for the second board being solved using the Breadth First algorithm.

## Specifics

Running this program not only gives an output in the terminal, but also creates a csv-file in the 'solutions' tab of this project. The csv-file displays the moves made for the particular boards that has been solved. The first line in the file displays which car is being moved for each move, which direction it went (either 1 or -1) and the amount of moves it took to solve the board. The next lines display the letter the car represents as well as the move that was made.

**Random and Archive algorithm**

When running the random and archive algorithm the terminal displays the amount of times the program tried to run the program (naming it: amount of tries). Whenever a board is solved the program starts a new game with the same board looking for faster solutions. The fastest solution found will also be displayed in the terminal as the amount of moves right under the amount of tries. Everytime a new fastest solution is found a csv-file is created and put in the folder 'solutions'. Beware that the program keeps running, finding new solutions and doesn't stop by itself. The only way to stop is by using a keyboard interrupt in the terminal.

**Breadth First algorithm**

When running the Breadth First algorithm the terminal displays the amount of moves it took to solve the board, as well as the time it took to solve it. After the board has been solved a csv-file will be created displaying the made moves and the program will quit automatically. Note that this algorithms takes a huge strain on the memory of the computer and will likely crash with bigger boards. Every 6x6 board can easily be solved in seconds, however bigger boards, like 9x9 or 12x12, will take much longer and often result in your program crashing due to a memory overload. This is because in the Breadth First algorithm the program looks for at every board possible until it finds the fastest solution and every board that has been visited is put in a dictionary, which can become incredibly long over time with the bigger boards.
