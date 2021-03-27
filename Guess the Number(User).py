import random

def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low   #could also be high because low=high
        feedback=input(f"Is the {guess} number too  high(H) or too low(L) or correct(C): ").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
            
    print(f"Congrats computer you guess the number {guess} correctly")
            
computer_guess(100)
