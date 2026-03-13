from products import Product
from store import Store

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = Store(product_list)

def start(store: Store):
    while True:
        show_main_menu()
        option = int(input("Please choose a number:"))
        if option == 1:
            display_products(store)
        if option == 2:
            # A bit weird that the demo project doesn't use formatting here like in option 1
            print(f"Total of {store.get_total_quantity()} items in store.")
        if option == 3:
            make_order(store)
        if option == 4:
            False

def display_products(store: Store):
    print("-----")
    for i, product in enumerate(store.get_all_products(), start=1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
    print("-----")

def make_order(store:Store):
    cart = []
    display_products(store)
    print("When you want to finish order, enter empty text.")

    # Keep adding products until empty quantity
    while True:
        product_id = input("Which product # do you want?")
        quantity = input("What amount do you want?")

        # Ordering is done.
        if quantity == "":
            break

        try:
            # Check that the product request wasn't nonsense
            product = product_list[int(product_id) - 1]
        except:
            # Product is nonsesne, but the cart may still be value
            print("Error adding product!")
            break

        cart.append((product, int(quantity)))
        print("Product added to list!\n")

    # Ordering is done
    if cart:
        total = store.order(cart)
        if total > 0:
            print(f"Order made! Total payment: ${total}")

def show_main_menu():
    # I didn't want to do this in a single print call
    print("   Store Menu\n   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

start(best_buy)