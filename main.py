from hangman_art import stages, logo
from hangman_word import word_list
import random

print(logo)

word = random.choice(word_list)
print(word)

life =6

lis =[]
for _ in word:
    lis.append("_")

print(lis)

is_game_on =True

while is_game_on:
    print(f"you have {life} life to guess the word")
    guess = input('guess the letter in the word ').lower()
    for index in range(len(word)):
        if guess == word[index]:
            lis[index] =guess
    print(lis)        
    if guess not in word:
        life -=1
        print(f"{stages[life]}") 

        if life ==0:
            is_game_on =False
            print('you have no extra attempts to guess the word')     

    if "_" not in lis:
        is_game_on =False
        print("you win")          
        
