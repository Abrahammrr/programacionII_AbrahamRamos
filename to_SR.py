class SR:
    def __init__(self):
        self.StudentRegistList = []

    def add_student(self, student):
        self.StudentRegistList.append(student)
        print (f"Student{student} added succesfully")

    def remove_student(self, student_id,delete):
        if student_id in self.StudentRegistList:
         self.StudentRegistList.remove(student_id)
        print (" the student {} was deleted succesfully")

    def find_student(self, student_id):
        if student_id in self.StudentRegistList:
         print (student_id)
        else:
            print ("there is no student with the {student_id} ID")

    def list_students(self):
        if len (self.StudentRegistList) == 0:
            print (" theres no students saved here")
            for student_id in self.StudentRegistList:
                print (f"This are the students saved: {student_id}")

#CRUD