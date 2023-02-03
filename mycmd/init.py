import os
import sys
from exceptions import InvalidCommand
from handlers import Handlers


def cmd():
    path = 'C:/'
    handlers = Handlers(path)

    while True:
        path = handlers.terminal.path
        command = input(f'{path}>').split()

        if len(command) == 1:
            command.append(None)

        match command:
            case 'dir' | 'ls' as command, *args:
                handlers.scan()

            case 'cd' as command, name:
                name = formatting(name)
                handlers.change_dir(name)

            case 'md' | 'mkdir' as command, name:
                name = formatting(name)
                if name is None:
                    print('You did not type the name of directory!')
                    return None
                handlers.create_dir(name)

            case 'echo' as command, name:
                name = formatting(name)
                if name is None:
                    print('You did not type the name of file!')
                    return None
                handlers.create_file(name)

            case 'rename' as command, *args:
                if len(args) != 2:
                    print('Type please old and new names for file!')
                    return None
                args[0] = formatting(args[0])
                args[1] = formatting(args[1])
                handlers.rename(args[0], args[1])

            case 'remove' as command, name:
                if name is None:
                    print('You did not type the name of directory/file!')
                    return None
                name = formatting(name)
                handlers.remove(name)

            case 'read' as command, name:
                if name is None:
                    print('You did not type the name of file!')
                    return None
                name = formatting(name)
                handlers.read(name)

            case 'exit' as command, *args:
                print('Goodbye!')
                sys.exit(1)

            case _:
                print('Invalid command!')
                return None

def formatting(name: str) -> str | None:
    if name is None:
        return None
    return name.replace('_', ' ')
