from __future__ import annotations
from student import Student

class StudentRepository:
    students: list[Student]
    
    def __init__(self):
        self.students = []
        
    def add_student(self, s: Student):
        self.students.append(s)
        
    def get_student(self, index: int) -> Student:
        return self.students[index - 1]
    
    def remove_student(self, index: int):
        # s = self.get_student(index - 1)
        # self.students.remove(s)
        del self.students[index -]
        
    def count_students(self) -> int:
        return len(self.students)
                
    def save(self):
        pass
    
    def load(self):
        pass
    