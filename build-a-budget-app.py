class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = f"{entry['description'][:23]:23}"
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    spendings = []
    for cat in categories:
        spent = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spendings.append(spent)

    total_spent = sum(spendings)
    percentages = [int((s / total_spent) * 100 // 10) * 10 for s in spendings]

    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [cat.name for cat in categories]
    max_len = max(len(n) for n in names)

    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res

# --- TEST SUITE ---
if __name__ == "__main__":
    # Test 1-6: Basic Ledger Operations
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    
    # Test 7-11: Transfers
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55, "new shirt")
    
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15, "gas")

    print("--- CATEGORY PRINT TEST ---")
    print(food)
    
    print("\n--- SPEND CHART TEST ---")
    print(create_spend_chart([food, clothing, auto]))


