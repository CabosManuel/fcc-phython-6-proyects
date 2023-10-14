import random
import string


from random_words import words
from hangman_pics import hangman_pics


def get_word(list_words):
  word_to_guess = random.choice(list_words)

  while '-' in word_to_guess or ' ' in word_to_guess:
    word_to_guess = random.choice(list_words)

  return word_to_guess.upper()


def hangMan():
  print("\nTry to guess a word")

  word = get_word(words)
  
  letters_to_guess = set(word) # Conjunto, no tiene elementos repetidos
  letters_guessed = set() # != {} <- Diccionario
  alphabet = set(string.ascii_uppercase) # Abecedario sin "Ñ"

  lives = 6

  while len(letters_to_guess) > 0 and lives > 0:
    hearts = '♥' * lives
    print(f'{6} lives ' + hearts)
    print(f"Used letters: {' '.join(letters_guessed)}")

    word_progress = [
      # List Comprehension: En una linea según una condición agregar un dato a la lista
      letter
        if letter in letters_guessed 
        else '_'
      for letter in word 
    ]
    # Show hangman
    print(hangman_pics[lives])
    # Show letters separated
    print(f"Word: {' '.join(word_progress)}")

    letter_user = input("Type a letter: ").upper()

    # Add to letters_guessed,
    # if letter in alphabet and not in letters_guessed
    if letter_user in alphabet - letters_guessed: # Resta de "sets" (Conjuntos)
      letters_guessed.add(letter_user)

      # Remove to letters_to_guess,
      # If letter in letter_to_guess, else lost life
      if letter_user in letters_to_guess:
        letters_to_guess.remove(letter_user)
        print('')
      else:
        lives -= 1
        print(f"\nYour letter, {letter_user} not in word")
    # If letter has already been entered
    elif letter_user in letters_guessed:
      print("\nThis letter has already been entered")
    else:
      print("\nThis letter is not valid")

  if lives == 0:
    print(hangman_pics[0])
    print(f"You lose! the word was: {word}")
  else:
    print(f"You win! the word is: {word}")

hangMan()
