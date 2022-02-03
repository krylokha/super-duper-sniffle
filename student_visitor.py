from __future__ import annotations
import re
from typing import Protocol
from abc import abstractmethod
import student as st
from student_view import BriefStudentView, DetailedStudentView

class StudentVisitor(Protocol):
    def start_visit(self):
        pass
    
    def visit_student(self, index: int, s: st.Student):
        pass
    
    def finish_visit(self):
        pass
    
class BriefPrintVisitor(StudentVisitor):
    def start_visit(self):
        pass
    
    def visit_student(self, index: int, s: st.Student):        
        print(f'{index + 1}.', end = " ")
        BriefStudentView(s).view()
     
    def finish_visit(self):
        pass

class DetailedPrintVisitor(StudentVisitor):
    def start_visit(self):
        pass
    
    def visit_student(self, index: int, s: st.Student):
        print(f'=== {index + 1} ===')
        DetailedStudentView(s).view()
        
    def finish_visit(self):
        pass
    
class HighAchieverPrintVisitor(StudentVisitor):
    def __init__(self):
        self.count = 0
    
    def start_visit(self):
        self.count = 0
    
    def visit_student(self, index: int, s: st.Student):
        if s.is_high_achiever():
            DetailedStudentView(s).view()
            self.count += 1
    
    def finish_visit(self):
        if self.count == 0:
            print("Отличников нет")
    
# аналогично
class LowAchieverPrintVisitor(StudentVisitor):
    def start_visit(self):
        pass
    
    def visit_student(self, index: int, s: st.Student):
        count = 0
        for value in s.marks.values():
            if value < 3:
                count += 1
                DetailedStudentView(s).view()
                break
        if count == 0: 
            print('Неуспевающих нет')
    
    def finish_visit(self):
        pass