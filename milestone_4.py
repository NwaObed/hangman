import random
import milestone_2
import milestone_3

word_list = milestone_2.word_list


class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = [""]*len(self.word)
        self.num_letters = len(set(self.word_guessed))
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f'Good guess! {self.guess} is in the word')

            for idx, val in enumerate(self.guess):
                if val == self.ask_for_input.guess:
                    self.word_guessed[idx] = val
            self.num_letters =- 1

        else:
            self.num_lives -= 1
            print(f'Sorry, {self.guess} is not in the word')
            print(f'you have {self.num_lives} left')


    def ask_for_input(self):
        while True:
            self.guess = input('Please enter a single letter : ')
            if self.guess != 1 and self.guess.isalpha() is False:
                print(f"""Invalid letter. Please enter a single alphabetical 
                character""")
            elif self.guess in self.list_of_guesses:
                print(f'You already tried that letter')
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)

Game = Hangman(word_list)

Game.ask_for_input()