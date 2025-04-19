class NumberStringMultiplier:
    def __init__(self, number_string):
        self.number_string = number_string

    def getProduct(self):
        try:
            numbers = [int(num.strip()) for num in self.number_string.split(",")]
            product = 1
            for num in numbers:
                product *= num
            return product
        except ValueError:
            raise ValueError("Not valid string. Must contains int numbers separated from comma and spaces.")