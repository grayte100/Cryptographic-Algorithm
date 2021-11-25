# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#This is an encryption algorithm
#First, a dictionary containing all alphabets and their numerical equivalents is created
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7, 'h':8, 'i':9, 'j':10,'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17
        , 'r':18, 's':19, 't': 20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}


#Then the password is inputted
password = input ("Enter your password: ").lower()
passcode = []
for i in password:
    passcode.append(i)
#Then the numerical equivalent of the inputted password is found
values = []
for character in password:
    for key, value in dict.items():
        if key == character:
            values.append(value)

#Encryption proper
import random
x = sum(values)
m = 10000000000000000000000000000000000000000000000000000000000000000
for i in range (m):
	b = []
	for i in range (x):
		a = random.randint (0,x)
		b.append(a)
	c = sum (b)
	if c== x:
		print ("Cipher text is : ", b)
		break
    
#Time to decrypt
n = 10000000000000000000000000000000000000000000000000000000000000000
for i in range(n):
    reversal = []
    for i in range (0,random.randint(1, sum(b))):
        reversal.append(random.randint(1,sum(b)))
    original = []
    for val in reversal:
        for key, value in dict.items():
            if value == val:
                original.append(key)
    if original == passcode:
        print ("the reversed password is: ", original)
        break
        
                
        

                
