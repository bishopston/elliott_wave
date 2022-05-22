import pandas as pd

df = pd.read_csv("/home/alexandros/tech_analysis/ew_playground/BTC-USD_reduced.csv", sep=',',
                encoding="ISO-8859-7", header=0,
                names=['date','open','high','low','close','adj_close','volume'])

close = []

for i in df['close']:
    close.append(i)

wave_1 = []
wave_2 = []
wave_3 = []
wave_4 = []
_1_minus_2_diff = []
_3_minus_4_diff = []

#find wave_1_spot and wave_2_spot
for i in close[1:]:
    #print(i)
    closeindex = close.index(i)
    #check that accessed element is max so far
    if i > max(close[:closeindex]):
        #access all elements after i
        for j in close[(closeindex+1):]:
            #check that accessed element is smaller than i by at least 20%
            if round((i-j)/i,4) > 0.2:
                _1_minus_2_diff.append((round((i-j)/i,4)))
                wave_2.append(j)
                wave_1.append(i)


max_diff = max(_1_minus_2_diff)
print("difference between wave 1 and 2: " + str(max_diff))
max_diff_index = _1_minus_2_diff.index(max_diff)
#print(max_diff_index)
wave_2_spot = wave_2[max_diff_index]
print("wave 2: " + str(wave_2_spot))
wave_1_spot = wave_1[max_diff_index]
print("wave 1: " + str(wave_1_spot))
print(close.index(wave_1[max_diff_index]))
print(max(df.iloc[close.index(wave_1[max_diff_index]):(close.index(wave_1[max_diff_index])+1),0]))
wave_5_spot = max(close[(close.index(wave_1[max_diff_index])):])
print("wave 5: " + str(wave_5_spot))


#find wave_3_spot and wave_4_spot
for i in close[(close.index(wave_1_spot)+1):close.index(wave_5_spot)]:
    #print(i)
    
    closeindex = close.index(i)
    #check that accessed element is max between wave 1 and 5, accessed element is greater than wave 1 by 30% and wave 3 is longer than wave 1
    if i > max(close[close.index(wave_1_spot):closeindex]) and i > (1.33*wave_1_spot) and (closeindex - close.index(wave_1_spot) > close.index(wave_1_spot)):
        #access all elements after i and up to wave 5
        for j in close[(closeindex+1):close.index(wave_5_spot)]:
            #check that accessed element is greater than i and greater than wave 1
            if j < i and j > wave_1_spot:
                _3_minus_4_diff.append((round((i-j)/i,4)))
                wave_4.append(j)
                wave_3.append(i)
    

max_diff_3_4 = max(_3_minus_4_diff)
print("difference between wave 3 and 4: " + str(max_diff_3_4))
max_diff_3_4_index = _3_minus_4_diff.index(max_diff_3_4)
#print(max_diff_3_4_index)
wave_4_spot = wave_4[max_diff_3_4_index]
print("wave 4: " + str(wave_4_spot))
wave_3_spot = wave_3[max_diff_3_4_index]
print("wave 3: " + str(wave_3_spot))
print(close.index(wave_3[max_diff_3_4_index]))
