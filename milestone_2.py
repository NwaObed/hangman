import random

word_list = ['apple','banana','orange','cherry','pineapple']
print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Please enter a single letter : ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! This is not a valid input')