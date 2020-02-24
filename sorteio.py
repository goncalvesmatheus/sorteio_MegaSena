import random


class MyClass:
    def __init__(self):
        self.result = {}

    # Function start the random numbers
    def sorteio(self, repeat):
        try:
            # get the variable repeat and put in another string to convert for integer
            repeat_str = repeat.get()
            # converting the string repeat_str to integer and adding to variable repeat
            repeat = int(repeat_str)
            game = []
            i = 0
            while i < repeat:
                while len(game) < 6:
                    num = random.randrange(1, 60)
                    if num in game:
                        continue
                    else:
                        game.append(num)
                self.result[i] = sorted(game)
                i += 1
                game = []
            return self.result
        except:
            print('Informação inválida.')

    def advancedMode(self):
        print('Advanced Mode.')
