class Discount: #base discount value is zero, although this can be overidden by using methods from otheer classes
    def apply(self, amount):
        return 0
    
class PercentageDiscount(Discount): #allows the value of discount to be changed and applied as a percent to an order
    def __init__(self, percent):
        self.percent = percent
    def apply(self, amount):
        return amount * self.percent
    
class FixedDiscount: #applies a discount for a fixed amount to an order
    def __init__(self, amount):
        self.amount = amount
        
    def apply(self, amount): 
        return min(self.amount, amount)
   
class Pricing: #taxes for food and drink are set to 6% and 8% respectively
    food_tax = 0.06
    drink_tax = 0.08

    def __init__(self, tip_percent = 0):
        self.tip_percent = tip_percent
        self.discounts = []

    def add_discount(self, discount): #allows discount amount to be added
        self.discounts.append(discount)

    def calculate_subtotal(self, items_ordered): #calculates the order's subtotal
        return sum(item.item.get_price() * item.quantity for item in items_ordered)
        
    def apply_tax(self, items_ordered): #appplies tax based on whether an item is within the food category or drink category
        tax = 0
        for order_item in items_ordered:
            item = order_item.item
            qty = order_item.quantity
            if item.category == "food":
                tax += item.get_price() * qty * Pricing.food_tax
            elif item.category == "drink":
                tax += item.get_price() * qty * Pricing.drink_tax
        return tax

    def calculate_discounts(self, subtotal): #uses the subtotal and discount list to find the total discount
        total_discount = 0
        for a_discount in self.discounts:
            total_discount += a_discount.apply(subtotal)
        return total_discount
    def calculate_tip(self, amount): #applies a tip to the order based on its subtotal
        return amount * self.tip_percent

    def calculate_total(self, items_ordered): #calculates and returns the order's full total, now including all discounts, tips, and taxes
        subtotal = self.calculate_subtotal(items_ordered)
        discount = self.calculate_discounts(subtotal)
        after_discount = subtotal - discount
        tax = self.apply_tax(items_ordered)
        tip = self.calculate_tip(after_discount)
        final_total = after_discount + tax + tip
        return f"Calculating order...\nSubtotal: ${subtotal:.2f} \nDiscount: ${discount:.2f} \nTax: ${tax:.2f} \nTip: ${tip:.2f} \n.......... \nTotal: ${final_total:.2f}"
