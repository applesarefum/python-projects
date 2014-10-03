
def namein():
    name = input ("Who are you?").title ().strip()
    if name == ("Will") or ("William"):
        for count in range(3):
            passwordin()
        input('Too many attempts')
        input('program end')
    else:
        input('User Non-Existent')

def passwordin():
    password = input ("What's your Password?(Case-Sensitive)")
    if password == ('password'):
        input('Welcome, '+name)
    else:
        print('Incorrect')
        passwordin()

    
