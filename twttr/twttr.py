word=input("Input: ")
vowels="aeiouAEIUO"
output=' '
for c in word:
    if c not in vowels:
        output+=c
print("Output : ",output)
