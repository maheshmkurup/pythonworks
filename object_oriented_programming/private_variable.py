class BankAccount:

    def __init__(self,customer_name,mpin,account_type,balance):

        self.customer_name=customer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance

    def get_balance(self):

        print(self.__balance)

    def __str__(self):

        return self.customer_name
    
bank_account_instance=BankAccount("Hari",4376,"savings",4000)

print(bank_account_instance.mpin)  #=> mpin cannot be accessed because it is set to private

