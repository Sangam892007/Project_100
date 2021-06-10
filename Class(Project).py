class Atm(object):
    def __init__(self, Balance, DebitCardno):
            self.depicardno = DebitCardno
            self.balance = Balance
            print("Your current balance is " + str(self.balance))

    def depositamount(self):
        amount = input("Please enter the amount to be deposited")
        self.DEpositamount = int(amount)
        self.balance = self.balance + self.DEpositamount
        print("The remaining amount is:" + str(self.balance))

    def withdrawalamount(self):
        amounttaken = input("Please enter the amount to be withdrawed")
        self.WIthdrawalamount = int(amounttaken)
        if self.WIthdrawalamount > self.balance:
            print("Insuffiesient balance")
        else:
            self.balance = self.balance - self.WIthdrawalamount
            print("Your remaining balance is: " + str(self.balance))

CardNumber = Atm(10000, 989634562)

CardNumber.depositamount()
CardNumber.withdrawalamount()

