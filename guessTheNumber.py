# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:26:50 2022

@author: mbuch
"""

def main():
    import numpy
    import sys
    
    generatedNumber = numpy.random.choice(range(1,1000))
    numberOfTries = 1
    
    print('I am thinking about the number from 1 to 1000.')
    print('Guess the number')
    
    while True:
        guessNumber = int(input(print
                        (f'What is your guess number {numberOfTries}? >>> ')))
        
        if guessNumber == generatedNumber:
            print(f'Correct! You guessed in {numberOfTries} tries')
            sys.exit('Thanks for playing')
        elif guessNumber < generatedNumber:
            print('Your number is to small. Guess once again.')
            numberOfTries += 1
        elif guessNumber > generatedNumber:
            print('Your number is to big. Guess once again')
            numberOfTries += 1


if __name__ == '__main__':
    main()