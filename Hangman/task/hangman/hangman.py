import random
import re


# do initial checks for entered guess
def guess_checker(guess_char):
    if len(guess_char) > 1 or len(guess_char) == 0:
        return False, "Please, input a single letter.\n"

    if not re.search("[a-z]", guess_char):
        return False, "Please, enter a lowercase letter from the English alphabet.\n"

    if guess_char in guess_set:
        return False, "You've already guessed this letter.\n"

    guess_set.add(guess_char)
    return True, ""


def find_letter(letter, random_word):
    found_indexes = []
    for x, char in enumerate(random_word):
        if char == letter:
            found_indexes.append(x)
    return found_indexes


def replace_dash(guess_indexes, guess_char, random_word_dash):
    new_word = []

    for x, char in enumerate(random_word_dash):
        if x in guess_indexes:
            new_word.append(guess_char)
        else:
            new_word.append(char)
    return "".join(new_word)


def show_menu():
    valid_actions = ["play", "results", "exit"]
    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:\n')
        action = input()
        if action in valid_actions:
            return action


def play_game():
    random_word = random.choice(the_word_list)
    random_word_dash = "-" * len(random_word)
    attempts = 8
    did_win = False
    while attempts > 0:
        print(random_word_dash)
        print("Input a letter: ")
        guess = input()

        guess_tuple = guess_checker(guess)

        if guess_tuple[0]:
            # guess passed initial checks try and place letter
            indexes = find_letter(guess, random_word)
            if len(indexes) > 0:
                replacement = replace_dash(indexes, guess, random_word_dash)
                random_word_dash = replacement
                print()
            elif len(indexes) == 0:
                print("That letter doesn't appear in the word.\n")
                attempts -= 1

        else:
            # guess failed initial validation checks so do not remove entry, and try again
            print(guess_tuple[1])

        if random_word_dash.find("-") == -1:
            did_win = True
            break

    guess_set.clear()

    if attempts == 0 and not did_win:
        print("You lost!")
        return False
    else:
        print(f"You guessed the word {random_word}!")
        print("You survived!")
        return True


guess_set = set()
the_word_list = "python", "java", "swift", "javascript"
win_count = 0
lost_count = 0

print("H A N G M A N")

while True:
    play_action = show_menu()
    if play_action == "play":
        result = play_game()
        if result:
            win_count += 1
        else:
            lost_count += 1
    elif play_action == "results":
        print(f"You won: {win_count} times.")
        print(f"You lost: {lost_count} times.")
    else:
        break
