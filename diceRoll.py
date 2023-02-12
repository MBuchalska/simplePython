# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:30:20 2022

@author: mbuch
"""

def rollTheDice(numberOfDice, diceType, rollModifier):
    import numpy
    
    rollList = []
    rollSum = 0    

    for roll in range(1,numberOfDice+1):
        oneRoll = numpy.random.choice(range(1,diceType+1))  
        rollList.append(oneRoll)
        rollSum += oneRoll
        
    rollSum += rollModifier
    
    return [rollList, rollSum]



def basicRoll():
    print('Ok, let me guide you.')
    numberOfDice = int(input('How many dice? >>> '))
    diceType = int(input('What type of die? >>>'))
    rollModifier = int(input('Roll modifier: >>> '))
    
    print('-' * 30)
    print(f'Rolling {numberOfDice}d{diceType}+{rollModifier}')
    rollResult = rollTheDice(numberOfDice, diceType, rollModifier)
    
    print(f'Your roll results: {rollResult[0]}. Final result {rollResult[1]}')
    print('Next roll?')
    
    
    
def advanceRoll():
    
    dIndex = -1
    
    while dIndex == -1:
        roll = input('What roll should I do (i.e. 2d4+6)  >>> ')
        
        dIndex = roll.find('d')
        if dIndex == -1:
            print('Wrong roll. Choose a dice size')
        
    
    if dIndex == 0:
        numberOfDice = 1
    elif dIndex == 1:
        numberOfDice = int(roll[0])
    else:
        numberOfDice = int(roll[:dIndex])
       
    
    if '+' not in roll:
        diceType = int(roll[(dIndex+1):])
        rollModifier = 0
    else:
        diceType = int(roll[(dIndex + 1):roll.find('+')])
        rollModifier = int(roll[(roll.find('+')+1):])

    rollResult = rollTheDice(numberOfDice, diceType, rollModifier)

    print(f'Your roll results: {rollResult[0]}. Final result {rollResult[1]}')
    print('Next roll?')
    
    

def randomRoll():
    import numpy
    
    print('Ok. Lets do RANDOM roll!')
    
    numberOfDice = numpy.random.choice(range(1, 21)) 
    diceType = numpy.random.choice([4, 6, 8, 10, 12, 20, 100]) 
    rollModifier = numpy.random.choice(range(1, 21)) 
    
    print(f'Rolling {numberOfDice}d{diceType}+{rollModifier}')
    rollResult = rollTheDice(numberOfDice, diceType, rollModifier)
    
    print(f'Your roll results: {rollResult[0]}. Final result {rollResult[1]}')
    print('Next roll?')
    
    

def fireball():
    print('You cast Fireball')
    print('Your oponent failed his dexterity saving throw')
    print('Rolling 8d6 for damage')
    
    rollResult = rollTheDice(8, 6, 0)
    
    print(f'You roll {rollResult[1]}.')
    if rollResult[1] == 8:
        print('Your opponent is not impresed')
    elif rollResult[1] <= 20:
        print('It is getting a bit warm here...')
    elif rollResult[1] <= 30:
        print('That was painful for sure')
    elif rollResult[1] <= 40:
        print('You have created a human torch')
    elif rollResult[1] < 48:
        print('It was a massive fireball!')
    elif rollResult[1] == 48:
        print('Your opponent is a toast')


    
def main():
    
    import sys
    
    print('So you want to roll...')
    
    while True:
        print('-' * 30)
        print('What type of roll?')    
        print('1. Simple roll. Guide me please')
        print('2. Advance D&D type roll')
        print('3. Lets go RANDOM!')
        print('4. I cast Fireball!')
        print('5. Finish')
        
        userChoice = int(input('>>> '))
        if userChoice == 1:
            basicRoll()
        elif userChoice == 2:
            advanceRoll()
        elif userChoice == 3:
            randomRoll()
        elif userChoice == 4:
            fireball()
        elif userChoice == 5:
            sys.exit('Good bye. See you later :)')
            



if __name__ == '__main__':
    main()
    
#%%
