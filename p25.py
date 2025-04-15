numbers = [4, 7, 2, 7, 9, 4, 5, 6, 2, 8, 7]
duplicates = []


for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])


print("Duplicate values in the list are:", duplicates)