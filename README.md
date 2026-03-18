# Restaurant-Ordering-Project
## Overview
This program implements elements of Object Oriented Programming to function as a restaurant ordering system. This includes features such as accessing and modifying a menu, inventory, orders, and/or prices. 
This system allows you to:
Manage the restaurant inventory of food and drink items
Create and process orders
Apply taxes, tips, and discounts to items and orders
Generate receipts and display the ordering process



## Module Details
### 1. Inventory
Inventory (Class): 
* Stores menu items based upon IDs
* Features preset menu items
* Displays current menu with item details ex: stock/quantity


### 2. Menu

MenuItem (Base Class):
* Can create menu item objects and display attributes such name, price, category, availability, and stock.

FoodItem / DrinkItem (Subclasses):
* Create menu items categorized as food or drink.

Combo (Subclass):
* Allows for the combination of multiple items and to return details of such ex: price

 
### 3. Ordering

OrderItem (Class):
* Add items (food or drink) with quantities

Order (Class):
* Access and change order status
* created → confirmed → preparing → ready → served → paid
* Calculated total price, tax, tips, and discounts included, and displays receipts


### 4. Pricing

Dicount (Base Class):
* Base discount is set to the value of zero

PercentageDiscount (Subclass):
* Allows for the application a discount based on a percentage

FixedDicount (Class):
* Can override the Discount class and applied a discount of a specified value

Pricing (Class):
* Calculates:
* Subtotal
* Taxes (Preset - food: 6%, drink: 8%)
* Discounts
* Tips

  
### When Using/ Use Details
* Program loads preset menu items, ready to be accessed in orders
* By creating objects from the item classes and calling methods from the Inventory, Pricing, or Order classes, the user can select, create, and process orders
* Will display details called by methods such as a reciept, inventory, etc.
