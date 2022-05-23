# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#   Sample Input: 11, 12, 2022
#   Sample Output: 11/12/2022

#exam_start_date = (11, 12, 2022)
#print("The Exam will Start from: %i/%i/%i"%exam_sart_date)
#--------------------------------------------------------------
#print("Enter the date dd,mm,yyyy format.")
exam_start_date = input("Enter comma seperated date, format(dd,mm,yyyy):")
date_list = exam_start_date.split(",")
#print("The Exam will Start from:", date_list[0]+"/"+date_list[1]+"/"+date_list[2])
#-------------------------------------------------------------------------------------
if date_list[1] == "01":
    print("The Exam will Start from:", "Jan "+date_list[0]+", "+date_list[2])
elif date_list[1] == "02":
    print("The Exam will Start from:", "Feb "+date_list[0]+", "+date_list[2])
elif date_list[1] == "03":
    print("The Exam will Start from:", "Mar "+date_list[0]+", "+date_list[2])
elif date_list[1] == "04":
    print("The Exam will Start from:", "Apr "+date_list[0]+", "+date_list[2])
elif date_list[1] == "05":
    print("The Exam will Start from:", "May "+date_list[0]+", "+date_list[2])
elif date_list[1] == "06":
    print("The Exam will Start from:", "Jun "+date_list[0]+", "+date_list[2])
elif date_list[1] == "07":
    print("The Exam will Start from:", "Jul "+date_list[0]+", "+date_list[2])
elif date_list[1] == "08":
    print("The Exam will Start from:", "Aug "+date_list[0]+", "+date_list[2])
elif date_list[1] == "09":
    print("The Exam will Start from:", "Sep "+date_list[0]+", "+date_list[2])
elif date_list[1] == "10":
    print("The Exam will Start from:", "Oct "+date_list[0]+", "+date_list[2])
elif date_list[1] == "11":
    print("The Exam will Start from:", "Nov "+date_list[0]+", "+date_list[2])
elif date_list[1] == "12":
    print("The Exam will Start from:", "Dec "+date_list[0]+", "+date_list[2])
else:
    print("Enter a valid date in appropriate manner")