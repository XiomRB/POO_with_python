class UsernameLenException(Exception):
    pass

class UsernameCodyException(Exception):
    def __init__(self):
        self.message = 'El usuario no puede ser "codify"'
        super().__init__(self.message)

class CustomError1(Exception):
    def __init__(self):
        super().__init__('Error 1 de custom')
        
class CustomError2(Exception):
    def __init__(self):
        super().__init__('Error 2 de custom')
        
class CustomError3(Exception):
    def __init__(self):
        super().__init__('Error 3 de custom')

class PasswordError(Exception):
    def __init__(self):
        super().__init__('Hay un problema con la contraseña')
    
    def is_valid_to_raise(self):
        return len(self.__notes__ ) > 0
    
    def show_notes(self):
        for note in self.__notes__:
            print(">>>",note)
    
