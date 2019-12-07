#1. Get the i/p from the user for no of jobs n
#2. For a time interval (my case: 8:30 to 18:00), generate n random starttime and endtime(endtime> starttime)
#3. Arrange starttime based on sorted endtime
#4. First job always including in the count and remaining can be found out by comparing start time with the previous end time (s>=e)
#5. Store both n and count in a file.
#6. Plot the graph n v/s count

import csv
import random
import time
import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
from random import randint


def genLecture(m, n):

    x, y = randint(m, n), randint(m, n)
    if(x == y):
        x, y = randint(m, n), randint(m, n)
    if (x > y):
        x, y = y, x

    return x, y

print("enter value of n:")
f = int(input())
q = 0
x_vals = []
y_vals = []
while (q < 30):
    
    arr = []

    for i in range(0, f):
        x, y = genLecture(0, 500)
        arr.append([x, y])

    def shellSort(arr, n):

        gap = int(n/2)
        while(gap > 0):
            i = int(gap)
            while(i < n):
                temp = arr[i]
                j = i
                while (j >= gap and arr[j-gap] > temp):
                    arr[j] = arr[j - gap]
                    j = j - gap
                arr[j] = temp
                i = i + 1
            gap = int(gap/2)
        return arr
    arr = shellSort(arr,f)

    myarray = np.asarray(arr)
    h = 0
    count = 1
    for i in range(0,f-1):
        if(myarray[i+1,0]>=myarray[h,1]):
            count = count +1
            h = i+1
    mycount = np.array(count)    

    row = [f,count]
    with open('algo1.txt', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    
    x_vals.append(f)
    y_vals.append(count)
    q = q + 1
    f = q*500
    print(count,f)

pt.plot(x_vals, y_vals)
pt.show()
print("program completed")







