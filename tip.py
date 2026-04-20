def main():
    dollars = float(input("How much was the meal? ").strip("$"))
    percent = float(input("What percentage would you like to tip? ").strip("%"))
    tip = dollars * percent/100
    print(f"Leave ${tip:.2f}")
main()