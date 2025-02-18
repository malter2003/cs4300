# discount is a number representing percentage, so 50 would be interpreted as 50%
def calculate_discount(price, discount):
    return price * (1 - discount / 100)