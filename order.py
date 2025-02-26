class Order:
    def __init__(self):
        self._items = []

    def add_product(self, name, price, quantity):
        self._items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self._items)

    def checkout(self):
        total = self.calculate_total()
        print("Чек:")
        for item in self._items:
            print(f"{item['name']} - {item['price']} x {item['quantity']}")
        print(f"Итог: {total}")


if __name__ == '__main__':
    order = Order()
    order.add_product("Apple", 50, 3)
    order.add_product("Banana", 30, 2)
    order.checkout()

