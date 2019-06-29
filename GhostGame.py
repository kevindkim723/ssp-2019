# Purpose of this code is to create ghost game
# Project 1
# 6.21.2019
# Kevin Kim

#globals
content = []
with open("words.txt") as f:
    content = f.readlines()
f.close()
content = [x.strip() for x in content] #deletes all \n from the strings in the list

def checkIfCanFormWord(wordInput):
    wordLength = len(wordInput)
    for index in range(len(content)):
        if content[index][0:wordLength] == wordInput:
            return True

    return False
def checkIfOver3LetterWord(wordInput):
    wordLength = len(wordInput)
    if (wordLength <= 3):
        return False
    else:
        if (wordInput in content):
            return True

    return False

#game variables
turn = 0;
word = "";

player1win = False
player2win = False
while(not (player1win or player2win)):
    playnum = turn%2 + 1
    print("It is player" + str(playnum) + "'s turn")
    print("word is: " + word)
    x = input("Please enter the next letter: ").lower()
    word += x

    if ((checkIfOver3LetterWord(word)) or (not checkIfCanFormWord(word))):
        print("player " + str(playnum) + "has lost!")
        if(playnum == 1):
            player2win = True
        else:
            player1win = True
    turn+=1
    
    


