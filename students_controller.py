from __future__ import annotations
from calendar import c
from menu import Menu
from student import Student
from student_view import BriefStudentView, DetailedStudentView
from student_visitor import BriefPrintVisitor, DetailedPrintVisitor, HighAchieverPrintVisitor, LowAchieverPrintVisitor
from students_repository import StudentRepository

class StudentsController:
    students: StudentRepository
    main_menu: Menu
    
    def __init__(self, students, main_menu):
        self.students = students
        self.main_menu = main_menu
        self.selected_student = None
        
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
        for i in range(self.students.count_students()):
            self.students.visit(HighAchieverPrintVisitor())
    
    def get_low_achievement_students(self):
        for i in range(self.students.count_students()):
            self.students.visit(LowAchieverPrintVisitor())
        
    def edit_last_name(self):
        self.selected_student.last_name = str(input('Новая фамилия: '))
        
    def edit_first_name(self):
        self.selected_student.first_name = str(input('Новое имя: '))    
        
    def edit_middle_name(self):
        self.selected_student.middle_name = str(input('Новое отчество: '))
    
    def edit_group(self):
        self.selected_student.group = str(input('Новая группа: '))
        
    def add_mark(self):
        subj = str(input('Предмет: '))
        if subj in self.selected_student.marks:
            print('Оценка по этому предмету у студента уже есть')
        else:
            mark = int(input('Оценка: '))
            self.selected_student.create_marks(subj, mark)
        
    def edit_mark(self):
        subj = str(input('Предмет: '))
        if subj not in self.selected_student.marks:
            print('У студента ещё нет этого предмета')
        else:
            mark = int(input('Оценка: '))
            self.selected_student.marks[subj] = mark # по-другому изменение
            
    def remove_mark(self):
        subj = str(input('Предмет: '))
        confirm = str(input(f'Вы уверены, что хотите удалить оценку по {subj}? [Y/N] '))
        if confirm == 'Y':
            self.selected_student.marks.pop(subj)
    
    def select_student(self):
        self.students.visit(BriefPrintVisitor())
        chosen_student = int(input('Выберите студента: '))
        self.selected_student = self.students.get_student(chosen_student)
    
    def print_selected_student(self):
        print('Редактируемый студент: ')
        DetailedStudentView(self.selected_student).view()   
    
    def deselect_student(self):
        self.selected_student = None
    
    def run(self):
        self.main_menu.run()     

def main():
    main_menu = Menu('Главное меню')
    
    ivanov = Student('Иванов', 'Иван', 'Иванович', 'ОП-16')
    ivanov.create_marks('Математика', 5)
    ivanov.create_marks('Информатика', 5)
    petrov = Student('Петров', 'Петр', 'Петрович', 'ОП-16')
    repository = StudentRepository()
    repository.add_student(ivanov)
    repository.add_student(petrov)
    
    controller = StudentsController(repository, main_menu)

    main_menu.add_SimpleMenuItem('Список студентов', controller.list_students)
    main_menu.add_SimpleMenuItem('Добавить студента', controller.add_student)
    student_editor = main_menu.add_SubMenu('Редактировать студента')
    student_editor.add_SimpleMenuItem('Изменить фамилию', controller.edit_last_name)
    student_editor.add_SimpleMenuItem('Изменить имя', controller.edit_first_name)
    student_editor.add_SimpleMenuItem('Изменить отчество', controller.edit_middle_name)
    student_editor.add_SimpleMenuItem('Изменить группу', controller.edit_group)
    student_editor.add_SimpleMenuItem('Добавить оценку', controller.add_mark)
    student_editor.add_SimpleMenuItem('Изменить оценку', controller.edit_mark)
    student_editor.add_SimpleMenuItem('Удалить оценку', controller.remove_mark)
    main_menu.add_SimpleMenuItem('Удалить студента', controller.remove_student)
    main_menu.add_SimpleMenuItem('Показать неуспевающих', controller.get_low_achievement_students)
    main_menu.add_SimpleMenuItem('Показать отличников', controller.get_high_achievement_students)
    
    student_editor.set_on_start_command(controller.select_student)
    student_editor.set_on_print_command(controller.print_selected_student)
    student_editor.set_on_exit_command(controller.deselect_student)

    controller.run()
    
if __name__ == "__main__":
    main()
