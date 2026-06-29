import json
from student import Student

class StudentManager:
    
    def __init__(self):
        self.filename="data.json"
        self.students=[]
        self.load()
        
    def load(self):
        try:
            with open("data.json","r") as f:
                data=json.load(f)
                for item in data:
                    self.students.append(Student.from_dict(item))
                    
        except FileNotFoundError:
            pass
        
    def save(self):
         with open("data.json","w") as fs:
            json.dump([s.to_dict() for s in self.students], fs)
            
    def add(self):
        name=input("Enter the name of student: ")
        section=input("Enter the section of student: ")
        roll=int(input("Enter the roll no. of student: "))
        marks={}
        num_subjects=int(input("how many subjects do you have?: "))
        for i in range(num_subjects):
            subject=input("Enter suject name: ")
            mark=int(input("Enter the marks: "))
            marks[subject]=mark
        student = Student(name, section, roll, marks) 
        self.students.append(student)                   
        self.save()                                     
        print("Student added successfully!")
        
    def view(self):
        if not self.students:
            print("No students found!")
            return
        for student in self.students:
            print(student)
            
    def search(self):
        print("Search student by: 1.Name 2.Roll No.: ")
        w=int(input("Enter the choice selected: "))
        if w== 1:
            n=input("Enter the name of student: ")
            for student in self.students:
                if student.name == n:
                    print(student)
                    return
            print("no student found!!")
        elif w== 2:
            p=int(input("Enter the roll no. of student: "))
            for student in self.students:
                if student.roll == p:
                    print(student)
                    return
            print("no student found!!")
        else:
            print("invalid input!!")
            
    def update(self):
        lol=int(input("Enter the roll no. to of student: "))
        for student in self.students:
            if student.roll==lol:
                li=int(input("Update 1.Name 2.Section 3.Marks: "))
                if li==1:
                    student.name=input("Enter the new name: ")
                elif li==2:
                    student.section=input("Enter the new section: ")
                elif li==3:
                    marks={}
                    num_subject=int(input("Enter the no. of subjects to be updated: "))
                    for i in range(num_subject):
                        subject=input("Enter the name of the subject: ")
                        mark=int(input("Enter the marks: "))
                        marks[subject]=mark
                    student.marks=marks
                else:
                    print("inavlid input!!")
                self.save()
                print("updated successfully!!")
                return
        print("student not foun!!")
        
    def delete(self):
        delu=int(input("Enter the roll no. of student: "))
        for student in self.students:
            if student.roll==delu:
                self.students.remove(student)
                self.save()
                print("Delted successfully!!")
                return
        print("student not foun!!")
        
    def statistics(self):
        if not self.students: 
            print("No students found!")
            return
            
        topper=max(self.students, key=lambda s: s.average())
        print(f"Topper:{topper.name} has the average:{topper.average()}")
            
        class_avg= sum(s.average() for s in self.students) / len(self.students)
        print(f"Class avergae is: {class_avg}")
        
    
        