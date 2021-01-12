import csv

from pathlib import Path
from board import Board

class Solution:

    def __init__(self, game):
        self.game = game
        self.moves = []
        
    def solution(self): 
        i = 0 

        test_solution = [ ['A', '1'], ['C', '-2'], ['G', '-1']]
        
        while True:  
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                i += 1
            else: break

        with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['car', 'move']) 
            writer.writerows(test_solution)
            
