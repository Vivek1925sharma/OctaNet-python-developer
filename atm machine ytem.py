class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"  # default PIN, you can change it

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit Successful! Your new balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal Successful! Your new balance is ${self.balance:.2f}")

    def check_balance(self):
        print(f"Your current balance is ${self.balance:.2f}")

def main():
    atm = ATM(1000)  # create an ATM object with an initial balance of $1000

    while True:
        print("Welcome to the ATM!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            print("Ram Ram!")
            break
        else:
            print("Invalid choice. Please try again.")

        pin = input("Enter your PIN to continue: ")
        if not atm.check_pin(pin):
            print("Invalid PIN. Please try again.")
            continue

if __name__ == "__main__":
    main()