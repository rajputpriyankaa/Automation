from selenium import webdriver
from selenium.webdriver.common.by import By

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def get_total_price(self):
        return sum(product.price for product in self.products)

class Website:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.cart = Cart()

    def add_product_to_cart(self, product_name):
        add_to_cart_button_xpath = f"//a[contains(text(), '{product_name}')]/following-sibling::p/a"
        add_to_cart_button = self.driver.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()
        self.driver.switch_to.alert.accept()  # Handle alert

    def remove_product_from_cart(self, product_name):
        remove_button_xpath = f"//td[contains(text(), '{product_name}')]/following-sibling::td/a"
        remove_button = self.driver.find_element(By.XPATH, remove_button_xpath)
        remove_button.click()

    def verify_total_price(self, expected_total_price):
        total_price_element = self.driver.find_element(By.ID, "totalp")
        actual_total_price = int(total_price_element.text.split()[1])  # Extract numeric value from the text
        if actual_total_price == expected_total_price:
            print("Total price is correct.")
        else:
            print("Total price is incorrect.")

    def close(self):
        self.driver.quit()

# Usage
website = Website()

product1 = Product("Samsung Galaxy S6", 700)
product2 = Product("Nokia Edge", 250)

# Add products to cart
website.add_product_to_cart(product1.name)
website.add_product_to_cart(product2.name)

# Verify total price
website.verify_total_price(product1.price + product2.price)

# Remove a product
website.remove_product_from_cart(product2.name)

# Verify updated total price
website.verify_total_price(product1.price)

website.close()
