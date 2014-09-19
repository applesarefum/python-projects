lra=[["L","R"]]
def AAH():
    X=(2*X)
    print(X)
    AAH()
def leftright():
    lr=input("lr?").strip().upper()
    if lr=="L":
        input("LETF")
    if lr=="R":
        input("RGIHT")
        AAH()
    if lr=="T":
        input("LOL")
    leftright()
X=input("what is X?")
print(X)
leftright()

    
    
    
