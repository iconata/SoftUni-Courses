total_price = 0

while True:
    order = input()
    if order == "special" or order == "regular":
        break
    if float(order) < 0:
        print("Invalid price!")
    else:
        total_price += float(order)

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.20
    final_price = taxes + total_price
    if order == "special":
        final_price *= 0.90

    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {total_price:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {final_price:.2f}$''')
