#!/user/bin/env python3

x = 42
y = 73

#In the code block below, notice the position of the argumets in the format method
if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
    
#Notice that blocks do not scope variables. Variables are scoped by functions, objects, and modules.
print('z is {}'.format(z))