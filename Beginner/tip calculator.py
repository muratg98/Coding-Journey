print("Welcome to the tip calculator")
totalBill = input("What was the total bill? ")
totalPeople = input("How many people to split the bill? ")
tipPercent = input("What percentage tip would you like to give? 10, 12, or 15 ")
#(totalbill * 1.tippercent) / total people
tipvalue = 1 + (float(tipPercent) / 100)

payment = round((float(totalBill) * tipvalue) / int(totalPeople), 2)
print(f"Each person should pay: ${payment}")