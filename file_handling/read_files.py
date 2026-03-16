with open("example.txt", "r") as f:
    content = f.read()
    print(content)

with open("example.txt", "r") as f:
    print(f.readline())

with open("example.txt", "r") as f:
    print(f.readlines())