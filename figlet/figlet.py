import sys
import random
from pyfiglet import Figlet

figlet=Figlet()
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:

    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
user=input("Input : ")
print(f"Output : {figlet.renderText(user)}")
