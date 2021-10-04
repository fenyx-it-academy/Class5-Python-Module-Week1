student_name = input("Student Name : ")
student_number = input("Student number : ")

checklessonnumber = int(input("How many lesson do you want to check (between 1-5 at once) ? : "))

pointdict = dict()

if checklessonnumber >= 1 : 
    lesson1 = input("Lesson 1 name : ")
    lesson1me = int(input("{} Midterm Exam : ".format(lesson1)))*0.4
    lesson1f = int(input("{} Final : ".format(lesson1)))*0.6
    lesson1totalpoint = lesson1me+lesson1f
    pointdict[lesson1] = (lesson1totalpoint)

if checklessonnumber >= 2 : 
    lesson2 = input("Lesson 2 name : ")
    lesson2me = int(input("{} Midterm Exam : ".format(lesson2)))*0.4
    lesson2f = int(input("{} Final : ".format(lesson2)))*0.6
    lesson2totalpoint = lesson2me+lesson2f
    pointdict[lesson2] =(lesson2totalpoint)

if checklessonnumber >= 3 : 
    lesson3 = input("Lesson 3 name : ")
    lesson3me = int(input("{} Midterm Exam : ".format(lesson3)))*0.4
    lesson3f = int(input("{} Final : ".format(lesson3)))*0.6
    lesson3totalpoint = lesson3me+lesson3f
    pointdict[lesson3] =(lesson3totalpoint)

if checklessonnumber >= 4 : 
    lesson4 = input("Lesson 4 name : ")
    lesson4me = int(input("{} Midterm Exam : ".format(lesson4)))*0.4
    lesson4f = int(input("{} Final : ".format(lesson4)))*0.6
    lesson4totalpoint = lesson4me+lesson4f
    pointdict[lesson4] =(lesson4totalpoint)

if checklessonnumber == 5 : 
    lesson5 = input("Lesson 5 name : ")
    lesson5me = int(input("{} Midterm Exam : ".format(lesson5)))*0.4
    lesson5f = int(input("{} Final : ".format(lesson5)))*0.6
    lesson5totalpoint = lesson5me+lesson5f
    pointdict[lesson5] =(lesson5totalpoint)

elif checklessonnumber > 5 : 
    print("Try less than 5 lesson")

print(pointdict)

for i in pointdict :
    if pointdict[i] >= 50 :
        print(f"Congrats ! You pass for this {i} ")
    else : 
        print(f"You are not ready for this {i}lesson yet . Next year")
    
