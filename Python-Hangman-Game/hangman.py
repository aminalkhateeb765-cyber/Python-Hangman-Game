import random
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
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
words = ["bad", "sad", "happy"]
random_word = random.choice(words)
display = ["_"]*len(random_word)
print(" ".join(display))
print(HANGMANPICS[0])

lives = 7
guessed_letter = []
while "_" in display and lives > 0:
   guessed = input("Please guess a letter:")
   if guessed in guessed_letter:
      print("You already guessed that letter.")
      print(f"You have {lives} more tries ")
      continue
   guessed_letter.append(guessed)
   
   if guessed not in random_word:
      lives -= 1
      print(HANGMANPICS[7 - lives])

   
   for position in range(len(random_word)):
      if guessed == random_word[position]:
         display[position] = guessed

   print(f"You have {lives} more tries ")    
   print(" ".join(display))



if lives == 0:
   print("""
   YOU LOSE!
""")
   print(HANGMANPICS[-1])

else:
   print("""
   YOU WIN!
""")