import random
moves=['Rock','Paper','Scissors']

def pa():
        yn=input('Play again?(Y/N)').strip().upper()
        if yn=='Y':
            rps()
        elif yn=='N':
            pass
        else:
            print("Sorry, didn't get that")
            pa()

print("Welcome to Rock, Paper, Scissors!")

def rps():
    print('Rock, Paper, Scissors, Shoot!')
   #plch = Player Choice
    plch=input('What do you pick? ').strip().title()
   #aich = AI Choice
    aich=random.choice(moves)

    if plch==aich:
        print('You both chose '+plch+'!')
        print("It's a draw!")
    else:
        print('You chose '+plch+'!')
        print('Your opponent chose '+aich+'!')
    if plch=='Rock':
        if aich=='Scissors':
            print('You win!')
        elif aich=='Paper':
            print('You lose!')

    elif plch=='Paper':
        if aich=='Rock':
            print('You win!')
        elif aich=='Scissors':
            print('You lose!')

    elif plch=='Scissors':
        if aich=='Paper':
            print('You win!')
        elif aich=='Rock':
            print('You lose!')
#if plch!=moves do ONLY print(idk message)
    else:
        print("I don't know that one")
        rps()
    pa()
rps()
