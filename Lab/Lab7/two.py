class BankAccount(object):
    def __init__(self, bank_name, owner_name, account_number, current_balance):
        self.bank_name = bank_name
        self.owner_name = owner_name
        self.account_number = account_number
        self.current_balance = current_balance
    def deposit(self, many):
        many = abs(many)
        self.current_balance += many
    def withdraw(self, minu):
        if self.current_balance - minu < 0:
            print("Not have money enough to withdraw")
        else:
            self.current_balance -= minu
    def new_balance(self):
        print(f"Current Balance: {self.current_balance}")

bac = BankAccount("SDBank", "DDD", 2323344, 45455)
bac.deposit(5)
bac.withdraw(20)
bac.new_balance()
