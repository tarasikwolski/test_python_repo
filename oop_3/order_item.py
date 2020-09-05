from decimal import Decimal


class OrderItem:
    def __init__(self, name: str, value: int, price: Decimal):
        self.name = name
        self.value = value
        self.price = price
        self.all_price: Decimal = self.value * self.price

    def get_value(self) -> Decimal:
        if not self.is_correct():
            raise ValueError(f"Price can't be equal 0")
        return self.all_price

    def is_correct(self) -> bool:
        return self.all_price > Decimal(0)

    def show(self):
        print(f"{self.name} {self.price} zł. * {self.value} szt. {self.all_price} zł")

    def __str__(self):
        return f"{self.name} {self.price} zł. * {self.value} szt. {self.all_price} zł"


class Order:
    def __init__(self, order_items=None):
        # if order_items:
        #     self.order_items = order_items
        # else:
        #     self.order_items = []
        #
        self.order_items = order_items or []

    def add_item(self, order_item: OrderItem):
        if order_item.is_correct():
            self.order_items.append(order_item)

    def get_order_value(self):
        sum = Decimal(0)
        for item in self.order_items:
            sum += item.get_value()
        return sum

    def get_items_count(self) -> int:
        return len(self.order_items)

    def show(self):
        print("Witamy w Auchan!")
        for item in self.order_items:
            print(item)


def main():
    order_item = OrderItem("cukier", 3, Decimal(5.00))  # dodawanie produktów
    order_item1 = OrderItem("ryż", 5, Decimal(2.50))
    order_item.get_value()
    print(order_item)
    order = Order()  # dodawanie do orderu
    order.add_item(order_item)
    order.add_item(order_item1)
    print(order.get_order_value())
    print(order.get_items_count())
    order.show()


if __name__ == "__main__":
    main()
