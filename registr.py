import os
import mysql.connector.connection

mydb = mysql.connector.connect(
    host='localhost',
    user='a1',
    passwd='12345678',
    database='user'
)
mycursor = mydb.cursor()

class User:
    def __init__(self, name, login, password, age, gender):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        self.gender = gender
        self.option = ['0', '1', '2']
        self.gen_option = ['0', '1']

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

        if input_user == self.option[0]:
            self.exitt()

        if input_user == self.option[1]:
            self.register()

        else:
            self.log_in()

    def exitt(self):
        print('Good bye!')
        exit()

    def register(self):
        input_name = input('Name: ').strip().capitalize()
        while self.empty(input_name):
            self.clear()
            print("It's empty string please again")
            input_name = input('Name: ').strip().capitalize()

        input_login = input('Login: ').strip().lower()
        while self.empty(input_login):
            self.clear()
            print('Name: ', input_name)
            print("It's empty string please again")
            input_login = input('Login: ').strip().lower()

        input_password = input('Password: ').strip()
        while self.empty(input_password):
            self.clear()
            print('Name: ', input_name)
            print('Login', input_login)
            print("It's empty string please again")
            input_password = input('Password: ').strip()

        input_age = input('Age: ').strip()
        while self.empty(input_age) or not input_age.isdigit():
            self.clear()
            print('Name: ', input_name)
            print('Password: ', input_password)
            print('Login', input_login)
            print("It's empty string please again")
            input_age = input('Age: ').strip()

        input_gender = input('Gender: ').strip()
        while self.empty(input_gender) or input_gender not in self.gen_option:
            self.clear()
            print('Name: ', input_name)
            print('Password: ', input_password)
            print('Age: ', input_age)
            print('Login', input_login)
            print("""It's empty string please again
[1] - > male 
[0] - > female """)
            input_gender = input('Gender: ').strip()

        sql = 'insert into user (name, login, password, age, gender) values (%s, %s, %s, %s, %s)'
        val = input_name, input_login, input_password, input_age, input_gender
        mycursor.execute(sql, val)

        print("\nYou've successfully registered)")
        mydb.commit()

    def log_in(self):
        pass

    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def empty(a):
        return not a

dilshod = User('dilishod', 'shamshod', 'dili', 24, 1)
dilshod.enter_sys()
