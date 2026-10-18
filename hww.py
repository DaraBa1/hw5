secret_number = 67
guess = 0
attempts = 0  # Створюємо лічильник спроб, починаємо з 0

while guess != secret_number:
    guess = int(input("Вгадай число від 1 до 100: "))
    attempts += 1  # Додаємо 1 до лічильника при кожній спробі
    
    if guess > secret_number:
        print("Менше!")
    elif guess < secret_number:
        print("Більше!")
    else:
        # Виводимо загальну кількість спроб разом із вітанням
        print(f"Вгадав! Кількість спроб: {attempts}")