import random
from random import randint


def partition_random(arr,lo,hi):
    r = randint(lo, hi)
    print('Random pivot selected',arr[r])
    
    temp = arr[r]
    arr[r] = arr[hi]
    arr[hi] = temp
    return partition(arr,lo,hi)

def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 
  
        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition_random(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)