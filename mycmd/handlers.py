import os

from exceptions import DirNotFound, InvalidCommand, NotFound, AlreadyExists
from models import CmdConsole


class Handlers:
    def __init__(self, path) -> None:
        self.path = path
        self.terminal = CmdConsole(path)
        self.dir = self.scan_dir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)

    def scan_dir(self, path):
        with os.scandir(path) as entries:
            return [e.name for e in entries if os.path.isdir(e)]

    def scan_files(self, path):
        with os.scandir(path) as entries:
            return [e.name for e in entries if e.name.endswith('.txt')]

    def scan(self):
        return self.terminal.scan_dir()

    def change_dir(self, path: str):
        if path not in self.dir and path != '..':
            print('There is no such directory!')
            return None
        self.terminal.change_dir(path)
        self.dir = self.scan_dir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)

    def create_dir(self, name: str):
        if name in self.dir:
            check = input('Directory with the same name exists already! Do you want to replace it? y/n? ')
            if check == 'y':
                self.terminal.remove(name)
                self.terminal.create_dir(name)
                return None
            elif check == 'n':
                return None
            else:
                print('Invalid command!')
                return None
        self.terminal.create_dir(name)
        self.dir = self.scan_dir(self.terminal.path)

    def create_file(self, name: str):
        if name in self.files:
            check = input('File with the same name exists already! Do you want to replace it? y/n? ')
            if check == 'y':
                self.terminal.remove(name)
                self.terminal.create_text(name)
                return None
            elif check == 'n':
                return None
            else:
                print('Invalid command!')
                return None
        self.terminal.create_text(name)
        self.files = self.scan_files(self.terminal.path)

    def rename(self, old: str, new: str):
        if old not in self.dir and old not in self.files:
            print(self.scan())
            print('There is no such directory/file!')
            return None
        if new in self.dir and new in self.files:
            print('This name is already exists!')
            return None
        self.terminal.rename(old=old, new=new)
        self.dir = self.scan_dir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)

    def remove(self, name: str):
        if name not in self.dir and name not in self.files:
            print('There is no such directory/file!')
            return None
        self.terminal.remove(name=name)
        self.dir = self.scan_dir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)

    def read(self, name: str) -> str | None:
        if name not in self.files:
            print('There is no such directory/file!')
            return None
        self.terminal.file_read(name)











