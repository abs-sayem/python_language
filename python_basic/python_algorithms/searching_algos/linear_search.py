# Linear search is a sequensial searching algorithm - it searches from the first element to the last element sequentially.
# Suppose we have an array of n elements and we try to find an specific element(x) in the list of the elements.

# Define the module
#from itertools import count
#from operator import index


# Taking the list of elements and the target value
from itertools import count


elements = input("Enter comma seperated elements: ")
target = int(input("Enter the target value: "))

# Split the elements and make an array
seperated_list = elements.split(",")    # Splited elements by comma
the_list = [int(i) for i in seperated_list] # Make a list of int
#list_length = len(the_list)

# Define the module
def linear_search(the_list,target):
    for i in range(len(the_list)):
        count=0
        if(target==the_list[i]): print(f"{target} is {i+1} no item"); return(count+1); break
# Call the function
result = linear_search(the_list,target)
if(result!=1): print(f"'{target}' isn't in the list")