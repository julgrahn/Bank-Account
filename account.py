class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

jackChecking = Checking("jack.txt", 1)
jackChecking.transfer(100)
print(jackChecking.balance)
jackChecking.commit()
print(jackChecking.type)

johnChecking = Checking("john.txt", 1)
johnChecking.transfer(100)
print(johnChecking.balance)
johnChecking.commit()
print(johnChecking.type)

print(johnChecking.__doc__)