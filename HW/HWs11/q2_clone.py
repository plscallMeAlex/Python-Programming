class StationaryGood(object):
    def price(self,item):
        price = 0 * item
        return price

class Magazine(StationaryGood):
    def price(self,item):
        price = item * 70
        return price

class Book(StationaryGood):
    def price(self, item):
        price = item * 90
        return price

class Ribbon(StationaryGood):
    def price(self, item):
        price = item * 5
        return price
        

basket = {Magazine():3, Book():2, Ribbon():10}

def getTotalCost(basket):
    totalcost = 0
    for item, quantity in basket.items():
        totalcost += item.price(quantity)
    return totalcost


cost = getTotalCost(basket)
print("Total cost: ", cost)