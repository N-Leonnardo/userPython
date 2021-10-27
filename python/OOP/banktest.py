class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 100

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        (other_user).account_balance += amount
        print (str(amount))
        
guido = User("Guidim Silva", "mcleocrel@gmail.com")

guida = User("Guidinha Silva", "meucanalleo@gmail.com")

guido.display_user_balance()
guido.transfer_money(guida,50)
guida.display_user_balance()