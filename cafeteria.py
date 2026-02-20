#Week_1 variant 9

class MealCard:
    cafeteria_name = "Campus Cafe"
    min_balance = 5
    total_cards = 0
    def __init__(self, student, balance=0,transactions=None):
        self.student = student
        self.balance = balance
        if transactions is None:
            self.transactions = []
        else :
            self.transactions = transactions
        MealCard.total_cards += 1
    def deposit(self, amount):
        if amount>0:
            self.balance += amount 
            self.transactions.append(f"+{amount}")
            print(f"Deposited {amount}. Balance: {self.balance}")
    def purchase(self,amount):
        if self.balance - amount >= MealCard.min_balance :
            self.balance -= amount
            self.transactions.append(f"-{amount}")
            print(f"Purchased meal for {amount}. Balance: {self.balance}")
        else:
            print("Insufficient balance for purchase")
    def display_card(self):
        print(f"Student: {self.student}, Balance: {self.balance}, Cafeteria: {MealCard.cafeteria_name}")
    
    def show_transactions(self):
        for i in self.transactions:
            print(i)



card_1 = MealCard("Malika" , 15)
card_1.display_card()
card_1.deposit(30)
card_1.purchase(12)
card_1.purchase(10)
card_1.show_transactions()

print(f"Total cards: {MealCard.total_cards}")



