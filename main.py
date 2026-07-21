from utils.menu import main_menu
from utils.footer import footer

from managers.ec2_manager import ec2_menu
from managers.s3_manager import s3_menu
from managers.dynamodb_manager import dynamodb_menu


while True:

    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        ec2_menu()

    elif choice == "2":

        s3_menu()

    elif choice == "3":

        dynamodb_menu()

    elif choice == "4":

        footer()

        print("\nGood Bye!\n")

        break

    else:

        print("\nInvalid Choice")