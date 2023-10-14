import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def get_word():
  words = 'valoracion comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco anillo estrella'.split()

  return random.choice(words)


def hangMan():
  word = get_word()
  chars = list(word)
  num_chars = len(chars)

  # print(word)
  # print(chars)
  # print(num_chars)

  failures = 0

  print("Try to guess a word")
  # print(HANGMANPICS[failures])
  letter = input("\nType a letter: ")

  letterInWord = letter in word
  print(letterInWord)

  max = num_chars + 1

  # while failures != max or win:
  #   if letter in chars:
  #     print('guess')
  #   else:
  #     print('wrong')
  #     failures += 1
  #     print(HANGMANPICS[failures])
    




hangMan()
