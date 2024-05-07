import word_list  # Includes the list of words
import random  # For picking a random word
import colorama  # For colored output
colorama.init(autoreset=True)  # Reset the color after each print

# Backend stuff + game logic, done by Sam

class Wordle:  # Class for the game mechanics
    def __init__(self, word_list=word_list.words):
        """
        Initializes a new instance of the Wordle class.
        Parameters:
            word_list (list, optional): A list of words to choose from. Defaults to word_list.words
        Returns:
            None
        """
        self.word_list = word_list  # A list of words to choose from
        print("Welcome to definitely not wordle")

    def start_game(self):
        self.chosen_word = random.choice(self.word_list)  # Pick a random word from the list
        print(self.chosen_word)

    def end_game(self, has_won):
        """
        Ends the game with the given outcome and winner.

        Parameters:
            has_won (bool): If a player has won the game.

        Returns:
            None
        """
        if has_won:
            print("You won! The word was", colorama.Back.GREEN + self.chosen_word)
        else:
            print("You lost! The word was", colorama.Back.RED + self.chosen_word)

        if input("Do you want to play again? (y/n) ").lower() == "y":  # Ask if the player wants to play again
            player.guesses.clear()
            game.start_game()  # Start a new game
        else:
            print("Thanks for playing!")
            exit(0)  # Exit the program

    def check_guess(self, guess):
        """
        Checks if the given guess matches the chosen word and prints the letters in corresponding colors.

        Parameters:
            guess (str): The guessed word.

        Returns:
            None
        """
        output = ""
        if guess == self.chosen_word:
            print(colorama.Back.GREEN + colorama.Style.BRIGHT + self.chosen_word)
            self.end_game(True)
        else:
            for letter in range(5):
                if guess[letter] == self.chosen_word[letter]:
                    output += colorama.Back.GREEN + colorama.Style.BRIGHT + guess[letter]
                elif guess[letter] in self.chosen_word:
                    output += colorama.Back.YELLOW + colorama.Style.BRIGHT + guess[letter]
                else:
                    output += colorama.Back.RED + colorama.Style.BRIGHT + guess[letter]

        print(output)

class Player:
    def __init__(self):
        """
        Initializes a new instance of the Player class.

        Parameters:
            None

        Returns:
            None
        """
        self.guesses = []  # List of guesses the player has made

    def guess(self):
        """
        A function that allows the player to make a guess for a chosen word.
        Continuously prompts the player for a guess until a valid word is entered.
        Checks if the guess is valid, not already guessed, and of the correct length.
        Prints error messages for invalid or repeated guesses.
        Adds the valid guess to the list of guesses and checks it against the chosen word using 'game.check_guess'.

        Parameters:
            None

        Returns:
            None
        """
        while True:
            guess = input("Guess a five letter word: ").upper()
            if guess.isalpha() and len(guess) == 5:  # Checks if the guess is comprised 100% of letters and is 5 letters long
                break  # If it is, break out of the loop
            elif guess in self.guesses:  # If the guess has already been guessed, print an error message
                print("You already guessed that word")
            else:
                print("Please enter a valid word")  # If the guess is invalid, print an error message

        self.guesses.append(guess)  # Add the guess to the list of guesses the player has made
        game.check_guess(guess)  # Check if the guess is correct


game = Wordle()
player = Player()

game.start_game()

while len(player.guesses) < 6:
    player.guess()
