# put your python code here
numbers = input().split(" ")
search = input()

was_found = False
found = []

for x, number in enumerate(numbers):
    if search == number:
        found.append(str(x))
        was_found = True


if not was_found:
    print("not found")
else:
    print(" ".join(found))
