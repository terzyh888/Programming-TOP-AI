class Product:  # Включает информацию о цене, наличии на складе и категории товара.
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class Customer:  # Управляет информацией о пользователе и его истории заказов.
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
        self.orders = []


class ShoppingCart:  # Позволяет добавлять, удалять и обновлять количество товаров перед оформлением заказа.
    def __init__(self):
        self.products = []  # список товаров в корзине

    def add_product(self, product):
        self.products.append(product)
        print(f"Товар {product.name} добавлен в корзину.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар {product.name} удален из корзины.")

    def update_quantity(self, product, new_stock):
        product.stock = new_stock
        print(f"Количество товара {product.name} изменено на {new_stock}.")


class Order:  # Обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов.
    def __init__(self, customer):
        self.customer = customer
        self.items = customer.cart.products
        self.total_price = self.calculate_total()
        # Добавляем в историю и очищаем корзину
        customer.orders.append(self)
        customer.cart.products = []

    def calculate_total(self):
        subtotal = 0
        for p in self.items:
            subtotal += p.price

        # Простая скидка 5% и налог 10%
        discount = subtotal * 0.05 if subtotal > 100 else 0
        tax = (subtotal - discount) * 0.1
        total = subtotal - discount + tax
        return total


# Проверка работы:
p1 = Product("Телефон", 500, 10, "Электроника")
p2 = Product("Чехол", 20, 30, "Аксессуары")

buyer = Customer("Анна", "anna@mail.com")
buyer.cart.add_product(p1)
buyer.cart.add_product(p2)

my_order = Order(buyer)
print(f"Заказ оформлен! Сумма к оплате: {my_order.total_price} руб.")