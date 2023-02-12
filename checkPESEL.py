# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 22:35:09 2022

@author: mbuch
"""

# =============================================================================
# To check if 11 digit PESEL is correct you have to:
# 
# Multiply first number by 1
# multiply second number by 3
# multiply third number by 7
# multiply fourth number by 9
# multiplu fifth number by 1
# multiply sixth number by 3
# multiply seventh number by 7
# multiply eight number by 9
# multiply ninth number by 1
# multiply tenth number by 3
# multiply eleventh number by 1
# 
# If the sum of this numbers can be devided by 10 the pesel is correct.
# First 6 digits of pesel is a code for a date of birth. For people born after 
# year 2000, 20 is added to a month number.
# Tenth number is even for female and odd for male
# 
# This PESEL is correct: 44051401458, 22222222222
# This PESEL is incorrect: 12345678901
# =============================================================================

def main():
    
    peselList = list(input('Enter your PESEL number: '))
    decodeList = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    
    digitSum = 0

# PESEL check    
    for digit in range(11):
        digitSum += int(peselList[digit]) * decodeList[digit]

    if digitSum % 10 == 0:
        print('PESEL is correct')
        
        # gender check
        if int(peselList[9]) % 2 == 0:
            print('You are registered as a female')
        else:
            print('You are registered as a male')
                
        ## date of birth
        if int(peselList[2]) == 2:
            yearOfBirth = str(2000 + int(peselList[0]) * 10 + int(peselList[1]))
            monthOfBirth = peselList[3]
            dayOfBirth = str(int(peselList[4]) * 10 + int(peselList[5]))
            print(f'Your date of birth is {yearOfBirth}-{monthOfBirth}-{dayOfBirth}')
        elif int(peselList[2]) == 3:
            yearOfBirth = str(2000 + int(peselList[0]) * 10 + int(peselList[1]))
            monthOfBirth = str(10 + int(peselList[3]))
            dayOfBirth = str(int(peselList[4]) * 10 + int(peselList[5]))
            print(f'Your date of birth is {yearOfBirth}-{monthOfBirth}-{dayOfBirth}')
        elif int(peselList[2]) < 2:
            yearOfBirth = str(1900 + int(peselList[0]) * 10 + int(peselList[1]))
            monthOfBirth = str(int(peselList[2]) * 10 + int(peselList[3]))
            dayOfBirth = str(int(peselList[4]) * 10 + int(peselList[5]))
            print(f'Your date of birth is {yearOfBirth}-{monthOfBirth}-{dayOfBirth}')
            
    else:
        print('PESEL is incorrect')


    

if __name__ == '__main__':
    main()