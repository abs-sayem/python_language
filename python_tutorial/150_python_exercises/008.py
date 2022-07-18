# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

#color_list = ["Red","Green","White" ,"Black"]
colors = input("Enter some comma seperated color:")
color_list = colors.split(",")  # Make a list of the colors
#print(color_list)
def collect_first_last(color_list):
    print("1st Color:%s\nLast Color:%s"%(color_list[0], color_list[-1]))

collect_first_last(color_list)