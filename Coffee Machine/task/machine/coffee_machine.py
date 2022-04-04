
class CoffeeMachine:

    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    state = "main_menu"
    order = ""

    def __init__(self):

        self.menu()
        self.interface()

    def interface(self):

        command = input()
        self.process(command)

    def menu(self):

        if self.state == "main_menu":
            print("Write action (buy, fill, take, remaining, exit):")
            self.interface()
        elif self.state == "product_menu":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.interface()

    def process(self, command):

        if self.state == "main_menu":
            if command == "buy":
                self.buy()
            elif command == "fill":
                self.fill()
            elif command == "take":
                self.take()
            elif command == "remaining":
                self.remaining()
            elif command == "exit":
                exit()

        elif self.state == "product_menu":
            self.order = command
        elif self.state == "filling":
            self.order = command

    def buy(self):

        # water, milk, beans, cups dollars
        espresso = [250, 0, 16, 1, 4]
        latte = [350, 75, 20, 1, 7]
        cappuccino = [200, 100, 12, 1, 6]

        self.state = "product_menu"
        self.menu()
        drink_order = self.order
        drink = ""
        resources = ""

        if drink_order == "1":
            resources = self.check_resource(espresso)
            drink = espresso
        elif drink_order == "2":
            resources = self.check_resource(latte)
            drink = latte
        elif drink_order == "3":
            resources = self.check_resource(cappuccino)
            drink = cappuccino
        elif drink_order == "back":
            self.state = "main_menu"
            self.menu()

        if resources == "none":
            print("I have enough resources, making you a coffee!")
            self.make_coffee(drink)
            self.state = "main_menu"
            self.menu()
        else:
            print("Sorry, not enough {}!".format(resources))
            self.state = "main_menu"
            self.menu()

    def check_resource(self, required):

        out_of = "none"

        if required[0] > self.water:
            out_of = "water"

        if required[1] > self.milk:
            out_of = "milk"

        if required[2] > self.beans:
            out_of = "coffee beans"

        if required[3] > self.cups:
            out_of = "disposable cups"

        return out_of

    def make_coffee(self, ingredients):

        self.water -= ingredients[0]
        self.milk -= ingredients[1]
        self.beans -= ingredients[2]
        self.cups -= ingredients[3]
        self.money += ingredients[4]

    def fill(self):

        self.state = "filling"

        print("Write how many ml of water you want to add:")
        self.interface()
        self.water += int(self.order)
        print("Write how many ml of milk you want to add:")
        self.interface()
        self.milk += int(self.order)
        print("Write how many grams of coffee beans you want to add:")
        self.interface()
        self.beans += int(self.order)
        print("Write how many disposable coffee cups you want to add:")
        self.interface()
        self.cups += int(self.order)

        self.order = ""
        self.state = "main_menu"
        self.menu()

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0
        self.state = "main_menu"
        self.menu()

    def remaining(self):

        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("${} of money".format(self.money))

        self.menu()

my_machine = CoffeeMachine()
