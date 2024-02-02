import random
import hangman_art as art
import hangman_words as words

lives = len(art.stages) - 1

print(art.logo)
print("Welcome to the Hangman game!")

chosen_word = random.choice(words.word_list)
print(f"Chosen word is {chosen_word}")

display = []
for _ in chosen_word:
    display.append("_")

wrong_guess = []
endgame = False
while not endgame:
    print(art.stages[lives])
    guess = str(input("Guess a letter: ")).lower()
    
    if guess in words.turkish:
        print("This game uses the english alphabet, not the turkish one. Try again.")
        print(f"{"".join(display)} --> Wrong guesses: {wrong_guess}")
    else:
        if guess in display:
            print("That letter was used. Try another one.")
        
        if guess in wrong_guess:
            print("That letter was used. Try another one.")
        else:
            wrong_guess.append(guess)
            if guess not in chosen_word:
                lives -= 1
                print(f"You guessed wrong. Letter {guess} is not in the word. You lost a life.")
            else:
                wrong_guess.remove(guess)

        result = []
        blanks = display.count("_")
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                result.append(index)
                for _ in display:
                    display.pop(index)
                    display.insert(index, guess)
        new_blanks = display.count("_")
        
        if new_blanks < blanks:
            print(f"Bravo! There were {len(result)} instances of the letter {guess} in the word.")

        print(f"{"".join(display)} --> Wrong guesses: {wrong_guess}")
        
        if "_" not in display:
            endgame = True
            print("You win!")
        elif lives == 0:
            endgame = True
            print(art.stages[lives])
            print("You lost!")
