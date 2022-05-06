class atm(object):
    def __init__(self, pin, check_balance, cardnumber):
        self.pin = pin
        self.check_balance = check_balance
        self.cardnumber = cardnumber
    def balance(self):
        print("Your balance is" )

    def newpin(self):
        print("Your pin is", pin)

machine = atm("123", "$1,568", "7764")
print(machine.balance())
    

