import json
import random
from pathlib import Path
import sys

class Bank:
    database = 'data.json'
    
    def __init__(self):
        if Path(Bank.database).exists():
            with open(Bank.database) as fs:
                try:
                    self.data = json.loads()
                except Exception as err:
                    print("Some Error occurs, ",err)
                    self.data = []

        else:
            print("database does not loads")
            sys.exit(0)

    
    def update(self):
        with open(Bank.database,"a") as fs:
            json.dump(self.data,fs,indent=4)


    def generateAccountNumber(self):
        existing = {acc['account_number'] for acc in self.data}
        while True:
            acct = random.randint(10000000,99999999)
            if acct not in existing:
                return acct
            

    def createBankAccount(self):
        name = input("Enter Name: ").strip()
        try:
            age = int(input("Enter Age: "))
        except ValueError:
            print("Enter a valid age")
            return
        email = input("Enter Email: ")
        try:
            pin = int(input("Enter PIN No. "))
        except ValueError:
            print("Pin Number must be of 4 numbers")
            return
        account_number = self.generateAccountNumber()
        account = {
            "name":name,
            "age":age,
            "email":email,
            "pin":pin,
            "account_number":account_number,
            "balance":0
        }
        self.data.append(account)
        self.update()

        print("Account details created successfully!")
        print(f"Account Number: {account_number}")
        print("Please,note down your bank account number ")

    def find_account(self,account_no):
        with open(Bank.database) as fs:
            self.data = json.load(fs)
        for acc in self.data:
            if acc["account_number"] == account_no:
                return acc
            
            return None

    def authenticate(self,account_no,pin):
        acc = self.find_account(account_no)
        if acc and acc["pin"] == pin:
            return acc
        return None

    def depositMoney(self):
        try:
            account_no = int(input("Enter Account Number: "))
            pin = int(input("Enter your Pin Number: "))
            acc = self.authenticate(account_no,pin)
            

            if acc is None:
                print("Authentication IS Failed!")
                return
            
            try:
                amount = float(input("Enter amount to be deposited! "))
                if amount <= 0:
                    print("Amount must be positive")
                    return
                
            except ValueError:
                print("Amount must have a valid format")
                return
            
            acc["balance"] += amount
            self.update()
            print("Money deposited to your bank account successfully.")
            

        except ValueError:
            print("Account and Pin number must be numbers ")
            return 
        
    def withdrawMoney(self):
        try:
            account_number = int(input("Enter Bank Account Number: "))
            pin_number = int(input("Enter Pin Number: "))
            acc = self.authenticate(account_number,pin_number)

            if acc is None:
                return None
            
            try:
                amount = float(input("Enter Amount to be withdrawn! "))
                if amount > acc['balance']:
                    print("Insufficient Balance")
                    return
                
            except ValueError:
                print("Invalid Format")
                return
            
            acc['balance'] -= amount
            self.update()
            print("Amount Withdrawn from your bank successfully!")

        except ValueError:
            print("Account and Pin must be valid Numbers")
            return


    def showBankAccountDetails(self):
        try:
            account_number = int(input("Enter Bank Account Number: "))
            pin = int(input("Enter your Pin Number: "))
            acc = self.authenticate(account_number,pin)

            if acc is None:
                print("Account not found!")
                return
            
            print(f"***************** Your Account Details  *******************")
            for key,value in acc.items():
                if key != "pin":
                    print(f"{key} : {value}")

        except ValueError:
            print("Account number and Pin number both are not valid!")
            return


    def updateBankAccountDetails(self):
        try:
            account_no = int(input("Enter your bank account details: "))
            pin_no = int(input("Enter Pin Number: "))
            acc = self.authenticate(account_no,pin_no)

            if acc is None:
                print("Authentication Failed!")
                return
            
            name = input("Enter Name: ")
            email = input("Enter Email: ")

            try:
                age_str = input("Enter Age: ")
                age = int(age_str) if age_str else acc['age']

            except:
                print("Invalid Age Input!")
                age = acc['age']


            pin_str = input(f"Update Pin Number ({len(str(acc['pin'])) * '*'})").strip()
            if pin_str:
                if len(pin_str) == 4 and pin_str.isdigit():
                    pin = int(pin_str)
                else:
                    print("Invalid Pin, Keeping Old Pin!")
                    pin = acc['pin']

            else:
                pin = acc['pin']

            acc['name'] = name if name else acc['name']
            acc['email'] = email if email else acc['email']
            acc['age'] = age
            acc['pin'] = pin
            self.update()
            print("Bank Account details updated Successfully!")

        except ValueError:
            print("Invalid Account and Pin number")
            return
        
    def deactivateBankAccount(self):
         try:
            account_no = int(input("Enter your bank account details: "))
            pin_no = int(input("Enter Pin Number: "))
            
         except ValueError:
            print("Invalid Account details")
            return
         
         acc = self.authenticate(account_no,pin_no)

         if acc is None:
             print("Authentication Failed!")
             return

         confirm = input("Are you sure you wanted to deactivate your bank account.")
         if confirm.lower() == "yes":
            with open(Bank.database) as fs:
                self.data = json.load(fs)

            self.data.remove(acc)
            self.update()
            print("It was nice having you!")
            print("Your bank details successfully removed from our database")

         else:
             print("Deactivation Cancelled")

             
    

        
        


def start():
    while True:
        bank = Bank()
        print("Press 1 for creating your bank account")
        print("Press 2 for depositing money to your bank account")
        print("Press 3 for withdrawing money from your bank account")
        print("Press 4 for seeing your bank details.")
        print("Press 5 for updating your bank details")
        print("Press 6 for deleting your bank details")
        print("Press 7 for exiting our services.")


        user_input = input("Please, press button b/w 1 to 6: ")
        if user_input == "1":
            bank.createBankAccount()
        elif user_input == "2":
            bank.depositMoney()
        elif user_input == "3":
            bank.withdrawMoney()
        elif user_input == "4":
            bank.showBankAccountDetails()
        elif user_input == "5":
            bank.updateBankAccountDetails()
        elif user_input == "6":
            bank.deactivateBankAccount()

        elif user_input == "7":
            print("Thank you, for using our banking services ")
            sys.exit()

if __name__ == "__main__":
    start()