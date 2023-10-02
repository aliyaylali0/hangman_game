import random
import hangman_art
import hangman_words

print(hangman_art.logo)

stages = hangman_art.stages

word_list = hangman_words.word_list
word = random.choice(word_list)
word_length = len(word)
#testing code
print(f"The solition is {word}")

#create blanks
display = []
for a in range(0, len(word)):
    display.append('_')

live_index = int(len(stages)) - 1

al_ready_letter = []
game = True
while game:


    guess = input("Guess the letter: ").lower()

    al_ready_letter.append(guess)

    if guess in al_ready_letter:
        print("you have used this letter before")

    if guess in word:
        for position in range(word_length):
            letter = word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
        print(stages[live_index])

    else:
        live_index -= 1
        print(stages[live_index])

    if live_index == 0:
        print("You lost")
        game = False


    if '_' not in display:
        print("You Win")
        game = False



    print(display)