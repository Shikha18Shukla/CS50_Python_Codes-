months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            # Case 2: Format like "September 8, 1636"
            elif "," in date:
                month_name, rest = date.split(" ", 1)
                day, year = rest.replace(",", "").split()
                month = months.index(month_name) + 1
                day = int(day)
                year = int(year)

            else:
                raise ValueError
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        except (ValueError, IndexError):
            continue

main()

