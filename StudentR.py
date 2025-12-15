# generar un codigo para registrar estudiantes
from to_SR import SR

student_registry = SR()

while True:
    print ("Welcome to the students registration")
    print ("1.Add a student")
    print ("2.Remove a student")
    print ("3.Find a Student")
    print ("4.List the students")
    print ("5.Exit ThE ReGisT")
    
choice = input ("Type a number from 1 to 5")

if choice == "1.":
    studentId = input ("Enter student ID")
    StudentName = input ("Enter student Name")
    student_registry.add_student(student)
if choice == "2.":
      studentID = input ("Enter student ID")
      studentName = input ("Enter student name")
      student_registry.remove_student(student_id)
else:
    print  ("Theres no student with the name {studentName}")      
if choise == "3.": 
        StudentName = input ("Enter the ID of the student")
        student_registry.find_student(student_id)
if choice == "4.":
   student_registry.list_students(students) 
if choice == "5.":
    print ("thank you for register with us")                