from __future__ import annotations
from menu import Menu
from student import Student
from student_view import BriefStudentView, DetailedStudentView
from student_visitor import BriefPrintVisitor, DetailedPrintVisitor, HighAchieverPrintVisitor, LowAchieverPrintVisitor
from students_repository import StudentRepository

class StudentsController:
    
    def __init__(self):
        self.students = StudentRepository()
        self.students.load()
        self.main_menu = Menu('Главное меню')
        self.create_menu()
        self.selected_student = None
    
    def create_menu(self):
        self.main_menu.add_SimpleMenuItem('Список студентов', self.list_students)
        self.main_menu.add_SimpleMenuItem('Добавить студента', self.add_student)
        student_editor = self.main_menu.add_SubMenu('Редактировать студента')
        student_editor.add_SimpleMenuItem('Изменить фамилию', self.edit_last_name)
        student_editor.add_SimpleMenuItem('Изменить имя', self.edit_first_name)
        student_editor.add_SimpleMenuItem('Изменить отчество', self.edit_middle_name)
        student_editor.add_SimpleMenuItem('Изменить группу', self.edit_group)
        student_editor.add_SimpleMenuItem('Добавить оценку', self.add_mark)
        student_editor.add_SimpleMenuItem('Изменить оценку', self.edit_mark)
        student_editor.add_SimpleMenuItem('Удалить оценку', self.remove_mark)
        self.main_menu.add_SimpleMenuItem('Удалить студента', self.remove_student)
        self.main_menu.add_SimpleMenuItem('Показать неуспевающих', self.get_low_achievement_students)
        self.main_menu.add_SimpleMenuItem('Показать отличников', self.get_high_achievement_students)
        
        student_editor.set_on_start_command(self.select_student)
        student_editor.set_on_print_command(self.print_selected_student)
        student_editor.set_on_exit_command(self.deselect_student)
        
    def list_students(self):
        self.students.visit(DetailedPrintVisitor())
    
    def add_student(self):
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        middle_name = input('Введите отчество: ')
        group = input('Введите группу: ')
        student = Student(surname, name, middle_name, group)
        self.students.add_student(student)
        
    def remove_student(self):
        self.students.visit(BriefPrintVisitor())
        removing_student = int(input('Номер студента для удаления: '))
        if not (1 <= removing_student <= self.students.count_students()):
            print('Выбран неправильный номер студента')
        else:
            answer = str(input(f'Вы уверены, что хотите удалить студента {BriefStudentView(self.students.get_student(removing_student)).view()}? [Y/N] '))
            if answer == 'Y':
                self.students.remove_student(removing_student)
    
    def get_high_achievement_students(self):
        self.students.visit(HighAchieverPrintVisitor()) 

    def get_low_achievement_students(self):
        self.students.visit(LowAchieverPrintVisitor())
        
    def edit_last_name(self):
        self.selected_student.last_name = str(input('Новая фамилия: '))
        self.students.save()
        
    def edit_first_name(self):
        self.selected_student.first_name = str(input('Новое имя: '))  
        self.students.save()  
        
    def edit_middle_name(self):
        self.selected_student.middle_name = str(input('Новое отчество: '))
        self.students.save()
    
    def edit_group(self):
        self.selected_student.group = str(input('Новая группа: '))
        self.students.save()
        
    def add_mark(self):
        subj = str(input('Предмет: '))
        if subj in self.selected_student.marks:
            print('Оценка по этому предмету у студента уже есть')
        else:
            mark = int(input('Оценка: '))
            self.selected_student.create_marks(subj, mark)
            self.students.save()
        
    def edit_mark(self):
        subj = str(input('Предмет: '))
        if subj not in self.selected_student.marks:
            print('У студента ещё нет этого предмета')
        else:
            mark = int(input('Оценка: '))
            self.selected_student.marks[subj] = mark
            self.students.save()
            
    def remove_mark(self):
        subj = str(input('Предмет: '))
        confirm = str(input(f'Вы уверены, что хотите удалить оценку по {subj}? [Y/N] '))
        if confirm == 'Y':
            self.selected_student.marks.pop(subj)
            self.students.save()
    
    def select_student(self):
        self.students.visit(BriefPrintVisitor())
        chosen_student = int(input('Выберите студента: '))
        if not (1 <= chosen_student <= self.students.count_students()):
            print('Выбран неправильный номер студента')
            raise Exception()
        else:
            self.selected_student = self.students.get_student(chosen_student)
    
    def print_selected_student(self):
        print('Редактируемый студент: ')
        DetailedStudentView(self.selected_student).view()   
    
    def deselect_student(self):
        self.selected_student = None
    
    def run(self):
        self.main_menu.run()

    
if __name__ == "__main__":
    controller = StudentsController()
    controller.run()
