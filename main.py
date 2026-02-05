from account import PersonalAccount

# Создаем счет
acc = PersonalAccount(1, "Koshaliev")

def menu():
    print("\n=== PERSONAL BANK ACCOUNT ===")
    print("1. Посмотреть баланс")
    print("2. Пополнить счет")
    print("3. Снять деньги")
    print("4. История транзакций")
    print("5. Выйти")

while True:
    menu()
    choice = input("Выберите действие (1-5): ")
    
    if choice == "1":
        print(f"Текущий баланс: {acc.get_balance()}")

    elif choice == "2":
        try:
            amount = float(input("Введите сумму для пополнения: "))
            acc.deposit(amount)
            print(f"{amount} успешно внесено.")
        except ValueError:
            print("Введите корректное число.")

    elif choice == "3":
        try:
            amount = float(input("Введите сумму для снятия: "))
            acc.withdraw(amount)
        except ValueError:
            print("Введите корректное число.")

    elif choice == "4":
        print("\nИстория транзакций:")
        acc.print_transaction_history()

    elif choice == "5":
        print("Выход...")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
