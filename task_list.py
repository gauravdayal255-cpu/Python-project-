# टास्क लिस्ट: 3 टास्क लेता है और tasks.txt में सेव करता है
tasks = []

for i in range(3):
    task = input("Enter a task : ")
    tasks.append(task)

print("your tasks : ")
for t in tasks:
    print(t)

with open("tasks.txt", "w") as file:
    for t in tasks:
        file.write(t + "\n")

print("Tasks saved !")
