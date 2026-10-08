# नंबर गेस गेम: 1 से 100 के बीच का नंबर, सिर्फ़ 7 कोशिश
import random

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("1 से 100 के बीच अंदाज़ा लगाओ : "))
    tries = tries + 1

    if guess == number:
        print("सही! तुमने", tries, "बार में पकड़ लिया")
        break
    elif guess < number:
        print("थोड़ा बड़ा नंबर बोलो")
    else:
        print("थोड़ा छोटा नंबर बोलो")

    if tries == 7:
        print("हार गए! सही नंबर था", number)
        break
