from __future__ import annotations
from abc import ABC, abstractmethod
import student as st

class StudentView:
    student: st.Student
    
    def __init__(self, s: st.Student):
        self.student = s
    
    @abstractmethod
    def view(self):
        pass
    
class DetailedStudentView(StudentView):
    def __init__(self, s: st.Student):
        super().__init__(s)
    
    def view(self):
        print(f'Фамилия: {self.student.last_name}')
        print(f'Имя: {self.student.first_name}')
        print(f'Отчество: {self.student.middle_name}')
        print(f'Группа: {self.student.group}')
        print('Оценки: ')
        if len(self.student.marks) == 0:
            print('Оценок нет')
        else:
            for key, value in self.student.marks.items():
                print(f'{key} : {value}')

class BriefStudentView(StudentView):
    def __init__(self, s: st.Student):
        super().__init__(s)
        
    def view(self):
        print(f'{self.student.last_name} {self.student.first_name} {self.student.middle_name} ({self.student.group})')