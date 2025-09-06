class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def send_order(self):
        print("Order sent")

    def receive_order(self):
        print("Order received")


class Order:
    def __init__(self, date, number):
        self.date = date
        self.number = number

    def confirm(self):
        print("Order confirmed")

    def close(self):
        print("Order closed")


class SpecialOrder(Order):
    def __init__(self, date, number, private_client):
        super().__init__(date, number)
        self.private_client = private_client

    def confirm(self):
        print("Special order confirmed")

    def close(self):
        print("Special order closed")

    def dispatch(self):
        print("Special order dispatched")


class NormalOrder(Order):
    def confirm(self):
        print("Normal order confirmed")

    def close(self):
        print("Normal order closed")

    def dispatch(self):
        print("Normal order dispatched")

    def receive(self):
        print("Normal order received")