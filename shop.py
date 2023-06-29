class FundsError(Exception):
    pass


shop = {
    "book": 12.99,
    "bracelet": 109.99,
    "jeans": 29.99,
    "cat toy": 2.99
}
customer_money = 100


def purchase(item, customer_money):
    if customer_money >= shop.get(item):
        return True
    else:
        return False


def goodbye(item):
    print(f"Here's your {item}! Goodbye.\n")


def funds_issue(item, customer_money, attempts=1):
    if attempts == 3:
        raise FundsError(
            "Payment attempts exceeded (3). Please exit the shop.")

    choice = input(
        "Sorry, your payment did not work. Do you have more money? (y/n): ")
    if choice == "y":
        try:
            additional_money = float(input("How much more money? "))
            customer_money += additional_money
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid amount.")

        if purchase(item, customer_money):
            goodbye(item)
        else:
            attempts += 1
            funds_issue(item, customer_money, attempts)
    else:
        raise FundsError(
            "Payment attempts exceeded (3). Please exit the shop.")


def greeting():
    print("Welcome to the shop!\nWe have these items available:")
    for item in shop:
        print(f"{item}: £{shop.get(item)}")

    prompt = input("\nWhat would you like to purchase? Or 'exit' to leave: ")
    if prompt == 'exit':
        print("Thanks for coming to our shop!")
    elif prompt in shop.keys():
        try:
            if purchase(prompt, customer_money):
                goodbye(prompt)
            else:
                funds_issue(prompt, customer_money)
        except FundsError as error:
            print(error)
    else:
        raise ValueError("Sorry, this item is not in our shop.")


greeting()
