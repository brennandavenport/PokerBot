class Money:
    def __init__(self):
        self.money = 10

    def get_money(self):
        return self.money
    
    def set_money(self, new_money: int):
        self.money = new_money

m = Money()

hm = {
    "arjun" : m.get_money
}

print(hm["arjun"]())

m.set_money(100)

print(hm["arjun"]())