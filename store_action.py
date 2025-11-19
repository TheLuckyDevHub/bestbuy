import products
from store import Store

LINE_DRAW_SIZE = 65


def ini_store() -> Store:
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    return Store(product_list)


def view_products(store: Store) -> None:
    print("")
    print("=" * LINE_DRAW_SIZE)
    print("Available Products:")
    print("=" * LINE_DRAW_SIZE)
    all_products = store.get_all_products()
    postion = 1
    for product in all_products:
        print(
            f"{postion}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
        )
        postion += 1
    print("=" * LINE_DRAW_SIZE)
    print("")
    return all_products


def quit(store) -> None:
    print("")
    print("=" * LINE_DRAW_SIZE)
    print("Thank you for visiting BestBuy. Goodbye!")
    print("=" * LINE_DRAW_SIZE)
    print("")
    exit()


def view_total_amount(store: Store) -> None:
    print("")
    print("=" * LINE_DRAW_SIZE)
    print(f"Total of {store.get_total_quantity()} items in store")
    print("=" * LINE_DRAW_SIZE)
    print("")


def make_order(store: Store) -> None:
    print("")
    print("Make an Order:")
    all_products = view_products(store)
    order_list = []
    while True:
        try:
            print("When you want to finish order, enter = 0")
            product_choice = int(input(
                f"Enter the product number to order (1 to {len(all_products)}): "))
            if product_choice == 0:
                break
            if 1 <= product_choice <= len(all_products):
                selected_product = all_products[product_choice - 1]
                quantity = int(input(
                    f"Enter quantity for {selected_product.name}: "))
                if 0 < quantity <= selected_product.quantity:
                    order_list.append((selected_product, quantity))
                else:
                    print(f"Invalid quantity. Available quantity: {selected_product.quantity}")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if order_list:
        total_price = store.order(order_list)
        print(f"Order made! Total payment: ${total_price:.2f}")
    else:
        print("No items ordered.")

    print("=" * LINE_DRAW_SIZE)
    print("")
