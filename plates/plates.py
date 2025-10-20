def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
   
    if len(s) < 2 or len(s) > 6:
        return False


    if not s[:2].isalpha():
        return False


    if not s.isalnum():
        return False

    number_started = False
    for ch in s:
        if ch.isdigit():
            if not number_started:
                if ch == '0':
                    return False
                number_started = True
        elif number_started:
            return False

    return True

main()

