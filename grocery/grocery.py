def main():
    grocery_list = {}

    try:
        while True:
            item = input().strip().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        print()

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")

main()


