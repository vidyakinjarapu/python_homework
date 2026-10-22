def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        shown = "".join([letter if letter in guesses else '_' for letter in secret_word])
        print(shown)

        print(all(letter in guesses for letter in secret_word))
        return all(letter in guesses for letter in secret_word)
    
    return hangman_closure

secret = input("Enter the secret word: ")
secret = secret.lower()
hangman = make_hangman(secret)
done = False
while not done:
    letter = input("Guess a letter in the word: ")
    done = hangman(letter)
print("Correct! You guessed it!")