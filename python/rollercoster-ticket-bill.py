print("Welcome to the Rollercoaster!")
height = int(input("Whats your height in cm? "))
bill=0

if height>=120:
    print("you can go for the ride! and..")
    age= int(input("Whats your age?"))
    if age<12:
        bill=50
        print("That will be rs.50 for the ride")
    elif age<=18:
        bill=100
        print("That will be rs.100 for the ride")
    elif age>=45 and age<=55:
        print("Your ride will be free!")
    else:
        bill=150
        print("That will be rs.150 for the ride")
        
    photo=(input("Would you like to have a photo? yes or no..\n"))
    if photo=="yes":
        bill+=50
        
    print(f"Your total will be rs.{bill}")
else:
    print("Sorry, you have to grow taller to ride this!")
