greet = input("Greeting ").strip().lower()
if greet.startswith("hello"):
    print("$0")
elif "how you doing" in greet:
    print("$20")
elif "what's happening" in greet or "what's up" in greet:
    print("$100")
else:
    print("$20")



