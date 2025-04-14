def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

if __name__ == "__main__":
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    result = sum_of_even_numbers(start, end)
    print(f"The sum of even numbers from {start} to {end} is: {result}")
