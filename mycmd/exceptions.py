class DirNotFound(Exception):
    def __str__(self):
        print('There is no such directory!')
        return None

class InvalidCommand(Exception):
    def __str__(self):
        print('Invalid command!')
        return None

class NotFound(Exception):
    def __str__(self):
        print('There is no such directory/file!')
        return None

class AlreadyExists(Exception):
    def __str__(self):
        print('This name is already exists!')
        return None


