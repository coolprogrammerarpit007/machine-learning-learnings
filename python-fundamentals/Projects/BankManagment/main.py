import json
import random
import string
import sys
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fhand:
                data = json.loads(fhand.read())
        else:
            print("No Such file exists.")
    except Exception as err:
        print(f"An Error Occurs: {err}")

    @staticmethod
    def update():
        with open(Bank.database,"w") as fs:
            fs.write(json.dumps(Bank.data))

    def createAccount(self):
        data = {
            "name" : input("Enter Your Name: "),
            "age" : int(input("Enter your age: ")),
            "email":input("Enter your emailId: "),
            "pin" : int(input("Enter your 4-digit pin: ")),
            "accountNo.":1234,
            "balance":0
        }

        if data["age"] < 18 or len(str(data['pin'])) != 4:
            print("Sorry,you can not create your account: ")
            sys.exit(0)

        else:
            print("Account has been created successfully.")
            for item in data:
                print(f"{item}: {data[i]}")
            print("Please Note down your account Number.")
            Bank.data.append(data)
            Bank.update(data)



user = Bank()




def start():
    print("Press 1 for forecasting an account.")
    print("Press 2 for depositing money to your bank account.")
    print("Press 3 for withdrawing money from your bank account.")
    print("Press 4 for your bank details.")
    print("Press 5 for updating your bank details.")
    print("Press 6 for de-activating your bank account.")

    check = int(input("Enter your response: "))
    if check == 1:
        user.createAccount()

if __name__ == "main":
    start()