## File Name: cube.py
## This file functions to output the cube of odd numbers from 0 to 19. If the
## number is even, the number itself will be returned. This program features a
## function called cb(), that returns the cube of the number.
## Example Invocation: python3 cube.py
def cb(x):
  return x*x*x

for i in range(20):
  if i % 2 != 0:
    print(cb(i))
  else:
    print(i)
    



