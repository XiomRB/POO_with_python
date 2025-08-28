from exceptions import *

###################   manejando excepciones de python
def divide(dividendo:float | int, divisor:float | int):
    try:
        result = dividendo/divisor
    except ZeroDivisionError as error:
        print('No es posible dividir entre cero')
        print(error)
    except TypeError as error:
        print('Solo se aceptan valores numericos (float, int) para realizar la operacion')
    except Exception as error:
        print('Disculpa, no es posible completar la división')
        print(error)
    else:                     # se ejecuta solo si no ocurrio la excepcion,  es opcional
        print(result)
    finally:                  # siempre se ejecuta, al finalizar lo que este dentro de try o del except, tambien es opcional colocarla
        print('Ha terminado la división')


divide(4,[1.0])


#######################   mis propias excepciones
def validate_username(username:str):
    if username == None:
        raise Exception('No has proporcionado un usuario')
    if len(username) < 6:
        raise UsernameLenException('El usuario debe contener al menos 6 caracteres')
    if username == 'codify':
        raise UsernameCodyException
    return True

try:
    print(validate_username('codify'))
except UsernameCodyException as error:
    print(error)
except Exception as error:
    print(error)


#################    grupos de excepciones
try:
    raise ExceptionGroup(
        'Grupo de error del custom',
        [CustomError1(), CustomError2(), CustomError3()]
    )
except *CustomError1 as error:   #   para manejar una excepcion especifica de un grupo de excepciones, se coloca antes un asterisco
    print(error)
except *CustomError2 as error:
    print(error)
except *CustomError3 as error:
    print(error)
'''except ExceptionGroup as errors:
    print(errors)'''

##########################    agregando notas
def validate_password(password:str):
    password_error = PasswordError()

    if len(password) <= 5:
        password_error.add_note('La contraseña debe tener más de 5 caracteres')
    
    if '@' in password:
        password_error.add_note('La contraseña no debe contener una @')
    
    if password_error.is_valid_to_raise():
        raise password_error
    
    return True

try:
    validate_password('hola@')
except PasswordError as error:
    print(error)
    print(error.show_notes())
