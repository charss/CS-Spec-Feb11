class ClassGrade:
    def __init__(self,  stud_num):
        self.quiz_ave = 0
        self.stud_grade = 0
        self.char_grade = ''

    def compute_quiz(self,quiz_total):
        self.quiz_ave = (quiz_total/60)*100
        print("QuizPercentage: ")
    
    def compute_grade(self,midterm,final):
        self.stud_grade = (self.quiz_ave*.25)+(midterm*.25)+(final*.5)
    
    def compute_char(self):
        if (self.stud_grade <=100 or self.stud_grade >= 90):
            self.char_grade = 'A'
        elif (self.stud_grade <=89 or self.stud_grade >= 80):
            self.char_grade = 'B'
        elif (self.stud_grade <=79 or self.stud_grade >= 70):
            self.char_grade = 'C'
        elif (self.stud_grade <=69 or self.stud_grade >= 60):
            self.char_grade = 'D'
        else:
            self.char_grade = 'F'
            


num = input("Enter Student Number: ")
# name = input("Enter Student Name: ")
# prog = input("Enter Student Program: ")
# course = input("Enter Student Course: ")
stud_main = (num)
check = 1
total = 0
i = 1
print("Enter 3 Quizzes")
for i in range(1, 4):
    print("Quiz#",i," ",end='')
    quiz = int(input())
    if (quiz > 20):
        check=1
    else:
        total = total + quiz
        i+=1
    
    if (i==4):
        check=0
        

    