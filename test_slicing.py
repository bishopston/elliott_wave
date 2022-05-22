import pandas as pd

my_dataset = [6,5,7,3,8,12,45,2,9,10,56]

print(my_dataset[3:])
#"""
close = []

for i in my_dataset:
    close.append(i)

_1_minus_2 = []
_1_minus_2_diff = []

for i in close[1:]:
    
    print(i)
    closeindex = close.index(i)
    print(closeindex)
    print(close[:closeindex])
    if i > max(close[:closeindex]):
        #_1_minus_2 = []
        for j in close[(closeindex+1):]:
            print(j)
            if j < i:
                _1_minus_2.append(j)
                _1_minus_2_diff.append(i-j)

print(_1_minus_2)
print(_1_minus_2_diff)
print(max(_1_minus_2_diff))
#"""