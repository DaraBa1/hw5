money = float(input("Введіть суму грошей (грн): "))
price = float(input("Введіть ціну товару (грн): "))

if money >= price:
    change = money - price
    print(f"Вистачає, решта {change} грн")
else:
    lack = price - money
    print(f"Не вистачає {lack} грн")