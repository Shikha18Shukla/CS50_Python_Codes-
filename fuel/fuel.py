def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")

            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage >= 99:
                print("F")
            elif percentage <= 1:
                print("E")
            else:
                print(f"{percentage}%")
            break

        except (ValueError, ZeroDivisionError):
            pass  # continue prompting

if __name__ == "__main__":
    main()

