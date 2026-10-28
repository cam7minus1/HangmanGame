import random
is_running = True

def pick_random_word():
    words = ["Hello", "World", "Cool", "Cordy"]
    rand_index = random.randint(0, len(words)-1)
    return words[rand_index]

def display_board(data):

    msg_board = ""

    for entry in data:

        if entry["found"] == True:
            msg_board += entry["key"]
        else:
            msg_board += "_"

        msg_board += " "

    print(msg_board)

def display_past_guesses(data):
    msg = ""
    for char in data:
        msg += char + " "

    print(f"Already gussed: {msg}")

def run_game():
    global is_running
    max_attempts = 5
    selected_word = pick_random_word()
    guessed_list = []
    past_guesses = []

    for c in selected_word:
        entry = {
            "key": c,
            "found": False
        }
        guessed_list.append(entry)

    e_message = None
    while max_attempts > 0:

        print("\n" * 30)
        print("="*30)
        print("\n")
        display_board(guessed_list)
        print("\n")
        display_past_guesses(past_guesses)
        print("\n")
        print(f"Attempts remaining: {max_attempts}")
        print("="*30)

        if e_message:
            print(e_message)
            e_message = None

        guess = input("Choose a letter: ")

        # Check for invalid input
        if len(guess) != 1:
            e_message = "Invalid guess length try again!"
            continue

        # Ensure its not numbers or weird characters
        if not guess.isalpha():
            e_message = "Must be alphabetical guesses!"
            continue

        # Skip past guesses
        if guess in past_guesses:
            e_message = "You already guessed that try again!"
            continue

        # Check win and update data
        found_char = False
        guessed_all = True
        for entry in guessed_list:

            # Mark the key as found if we guessed it
            if entry["key"].lower() == guess.lower():
                found_char = True
                entry["found"] = True

            # If any are not found then set guessed_all to false
            if entry["found"] == False:
                guessed_all = False

        if guessed_all:
            print("You win!!!!")
            return

        if not found_char:
            # Append guess to past guesses
            past_guesses.append(guess)
            print("Incorrect... try again")
            max_attempts -= 1

    print("You lose! :(")


while is_running:

    run_game()

    play_again = input("Want to play again? (y/n)")
    if play_again.lower() == "n":
        is_running = False