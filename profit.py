class Entry:
    def __init__(self, name, cost, price, inventory):
        self.name = name
        self.cost = cost
        self.price = price
        self.inventory = inventory

    def profit (self):
        print(f"{self.name}".upper(), "Profit ($):", (self.price - self.cost) * self.inventory)

    def info(self):
        info = dict()
        info["cost_price"] = self.cost
        info["sale_price"] = self.price
        info["inventory"] = self.inventory
        print(info)

cake = Entry("cake", 5.4, 6, 21)
cake.info()
cake.profit()

mug = Entry("mug", 323, 24546, 3524658)
mug.profit()