def replace_character(input_string, c1, c2):
    result = []

    # Iterate through each character in the input_string
    for char in input_string:
        if char == c1:
            result.append(c2)  # Replace c1 with c2
        else:
            result.append(char)  # Keep the original character

    # Join the list of characters into a single string
    return ''.join(result)


# Example usage:
print(replace_character("hello world", 'o', '0'))  # Output: "hell0 w0rld"