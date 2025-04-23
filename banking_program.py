# This is a simple banking program that allows users to
# create an account, show balance , deposit money, and withdraw money.

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

def create_account(accounts):
    """Create a new bank account with an initial balance."""
    name = input("Enter your name: ")
    if name in accounts:
        print("An account with this name already exists.")
        return accounts[name]
    try:
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance <0:
            print("Initial balance cannot be negative.")
            return
        accounts[name] = {
            'name': name,
            'balance': initial_balance
        }
        print(f"Account created for {name} with balance {initial_balance}")
    except ValueError:
        print("Invalid input. Please enter a number.")    

def login(accounts):
    """Login to an existing account."""
    name = input("Enter your name: ")
    if name not in accounts:
        print("No account found with this name.")
        return None
    print(f"Logged in as {name}")
    return accounts[name]

def show_balance(account):
    """Display the current balance of the account."""
    print(f"Current balance: {account['balance']}")


def deposit(account):
    """Deposit money into the account."""
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <=0:
            print("Amount must be greater than zero.")
            return
        account['balance'] += amount
        print(f"Deposited {amount}. New balance: {account['balance']}")
    except ValueError:
        print("Invalid input. Please enter a number.")


def withdraw(account):
    """Withdraw money from the account."""
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <=0:
            print("Amount must be greater than zero.")
            return
        if amount > account['balance']:
            print("Insufficient funds.")
        else:
            account['balance'] -= amount
            print(f"Withdrew {amount}. New balance: {account['balance']}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_all_accounts(accounts):
    """Display all accounts when logged in as admin."""
    if not accounts:
        print("No accounts available.")
        return
    print("All accounts:")
    for name, details in accounts.items():
        print(f"Name: {details['name']}, Balance: {details['balance']}")

def delete_account(accounts):
    """Delete an account when logged in as admin."""
    if not accounts:
        print("No accounts available.")
        return
    name= input("Enter the name of the account to delete: ")
    if name in accounts:
        del accounts[name]
        print(f"Account for {name} deleted.")
    else:
        print("No account found with this name.")


def reset_balance(accounts):
    """Reset the balance of an account."""
    if not accounts:
        print("No accounts available.")
        return
    name=input("Enter the name of the account to reset balance: ")
    if name in accounts:
        accounts[name]['balance'] = 0
        print(f"Balance for {name} reset to 0.")
    else:
        print("No account found with this name.")


#main program
accounts= {}
is_running= True

while is_running:
    print("\nWelcome to National Banking System")
    print("1. Create Account")
    print("2. Login")
    print("3. Login as Adminstrator")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_account(accounts)
    elif choice == '2':
        account =login(accounts)
        if account:
            while True:
                print("\n1. Show Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Logout")
                action = input("Enter your choice: ")

                if action == '1':
                    show_balance(account)
                elif action == '2':
                    deposit(account)
                elif action == '3':
                    withdraw(account)
                elif action == '4':
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == '3':
        print("Admin Login")
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("Admin logged in successfully.")
            while True:
                print("\n1. Show All Accounts")
                print("2. Delete Account")
                print("3. Reset Account Balance")
                print("4. Logout")
                admin_action = input("Enter your choice: ")
                if admin_action == '1':
                    show_all_accounts(accounts)
                elif admin_action == '2':
                    delete_account(accounts)
                elif admin_action == '3':
                    reset_balance(accounts)
                    
                elif admin_action == '4':
                    print("Logging out...")
                    break
                else:   
                    print("Invalid choice. Please try again.")
    elif choice == '4':
        confirm_exit= input("Are you sure you want to exit? (y/n): ").lower()
        if confirm_exit =='y':
            print("Exiting the program...")
            is_running = False
        else:
            print("Returning to main menu...")    
    else:
        print("Invalid choice. Please try again.")