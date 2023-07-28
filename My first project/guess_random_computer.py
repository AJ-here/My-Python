import random
def computer_guess(x):
        low=1
        high=x
        feedback = ''
        while feedback != 'c':
                guess=random.randint(low,high)
                feedback= input(f' if {guess} Enter h for high , l for low ,c for correct')
                if feedback=='h':
                    high =guess-1
                elif feedback =='l':
                    low =low+1
        print('guess is right {guess}')