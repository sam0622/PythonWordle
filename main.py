import word_list
import random

class Wordle:
    def __init__(self, word_list=word_list.words):
        """
        Initializes a new instance of the Wordle class.
        Parameters:
            word_list (list, optional): A list of words to choose from. Defaults to word_list.words.
        Returns:
            None
        """
        self.word_list = word_list  # A list of words to choose from

    def start_game(self):
        self.word = random.choice(self.word_list)  # Pick a random word from the list
        
    def end_game(self, has_won, winner):
        """
        Ends the game with the given outcome and winner.

        Parameters:
            outcome (str): The outcome of the game.
            winner (str): The winner of the game. For use if two players are competing.

        Returns:
            None
        """
        pass


class Player:
    def __init__(self):
        self.guesses = []
        self.score = 0
        self.letters = []

    def guess(self, guess):
        guess = input("Guess a word: ").upper()
        self.guesses.append(guess)
        if guess == game.word:
            game.end_game(True, player)




game = Wordle()
player = Player()