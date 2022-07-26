# import numpy as np

_input= [0,0,0,2,3,4,5,7,8,9,10,10,11,11,11,11,15,15,15,18,18,18,20,20,20]

l = 1

for r in range(1,len(_input)):#iterate through the array starting from the second element
    if _input[r] != _input[r-1]:#Check if the current element does not equate the second element
        _input[1] = _input[r]#
        l += 1
        
print(l)

