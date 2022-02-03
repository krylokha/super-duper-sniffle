from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Student:
    last_name: str
    first_name: str
    middle_name: str
    group: str
    marks: dict[str, int] = field(default_factory= lambda: {})
                
    def create_marks(self, subj: str, mark: int):
        self.marks[subj] = mark
        
    def is_high_achiever(self) -> bool:
        flag = False
        for mark in self.marks.values():
            if mark == 5:
                flag = True
            else:
                flag = False
                break
        return flag
    
    def is_low_achiever(self) -> bool:
        for mark in self.marks.values():
            if mark < 3:
                return True
        return False
            
    