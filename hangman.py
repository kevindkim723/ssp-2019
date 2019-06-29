# Purpose of this code is to create hangman game
# Project 1
# 6.21.2019
# Kevin Kim

import random

def findandreplace(word, letter):
    output = ""
    i = 0
    for char in word:
        if char == letter:
            output = output + letter
        else:
            output = output + hud[i]
        i += 1
    return output;


words = ["apple", "banana", "carrot", "cranberry"]
lives = 7
solution = random.choice(words)
hud = "";
i=0;
guess = ""
while i < len(solution):
    hud += "*"
    i = i + 1

while lives > 0:
    print("Guesses left: " + str(lives))
    print("Your current word: " + hud)
    guess = input("Enter a guess of a letter: ").lower()
    if solution.find(guess) != -1 and guess != "":
        print("correct!")
        hud = findandreplace(solution, guess)
    else:
        print("Ur WroNG XD!")
        lives-=1
    if hud.find("*") == -1:
        print("you win!")
        break
    
    

print("game over! Word was: " + solution)
         
