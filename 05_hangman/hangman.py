import random
import string


from random_words import words


def get_word(list_words):
  word_to_guess = random.choice(list_words)

  while '-' in word_to_guess or ' ' in word_to_guess:
    word_to_guess = random.choice(list_words)

  return word_to_guess.upper()


def hangMan():
  print("\nTry to guess a word")

  word = get_word()
  # chars = list(word)
  # length = len(chars)
  
  letters_to_guess = set(word) # Conjunto, no tiene elementos repetidos
  letters_guessed = set() # != {} <- Diccionario
  alphabet = set(string.ascii_uppercase) # Abecedario sin "Ñ"

  lives = 6

  while len(letters_to_guess) > 0 and lives > 0:
    hearts = '♥' * lives
    print(f'{6} lives ' + hearts)
    print(f'Used letters: {' '.join(letters_guessed)}')


    # print(HANGMANPICS[failures])
    

    letter = input("\nType a letter: ")

    if letter in chars:
      print('guess')
    else:
      print('wrong')
      failures += 1
      print(HANGMANPICS[failures])


hangMan()
