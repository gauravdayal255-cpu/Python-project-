# कैलकुलेटर: फंक्शन के साथ, + - * / ^ पाँच ऑपरेशन
def jodo(a, b):
    return a + b

def ghataao(a, b):
    return a - b

def guna(a, b):
    return a * b

def bhaag(a, b):
    if b == 0:
        return "0 से भाग नहीं हो सकता"
    return a / b

def power(a, b):
    return a ** b

a = float(input("पहला नंबर : "))
op = input("ऑपरेशन (+, -, *, /, ^) : ")
b = float(input("दूसरा नंबर : "))

if op == "+":
    print("जवाब :", jodo(a, b))
elif op == "-":
    print("जवाब :", ghataao(a, b))
elif op == "*":
    print("जवाब :", guna(a, b))
elif op == "/":
    print("जवाब :", bhaag(a, b))
elif op == "^":
    print("जवाब :", power(a, b))
else:
    print("गलत ऑपरेशन")
