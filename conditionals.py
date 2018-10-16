#!/user/bin/env python3

x = 73
y = 73

#Notice the use of the : and the formatting
if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
else:
    print("They're the same")