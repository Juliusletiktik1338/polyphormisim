class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"


# Inherited class to demonstrate polymorphism
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def call(self, number):
        return f"Calling {number} from {self.model} smartwatch..."

    def track_steps(self, steps):
        return f"{self.model} tracked {steps} steps today!"

    def __str__(self):
        return f"{self.brand} {self.model} Smartwatch - ${self.price}, Battery Life: {self.battery_life} hours"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, 48)

    print(phone)
    print(phone.call("123-456-7890"))
    print(phone.send_message("123-456-7890", "Hello!"))

    print(watch)
    print(watch.call("987-654-3210"))
    print(watch.track_steps(5000))