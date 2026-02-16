'''
1.Write a Python class BankAccount that manages a simple bank account with the following features:
Requirements:
Initialize with account number, holder name, and initial balance (default 0)
Implement deposit(amount) method that adds money (must be positive)
Implement withdraw(amount) method that removes money (check sufficient balance)
Implement get_balance() method to return current balance
Implement transfer(amount, target_account) to transfer money to another account
Maintain transaction history (list of all transactions with type, amount, and timestamp)
Implement __str__() for readable representation
'''

from datetime import datetime
# for timestamp

class BankAccount():
    def __init__(self, acc_num, holder_name, balance=0):
        self.acc_num = acc_num
        self.holder_name = holder_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount < 0:
            return 'INVALID AMOUNT'
        self.balance += amount
        # Transaction history
        self.transaction_history.append({'Type':'Deposite', 'Amount':amount, 'Time':datetime.now()})

    def withdraw(self, amount):
        if amount <= 0:
            return 'INVALID AMOUNT'
        if amount > self.balance:
            return 'INSUFFICIENT BALANCE'
        self.balance -= amount
        # Transaction history
        self.transaction_history.append({'Type':'Withdraw', 'Amount':amount, 'Time':datetime.now()})

    def get_balance(self):
        return self.balance

    def transfer(self, amount, dst_acc):
        if amount <= 0:
            return 'INVALID AMOUNT'
        if amount > self.balance:
            return 'INSUFFFICIENT BALANCE'
        self.balance -= amount
        dst_acc.balance += amount
        # Transaction history
        self.transaction_history.append({'Type':'Transfer_OUT', 'Amount':amount, 'Time':datetime.now()})
        dst_acc.transaction_history.append({'Type':'Transfer_IN', 'Amount':amount, 'Time':datetime.now()})




    def __str__(self):
        return (f'ACC_NO : {self.acc_num} \nHOLDER_NAME : {self.holder_name}\nBALANCE : {self.balance} \n')


a1 = BankAccount(1410, 'Raj', 4535)
a2 = BankAccount(1510, 'Manoj', 2450)
a3 = BankAccount(1610, 'Akash', 1000)
print('Initial Balance')
print(a1)
print(a2)
print(a3)

print('\nDeposite')
a1.deposit(500)
a2.deposit(700)
print(a1)
print(a2)

print('\nTransfer')
a1.transfer(800, a2)
a2.transfer(1500, a3)
a3.transfer(845, a1)
print(a1)
print(a2)
print(a3)

print('\nWithdraw')
a1.withdraw(200)
a2.withdraw(600)
a3.withdraw(550)
print(a1)
print(a2)
print(a3)

print()
print(a1.__str__())
print(a2.__str__())
print(a3.__str__())

print('\nTRANSACTION HISTORY:')
print('USER : RAJ')
for tr in a1.transaction_history:
    print(f"{tr['Type']} | {tr['Amount']} | {tr['Time']} ")
print('\nUSER : Manoj')
for tr in a1.transaction_history:
    print(f"{tr['Type']} | {tr['Amount']} | {tr['Time']} ")
print('\nUSER : Akash')
for tr in a1.transaction_history:
    print(f"{tr['Type']} | {tr['Amount']} | {tr['Time']} ")

print()
print()
a4 = BankAccount(1111, 'Sam')
print(a4)
print()
print('\nINVALID CASES')
print(a4.deposit(-1000))
print(a3.withdraw(-200))
print(a2.withdraw(500000))
print(a1.transfer(20000, a3))
print(a3.transfer(-250, a2))

print('\nGET BALANCE')
print(a1.get_balance())
print(a2.get_balance())
print(a3.get_balance())
print(a4.get_balance())


