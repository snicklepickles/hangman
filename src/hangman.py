from random import choice


# prints the word with guessed letters, masking un-guessed characters with dashes
def guessed_word(guesses, target):
    return ''.join(letter if letter in guesses else '-' for letter in target)


# prompts user to input letters until attempts are exhausted or word is guessed
def play_game():
    word = choice(["python", "java", "swift", "javascript"])
    guessed_letters = set()
    attempts = 8

    while True:
        if attempts == 0:
            print("\nYou lost!")
            results[1] += 1
            break
        print('\n' + guessed_word(guessed_letters, word))
        if set(word).issubset(guessed_letters):
            print(f"\nYou guessed the word {word}!\nYou survived!")
            results[0] += 1
            break
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
        elif guess.isupper() or not guess.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif guess in guessed_letters:
            print("You've already guessed this letter.")
        elif guess not in word:
            print("That letter doesn't appear in the word.")
            guessed_letters.add(guess)
            attempts -= 1
        else:
            guessed_letters.add(guess)


# displays menu where players can choose to either play, see their score, or exit
results = [0, 0]  # wins, losses
print(f"H A N G M A N")

while True:
    cmd = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if cmd == 'exit':
        break
    elif cmd == 'play':
        play_game()
    elif cmd == 'results':
        print(f"You won: {results[0]} times. You lost: {results[1]} times.")
