#2017-12-16,17760.300781,19716.699219,17515.300781,19497.400391,19497.400391,12740599808
#2018-12-16,3236.274658,3305.753174,3233.819824,3252.839111,3252.839111,3744248994
#16244,56128


import pandas as pd

df = pd.read_csv("/home/alexandros/tech_analysis/ew_playground/BTC-USD_reduced.csv", sep=',',
                encoding="ISO-8859-7", header=0,
                names=['date','open','high','low','close','adj_close','volume'])

close = []

for i in df['close']:
    close.append(i)

wave_1 = []
wave_2 = []
_1_minus_2_diff = []

#find wave_1_spot and wave_2_spot
for i in close[1:]:
    #print(i)
    closeindex = close.index(i)
    if i > max(close[:closeindex]):
        #_1_minus_2 = []
        for j in close[(closeindex+1):]:
            #print(j)
            if j < i and round((i-j)/i,4) > 0.2:
                _1_minus_2_diff.append((round((i-j)/i,4)))
                wave_2.append(j)
                wave_1.append(i)
                    

max_diff = max(_1_minus_2_diff)
print(max_diff)
max_diff_index = _1_minus_2_diff.index(max_diff)
print(max_diff_index)
wave_2_spot = wave_2[max_diff_index]
print(wave_2_spot)
wave_1_spot = wave_1[max_diff_index]
print(wave_1_spot)
print(close.index(wave_1[max_diff_index]))
#print(len(_1_minus_2_diff))
wave_5_spot = max(close[(close.index(wave_1[max_diff_index])):])
print(wave_5_spot)
