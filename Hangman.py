from random import choice


class Hangman:

    def __init__(self):
        self.word = choice(('python', 'java', 'kotlin', 'javascript'))
        self.dashes = list('-' * len(self.word))
        self.lives = 8
        self.set_of_letters = set()
        
    def menu(self):
        print('H A N G M A N\n')
        play_opt = input("""Type "play" to play the game, "exit" to quit:""")
        if play_opt == "play":
            self.play()

    def check_guessed_word(self, letter):  
            if len(letter) != 1:
                print("You should input a single letter")
                return            
            if not letter.islower():
                print("Please enter a lowercase English letter")
                return
            if letter not in self.set_of_letters:
                if letter not in self.word:
                    self.lives = self.lives - 1
                    print("That letter doesn't appear in the word")
                else:
                    for word_index in range(len(self.word)):
                        if self.word[word_index] == letter:
                            self.dashes[word_index] = letter
                self.set_of_letters.add(letter)
            else:
                print("You've already guessed this letter")


    def play(self):
        while self.lives != 0:
            print()
            print(''.join(self.dashes))
            letter_input = input('Input a letter: ')
            self.check_guessed_word(letter_input)
            if '-' not in self.dashes:
                print(''.join(self.dashes))
                print('You guessed the word!\nYou survived!')
                break
        if self.lives == 0:
            print('You lost!')


Hangman().menu()
