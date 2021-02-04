import sys
import random
import stdio
words_file = open ('cpsc231-lexicon.txt')
words_lines = words_file.readlines()
words_file.close()
num_words = len(words_lines)
sys.argv[1] = words_file

words_list = []
new_list = []
bad_guesses = ""
all_guesses = []
guesses = 8
#making list with just 4+ letter words from lexicon
for i in range(num_words):
    words = words_lines[i].rstrip()
    words_list.append(words)
for i in words_list:
    if len(i)>=4:
        new_list.append(i)

print("Hello! Welcome to CPSC 231 Console Hangman!")
print("The secret word looks like:")
#shows secret word as dashes
secret_word = random.choice(new_list)
dashes = "-"*len(secret_word)
secret_list = list(secret_word)
dashes_list = list(dashes)
reveal = dashes_list
print("".join(reveal))
print("The number of guesses you have left is:", guesses)

while guesses > 0 and "-" in dashes_list:

    print("What is your next guess?")
    guess_typed=stdio.readString()
    all_guesses.append(guess_typed)

    for i in range(len(secret_list)):
        if secret_list[i] == guess_typed:
            dashes_list[i] = secret_list[i]
            reveal = dashes_list
    #correct guess
    if guess_typed in dashes_list:
        print("".join(reveal))
        print("Nice Guess!")
    #wrong guess
    else:
        if guess_typed not in bad_guesses:
            print("Sorry, there is no", guess_typed)
            bad_guesses += guess_typed
            print("Your incorrect guesses are:", bad_guesses)
            guesses -= 1
            print("The number of guesses you have left is:", guesses)

        elif guess_typed in all_guesses:
            print("You have already tried", guess_typed, "please choose a different letter.")
                

    #if the game has been won
    if "-" not in dashes_list:
        print("Congratulations! The word was", secret_word)
        print("You win!")
        break
    #if the game has been lost
    if guesses == 0:
        print("Unfortunately, you could not guess the word.")
        print("The word was", secret_word)
        print("GAME OVER")
        break