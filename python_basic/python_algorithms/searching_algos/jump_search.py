# Jump algorithm works in this way--
    # Initialize with a lower_bound and a higher_bound of block_size difference
    # Ensures if the target data is the lower/higher bound or between them
    # If between them: then it applies a linear search among the remaining values
    # If not: changed the higher bound as new lower bound and  higher_bound as block_size difference
    #   0     1     2     3     4     5     6     7     8     9    10    11  
    #|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
    #| 100 |  6  | 89  | 45  |  9  | 78  | 34  |  1  | 70  | 45  |  10 | 56  |
    #|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
    # Jump algorithm required a sorted array

    # Taking the list of elements and the target value

# Import the libraries
import math

#elements = input("Enter comma seperated elements:")
#target = int(input("Enter the target value:"))
seperated_list = [5,50,15,1,900,190,12,75,111,34,89,90]
target = 67

# Split the elements and make an array
#seperated_list = elements.split(",")    # Splited elements by comma
the_list = sorted([int(i) for i in seperated_list])    # Make a sorted list of int
print(f"The sorted list: {the_list}")


# Define the jump search module
def jump_search(the_list,target):
    #list_length = len(the_list)
    step_size = math.ceil((len(the_list)/6.67616402))     #ln(len(the_list))
    #count = 0
    lbound = 0
    ubound = ((lbound+step_size)-1)
    if(ubound > len(the_list)): ubound = ubound
    else: ubound = len(the_list)
    #print(f"Lower Bound: {lbound}\nUpper Bound: {ubound}")
    while(the_list[lbound] != target):
        if(the_list[lbound]==target): print(lbound)
        elif(the_list[ubound]==target): print(ubound)
        elif(target>the_list[lbound] and target<the_list[ubound]):
            lbound+=1
            ubound-=1
            while(the_list[lbound] != target): lbound+=1
            print(lbound)
        else:
            lbound = ubound+1
            ubound = ubound+step_size
            if(ubound > len(the_list)): ubound=ubound
            else: ubound=len(the_list)
    print(lbound)
            

jump_search(the_list,target)           