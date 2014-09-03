import random
input("Welcome to the Magic 8 Ball.")
input("Enter your query, see your fate")
answers = ["Yes","No","Maybe","Perhaps","I am unsure"]
def ask():
    print ("What would you like to know?")
    question = input ("> ")
    print(question)
    answer = random.choice(answers)
    print(answer)
    ask()
ask()
