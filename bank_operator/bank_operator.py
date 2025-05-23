from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def get_user_idx():
    if not users:
        raise ValueError("No users available. Please create a user first.")

    while True:
        idx = int(input("Select user number: ")) - 1
        if 0 <= idx < len(users):
            break
        else:
            print("Invalid user number. Please try again.")
    return idx

def get_user():
    idx = get_user_idx()
    return users[idx]

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
    else:
        users.append(user)
        print(f"User {name} created.\n")

def list_users():
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("No users available. Please create a user first.\n")
        return

    list_users()
    idx = get_user_idx()
    user = users[idx]


    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    account_choice = int(input("Enter your choice (1, 2, 3) or any other number for a generic account: "))
    amount = float(input("Enter initial deposit: "))

    if account_choice == 1:
        account = SavingsAccount(user, amount)
    elif account_choice == 2:
        account = StudentAccount(user, amount)
    elif account_choice == 3:
        account = CurrentAccount(user, amount)
    else:
        print("Creating a generic account.")
        account = BankAccount(amount)

    users[idx].add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    list_users()
    if not users:
        print("No users available. Please create a user first.\n")
        return
    user = get_user()
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts[acc_idx].deposit(amount)

def withdraw_money():
    list_users()
    if not users:
        print("No users available. Please create a user first.\n")
        return
    user = get_user()
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    if not users:
        print("No users available. Please create a user first.\n")
        return
    user = get_user()
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

