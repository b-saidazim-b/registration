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
        self.log_in_option = ['0', '1', '2', '3']


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
            print("It's empty string please again or such a login exists")
            input_name = input('Name: ').strip().capitalize()

        input_login = input('Login: ').strip().lower()
        while self.empty(input_login) or self.check_log_registr(input_login):
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
        input_login = input('Login: ').strip().lower()
        while self.empty(input_login) or not self.check_log_registr(input_login):
            self.clear()
            print("It's empty string please again")
            input_login = input('Login: ').strip().lower()

        input_password = input('Password: ').strip()
        while self.empty(input_password):
            self.clear()
            print('Login', self.input_login)
            print("It's empty string please again")
            input_password = input('Password: ').strip()
        self.enter_log_in()

    def show_log_in(self):
        self.clear()
        print('''
            Welcome to Log in
        [0] ---> Exit
        [1] ---> Change login
        [2] ---> Change password
        [3] ---> Delete account
        ''')

    def enter_log_in(self):
        self.clear()
        self.show_log_in()
        input_user = input('[0, 1, 2, 3]: ').strip()
        while input_user not in self.log_in_option:
            self.clear()
            self.show_menu()
            print('Invalid syntax!')
            input_user = input('[0, 1, 2, 3]: ').strip()

        if input_user == self.log_in_option[0]:
            self.exitt()

        if input_user == self.log_in_option[1]:
            self.change_login()

        if input_user == self.log_in_option[2]:
            self.change_password()

        if input_user == self.log_in_option[3]:
            self.del_acc()

    def change_login(self):
        old_log = input('Enter your old login: ').strip().lower()
        new_log = input('Enter your new login: ').strip().lower()
        mycursor.execute(f"update user set login='{new_log}' where login='{old_log}'")
        mydb.commit()
        print('Your login has been changed!')

    def change_password(self):
        old_pass = input('Enter your old password: ').strip()
        new_pass = input('Enter your new password: ').strip()
        mycursor.execute(f"update user set password='{new_pass}' where password='{old_pass}'")
        mydb.commit()
        print('Your password has been changed!')


    def del_acc(self):
        log = input('Enter your old password: ').strip().lower()
        mycursor.execute(f"delete from user where login='{log}'")
        mydb.commit()


    def check_log_registr(self, log):
        mycursor.execute(f"select login from user where login = '{log}';")
        my_log = mycursor.fetchall()
        if my_log:
            return True
        return False


    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def empty(a):
        return not a


dilshod = User('dilishod', 'shamshod', 'dili', 24, 1)
dilshod.enter_sys()
