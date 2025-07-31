#1
records = [
    {'name': "rice", "price": 120, "category": "grocery"},
    {'name': "sugar", "price": 220, "category": "grocery"},
    {'name': "wheat", "price": 320, "category": "grocery"},
    {'name': "rcereal", "price": 420, "category": "grocery"},
]

with open("grocery.txt", "w") as f:
    f.write("ID\tNAME\tPRICE\tCATEGORY\n")
    for i, item in enumerate(records, start=1):
        f.write(f"{i}\t{item['name']}\t{item['price']}\t{item['category']}\n")

with open("grocery.txt", "r") as f:
    contents = f.read()
    print(contents)


#2
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file.")

with open("sample.txt", "r") as f:
    print(f.read(5))
    f.seek(0)
    print(f.read(4))
    f.seek(7)
    print(f.read(4))
