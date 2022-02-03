from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Student:
    last_name: str
    first_name: str
    middle_name: str
    group: str
    marks: dict[str, int]
    
    def __init__(self, last_name, first_name, middle_name, group):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.group = group
        self.marks = {}
                
    def create_marks(self, subj: str, mark: int):
        self.marks[subj] = mark
    