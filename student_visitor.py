from __future__ import annotations
import re
from typing import Protocol
from abc import abstractmethod
import student as st
from student_view import BriefStudentView, DetailedStudentView

class StudentVisitor(Protocol):
    def start_visit():
        pass
    
    def visit_student(index: int, s: st.Student):
        pass
    
    def finish_visit():
        pass
    
class BriefPrintVisitor(StudentVisitor):
    @staticmethod
    def start_visit():
        pass
    
    @staticmethod
    def visit_student(index: int, s: st.Student):        
        print(f'{index + 1}.', end = " ")
        BriefStudentView(s).view()
    
    @staticmethod    
    def finish_visit():
        pass

class DetailedPrintVisitor(StudentVisitor):
    @staticmethod
    def start_visit():
        pass
    
    @staticmethod
    def visit_student(index: int, s: st.Student):
        print(f'=== {index + 1} ===')
        DetailedStudentView(s).view()
        
    @staticmethod
    def finish_visit():
        pass
    
class HighAchieverPrintVisitor(StudentVisitor):
    @staticmethod
    def start_visit():
        pass
    
    @staticmethod
    def visit_student(index: int, s: st.Student):
        count = 0
        for value in s.marks.values():
            if value == 5:
                count += 1
            if count == len(s.marks):
                return DetailedStudentView(s).view()
        return print('Отличников нет')
    
    @staticmethod
    def finish_visit():
        pass
    
class LowAchieverPrintVisitor(StudentVisitor):
    @staticmethod
    def start_visit():
        pass
    
    @staticmethod
    def visit_student(index: int, s: st.Student):
        count = 0
        for value in s.marks.values():
            if value < 3:
                count += 1
                DetailedStudentView(s).view()
                break
        if count == 0: 
            print('Неуспевающих нет')
    
    @staticmethod
    def finish_visit():
        pass