class Atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 1000  # Initial balance for demonstration purposes

    def display_menu(self):
        print("1. Cash Withdrawal")
        print("2. Balance Enquiry")
        print("3. Exit")

    def cash_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def balance_enquiry(self):
        print(f"Your current balance is: ${self.balance}")