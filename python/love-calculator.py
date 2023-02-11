print("Welcome to the LOVE Calculator❤️")
name1 = input("What is your name?")
name2 = input("what is their name?")

combineNames= name1+name2
lowerCase_n1=combineNames.lower()

t = lowerCase_n1.count("t")
r = lowerCase_n1.count("r")
u = lowerCase_n1.count("u")
e = lowerCase_n1.count("e")
true = t+r+u+e

l = lowerCase_n1.count("l")
o = lowerCase_n1.count("o")
v = lowerCase_n1.count("v")
e = lowerCase_n1.count("e")
love = l+o+v+e

love_score = int(str(true)+str(love))

if love_score<=10 or love_score>=90:
    print(f"YOur score is {love_score}, you go together like coke and mentos!!")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")