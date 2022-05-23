import pandas as pd
import sys

df = pd.read_csv("~/tech_analysis/ew_playground/BTC-USD_reduced.csv", sep=',',
                encoding="ISO-8859-7", header=0,
                names=['date','open','high','low','close','adj_close','volume'])

close = []

for i in df['close']:
    close.append(i)

wave_1 = []
wave_2 = []
wave_3 = []
wave_4 = []
wave_a = []
wave_b = []
_1_minus_2_diff = []
_3_minus_4_diff = []
_b_minus_a_diff = []

#try:
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

if not _1_minus_2_diff:
    print("waves 1 and 2 cannot be found")
else:
    max_diff = max(_1_minus_2_diff)
    print("difference between wave 1 and 2: " + str(max_diff))
    max_diff_index = _1_minus_2_diff.index(max_diff)
    #print(max_diff_index)
    wave_2_spot = wave_2[max_diff_index]
    wave_1_spot = wave_1[max_diff_index]
    #print(close.index(wave_1[max_diff_index]))
    wave_5_spot = max(close[(close.index(wave_1[max_diff_index])):])
    print("wave 1: " + str(wave_1_spot))
    print("wave 1 date: " + str(max(df.iloc[close.index(wave_1[max_diff_index]):(close.index(wave_1[max_diff_index])+1),0])))
    print("wave 2: " + str(wave_2_spot))
    print("wave 2 date: " + str(max(df.iloc[close.index(wave_2[max_diff_index]):(close.index(wave_2[max_diff_index])+1),0])))

#find wave_3_spot and wave_4_spot
for i in close[(close.index(wave_1_spot)+1):close.index(wave_5_spot)]:
    #print(i)
    
    closeindex = close.index(i)
    #check that accessed element is max between wave 1 and 5, wave 3 is greater than 1,5 and wave 3 is longer than wave 1
    if i > max(close[close.index(wave_1_spot):closeindex]) and (i - wave_2_spot) > wave_1_spot and (i - wave_2_spot) > (wave_5_spot - i) and (closeindex - close.index(wave_1_spot) > close.index(wave_1_spot)):
        #access all elements after i and up to wave 5
        for j in close[(closeindex+1):close.index(wave_5_spot)]:
            #check that accessed element is greater than i and greater than wave 1
            if j < i and j > wave_1_spot:
                _3_minus_4_diff.append((round((i-j)/i,4)))
                wave_4.append(j)
                wave_3.append(i)

if not _3_minus_4_diff:
    print("waves 3 and 4 cannot be found")
else:
    max_diff_3_4 = max(_3_minus_4_diff)
    print("difference between wave 3 and 4: " + str(max_diff_3_4))
    max_diff_3_4_index = _3_minus_4_diff.index(max_diff_3_4)
    #print(max_diff_3_4_index)
    wave_4_spot = wave_4[max_diff_3_4_index]
    wave_3_spot = wave_3[max_diff_3_4_index]
    print("wave 3: " + str(wave_3_spot))
    print("wave 3 date: " + str(max(df.iloc[close.index(wave_3[max_diff_3_4_index]):(close.index(wave_3[max_diff_3_4_index])+1),0])))
    print("wave 4: " + str(wave_4_spot))
    print("wave 4 date: " + str(max(df.iloc[close.index(wave_4[max_diff_3_4_index]):(close.index(wave_4[max_diff_3_4_index])+1),0])))
    print("wave 5: " + str(wave_5_spot))
    print("wave 5 date: " + str(max(df.iloc[close.index(wave_5_spot):(close.index(wave_5_spot)+1),0])))


#find wave_a_spot and wave_b_spot
for i in close[(close.index(wave_5_spot)+1):]:
    closeindex = close.index(i, (close.index(wave_5_spot)+1))
    #print(close.index(wave_5_spot))
    #print(closeindex)
    #check that accessed element is min so far
    if i < min(close[(close.index(wave_5_spot)):closeindex]):
        #access all elements after i
        for j in close[(closeindex+1):]:
            #check that accessed element is smaller than i by at least 20%
            if round((j-i)/i,4) > 0.2:
                _b_minus_a_diff.append((round((j-i)/i,4)))
                wave_b.append(j)
                wave_a.append(i)    

if not _b_minus_a_diff:
    print("waves A, B and C cannot be found")
else:
    max_diff_b_a = max(_b_minus_a_diff)
    print("difference between wave a and b: " + str(max_diff_b_a))
    max_diff_b_a_index = _b_minus_a_diff.index(max_diff_b_a)
    wave_a_spot = wave_a[max_diff_b_a_index]
    wave_b_spot = wave_b[max_diff_b_a_index]
    wave_c_spot = min(close[(close.index(wave_b[max_diff_b_a_index])):])
    print("wave a: " + str(wave_a_spot))
    print("wave a date: " + str(max(df.iloc[close.index(wave_a[max_diff_b_a_index]):(close.index(wave_a[max_diff_b_a_index])+1),0])))
    print("wave b: " + str(wave_b_spot))
    print("wave b date: " + str(max(df.iloc[close.index(wave_b[max_diff_b_a_index]):(close.index(wave_b[max_diff_b_a_index])+1),0])))
    print("wave c: " + str(wave_c_spot))
    print("wave c date: " + str(max(df.iloc[close.index(wave_c_spot):(close.index(wave_c_spot)+1),0])))



#print(close.index(wave_3[max_diff_3_4_index]))



# except:
#     print(sys.exc_info()[1])source venv/bin/activate