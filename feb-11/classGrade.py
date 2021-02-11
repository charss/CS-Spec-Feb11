import math

class ClassGrade:
    def __init__(self, stud_num, stud_name, stud_program, stud_course):
        self.quiz_ave = 0
        self.stud_grade = 0
        self.char_grade = ''
        self.stud_num = stud_num
        self.stud_name = stud_name
        self.stud_program = stud_program
        self.stud_course = stud_course
    
    def compute_quiz(self,quiz_total):
        self.quiz_ave = (quiz_total / 60) * 100
        print(f'Quiz Percentage  : {self.quiz_ave:.2f}')
    
    def compute_grade(self,midterm,final):
        self.stud_grade = (self.quiz_ave * 0.25) + (midterm * 0.25) + (final * 0.5)
        return self.stud_grade
    
    def compute_char(self):
        if (self.stud_grade <= 100 and self.stud_grade >= 90):
            self.char_grade = 'A'
        elif (self.stud_grade <=89 and self.stud_grade >= 80):
            self.char_grade = 'B'
        elif (self.stud_grade <=79 and self.stud_grade >= 70):
            self.char_grade = 'C'
        elif (self.stud_grade <=69 and self.stud_grade >= 60):
            self.char_grade = 'D'
        else:
            self.char_grade = 'F'
        
        return self.char_grade
            
class ClassStudInfo(ClassGrade):
    def __init__(self, stud_num, stud_name, stud_program, stud_course):
        super().__init__(stud_num, stud_name, stud_program, stud_course)


ans = 'Y'

while ans == 'Y':
    check = 1
    total = 0
    i = 1

    num = input("Enter Student Number: ")
    name = input("Enter Student Name: ")
    prog = input("Enter Student Program: ")
    course = input("Enter Student Course: ")
    stud_main = ClassStudInfo(num, name, prog, course)

    print("Enter 3 Quizzes")
    while (check == 1):
        quiz = int(input(f'    Quiz #{i}: '))
        if (quiz > 20):
            check = 1
        else:
            total += quiz
            i += 1
        
        if (i == 4):
            check = 0
            
    stud_main.compute_quiz(total)

    # FINALS
    check = 1
    while (check == 1):
        mid = int(input("Midterm Exam     : "))
        check = 1 if (mid > 100 or mid < -1) else 0


    # FINALS
    check = 1
    while (check == 1):
        fin = int(input("Final Exam       : "))
        check = 1 if (fin > 100 or fin < -1) else 0

    print('*********************************')
    print(f'Student Grade    : {math.floor(stud_main.compute_grade(mid,fin))}')
    print('Equivalent Grade :', stud_main.compute_char())
    print('*********************************')
    ans = input('Do you want to compute again (Y/N)? ').upper()
    print()

