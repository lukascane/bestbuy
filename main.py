class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        print(product_info)
        return product_info

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception(f"Product '{self.name}' is not active.")
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")
        if quantity > self.quantity:
            raise Exception(f"Not enough quantity available. Requested: {quantity}, Available: {self.quantity}")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
