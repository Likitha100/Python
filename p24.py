numbers = [23, 5, 89, 12, 44, 3, 77]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest number in the list is:", smallest)
print("Largest number in the list is:", largest)