#!/user/bin/env python3

#Python provides two types of loops, while loop and for loop

words = ['one', 'two', 'three', 'four', 'five']

#While loop
n = 0
while(n < 5):
    print(words[n])
    n += 1
    
#For loop
for word in words:
    print(word)