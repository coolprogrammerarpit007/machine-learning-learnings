from pathlib import Path
import sys
import os

def readFileAndFolderStructure():
    path = Path('')
    items = list(path.rglob('*'))
    for index,item in enumerate(items):
        print(f"{index + 1}: {item}")


def create_file():
    try:
        readFileAndFolderStructure()
        file_name = input("Enter Your File Name: ")
        p = Path(file_name)
        if not p.exists():
            with open(p,"w") as f_hand:
                data = input("What do you wanted to write: ")
                f_hand.write(data)

            print("Your File has been created sucessfully!")

        else:
            print("File is already existed before")

    except Exception as err:
        print(f"Some error {err} occurs!")

def read_file():
    try:
        readFileAndFolderStructure()
        file_name = input("Enter File Name: ")
        file_path = Path(file_name)

        if file_path.exists():
            with open(file_path,"r") as fhand:
                lines = fhand.read()
                # for line in lines:
                #     print(line)
                print(lines)

            print("File has been readed successfuly")
        else:
            print("This file do not existed!")

    except Exception as error:
        print("Some error occurs: ",error)

def update_file():
    try:
        readFileAndFolderStructure()
        name = input("Tell Which file do you wanted to update!")
        file_path = Path(name)
        if file_path.exists() and file_path.is_file():
            print("Press 1 for changing the name of the file! ")
            print("Press 2 for Overwriting the file.")
            print("Press 3 for Updating data inside file: ")
            user_choice = input("Enter Your Choice: ")

            if user_choice == "1":
                new_file_name = input("Tell new name of file: ")
                new_file_path = Path(new_file_name)
                file_path.rename(new_file_path)
                print("File name updated sucessfully!")

            elif user_choice == "2":
                with open(file_path,"w") as f_hand:
                    new_content = input("Enter the content which you wanna write! ")
                    f_hand.write(new_content)

            elif user_choice == "3":
                with open(file_path,"a") as f_hand:
                    data = input("Enter your new data: ")
                    f_hand.write(data)

            else:
                print("You entered a wrong choice.")
                sys.exit(1)
        else:
            print("File do not existed.")
            sys.exit(1)

    except Exception as err:
        print(f"Some {err} named error occurs.")

def delete_file():
    try:
        readFileAndFolderStructure()
        file_name = input("Enter File name to be deleted! ")
        file_path = Path(file_name)
        if file_path.exists() and file_path.is_file():
            os.remove(file_path)
            print("File removed successfully!")

        else:
            print("File does not existed!")
            sys.exit(1)
    except Exception as err:
        print(f"Some {err} named error occurs.")

print("Press 1 for creating a file.")
print("Press 2 for reading a file.")
print("Press 3 for updating a file.")
print("Press 4 for deleting a file.")


try:
    user_option = input("Enter Your Choice: ")

except Exception as err:
    print(f"Sorry, error occurs as {err}" )

else:
    if user_option == "1":
        create_file()

    elif user_option == "2":
        read_file()

    elif user_option == "3":
        update_file()

    elif user_option == "4":
        delete_file()

    else:
        print("User has choosen a wrong file name: ")
        sys.exit(1)





