class MenuItem:
    def __init__(self, id, name, price, category, available = True, stock = 0): #sets the instance variables for each menu item
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.available = available
        self.stock = stock
        
    def get_price(self): #returns the price of an item
        return self.price
    def item_details(self): #returns a statement of the details of an item such as its id
        return f"Item {self.name} - {self.id}, ${self.price}, Category: {self.category}, Stock: {self.stock}"
    def toggle_availability(self): #allows availability of an item to be switched
        self.available = not self.available
    def adjust_stock(self, quantity): #allows the stock of an item to be updated
        self.stock = quantity
        
class FoodItem(MenuItem): #creates items that are in the food category based on the parent class MenuItem
    def __init__(self, id, name, price, available = True, ):
        super().__init__(id, name, price, "food", available)
        
class DrinkItem(MenuItem): #creates items that are in the drink category based on the parent class MenuItem
    def __init__(self, id, name, price, available = True):
        super().__init__(id, name, price, "drink", available)

class Combo(MenuItem):
    def __init__(self, id, name, items, discount = 0.10): #sets the specific variable for each instance of a combo through the MenuItem parent class
        super().__init__(id, name, 0, "combo", True) #base price initialized as zero but is still changeable
        self.items = items
        self.discount = discount
        
    def get_price(self): #returns the price of a combo item
        discounted_price = sum(item.get_price() for item in self.items)
        return discounted_price * (1-self.discount)
    
    def combo_details(self): #returns the attributes of the combo
        all_items = ", ".join(item.name for item in self.items)
        return f"{self.name} Combo ({all_items}), is ${self.get_price():.2f}"
