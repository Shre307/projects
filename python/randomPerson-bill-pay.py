import random
name_string= input("Give me everyone's names, separated by a comma.\n")
names = name_string.split(", ")

num_items=len(names)
random_choice=random.randint(0,num_items-1)
bill_payer=names[random_choice]

print(f"{bill_payer} will be paying for today's meal!")