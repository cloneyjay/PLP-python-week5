from Activity1 import BankAccount, SavingsAccount, createAccount

def display_menu():
    print("\n=== Banking System Menu ===")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    return input("Enter your choice (1-5): ")

def main():
    accounts = {}  # Dictionary to store accounts with account number as key
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            account = createAccount()
            if isinstance(account, (BankAccount, SavingsAccount)):
                accounts[account.AccountNumber] = account
        
        elif choice == "2":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to deposit: "))
                result = accounts[acc_num].deposit(amount)
                print(result)
            else:
                print("Account not found!")
        
        elif choice == "3":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                amount = float(input("Enter amount to withdraw: "))
                result = accounts[acc_num].withdraw(amount)
                print(result)
            else:
                print("Account not found!")
        
        elif choice == "4":
            acc_num = input("Enter account number: ")
            if acc_num in accounts:
                print(f"Current Balance: ${accounts[acc_num].Balance:.2f}")
            else:
                print("Account not found!")
        
        elif choice == "5":
            print("Thank you for using our banking system!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()