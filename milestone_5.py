import random
import milestone_2
import milestone_3

word_list = milestone_2.word_list


class Hangman():
    """
    word_list : list of fruits
    word : fruit randomly picked from list of fruits
    word_guessed : list of the single letter/charater picked by the user to 
                    form the 'fruit word'
    num_letters : number of chacters that make up the randomly picked word
    num_lives : number of attempts the user have to guess the fruit word correctly
    guess : single charater/letter picked by the user at each attempt
    """
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

            for idx, val in enumerate(self.word):
                if val == self.ask_for_input():
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
        return self.guess

    def play_game(self, word_list):
        self.num_lives = 5
        game = Hangman(word_list, self.num_lives)

        while True:
            if self.num_lives == 0:
                print('You lost!')
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            elif self.num_lives != 0 and self.num_letters <= 0:
                print('Congratulations. You won the game!')
                break

    #play_game(word_list)

Game = Hangman(word_list)

Game.play_game(word_list)