from atm import Atm

cashier = Atm('1234')

def select_option():
    print(
        '''
        Bienvenido a tu cajero!!! 
        Qué opción deseas realizar? 
        d. Depositar 
        r. Retirar 
        s. Ver saldo 
        p. Actualizar pin
        ''' 
    )
    return input()

def make_transaction(option):
    if option == 'd':
        amount = input('Ingresa la cantidad a depositar: ')
        cashier.deposit(float(amount))
    elif option == 'r':
        amount = input('Ingresa la cantidad a retirar: ')
        cashier.withdraw(float(amount))
    elif option == 'p':
        new_pin = input('Ingresa el nuevo pin (debe contener 4 caracteres): ')
        cashier.change_pin(new_pin)
    elif option == 's':
        cashier.show_balance()
    else:
        print('Esta opción no existe. Adios!')

option = select_option()
make_transaction(option)
