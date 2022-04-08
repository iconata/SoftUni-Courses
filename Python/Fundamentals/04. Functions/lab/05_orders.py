def order_calculator(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "water":
        return quantity * 1
    elif product == "coke":
        return quantity * 1.4
    elif product == "snacks":
        return quantity * 2


curr_product = input()
curr_quantity = int(input())
print(f"{order_calculator(curr_product, curr_quantity):.2f}")
