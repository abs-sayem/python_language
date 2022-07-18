# The problem is: 
#   > Take a number and apply two rules
#   > R1: If the number is odd - mutliply it by 3 and add 1 (7x3+1)
#   > R2: If the number is even - divide it by 2 (8/2)
# This will end up with a conjesture: Every positive integer, if we apply the rules it will eventually end up 
# in the 4, 2 & 1 loop.
# Also called 3n+1 problem
# Raised in 1930s
# It leads us to Benford's Law - Evenly distributed downword curve - apply to detect fraud, 
# in election to detect irregularities, If your income tax obey the Benford's law, you're probably honest.

number = int(input("Enter a number:"))

def collatz_conjecture(number):
    number_list=[]
    if(number==0): number_list.append(number); return(number_list)
    else:
        number_list.append(number)
        while(number!=0):
            if((number%2)==0):
                number=(number/2)
            else:
                number=((number*3)+1)
            number_list.append(number)
sequence=collatz_conjecture(number)
print("The sequence is:",sequence)