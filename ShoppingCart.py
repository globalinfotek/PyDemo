
 
#Created on October 27 2018
#This Implements a simple ShoppingCart Class with
#adding Items, applying discounts on items when applied
#@Author Krishna V Chaganti
class ShoppingCart:
    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def discount(self, item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount

    def itemPrice(self, item, price):
        self.prices[item] = price

    def item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def getTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.itemTotal(item, cnt)
        return total

    def itemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.itemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def itemDiscountedTotal(self, item, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total

    def readPricesFile(self, filename):
        with open(filename) as inFile:
            for line in inFile:
                tokens = line.split()
                self.itemPrice(tokens[0], int(tokens[1]))


