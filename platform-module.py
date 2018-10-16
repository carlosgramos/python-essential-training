#! /usr/bin/env python3

import platform

#Everything in Python3 is an object. Here, you are calling the format funciton on the string object.
print('This is python version {}'.format(platform.python_version()))