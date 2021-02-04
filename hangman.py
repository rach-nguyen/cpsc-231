import sys
import random
import stdio
import hangdraw
def draw_man():

        if guesses <=7:
            hangdraw.head()
        if guesses <=6:
            hangdraw.torso()
        if guesses <=5:
            hangdraw.left_arm()
        if guesses <=4:
            hangdraw.right_arm()
        if guesses <=3:
            hangdraw.left_leg()
        if guesses <=2:
            hangdraw.right_leg()
        if guesses <=1:
            hangdraw.gallows()
        if guesses == 0:
            hangdraw.face()

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

print("The secret word looks like:")
#shows secret word as dashes
secret_word = random.choice(new_list)
dashes = "_ "*len(secret_word)
secret_list = list(secret_word)
dashes_list = list(dashes)
reveal = dashes_list
print("".join(reveal))
hangdraw.wrong()
hangdraw.word(reveal)

while guesses > 0 and "_" in dashes_list:

    print("What is your next guess?")
    guess_typed=stdio.readString()
    all_guesses.append(guess_typed)

    for i in range(len(secret_list)):
        if secret_list[i] == guess_typed:
            dashes_list[i*2] = secret_list[i]
            reveal = dashes_list
    #correct guess
    if guess_typed in dashes_list:
        print("".join(reveal))
        hangdraw.word(reveal)
        print("Nice Guess!")
        
    #wrong guess
    else:
        if guess_typed not in bad_guesses:
            print("Sorry, there is no", guess_typed)
            bad_guesses += guess_typed
            print("Your incorrect guesses are:", bad_guesses)
            guesses -= 1
            hangdraw.wrong_letters(bad_guesses)
            draw_man()

        elif guess_typed in all_guesses:
            print("You have already tried", guess_typed, "please choose a different letter.")
                
    #if the game has been won
    if "_" not in dashes_list:
        hangdraw.win()
        break
    #if the game has been lost
    if guesses == 0:
        print("Unfortunately, you could not guess the word.")
        print("The word was", secret_word)
        hangdraw.lose()
        break