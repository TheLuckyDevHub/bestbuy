# BestBuy Store

A simple command-line interface (CLI) application for managing a store.

## Features

*   List all products in the store.
*   Show the total amount of all products in the store.
*   Make an order.
*   Quit the application.

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone .
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd BestBuy
    ```
3.  **Install the dependencies:**
    
    This project has no external dependencies.
    
4.  **Run the application:**
    ```bash
    python main.py
    ```

## Project Structure

```
.
├── .gitignore
├── main.py
├── products.py
├── requirements.txt
├── store_action.py
└── store.py
```

*   `main.py`: The entry point of the application. It contains the main loop and the menu.
*   `products.py`: Contains the `Product` class.
*   `store.py`: Contains the `Store` class.
*   `store_action.py`: Contains the functions that implement the store features.
*   `requirements.txt`: A list of the Python packages that the project depends on.
