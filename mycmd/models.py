import os

class CmdConsole:

    def __init__(self, path: str) -> None:
        self.path = path

    def scan_dir(self):
        with os.scandir(self.path) as entries:
            for entry in entries:
                name = entry.name.replace(' ', '_')
                if os.path.isdir(entry):
                    print(f'<DIR>  {name}')
                else:
                    print(f'\t\t {name}')

    def change_dir(self, path: str):
        self.path = os.path.abspath(os.path.join(self.path, path))
        return self.path

    def create_dir(self, name: str):
        os.mkdir(os.path.join(self.path, name))

    def create_text(self, name: str):
        with open(os.path.join(self.path, name), 'w') as file:
            file.write(input('Write some text: '))

    def rename(self, old: str, new: str):
        os.rename(os.path.join(self.path, old), os.path.join(self.path, new))

    def remove(self, name: str):
        if name.endswith('.txt'):
            os.remove(os.path.join(self.path, name))
        else:
            os.rmdir(os.path.join(self.path, name))

    def file_read(self, name: str) -> str:
        with open(os.path.join(self.path, name), 'r') as file:
            print(file.read())










