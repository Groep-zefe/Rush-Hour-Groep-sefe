import csv

from pathlib import Path
from board import Board

class Solution:

    def __init__(self, game, results):
        self.game = game
        self.results = results
        
    def solution(self): 
        i = 0 
        print(len(self.results))
        while True:  
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                i += 1
            else: break

        with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['car', 'move', len(self.results)]) 
            writer.writerows(self.results)
            
