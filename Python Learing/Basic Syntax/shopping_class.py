class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        self.total = 0

    def getTotalItem(self):
        print(f'Total Items: {len(self.cart)}')

    def addToCar(self, item, quantity, price):
        alreadyAdded = False
        for cartItem in self.cart:
            if cartItem['item'] == item:
                alreadyAdded = True
            
        if alreadyAdded:
            print(f'{item} already added in cart')
            return

        product = {'item':item, 'quantity': quantity, 'price':price}
        self.cart.append(product)
        self.total += (price*quantity)
        print(f'Item {item} added to cart succesfully')

    def removeFromCart(self, item):
        notAdded = True
        for cartItem in self.cart:
            if cartItem['item'] == item:
                notAdded = False
        if notAdded:
            print(f'{item} not added to cart')
            return
        
        newCart = []
        for cartItem in self.cart:
            if cartItem['item'] != item:
                newCart.append(cartItem)

        self.cart = newCart
        print(f'{item} removed from the cart')


    def checkOut(self, amount):
        if self.total > amount:
            print(f'You need {self.total - amount} more to proceed')
            return
        print(f'Total Bill: {self.total}')
        print(f'Congratualtions! Here is your change {amount - self.total}')


someone = Shopping("Someone")
someone.addToCar("Brush", 2, 80)
someone.addToCar("Pen", 2, 10)
someone.addToCar("Paper", 20, 8)
someone.addToCar("Brush", 2, 80)

someone.getTotalItem()
someone.removeFromCart('Pen')
someone.removeFromCart('PenX')
someone.checkOut(59)