
import random

words = ["apple", "train", "river", "cloud", "brain"]
secret_word = random.choice(words)

guessed_letters = []
tries = 6

print("🎮 Welcome to the Hangman Game!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

while tries > 0:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}")

    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word: ", display.strip())

    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 You won! The word was:", secret_word)
        break

if tries == 0:
    print("\n💀 Game over! The correct word was:", secret_word)
