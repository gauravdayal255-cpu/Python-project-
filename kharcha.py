# खर्चे का हिसाब: हर खर्चा kharcha.txt में जुड़ता है और आखिर में कुल दिखता है
total = 0

while True:
    item = input("किस चीज़ पर खर्च हुआ (रुकने के लिए q) : ")
    if item == "q":
        break
    amount = float(input("कितना रुपया : "))
    total = total + amount

    with open("kharcha.txt", "a") as file:
        file.write(item + " - " + str(amount) + "\n")

print("आज का कुल खर्चा :", total)
