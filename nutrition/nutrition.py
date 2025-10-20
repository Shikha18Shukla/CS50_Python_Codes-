def main():
    fruit=input("Item : ").strip().title()
    fruits={"Apple" :130 , "Banana":110 , "Sweet Cherries":100 , "Pear": 100, "Avocado":50 , "Kiwifruit":90 , "Lemon":15}
    if fruit  in fruits :
        print(f"Calories : {fruits[fruit]}")

main()
