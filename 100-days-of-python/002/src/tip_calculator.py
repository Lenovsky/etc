def main():
    print("Welcome to the tip calculator.")

    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    split_bill = bill / people * (1 + tip / 100)

    print(f"Each person should pay: ${split_bill:.2f}")


if __name__ == "__main__":
    main()
