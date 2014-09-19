import random
input("Welcome to the Magic 8 Ball.")
input("Enter your query, see your fate")
answers = ["Yes","No","Maybe","Perhaps","I am unsure","Yes","No","Maybe","Perhaps","I am unsure","No","Maybe","Perhaps","I am unsure","No","Maybe","Perhaps","I am unsure","IDK BRUH"]
def ask():
    print ("What would you like to know?")
    question = input ("> ").lower().strip()
    if question != "penis?":
        print(question)
        answer = random.choice(answers)
        print(answer)
    else:
        print(question)
        input("penis.")
    ask()
ask()
