import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'Enter a random numberbetween 1 and {x} :'))
        if guess < random_number:
            print("Sorry try higher")
        elif guess > random_number:  
            print("sorry try lower")
    print(f"correct guess in {random_number}")
guess(10)





