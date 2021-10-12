import os


class User:
    def __init__(self, name, login, password, age, gender):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        self.gender = gender
        self.option = ['0', '1', '2']

    def show_menu(self):
        print('''
        [0]  -->  Exit  
        [1]  -->  Register
        [2]  -->  Log in
        ''')

    def enter_sys(self):
        self.clear()
        self.show_menu()
        input_user = input('[0, 1, 2]: ').strip()
        while input_user not in self.option:
            self.clear()
            self.show_menu()
            print('Invalid syntax!')
            input_user = input('[0, 1, 2]: ').strip()

    def exitt(self):
        print('Good bye!')
        exit()

    def register(self):
        pass

    def log_in(self):
        pass

    @staticmethod
    def clear():
        os.system('clear')


dilshod = User('dilishod', 'shamshod', 'dili', 24, 1)
dilshod.enter_sys()
