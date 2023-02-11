print("Welcome to the tip calculator!")
bill=input("Whats the total bill? rs.")
tip= input("What percentage tip would you like to give? say 10,12, or 15..\n")
split=input("how many people will be splitting the Bill? ")
total=round(((float(bill)*int(tip))/100)+float(bill)/int(split))
print((f"Each person should pay: rs.{total}"))
 