import os

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number: int, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(initial_balance)
        self.logfile = f"{self.account_number}_transactions.txt"
        
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w") as f:
                f.write(f"Account Created for {self.account_holder} with Balance: Rs.{self.balance:.2f}\n")

    def log_transaction(self, action: str, amount: float):
        """Helper function to log transaction details to a file."""
        with open(self.logfile, "a") as f:
            f.write(f"{action}: Rs.{amount:.2f} | Remaining Balance: Rs.{self.balance:.2f}\n")

    def deposit(self, amount: float):
        """Deposits money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Successfully deposited Rs.{amount:.2f}.")
        self.log_transaction("Deposited", amount)

    def withdraw(self, amount: float):
        """Withdraws money from the account, raising an exception if funds are too low."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            raise InsufficientBalanceError(f"Insufficient funds! Available balance is Rs.{self.balance:.2f}.")
        
        self.balance -= amount
        print(f"Successfully withdrew Rs.{amount:.2f}.")
        self.log_transaction("Withdrew", amount)

    def balance_inquiry(self):
        """Displays the current balance."""
        print(f"\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: Rs.{self.balance:.2f}")



account_numbers = []       
customer_accounts = {}     


while True:
    print("\n=== BANKING MANAGEMENT SYSTEM ===")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Balance Inquiry")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        try:
            acc_num = int(input("\nEnter New Account Number: "))
            if acc_num in account_numbers:
                print("Error: Account number already exists.")
                continue
                
            name = input("Enter Account Holder Name: ")
            initial_dep = float(input("Enter Initial Deposit Amount: "))
            if initial_dep < 0:
                print(" Error: Initial deposit cannot be negative.")
                continue

            account = BankAccount(acc_num, name, initial_dep)
            account_numbers.append(acc_num)
            customer_accounts[acc_num] = account
            print(f" Account successfully created for {name}!")

        except ValueError:
            print("Error: Account number and deposit must be numeric values.")

    elif choice in ['2', '3', '4']:
        try:
            acc_num = int(input("\nEnter Account Number: "))
            if acc_num not in customer_accounts:
                print("Error: Account number not found.")
                continue
            
            account = customer_accounts[acc_num]

            if choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

            elif choice == '3':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except InsufficientBalanceError as e:
                    print(f"Transaction Failed: {e}")

            elif choice == '4':
                account.balance_inquiry()

        except ValueError:
            print("Error: Please enter valid numbers.")

    elif choice == '5':
        print("\nThank you for banking with us. Goodbye!")
        break
        
    else:
        print(" Invalid option! Please select a valid menu choice (1-5).")
