import inflect

p = inflect.engine()
names = []  

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()

formatted = p.join(names)
print(f"Adieu, adieu, to {formatted}")
