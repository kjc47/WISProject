import sys
from app.commands import Command


class CalenderCommand(Command):
    def execute(self):
        print(f'I will check your calender.')