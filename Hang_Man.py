import random
import hangman_stages
import word_file
# word_list=['apple','Banana','Potato','beautiful']
lives=6
Word=random.choice(word_file.Words)
print(Word)

display=[]

# for letter in Word:
for i in range(len(Word)):
  display+='_'
print(display)  

game_over=False

while not game_over:
  guessed_letter=input("Guess a Letter:").lower()

  for position in range(len(Word)):
   letter = Word[position]

   if letter == guessed_letter:
     display[position]=guessed_letter

  print(display)

  if guessed_letter not in Word:
    lives-=1  

    if lives==0:
      game_over=True
      print("💀 GAME OVER! You fought bravely, but the word got the best of you! 💀")
  if '_' not in display:
    game_over=True
    print("🌟 VICTORY! You cracked the code, beat the gallows, and saved a life today! 🌟")

  print(hangman_stages.STAGES[lives])  