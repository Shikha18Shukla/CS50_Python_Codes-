import emoji

def main():
    user=input("Input : ")
    convert=emoji.emojize(user,language="alias")
    print(f"Output : {convert}")
if __name__=="__main__":
    main()

