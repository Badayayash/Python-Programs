from itertools import islice 
#kth smallest element find
import math  
import statistics

def mediankth():
    k = int(input("Enter the kth smallest number's index:"))
    n = int(input("Enter the Size of array:"))
    userarray=[]

    for x in range(n):
	    temp = int(input("Enter the {}st element in array:".format(x)))
	    userarray.append(temp)

    print("\n")
    print("User Entered Array: {}".format(userarray))

#step1 make clusters or groups of  user entered array
            
    num = len(userarray)
    sqrtnum =  math.sqrt(num) #square root 
    print("\n")

    print("squareroot : {}".format(math.floor(sqrtnum)))

    cut= math.floor(sqrtnum)
    modulus = num%cut  #remainder
    
    new = num - modulus # this is the number which can be equally sliced into pieces

    list1,list2,list3,list4 = [],[],[],[]   #declaring 4 lists

    
# list of length in which we have to split
    length_to_split = []

    for x in range(3):
        length_to_split.append(math.floor(new/cut))

    length_to_split.append(modulus)   #if num = 17 ,cut =4 e.g length_to_split = [5,5,5,2]     

  
# Using islice 
    Inputt = iter(userarray)   #userarray is input 

    Output = [list(islice(Inputt, elem)) for elem in length_to_split]  #output is list of sublists (note:we cut output as per length_to_split)
  
    print("\n")

    for i in range(4):
        if Output[i]:
            pass
        else:
            Output.pop(i)   # deleting empty sublists coz it is creating trouble for median method returning
                    


    print("cut lists:{}".format(Output))
    


#step 2 find median of medians i.e of cut lists
    medianlist=[]
    for x in range(len(Output)):
        medianlist.append(statistics.median(Output[x]))
    
    print("\n")
    print("median of all cut lists : {}".format(medianlist))    
     
    pivot =statistics.median(medianlist) # pivot is median of medians i.e a single number
     
    
    print("\n")

    print("Median of median of array is : {}".format(pivot))
    #indexvar = userarray.index(pivot)   #xindex is index of pivot in userarray  

# finding kth smallest element
    userarray.sort()
   
    print("\n ")

    print("Sorted array : {}".format(userarray))

   
    print("\n")


    print("kth smallest element is : {}".format(userarray[k-1]))



        



if __name__ == '__main__':
    mediankth()
