from products import Product


class Store:
    """
    Represents a store that manages a collection of products.
    """

    def __init__(self, products: list):
        """
        Initializes the store with a list of products.

        Args:
            products (list): A list of Product objects.

        Raises:
            ValueError: If products is not a list or if any item in the list
                        is not an instance of the Product class.
        """
        self.name = 'Best buy store'

        if not isinstance(products, list):
            raise ValueError("Products must be provided as a list.")
        if not all(isinstance(p, Product) for p in products):
            raise ValueError(
                "All items in products list must be Product instances.")

        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): The Product object to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product (Product): The Product object to remove.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        """
        Returns a list of all active products in the store.

        Returns:
            list: A list of active Product objects.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Processes an order for a list of products.

        Args:
            shopping_list (list[tuple[Product, int]]): A list of tuples,
                where each tuple contains a Product object and the
                quantity to order.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If a product in the shopping list is not found in the
                        store or if the requested quantity is not available.
        """
        total_cost = 0.0

        for product, amount in shopping_list:
            product_in_store = next(
                (p for p in self.products if p.name == product.name), None)
            if product_in_store is None:
                raise ValueError(
                    f"Product '{product.name}' not found in store.")
            if amount > product_in_store.get_quantity():
                raise ValueError(
                    f"Not enough quantity for product '{product.name}'.")

            total_cost += product_in_store.buy(amount)

        return total_cost
