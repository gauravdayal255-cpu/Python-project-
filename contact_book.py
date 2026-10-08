# कॉन्टैक्ट बुक: क्लास, डिक्शनरी और फ़ाइल (contacts.txt) के साथ
class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    naam, number = line.strip().split(",")
                    self.contacts[naam] = number
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, "w") as file:
            for naam in self.contacts:
                file.write(naam + "," + self.contacts[naam] + "\n")

    def jodo(self, naam, number):
        self.contacts[naam] = number
        self.save()
        print("जुड़ गया")

    def khojo(self, naam):
        if naam in self.contacts:
            print(naam, "का नंबर :", self.contacts[naam])
        else:
            print("यह नाम लिस्ट में नहीं है")

    def hatao(self, naam):
        if naam in self.contacts:
            del self.contacts[naam]
            self.save()
            print("हट गया")
        else:
            print("यह नाम लिस्ट में नहीं है")

book = ContactBook("contacts.txt")

while True:
    print("1. नया कॉन्टैक्ट  2. खोजो  3. हटाओ  4. बाहर")
    choice = input("चुनिए : ").strip()
    if choice == "1":
        naam = input("नाम : ").strip()
        number = input("नंबर : ").strip()
        book.jodo(naam, number)
    elif choice == "2":
        book.khojo(input("किसका नंबर चाहिए : ").strip())
    elif choice == "3":
        book.hatao(input("किसे हटाना है : ").strip())
    elif choice == "4":
        break
    else:
        print("गलत विकल्प")
