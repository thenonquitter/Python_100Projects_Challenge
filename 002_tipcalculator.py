bill = int(input("What was the total bill? ")) #str
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? ")) #str
people = int(input("How many people to split the bill? ")) #str

# print(type(bill), type(tip), type(people))

result = round((bill + bill * (tip / 100)) / people, 2)

print(f"Each person should pay {result}.")