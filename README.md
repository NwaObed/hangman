# Hangman


<p align="center">
  <img src="https://m.media-amazon.com/images/I/71muLEFqj4L.png">
</p>
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1
In this milestone, I was able to set up GitHub. GitHub is a version control software used to keep track of project development. I installed GitHub, and created a repo that will host my project file remotely. This technique will enable me to work on different aspects of the same project independently and in the end merge them to have a complete project.

## Milestone 2
Yes, it is connected to the previous milestone. First, this README.md was part of the files I created while creating the repo. Second, I cloned the repo to my local machine which the same as downloading the repo before I started performing the required tasks. 

- I have imported the random module that was used to randomly pick a word from the list of words provided.

## Milestone 3
I created two functions in this milestones -- ```check_guess``` to check and ensure the user input is a single alphabetical character and ```ask_for_input``` to get the player's guess or input.

## Milestone 4
In this milestone I have implemented the Hangman class, creating the class constructor method _init_ where all the class attributes has been declared and two other methods to ask for the user input and then check it.

## Milestone 5

I have completed the whole game following the following steps:

### Defining the ```Hangman``` class
- Using the keyword ```class```, I defined the class object ```Hangman```
- Next, I initiated the attributes of the class with ```__init__()``` method. This method gives initial values of the attributes each time an instance of ```Hangman``` class is created. It is not mandatory to use it, but it is a good practice to use easily when we have attributes that have default values.

### Defining the methods.
Methods are functions defined within a ```class``` object. As such, all methods are functions but the converse is not always true. In this game, there are three methods:
#### ask_for_input() method
This method takes no positional argument. It collects inputs from the user using the keyword ```input```. After receiving the input from the user, it then does the following four works:
- Ensure the user input is a single alphabetical character, otherwise iterate until the user enters a single alphabetical character
- Ensure, the user does not enter the same alphabetical character twice
- Keep a record of the user inputs in a ```list_of_guesses```.

#### check_guess() method
This method takes one positional argument -- user guess. It performs the following functions:
- Ensures the user input is in lowercase
- Checks if the user input is correct ie if the single alphabetical character is in the randomly picked word
- If the user input is correct, insert in the correct position of the random word.

#### play_game() method
This is the chief method that sets the game in motion. It takes one positional argument -- list of fruits. It then creates an instance of the ```Hangman``` object and finally allows the user to play the game until they either win or lose. Each user has a number of lives (```num_of_lives```) with default value of 5 that is the number of wrong guesses allowed and not the number of attempts. So a user will lose if they record ```num_of_lives``` wrong guesses. On the other hand, the user will win when the user have not exhausted their ```num_of_lives``` and have guessed all the ```unique``` charaters of the random word.