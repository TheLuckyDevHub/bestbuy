import store_action
from store import Store


def get_menu_choice(max_id: int) -> int:
    """
    Prompts the user for a menu choice and validates the input.

    Args:
        max_id: The maximum valid menu choice.

    Returns:
        The user's validated choice as an integer.
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= max_id:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_id}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def start(store: Store):
    """
    Displays the store menu, gets the user's choice, and executes the corresponding action.
    """
    print()
    print('Store Menu')
    print('----------')
    
    menu_options = [
        ("List all products in store", store_action.view_products),
        ("Show total amount in store", store_action.view_total_amount),
        ("Make an order", store_action.make_order),
        ("Quit", store_action.quit),
    ]

    for i, (text, _) in enumerate(menu_options, 1):
        print(f"{i}. {text}")

    choice = get_menu_choice(len(menu_options))
    menu_options[choice - 1][1](store)


def main():
    """
    Initializes the store and runs the main application loop.
    """
    print()
    print('Welcome to BestBuy!')
    print('='*store_action.LINE_DRAW_SIZE)
    store = store_action.ini_store()
    while True:
        start(store)


if __name__ == "__main__":
    main()
