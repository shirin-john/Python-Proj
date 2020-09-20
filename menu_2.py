import getconn
from  new_member_ import n_member
import operations
import time
from emoji import emojize as e

def options():
    while True:
        n = n_member()
        print("_" * 130)
        print(e("\t\t\t:books::child: LITTLE READERS :child::books:"))
        print("\nWould You Like To:")
        print("1. Browse Books \n2. Logout")
        choice = int(input("\nPlease Enter Your Choice: "))

        if choice == 1:
            import book_menu
            
        elif choice == 2:
            print("\nThank You! \n")
            print("\nLogging Out...")
            time.sleep(2)
            print("\nLogged Out.")
            import menu_1
        else:
            print("Invalid Choice")
            break
options()

