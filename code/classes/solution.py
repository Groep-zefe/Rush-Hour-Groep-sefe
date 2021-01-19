import csv
import time

from pathlib import Path
from board import Board

class Solution:

    def __init__(self, game, results):
        self.game = game
        self.results = results
        self.fastest_game = 100000

    def find_fastest(self):
        i = 0 
        while True:  
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                with open(f'solutions/solution_game_{self.game}.{i}.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    row1 = next(reader)
                    self.fastest_game = int(row1[2])
                i += 1
            else: 
                break
        # print(f"first {self.fastest_game}")
        
    def save_solution(self): 
        # print(f"so fast {len(self.results)}")
        if len(self.results) < self.fastest_game:
            self.fastest_game = len(self.results)
            print(f"I am speed! {self.fastest_game}")
            time.sleep(2)
            i = 0 
            while True:  
                my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
                if my_file.is_file():
                    i += 1
                else: break

            with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['car', 'move', len(self.results)]) 
                writer.writerows(self.results)
            
    def result_check(self):
        if len(self.results) >= self.fastest_game:
            return True
        
                
