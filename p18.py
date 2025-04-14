def remove_char(s, char):
    return s.replace(char, '')

if __name__ == "__main__":
    s = input("Enter a string: ")
    char = input("Enter the character to remove: ")

    if len(char) != 1:
        print("Please enter a single character to remove.")
    else:
        result = remove_char(s, char)
        print("Resulting string:", result)