height=float(input("whats your height? "))
weight=float(input("whats your weight? "))
bmi= round(weight/height**2)

if bmi<18.5:
    print(f"Your bmi is {bmi},and that makes u skinny bitch!")
elif bmi<25:
    print(f"Your bmi is {bmi},and I mean its alright..")
elif bmi<30:
    print(f"Your bmi is {bmi},and Damn eat less you pig!")
elif bmi<35:
    print(f"Your bmi is {bmi},and Damn eat less you big fat pig!")
else:
    print(f"Your bmi is {bmi},and Plz dont eat me!you fatso freak!!")