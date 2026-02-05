from account import PersonalAccount

acc = PersonalAccount(1, "Test User")

acc.deposit(500)
assert acc.get_balance() == 500

acc.withdraw(200)
assert acc.get_balance() == 300

acc.withdraw(500)  # превышает баланс
assert acc.get_balance() == 300

acc + 100
assert acc.get_balance() == 400

acc - 50
assert acc.get_balance() == 350

print("All tests passed!")
