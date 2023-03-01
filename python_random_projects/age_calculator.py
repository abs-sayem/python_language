# A python program that can calculate age from date of birth and current date

# Assigining Months
from itertools import count


def assign_month(month):
    if month == "01":
        return "Jan"
    elif month == "02":
        return "Feb"
    elif month == "03":
        return "Mar"
    elif month == "04":
        return "Apr"
    elif month == "05":
        return "May"
    elif month == "06":
        return "Jun"
    elif month == "07":
        return "Jul"
    elif month == "08":
        return "Aug"
    elif month == "09":
        return "Sep"
    elif month == "10":
        return "Oct"
    elif month == "11":
        return "Nov"
    elif month == "12":
        return "Dec"

# Check Leap Year
def is_leapyear(year):
    if(year%4 == 0 and year%100 == 0 and year%400 == 0):
        return 1
    elif(year%4 == 0 and year%100 != 0):
        return 1
            
# Checking Year and Date Validity
def is_valid(date):
    if(is_leapyear(date[2])==1 and assign_month(date[1])=="Feb" and date[0]<=28):
        return 1
    elif(date[1]=="Apr" and date[0]<=30):
        return 1
    elif(date[1]=="Jun" and date[0]<=30):
        return 1
    elif(date[1]=="Sep" and date[0]<=30):
        return 1
    elif(date[1]=="Nov" and date[0]<=30):
        return 1
    else:
        return 0

# Calculate Age
def calculate_age(cdate, bdate):
    def calculate_day(cday, bday):
        if(cday<bday): day=(((cday+30)-bday)+1); count=1; return(day,count)
        else: day = ((cday-bday)+1); count=0; return(day,count)
    def calculate_month(cmonth, bmonth, count):
        if(count==1):
            bmonth+=1
            if(cmonth<bmonth): month=((cmonth+12)-bmonth); count=1; return(month,count)
            else: month=(cmonth-bmonth); count=0; return(month,count)
        else:
            if(cmonth<bmonth): month=((cmonth+12)-bmonth); count=1; return(month,count)
            else: month=(cmonth-bmonth); count=0; return(month,count)
    def calculate_year(cyear,byear,count):
        if(count==1):
            byear+=1
            year=(cyear-byear); return(year)
        else:
            year=(cyear-byear); return(year)

    # Call the modules
    day = calculate_day(cdate[0], bdate[0])
    if(day[1]==1):
        month = calculate_month(cdate[1], bdate[1], count=1)
    else:
        month = calculate_month(cdate[1], bdate[1], count=0)
    if(month[1]==1):
        year = calculate_year(cdate[2], bdate[2], count=1)
    else:
        year = calculate_year(cdate[2], bdate[2], count=0)
    return(day[0],month[0],year)

# Main Part
date_of_birth = input("Enter your Date of Birth(dd,mm,yyyy):")
current_date = input("Enter the Current Date(dd,mm,yyyy):")

# Split the vlues by comma
db_list = date_of_birth.split(",")
cd_list = current_date.split(",")

print("Your Date of Birth:", assign_month(db_list[1])+" "+db_list[0]+", "+db_list[2])

# Make the string list to int list
db = [int(i) for i in db_list]
cd = [int(i) for i in cd_list]

if(len(db_list[0])!=2 or len(db_list[0])!=2 or len(cd_list[1])!=2 or len(db_list[1])!=2 or len(cd_list[2])!=4 or len(db_list[2])!=4): # Check the day, month and year's digit numbers
    print("Something happend with the date. Enter a valid date!")
else:
    if((cd[0]<1 or cd[0]>31) or (cd[1]<1 or cd[1]>12)): # Check the range of day and month
        print("Day or Month exceed the limit. Enter a valid date!")
    else:
        #print("Calculating Age...")  
        age = calculate_age(cd, db)
print("Your Age:", str(age[2])+" Year "+str(age[1])+" Month "+str(age[0])+" Day")