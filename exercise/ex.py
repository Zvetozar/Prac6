with open("data.txt", "w") as f:
    f.write("Hello\n")
    f.write("Python\n")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)

with open("data.txt", "a") as f:
    f.write("New line added\n")

with open("data.txt", "r") as f:
    print(f.read())
#2
import shutil
import os

shutil.copy("data.txt", "backup.txt")

if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("Backup deleted")
#3
import os

os.makedirs("example/folder/test", exist_ok=True)

print(os.listdir())

print(os.getcwd())

#4
import os

for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

#5
import shutil

shutil.copy("data.txt", "example/data_copy.txt")

shutil.move("example/data_copy.txt", "example/moved_data.txt")

#6
from functools import reduce

nums = [1,2,3,4,5]

squares = list(map(lambda x: x*x, nums))
print(squares)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

total = reduce(lambda x,y: x+y, nums)
print(total)

#7
names = ["Ivan","Anna","Bob"]
scores = [90,85,88]

for i,name in enumerate(names):
    print(i,name)

for name,score in zip(names,scores):
    print(name,score)

#8
nums = [1,2,3,4]

print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))

print(sorted(nums))

a = "10"
b = "3.14"

print(int(a))
print(float(b))
print(str(100))