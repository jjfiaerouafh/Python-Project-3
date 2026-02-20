#MOBILE PHONE DETAILS
class Mobile:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, discount_amount):
        if 0 < discount_amount <= self.price:
            self.price -= discount_amount
            print("Discount applied successfully.")
        else:
            print("Invalid discount amount.")

    def display_mobile(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


# Creating object
mobile1 = Mobile("Samsung", "Galaxy S23", 75000)

# Calling methods
mobile1.display_mobile()
mobile1.apply_discount(5000)
mobile1.display_mobile()