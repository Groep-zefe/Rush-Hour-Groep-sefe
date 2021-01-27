import csv
import time
import os, sys

from pathlib import Path

from code.classes.board import Board
from code.algorithms.breadth_first import Breadth


class Solution:
    def __init__(self, game, results):
        """ Generates a given solution in a csv file."""

        self.game = game
        self.results = results
        self.fastest_game = 100000
        self.path = "solutions/" 
        self.dirs = os.listdir(self.path)

     
    def find_fastest(self):
        """ Finds the fastest solution that has been found for a game."""

        i = 0 
    
        for file in self.dirs: 
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                with open(f'solutions/solution_game_{self.game}.{i}.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    row1 = next(reader)
                    self.fastest_game = int(row1[2])
            i += 1

   
    def save_solution(self): 
        """ Saves the solution only if there faster than the fastest."""
        
        if len(self.results) < self.fastest_game:
            self.fastest_game = len(self.results)
            
            i = 0 
            for file in self.dirs:  
                my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
                if my_file.is_file():
                    i += 1

            # Writes the solution in a csv file in the right format
            with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['car', 'move', len(self.results)]) 
                writer.writerows(self.results)
    
    # Checks if the current solution is not longer than the fastest        
    def result_check(self):
        if len(self.results) >= self.fastest_game:
            return True
    

        
                
