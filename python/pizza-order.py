print("YO, Welcome to the Pizzaaa Hut!")
size= input("What size pizza do you want? S, M, or L \n")
pepperoni= input("Do you want pepperoni? Y or N \n")
cheese = input("Do you any extra cheese? Y or N \n")

bill=0
if size=="s":
    bill+=100
elif size=="m":
    bill+=150
else:
    bill+=200
if pepperoni=="y":
    if size=="s":
        bill+=20
    else:
        bill+=30
if cheese=="y":
    bill+=20
    
print(f"Your total bill will be rs.{bill}")