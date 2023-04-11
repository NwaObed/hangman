import random
#import milestone_2

#word_list = milestone_2.word_list


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
        self.num_letters = int(len(set(self.word))) 
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f'Good guess! {guess} is in the word')
            for idx, val in enumerate(self.word):
                if val == guess:
                    self.word_guessed[idx] = val
            self.num_letters -= 1
            

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'you have {self.num_lives} left')


    def ask_for_input(self):
        while True:
            user_choice = input('Please enter a single letter : ')
            if len(user_choice) != 1 and user_choice.isalpha() is False:
                print(f"""Invalid letter. Please enter a single alphabetical 
                character""")
            elif user_choice in self.list_of_guesses:
                print(f'You already tried that letter')
            else:
                self.check_guess(user_choice)
                self.list_of_guesses.append(user_choice)
                break
        
def play_game(word_list):
    
    game = Hangman(word_list)

    while True:
        print(game.num_lives)
        print(game.word)
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

word_list = ['apple','banana','orange','cherry','pineapple']

play_game(word_list)