from itertools import product

class MasterMindSolver:
    color_list = [chr(i) for i in range(65,91)]
    possible_solutions = set()
    guess_dict = dict()
    
    
    def __init__(self, color_num = 6, game_num = 4):
        self.color_list = self.color_list[:color_num]
        all_combination = product(self.color_list, repeat = game_num)
        for p in all_combination:
            self.possible_solutions.add(''.join(list(p)))

    
    def filter_solutions(self):
        for guess, result in self.guess_dict.items():
            self.possible_solutions = set(filter(lambda x: result == self.evaluate_solution(guess, x), self.possible_solutions))

    
    def evaluate_solution(self, guess, solution):
        a, b = 0, 0
        solution_length = len(solution)
        solution_copy = []
        guess_copy = []
        for i in range(solution_length):
            if solution[i] == guess[i]:
                a += 1
            else:
                solution_copy.append(solution[i])
                guess_copy.append(guess[i])
        
        for g in guess_copy:
            if g in solution_copy:
                solution_copy.remove(g)
                b += 1

        return (a,b) 

    def start(self):
        game_round = 0
        while game_round < 10:
            input_game = input("input Guess and result: ")
            input_game = input_game.split(' ')
            input_guess = input_game[0]
            input_result =  tuple(map(int, list(input_game[1])))
            self.guess_dict.update([(input_guess, input_result)])
            self.filter_solutions()
            if len(self.possible_solutions) == 0:
                print("Can't find solution for the game")
                break
            elif len(self.possible_solutions) == 1:
                print("Solution is {}".format(self.possible_solutions))
                break
            print('possible solutions:')
            print(self.possible_solutions)
            game_round += 1



if __name__ == '__main__':
    solver = MasterMindSolver()
    solver.start()
