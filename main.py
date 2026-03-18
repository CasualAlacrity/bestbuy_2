from product import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPricePromotion, ThirdOneFreePromotion, PercentDiscountPromotion
from store import Store

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
                NonStockedProduct("Windows License", price=125),
                LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = SecondHalfPricePromotion("Second Half price!")
third_one_free = ThirdOneFreePromotion("Third One Free!")
thirty_percent = PercentDiscountPromotion("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)


def start(store: Store):
    while True:
        show_main_menu()

        try:
            option = int(input("Please choose a number: "))

        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue

        if option == 1:
            display_products(store)
        elif option == 2:
            # A bit weird that the demo project doesn't use formatting here like in option 1
            print(f"Total of {store.get_total_quantity()} items in store.")
        elif option == 3:
            make_order(store)
        elif option == 4:
            break
        else:
            print("Invalid choice.")


def display_products(store: Store):
    print("-----")
    for i, product in enumerate(store.get_all_products(), start=1):
        print(f"{i}. {product}")
    print("-----")


def make_order(store: Store):
    cart = []
    display_products(store)
    print("When you want to finish order, enter empty text.")

    products = store.get_all_products()

    # Keep adding products until empty quantity
    while True:
        product_id = input("Which product # do you want? ")

        if product_id == "":
            break

        quantity = input("What amount do you want? ")

        # Ordering is done.
        if quantity == "":
            break

        try:
            # Check that the product request wasn't nonsense
            product = products[int(product_id) - 1]
            quantity = int(quantity)
        except (ValueError, IndexError):
            # Product is nonsesne, but the cart may still be value
            print("Error adding product!")
            continue

        cart.append((product, int(quantity)))
        print("Product added to list!\n")

    # Ordering is done
    if cart:
        try:
            total = store.order(cart)
            print(f"Order made! Total payment: ${total}")
        except ValueError as e:
            print(f"Order failed: {e}")


def show_main_menu():
    # I didn't want to do this in a single print call
    print("   Store Menu\n   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


start(best_buy)
