class Product:
    """
    Represents a product with a name, price, and quantity.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        self.set_name(name)
        self.set_price(price)
        self.set_quantity(quantity)

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"{self.name} (${self.price:.2f} - {self.quantity} in stock)"

    def set_name(self, name):
        """
        Sets the name of the product.

        Args:
            name (str): The name of the product.

        Raises:
            ValueError: If the name is empty.
        """
        if not name:
            raise ValueError("Product name cannot be empty.")
        self.name = name

    def set_price(self, price):
        """
        Sets the price of the product.

        Args:
            price (float): The price of the product.

        Raises:
            ValueError: If the price is not a number, is None, or is negative.
        """
        if not isinstance(price, (int, float)):
            raise ValueError("Product price must be a number.")
        if price is None:
            raise ValueError("Product price cannot be None.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        self.price = price

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.

        Args:
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If the quantity is not an integer or is negative.
        """
        if not isinstance(quantity, int):
            raise ValueError("Product quantity must be an integer.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.quantity = quantity
        self.active = quantity > 0


    def get_quantity(self):
        """
        Returns the quantity of the product.
        """
        return self.quantity

    def is_active(self):
        """
        Returns True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Returns a string with the product's details.
        """
        return f"Product: {self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"

    def get_amount_price(self, amount):
        """
        Calculates the price for a given amount of the product.

        Args:
            amount (int): The amount to calculate the price for.

        Returns:
            float: The total price for the given amount.

        Raises:
            ValueError: If the amount is not a positive integer.
        """
        if not isinstance(amount, int):
            raise ValueError("Purchase amount must be an integer.")
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")

        return self.price * amount

    def buy(self, amount):
        """
        Buys a given amount of the product.

        Args:
            amount (int): The amount to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the amount is not a positive
            integer or if there is not enough stock.
        """
        if not isinstance(amount, int):
            raise ValueError("Purchase amount must be an integer.")
        if amount <= 0:
            raise ValueError("Purchase amount must be positive.")

        if self.quantity - amount < 0:
            raise ValueError("Not enough stock to complete the purchase.")

        self.set_quantity(self.quantity - amount)
        return self.get_amount_price(amount)
