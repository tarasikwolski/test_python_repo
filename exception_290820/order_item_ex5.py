class OrderItemError(ValueError):
    pass


class OrderItem:
    def is_correct(self):
        raise OrderItemError("Zamówienie niepoprawne")


def main():
    order_item = OrderItem()
    try:
        order_item.is_correct()
    except (OrderItemError, Exception) as oie:
        print(f'Złapany mój błąd {oie.args}')


if __name__ == "__main__":
    main()
