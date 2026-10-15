class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_number = acc_no

    def debit(self):
        dr_am = int(input("Enter the amount you want to debit:"))
        self.balance = self.balance-dr_am
        print(f"Rs.{dr_am} is debited from the acount.")
        print(f"Total Balance=Rs.{self.balance}")

    def credit(self):
        cr_am = int(input("Enter the amount you want to debit:"))
        self.balance = self.balance + cr_am
        print(f"Rs.{cr_am} is credited from the acount.")
        print(f"Total Balance=Rs.{self.balance}")

    def total_balance(self):
        return self.balance


acc1 = Account(10000, 5959)
print(acc1.balance)
print(acc1.account_number)
acc1.debit()
acc1.credit()
