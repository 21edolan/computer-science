guessesremaining=7
spare=''
word='monday'
print('the word to guess is:','___')
print('amount of guesses:',guessesremaining)
correct='_'*len(word)
guesst=input('guess a letter:')
guess=guesst.lower()
spare=spare+guess
while guessesremaining>0:
    if guess in word:
        print('letter in word')
        index=word.find(guesst)
        correct=correct[0:index]+guesst+correct[index+1:]
        print(correct)
        if correct==word:
            print('well done!')
            break
    else:
        print('letter not in word')
        guessesremaining=guessesremaining-1
        print('guesses remaining:',guessesremaining)
    guesst=input('guess a letter:')
    guess=guesst.lower()
    while guess in spare:
        print('you\'ve already used this letter')
        print('the letters you have used are-',spare)
        guesst=input('guess a letter:')
        guess=guesst.lower()
    spare=spare+guess
print('game over')