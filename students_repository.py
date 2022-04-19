from __future__ import annotations
from student import Student
from student_visitor import StudentVisitor
from dataclasses import (asdict, dataclass)
import json

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
        result = []
        for student in self.students:
            result.append(asdict(student))
        with open("students.json", "w", encoding="utf-8") as f:
            json.dump(result, f)
    
    def load(self):
        self.students = []
        with open("students.json", "r", encoding="utf-8") as f:
            students_data = json.load(f)
        for student in students_data:
            self.students.append(Student(**student))