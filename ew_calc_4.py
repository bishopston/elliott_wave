import pandas as pd
import sys

df = pd.read_csv("C:/Alex/elliott_wave/elliott_wave/BTC-USD.csv", sep=',',
                encoding="ISO-8859-7", header=0,
                names=['date','open','high','low','close','adj_close','volume'])

close = []

for i in df['close']:
    close.append(i)

wave_1 = []
wave_1a = []
wave_2 = []
wave_2a = []
_1_minus_2_diff = []
_1a_minus_2a_diff =[]

global_min = min(close)
global_max = max(close)
global_min_index = close.index(global_min)
global_max_index = close.index(global_max)
#print(global_min, global_min_index)

for i in close[global_min_index+1:]:
    #print(i)
    closeindex = close.index(i, global_min_index+1)
    fib_100 = i - global_min
    #print(fib_100)
    #check that accessed element is max so far
    if i > max(close[:closeindex]):
        #access all elements after i
        for j in close[(closeindex+1):]:
            #global_max = max(close[closeindex:])
            #check if global_min is prior to global_max
            if global_min_index < global_max_index:
                #check that accessed element retraces at least 23.6%
                if close.index(j) < global_max_index and round((i-j)/fib_100,4) > 0.236:
                    _1_minus_2_diff.append((round((i-j)/fib_100,4)))
                    wave_2.append(j)
                    wave_1.append(i)
            else:
                if round((i-j)/fib_100,4) > 0.236:
                    _1_minus_2_diff.append((round((i-j)/fib_100,4)))
                    wave_2.append(j)
                    wave_1.append(i)

if not _1_minus_2_diff:
    print("waves 1 and 2 cannot be found")
else:
    max_diff = max(_1_minus_2_diff)
    print("price retracement between wave 1 and 2: " + str(max_diff*100) + "%")
    max_diff_index = _1_minus_2_diff.index(max_diff)
    #print(max_diff_index)
    wave_2_spot = wave_2[max_diff_index]
    wave_1_spot = wave_1[max_diff_index]
    global_fib_100 = wave_1_spot - global_min
    #print(close.index(wave_1[max_diff_index]))
    #wave_5_spot = max(close[(close.index(wave_1[max_diff_index])):])
    print("wave 1: " + str(wave_1_spot))
    print("wave 1 date: " + str(max(df.iloc[close.index(wave_1[max_diff_index]):(close.index(wave_1[max_diff_index])+1),0])))
    print("wave 2: " + str(wave_2_spot))
    print("wave 2 date: " + str(max(df.iloc[close.index(wave_2[max_diff_index]):(close.index(wave_2[max_diff_index])+1),0])))
    print("Fibbonacci 100%: ", round(global_fib_100,2))


    for i in close[(close.index(wave_2_spot)+1):]:
        #print(i)
        closeindex = close.index(i, (close.index(wave_2_spot)+1))
        #fib_100 = i - global_min
        #print(fib_100)
        #check that accessed element is max so far
        if i > max(close[(close.index(wave_2_spot)):closeindex]) and i < wave_1_spot and round((i-wave_2_spot)/fib_100,4) > 0.382:
            #access all elements after i
            for j in close[(closeindex+1):]:
                #global_max = max(close[closeindex:])
                #check that accessed element retraces at least 23.6%
                if round((i-j)/fib_100,4) > 0.146:
                    _1a_minus_2a_diff.append(round((i-j)/fib_100,4))
                    wave_2a.append(j)
                    wave_1a.append(i)

    max_diff_a = max(_1a_minus_2a_diff)
    print("price retracement between wave 1a and 2a: " + str(max_diff_a*100) + "%")
    max_diff_a_index = _1a_minus_2a_diff.index(max_diff_a)
    #print(max_diff_index)
    wave_2a_spot = wave_2a[max_diff_a_index]
    wave_1a_spot = wave_1a[max_diff_a_index]
    #wave_5_spot = max(close[(close.index(wave_1[max_diff_index])):])
    print("wave 1a: " + str(wave_1a_spot))
    print("wave 1a date: " + str(max(df.iloc[close.index(wave_1a[max_diff_a_index]):(close.index(wave_1a[max_diff_a_index])+1),0])))
    print("wave 2a: " + str(wave_2a_spot))
    print("wave 2a date: " + str(max(df.iloc[close.index(wave_2a[max_diff_a_index]):(close.index(wave_2a[max_diff_a_index])+1),0])))
    print("price increase between wave 2 and 1a: " + str(max_diff_a*100) + "%")