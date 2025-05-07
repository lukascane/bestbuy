from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n==== Welcome to Best Buy ====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print("\nAvailable Products:")
            for i, product in enumerate(store.get_all_products(), start=1):
                print(f"{i}. {product.show()}")

        elif choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal quantity in store: {total}")

        elif choice == "3":
            products = store.get_all_products()
            shopping_list = []

            print("\nMake an order:")
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.show()}")

            while True:
                try:
                    prod_num = int(input("\nEnter product number to buy (0 to stop): "))
                    if prod_num == 0:
                        break
                    if not 1 <= prod_num <= len(products):
                        print("Invalid product number. Try again.")
                        continue

                    quantity = int(input("Enter quantity: "))
                    selected_product = products[prod_num - 1]
                    shopping_list.append((selected_product, quantity))
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            try:
                total_price = store.order(shopping_list)
                print(f"\nOrder placed! Total cost: ${total_price}")
            except Exception as e:
                print(f"Error placing order: {e}")

        elif choice == "4":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please select from the menu.")


def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
