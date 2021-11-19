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

    def __init__(self, title):
        super().__init__(title)
        self.items = []
        self.is_running = False


    def run(self):
        self.is_running = True
        while self.is_running:
            self.__print_menu()
            self.__handle_user_input()

    def add_MenuItem(self, item: MenuItem):
        self.items.append(item) # Исправь позже на аппенд, это питон, а не урок по моветону

    def __print_menu(self):
        for item in self.items:
            print(item.get_title())

    def __handle_user_input(self):
        pass
    # номер пункта меню, не забывать про шибку, если что-то неправильно

class SimpleMenuItem(MenuItem):
    action: Callable

    def __init__(self, title, action):
        super().__init__(title)
        self.action = action

    def run(self):
        self.action()