class BankAccount:
    all_accounts =[]

    def __init__(self, int_rate, balance) -> None:
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def make_deposit(self, ammount):
        self.balance += ammount
        return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self

    def make_withdraw(self, ammount):
        self.balance -= ammount
        return self

    def display_account_info(self):
        print(self.balance)
    

    @classmethod
    def accounts(cls):
        for x in cls.all_accounts:
            x.display_account_info()

        

acct1 = BankAccount(5, 2000)
acct2 = BankAccount(2, 1500)


acct1.make_deposit(500).make_deposit(600).make_deposit(700).make_withdraw(1477).yield_interest().display_account_info()
acct2.make_deposit(4000).make_deposit(4000).make_withdraw(1477).make_withdraw(1477).yield_interest().display_account_info()

BankAccount.accounts() 