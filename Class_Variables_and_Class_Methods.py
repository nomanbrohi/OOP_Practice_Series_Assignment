class Bank():
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

acc1 = Bank()
acc2 = Bank()

print("Before Changing:")
print(f"acc1 = {acc1.bank_name}")
print(f"acc1 = {acc1.bank_name}")

Bank.change_bank_name("State Bank")

print("\nAfter Changing:")
print(f"acc1 = {acc1.bank_name}")
print(f"acc1 = {acc1.bank_name}")