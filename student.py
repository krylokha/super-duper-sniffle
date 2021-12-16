from __future__ import annotations
from dataclasses import dataclass
from students_repository import StudentRepository

@dataclass
class Student:
    last_name: str
    first_name: str
    middlle_name: str
    group: str
    marks: dict[str, int]
    
    def __init__(self, last_name, first_name, middle_name, group, marks):
        self.last_name = last_name
        self.first_name = first_name
        self.middlle_name = middle_name
        self.group = group
        self.marks = {}
        
    # скорее можно без геттеров!    Лучше не пользоваться
        
    def get_last_name(self):
        return self.last_name   
    
    def get_first_name(self):
        return self.first_name
    
    def get_middle_name(self):
        return  self.middlle_name
    
    def get_group(self):
        return self.group
    
    # def get_marks(self):
    #     return self.marks
    
    def print_extented_form(self):
        print(f'Фамилия: {self.get_last_name()}')
        print(f'Имя: {self.get_first_name()}')
        print(f'Отчество: {self.get_middle_name()}')
        print(f'Группа: {self.get_group()}')
        print('Оценки:')
        for key in self.marks.keys():
            print(f'{key}: {self.marks[key]}')
    
    def print_shorted_form(self):
        print(f'{self.get_last_name()} {self.get_first_name()} {self.get_middle_name()} ({self.get_group()})')
        
    # проверка на отличника
    # проверка на не отличника