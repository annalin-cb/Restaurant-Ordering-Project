class Inventory:
  def __init__(self): #tracks each item already set to the menu and newly added items
    self.menu_items = {}
    self.next_id = 1 #tracks each items id

def add_item(self, item): #adds an item to the menu
  self.menu_items[item.id] = item
  
def preset_items(self):
  from menu_final import FoodItem, DrinkItem #using these methods from the MenuItem class, preset menu items are created
  self.add_item(FoodItem(self.next_id, "Alfredo Pasta", 9.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Mozzarella Sticks", 4.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Chicken Soup", 5.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Side of Calamari", 6.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Side of Shrimp", 6.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Lasagna", 9.99, "food", True))
  self.next_id += 1
  self.add_item(FoodItem(self.next_id, "Alfredo Pasta", 9.99, "food", True))
  self.next_id += 1
  self.add_item(DrinkItem(self.next_id, "Choice Soda", 3.99, "drink", True))
  self.next_id += 1
  self.add_item(DrinkItem(self.next_id, "Iced Tea", 2.99, "drink", True))
  self.next_id += 1
  self.add_item(DrinkItem(self.next_id, "Choice Lemonade", 2.99, "drink", True))
  self.next_id += 1
  self.add_item(DrinkItem(self.next_id, "Hot Coffee", 3.99, "drink", True))
  self.next_id += 1
  self.add_item(DrinkItem(self.next_id, "Water", 1.99, "drink", True))
  self.next_id += 1

def current_inventory(self): #displays the current inventory with each items specific details
  for item in self.menu_items.values():
    print(f"{item.id}: {item.name}, ${item.get_price()}, {item.category}")
