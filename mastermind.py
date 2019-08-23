# Master Mind
import random

class MasterMind:
    colors = ['A','B','C','D','E','F','G']
    def __init__(self, color_num = 6, game_num = 4):
        self.solution = []
        self.colors = self.colors[:color_num]
        for i in range(game_num):
            self.solution.append(random.choice(self.colors))
        self.round = 1
        self.game = [] # list of guess ['ABCD', ...]
        self.result = [] # list of tuple [(A,B), ...]
        print('--- Master Mind ---')
        print('colors: {}'.format(','.join(self.colors)))
        print('===================')

    def evaluate(self, guess):
        game_num = len(self.solution)
        if len(guess) != game_num:
            print('must input {} colors each round'.format(game_num))
            return
        a, b = 0, 0
        solution_copy = []
        guess_copy = []
        for i in range(game_num):
            if self.solution[i] == guess[i]:
                a += 1
            else:
                solution_copy.append(self.solution[i])
                guess_copy.append(guess[i])
        
        for g in guess_copy:
            if g in solution_copy:
                solution_copy.remove(g)
                b += 1

        print('round {} : A: {}  B: {}'.format(self.round, a, b))
        self.result.append((a,b))
        self.round += 1            

    def hint(self):
        print('game over, the solution is: {}'.format(','.join(self.solution)))

    def play(self):
        while self.round <= 12:
            guess = input("input {} colors: ".format(len(self.solution)))
            self.evaluate(guess)
            if(self.result[-1] == (4,0)):
                print("Congratulations!")
                break
        self.hint()

if __name__ == '__main__':
    mastermind = MasterMind()
    mastermind.play()

    
