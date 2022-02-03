from __future__ import annotations
from student import Student
from student_visitor import StudentVisitor

class StudentRepository:
    students: list[Student]
    
    def __init__(self):
        self.students = []
        
    def add_student(self, s: Student):
        self.students.append(s)
        
    def get_student(self, index: int) -> Student:
        return self.students[index - 1]
    
    def remove_student(self, index: int):
        del self.students[index - 1]
        
    def count_students(self) -> int:
        return len(self.students)
            
    def visit(self, v: StudentVisitor):
        v.start_visit()
        for i, student in enumerate (self.students):
            v.visit_student(i, student)
        v.finish_visit()
            
    def save(self):
        pass
    
    def load(self):
        pass
