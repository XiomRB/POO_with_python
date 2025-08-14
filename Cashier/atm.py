class Atm:

    def __init__(self,pin):
        self.__pin = pin
        self._balance = 1000.00
    
    def deposit(self, amount):
        self._balance += amount
        print("Deposito exitoso")
        self.show_balance()
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print("Retiro exitoso")
            self.show_balance()
        else:
            print("No tienes suficiente saldo para retirar esa cantidad.")

    def show_balance(self):
        print(f"El saldo de la cuenta es Q. {self._balance}")
    
    def change_pin(self, new_pin):
        if(self.__pin == new_pin):
            print('El pin es el que usas ahora')
        else:
            self.__set_pin(new_pin)
            
    def __set_pin(self,new_pin):
        if len(new_pin) == 4:
            self.__pin = new_pin
            print('Pin seteado exitosamente')
        else:
            print('El pin debe contener 4 digitos')