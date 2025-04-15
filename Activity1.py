import random

used_accounts = set()
class BankAccount():
    def __init__(self):
        self.Owner = None
        self.Balance = 0.0
        self.AccountNumber = self.generate_account_number()

    def generate_account_number(self):
        while True:
            number = ''.join(str(random.randint(0,9)) for _ in range(10))
            if number not in used_accounts:
                used_accounts.add(number)
                return number

    def deposit(self, amount):
        if(amount <= 0):
            return "invalid amount"
        if(amount > 200000):
            return "amount exceeds daily limit"
        
        self.Balance += amount
        return "deposit successful"

    def withdraw(self, amount):
        if(amount <= 0):
            return "invalid amount"
        if(amount > 200000):
            return "amount exceeds daily limit"
        if(amount > self.Balance):
            return "insufficient funds"
        
        self.Balance -= amount
        return "withdrawal successful"


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.InterestRate = 3.5  # 3.5% interest rate

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > 2000000:
            return "Amount exceeds the Daily limit"
        
        interest_amt = amount * (self.InterestRate / 100)
        self.Balance += amount + interest_amt
        return "Deposit successful"


def createAccount():
    owner_name = input("Please input your name: ")
    account_type = input("Enter account type (1 for Regular, 2 for Savings): ")
    
    if account_type == "1":
        account = BankAccount()
    elif account_type == "2":
        account = SavingsAccount()
    else:
        return "Invalid account type selected"
    
    account.Owner = owner_name
    print(f"Account created successfully!")
    print(f"Account Number: {account.AccountNumber}")
    print(f"Owner: {account.Owner}")
    print(f"Current Balance: ${account.Balance:.2f}")
    
    return account

# Example usage
if __name__ == "__main__":
    account = createAccount()
