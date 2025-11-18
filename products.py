class Product:

    def __init__(self, name, price, quantity):
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)
        self.active = True

    def __str__(self):
        return f"{self.name} (${self.price:.2f} - {self.quantity} in stock)"

    def set_name(self, name):
        if not name:
            raise ValueError("Product name cannot be empty.")
        self.name = name

    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Product price must be a number.")
        if price is None:
            raise ValueError("Product price cannot be None.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.price = price

    def set_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise ValueError("Product quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"Product: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def get_amount_price(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Purchase amount must be an integer.") 
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")

        return self.price * amount

    def buy(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Purchase amount must be an integer.") 
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")

        if self.quantity - amount < 0:
            raise ValueError("Not enough stock to complete the purchase.")

        self.quantity -= amount
        return self.get_amount_price(amount)
