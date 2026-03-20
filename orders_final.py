class OrderItem: 
  def __init__(self, item, quantity): #for each item order the item name and quantity have to be stated
    self.item = item
    self.quantity = quantity

  def get_total(self): #returns the base total of the order based on how many of the item was ordered
    return self.item.get_price() * self.quantity

class Order: #outlines the ordering process
  status_descriptions = {"created": ["confirmed"], "confirmed": ["preparing"], "preparing": ["ready"], "ready": ["served"], "served": ["paid"], "paid": []}
  def __init__(self):
    self.items = []
    self.status = "created"

  def add_item(self, item, quantity): #establishes that an order cannot be changed after its creation
    if self.status != "created":
      raise Exception("An order cannot be modified after being created")
    self.items.append(OrderItem(item, quantity))

  def change_status(self, new_status): #calls to change the status of an order, status name must be valid
    if new_status in Order.status_descriptions[self.status]:
      self.status = new_status
      print(f"Order {new_status}")
    else:
      raise Exception("Invalid status")
    
  def confirm_order(self): #each indivual part of the ordering process which may be called on a order
    self.change_status("confirmed")
  def prepare_order(self):
    self.change_status("preparing")
  def ready_order(self):
    self.change_status("ready")
  def serve_order(self):
    self.change_status("served")
  def pay_order(self):
    if self.status != "served":
      raise Exception("Order must be served to pay")
    else:
      self.change_status("paid")

  
  def print_receipt(self, pricing): #prints string outlining a receipt based on the items within an order
    print("\n-------- RECEIPT --------")
    for order_item in self.items:
      name = order_item.item.name
      qty = order_item.quantity
      price = order_item.get_total()
      print(f"{name} x{qty} = ${price:.2f}")
    print("\n-------------------------")
    print(pricing.calculate_total(self.items))
    print("-------------------------")

  def finalize_order(self): # reduces stock for all items in the order after payment
    if self.status != "paid":
      raise Exception("Order must be paid to finalize stock")
    for order_item in self.items:
      item = order_item.item
      if item.stock < order_item.quantity:
        raise Exception(f"Not enough stock for {item.name}")
      item.stock -= order_item.quantity

