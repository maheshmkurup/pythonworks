class Bank:

    accno:int

    balance:int

    acc_type:str

    customer_name:str

    def __init__(self,accno,balance,acc_type,customer_name):

        self.accno=accno

        self.balance=balance

        self.acc_type=acc_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account {self.accno} has been credited with amount {amount} avail balance {self.balance}")

    def withdraw(self,amount):

        if self.balance<amount:

            print("insufficient balance")

        else:

            self.balance-=amount

            print(f"your account {self.accno} has been debited with amount {amount} avail balance {self.balance}")

    def get_balance(self):

        print("your available balance is",self.balance)

customer_instance1=Bank(34754,3000,"savings","Mahesh")

customer_instance1.withdraw(500)

customer_instance1.deposit(1000)

customer_instance1.get_balance()

  


