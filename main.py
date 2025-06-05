# This is a sample Python script.
import sys
from asyncio import new_event_loop


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Running')
    print(f'Python Version: {sys.version}')
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Person:

    def __init__(self, first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def change_last_name(self, new_lastname:str):
        self.last_name = new_lastname