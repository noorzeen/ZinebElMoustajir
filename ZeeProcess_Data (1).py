#---------------------------------------------------
#------Created  : 20/01/2025 Zineb El Moustajir
#------Modified : 
#------Description : Software Foundations Assessment
#----------------------------------------------------


#-----Define Funtions---------------
def calculate_average(scores):
    return sum(scores) / len(scores)


def assign_grade(average):
    if average >= 92:
        return 'A'
    elif average >= 85:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
#-----End Funtions---------------



# importing csv module
import csv



# initializing the students list
students = []

# reading csv file
with open('ZeeStudents.csv', 'r') as file:
        # creating a csv reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader) 
        
        # extracting field names through first row
        for row in reader:
            name, math, arabic, french = row
            average = calculate_average([int(math), int(arabic), int(french)])
            math=int(math)
            arabic=int(arabic)
            french=int(french)
            M_grade = assign_grade(math)
            S_grade=assign_grade(arabic)
            E_grade=assign_grade(french)
            students.append([name, math, arabic, french, M_grade, S_grade, E_grade])

with open('ZeeStudent_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Arabic', 'French', 'M_Grade', 'S_Grade','E_Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')




