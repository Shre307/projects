import random

word_list = ["sam", "balayya", "thor"] 
chosen_word = random.choice(word_list)
print(f"pssst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display+="_"
print (display)

end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter==guess:
            display[position] = letter
    print(display)
    
    if "_" in display:
        end_of_game = True
        print("You Win!")