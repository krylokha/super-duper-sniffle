from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, List

class MenuItem(ABC):
    title: str

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def run(self):
        pass

    def get_title(self) -> str:
        return self.title

class Menu(MenuItem):
    items: list[MenuItem]
    is_running: bool

    def __init__(self, title, **kwargs):
        super().__init__(title)
        is_main_menu = kwargs.get("is_main_menu", True)
        self.items = []
        self.is_running = False
        self.is_main_menu = is_main_menu

    def run(self):
        self.is_running = True
        while self.is_running:
            self.__print_menu()
            self.__handle_user_input()

    def add_SimpleMenuItem(self, item: MenuItem, action):
        simple_menu_item = SimpleMenuItem(item, action)
        self.items.append(simple_menu_item)
        return simple_menu_item
        
    def add_SubMenu(self, title):
        submenu = Menu(title = title, is_main_menu = False)
        self.items.append(submenu)
        return submenu

    def __print_menu(self):
        for i, item in enumerate(self.items):
            print(f'{i+1}. {item.get_title()}')
        if self.is_main_menu:
            print(f'{len(self.items) + 1}. Выход')
        else:
            print(f'{len(self.items) +1}. Назад') 

    def __handle_user_input(self):
        inp = int(input("Выберите пункт меню: "))
        if inp > len(self.items) + 1 or inp < 1:
            print('Вы ввели некорректный пункт меню!')
        elif inp == len(self.items) + 1:
            self.is_running = False
        else:
            self.items[inp - 1].run()

class SimpleMenuItem(MenuItem):
    action: Callable

    def __init__(self, title, action):
        super().__init__(title)
        self.action = action

    def run(self):
        self.action()
    
def test():
    print('Hello, World!')

main_menu = Menu('Главное меню')

main_menu.add_SimpleMenuItem('Список студентов', test)
main_menu.add_SimpleMenuItem('Добавить студента', test)
student_editor = main_menu.add_SubMenu('Редактировать студента')
main_menu.add_SimpleMenuItem('Удалить студента', test)
main_menu.add_SimpleMenuItem('Показать отличников', test)
main_menu.add_SimpleMenuItem('Показать неуспевающих', test)
    
main_menu.run()