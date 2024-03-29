# Take the course numbers:
import numbers

# Take the course numbers:
def getNumbers(courses):
    course_numbers = []
    for i in range(courses):
        course_numbers.append(float(input(f"Enter course {i} number: ")))
    return(course_numbers)

# Take the course grades:
def getGrades(courses):
    course_grades = []
    for i in range(courses):
        course_grades.append(float(input(f"Enter course {i} grade: ")))
    return(course_grades)

# Compare and assigns the numbers equbalance to MEXT standards:
# (100-80) = A = 3 | (79-70) = B = 2 | (69-60) = C = 1 | (<60) = F = 0
def courseNumber(numbers):
    course_number = 0
    for i in range(len(numbers)):
        if(numbers[i] >= 80): course_number += (3*3)
        elif(numbers[i] <= 79 and numbers[i] >= 70): course_number += (3*2)
        elif(numbers[i] <= 69 and numbers[i] >= 60): course_number += (3*1)
        else: course_number += (3*0)
    print("Your MEXT Standard GPA: ", course_number/(no_courses*3))

def courseGrade(grades):
    course_grade = 0
    for i in range(len(grades)):
        if(grades[i] >= 4): course_grade += (3*3)
        elif(grades[i] < 4 and grades[i] >= 3.75): course_grade += (3*2)
        elif(grades[i] < 3.75 and grades[i] >= 3.5): course_grade += (3*1)
        else: course_grade += (3*0)
    print("Your MEXT Standard GPA: ", course_grade/(len(grades)*3))

# How many courses he has:
no_courses = int(input("Enter the number of 3-credit courses: "))
#print(courses)
# Chose number based or grade based
print("Choose your prefered type:\n\t1) Grade\n\t2) Number")
type = int(input("What type of input you want to provide: "))
# Call the input taking modules
if(type == 1):
    grades = getGrades(no_courses)
    courseGrade(grades)
elif(type == 2):
    numbers = getNumbers(no_courses)
    courseNumber(numbers)