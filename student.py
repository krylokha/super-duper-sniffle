from __future__ import annotations
from dataclasses import dataclass

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
        
    def show_students(self):
        pass