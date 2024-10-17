from cryptography.fernet import Fernet
import os

####TO DO: Add functionality for - Remove login and Update login

class PasswordManager:
    def __init__(self):
        code_path = "C:/Users/kashi/Downloads/GitHub Repositories/Python Projects/passwordManager/code.code"
 
        try:
            # get the size of file
            code_size = os.stat(code_path).st_size
        
            # if file size is 0, it is empty
            if (code_size == 0):
                self.code = self.set_code()
            else:
                self.code = self.load_code()
        
        # if file does not exist, then exception occurs
        except FileNotFoundError as e:
            self.code = self.set_code()

        key_path = "C:/Users/kashi/Downloads/GitHub Repositories/Python Projects/passwordManager/key.key"
 
        try:
            # get the size of file
            key_size = os.stat(key_path).st_size
        
            # if file size is 0, it is empty
            if (key_size == 0):
                self.key = self.generate_key()
            else:
                self.key = self.load_key()
        
        # if file does not exist, then exception occurs
        except FileNotFoundError as e:
            self.key = self.generate_key()

        self.login_file = None
        self.site_dict = {}

    
    def set_code(self, code_file="code.code"):
        invalid = True

        while invalid:
            try:
                print("Create a 6 digit passcode")
                code = int(input("Passcode for your password manager: "))
                code = str(code)
                if len(code) == 6:
                    self.code = code
                    with open(code_file, "w") as code_file:
                        code_file.write(self.code)
                    print("Code set successfully")
                    invalid = False
                    return self.code
                else:
                    print("Passcode was not of 6 digits, please try again.")
            except:
                print("Passcode was not of 6 digits, please try again.")

    def check_code(self):
        try:
            print("Input your 6 digit passcode")
            code = int(input("Passcode for your password manager: "))
            code = str(code)
            if code == self.code:
                print("Success!")
                return True
            else:
                print("Passcodes did not match, please try again.")
                self.check_code()
        except:
            print("Passcode was not of 6 digits, please try again.")
            return self.check_code()
    
    def load_code(self, code_file="code.code"):
        with open(code_file, "r") as code_file:
            self.code = code_file.read()
            return self.code
        
    def change_code(self):
        self.check_code()
        self.set_code()

    def generate_key(self, key_file="key.key"):
        self.key = Fernet.generate_key()
        with open(key_file, "wb") as key_file:
            key_file.write(self.key)
        return self.key
        

    def load_key(self, key_file="key.key"):
        with open(key_file, "rb") as key_file:
            self.key = key_file.read()
        return self.key

    def create_login_file(self, path, initial_values=None):
        self.login_file = path
        if initial_values is not None:
            for site, login in initial_values.items():
                self.add_login(site, login[0], login[1])

    def load_login_file(self, path):
        self.login_file = path
        with open(path, 'r') as f:
            for line in f:
                site, login = line.split(": ")
                username, encrypted = login.split(" - ")
                self.site_dict[site] = (username, encrypted)

    def add_login(self, site, username, password):
        encrypted = self.encrypt_password(password)
        self.site_dict[site] = (username, encrypted.decode())
        if self.login_file is not None:
            with open(self.login_file, 'a+') as f:
                f.write(site + ": " + username + " - " + encrypted.decode() + "\n")

    def get_login(self, site):
        if len(self.site_dict) != 0:
            return f"Username: {self.site_dict[site][0]}, Password: {self.decrypt_password(self.site_dict[site][1])}"
        else:
            print("No logins for this file. Must add login first.")

    def encrypt_password(self, password):
        f = Fernet(self.key)
        return f.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        f = Fernet(self.key)
        return f.decrypt(encrypted_password.encode()).decode()


def main():

    pm = PasswordManager()

    pm.check_code()

    print("""
    (1) Change code
    (2) Create Login File
    (3) Load Login File
    (4) Add Login
    (5) Get Login
    (q) Quit
    """)

    done = False

    while not done:
        choice = input("Selection: ")
        if choice == "1":
            pm.change_code()
        elif choice == "2":
            path = input("Enter file name: ")
            pm.create_login_file(path)
            print("Login file created successfully.")
        elif choice == "3":
            path = input("Enter file name: ")
            pm.load_key()
            pm.load_login_file(path)
            print("Login file loaded successfully.")
        elif choice == "4":
            site = input("Enter the site: ")
            username = input("Enter Username: ")
            password = input("Enter password: ")
            pm.add_login(site, username, password)
            print("Login added successfully.")
        elif choice == "5":
            sites = list(pm.site_dict.keys())
            if len(sites) != 0:
                print("Select a site:")
                for i, site in enumerate(sites, start=1):
                    print(f"{i}. {site}")

                invalid = True
                while invalid:
                    selection = input("Enter the number associated with the desired site: ")
                    try:
                        site = sites[int(selection) - 1]
                        print(f"Login for {site}:\n{pm.get_login(site)}")
                        invalid = False
                    except:
                        print("Invalid selection, try again.")   
            else:
                print("No logins for this file. Must add login first.") 
        elif choice == "q":
            done = True
            print("Password manager closed.")
        else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
