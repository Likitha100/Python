def count_char_occurrences(s, char):
    return s.count(char)

if __name__ == "__main__":
    s = input("Enter a string: ")
    char = input("Enter the character to count: ")

    if len(char) != 1:
        print("Please enter a single character to count.")
    else:
        count = count_char_occurrences(s, char)
        print(f"The character '{char}' appears {count} time(s) in the string.")