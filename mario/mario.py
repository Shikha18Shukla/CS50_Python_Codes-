def main():
    height=int(input("Enter the height of pyramid :"))
    pyramid(height)
def pyramid(n):
    for i in range(n):
        print("#" * (i+1))
if __name__=="__main__":
    main()
