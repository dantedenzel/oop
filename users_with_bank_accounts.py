class BankAccount:
    all_accounts =[]

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def display_account_info(self):
        print(self.balance)
    
    def yield_interest(self):
        self.balance *= self.int_rate
        return self

    @classmethod
    def accounts(cls):
        for x in cls.all_accounts:
            x.display_account_info()

class User:
    def __init__(self, name, email=""):
        self.name = name
        self.email = email
        self.account = []

    def deposit(self, acct_num, ammount):
        self.account[acct_num].balance += ammount
        return self

    def withdraw(self, acct_num, ammount):
        self.account[acct_num].balance -= ammount
        return self
    
    def create_account(self):
        self.account.append(BankAccount(.02, 0))

    def display_user_balance(self,acct_num):
        print(self.account[acct_num].balance)
    
    def transfer_money(self, acct_num, friend, ammount):
        self.account[acct_num].balance -= ammount
        friend.balance += ammount
        print(f"My balance: {self.balance} Friend's Balance: {friend.balance}")

user1= User("Dante", "danteburnett@gmail.com")
user2= User("Etnad", "ttenrubetnad@gmail.com")


user1.create_account()
user1.create_account()
user1.deposit(0, 3500).deposit(0, 400).display_user_balance(0)
user1.deposit(1,500).display_user_balance(1)