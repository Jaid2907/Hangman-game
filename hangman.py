import random as rd
from sys import flags
word_list = ["lick",
             "church",
             "thick",
             "wretched",
             "puncture",
             "grateful",
             "bawdy",
             "shame",
             "stomach",
             "alcoholic",
             "windy",
             "accept",
             "umbrella",
             "boundless",
             "milky",
             "cheer",
             "defective",
             "squeeze",
             "try",
             "order",
             "prefer",
             "lace",
             "vacuous",
             "fold",
             "destruction",
             "thread",
             "remain",
             "travel",
             "sturdy",
             "holiday",
             "dispensable",
             "boring",
             "pricey",
             "sun",
             "tooth",
             "null",
             "need",
             "cows",
             "macho",
             "phobic",
             "arrange",
             "winter",
             "hallowed",
             "descriptive",
             "precede",
             "tight",
             "yard",
             "frantic",
             "price",
             "kitty"
             ]
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
choosen_word = word_list[rd.randint(0,len(word_list)-1)]
choosen_word_arr = []
for i in range(1,len(choosen_word)+1):
  choosen_word_arr.append("_")
str = "".join(choosen_word_arr)
print(f"Current status {str}\n")
hangman_index = 0;

while True:
  choosen_char = input("Guess a letter of the word ----> ")
  flag = 0
  for i in range(0, len(choosen_word)):
    if(choosen_word[i] == choosen_char):
      flag = 1
      choosen_word_arr[i] = choosen_char;
  
  if(flag == 1):
    print("Character is present in word\n")
  else:
    print("You lost one life of Hangman\n")
    print(f"{HANGMANPICS[hangman_index]}")
    hangman_index += 1
  
  str = "".join(choosen_word_arr)
  print(f"Current status {str}\n")
  
  if(hangman_index == len(HANGMANPICS)):
    print("You lost the game")
    print(f"The original word was {choosen_word}")
    break
  elif(choosen_word_arr.count("_") == 0):
    print("Congratulations !!!  You won the game")
    break
  
    