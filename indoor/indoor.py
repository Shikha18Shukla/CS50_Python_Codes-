def main():
    text=input("say something")
    lowered=""
    for char in text :
        if char.isupper():
            lowered+=char.lower()
        else:
            lowered+=char

    print(lowered)
main()
