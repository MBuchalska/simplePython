# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:21:09 2022

@author: mbuch
"""

def main():
    import string
    import numpy
    import random
    
    alphabet = list(string.ascii_letters)
    passwordList = []
    
    print('Welcome in the password generator')
    passwordLength = int(input('Enter the length of your password: >>> '))
    
    for letter in range(passwordLength):
        letter = numpy.random.choice(alphabet)
        passwordList.append(letter)
        
    
    random.shuffle(passwordList)
    finalPassword = ''.join(passwordList)
    print(f'Your randomly generated password: {finalPassword}')
    
    

if __name__ == '__main__':
    main()