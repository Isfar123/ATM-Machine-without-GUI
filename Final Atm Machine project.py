def inside_options():
    print("***Options***")
    print("Press 1 to change pin")
    print("Press 2 to check balance")
    print("Press 3 to deposite balance")
    print("Press 4 to Withdraw")
    print("Press 5 to exit")
def deposit():
    deposit = int(input("Enter deposite value in multiples of 500 = "))
    with open("another file.py", "r") as f:
        balance = f.read()
    balance = int(balance) + deposit
    with open("another file.py", "w") as d:
        d.write(str(balance))
        print("Deposit successfully Done! Balance is now ", balance,"Taka")
        
def withdraw():
    with open("another file.py", "r") as s:
        f = s.read()
        if int(f) > 0:
            print("Withdraw is possible")
            withdraw = int(input("Enter how much you want to withdraw? "))
            if withdraw%500==0:
                if withdraw<=100000:
                    with open("another file.py", "r") as f:
                        balance = f.read()
                    balance = int(balance) - withdraw
                    with open("another file.py", "w") as d:
                        d.write(str(balance))
                        print(withdraw,"taka withdrawn successfully! Balance is now ", balance,"taka")
                else:
                    print("Sorry cannot withdraw more than 1 lac!")
            else:
                print("Sorry only allowed to withdraw multiples of 500")
        else:
            print("Sorry insufficient Cash!")

def change_pin():
    new_pin = (input("Enter new pin = "))
    with open("pin.py", "w") as f:
        d = f.write(new_pin)

def check_balance():
    with open("another file.py") as b:
        print("Your balance is = ", b.read(),"taka")

def main_homepage():
    print("Press 1 for Login")
    print("Press 2 for Admin Mode")
    print("Press 3 for Exit")


print("Welcome to the home page!")
card_block=0
main_option=5
print("****************")
while True:
    main_homepage()
    main_option = int(input("Select an option from above = "))
    if main_option==3:
        print("Thank you for using EBL!")
        print("Take Care!")
        break
    main_homepage()
    if main_option==1:
        user_name = input("Enter your user name = ")
        if user_name=="barry":
            tries = 0
            user_input_pin=0
            s=10
            while user_input_pin != s and tries < 3:
                user_input_pin = int(input("Enter your 3 digit pin = "))
                with open("pin.py", "r") as f:
                    s = f.read()
                if user_input_pin == int(s):
                    tries =3
                    print("Log in Sucess!")
                    while True:
                        inside_options()
                        option = int(input("What would you like to do? "))
                        if option == 1:
                            change_pin()
                        elif option == 2:
                            check_balance()
                        elif option == 3:
                            deposit()
                        elif option == 4:
                            withdraw()
                        elif option==5:
                            print("Going back to previous menu")
                            break
                else:
                    print("Sorry try again!")
                    tries += 1
                if tries==3 and user_input_pin!=int(s):
                    print("Card Blocked")
                    card_block = 1
                    break

    elif main_option==2:
        print("This section is only if your card is block!")
        if card_block==1:
            print("Admin mode access!")
            special_card_numer = int(input("Enter Special card number  = "))
            main_pin="admin000"
            if special_card_numer ==000000000 and main_pin=="admin000":
                card_block=0
                print("Card Unblocked!!")

            else:
                print("Sorry entered wrong special card number or pin")
        else:
            print("Sorry card is not blocked!")



'''user_name=input("Enter your user name = ")
if user_name=="barry":
    tries = 0
    user_input_pin=0
    s=10
    card_block=0
    while user_input_pin != s and tries < 3:
        user_input_pin = int(input("Enter your 3 digit pin = "))
        with open("pin.py", "r") as f:
            s = f.read()
        if user_input_pin == int(s):
            tries =3
            print("Log in Sucess!")
            while True:
                options()
                option = int(input("What would you like to do? "))
                if option == 1:
                    change_pin()
                elif option == 2:
                    check_balance()
                elif option == 3:
                    deposit()
                elif option == 4:
                    withdraw()
                elif option==5:
                    print("Thank you for using EBL BANK TAKE CARE!")
                    break
        else:
            print("Sorry try again!")
            tries += 1
        if tries==3 and user_input_pin!=int(s):
            print("Card Blocked")
            card_block = 1
            break'''

