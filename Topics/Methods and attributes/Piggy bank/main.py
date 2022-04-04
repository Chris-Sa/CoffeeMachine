class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):

        money = self.dollars + self.cents / 100
        deposit = deposit_dollars + deposit_cents / 100

        total = money + deposit
        # print(total)
        self.dollars = int(total)
        self.cents = int(round((total - self.dollars) * 100, 0))


# my_bank = PiggyBank(1, 1)
#
# my_bank.add_money(500, 500)
#
# print(my_bank.dollars, my_bank.cents)