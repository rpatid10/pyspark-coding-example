def solution(input_string):
    result = []

    for char in input_string:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32
            result.append(chr(ord(char) - 32))
        # Check if the character is an uppercase letter
        elif 'A' <= char <= 'Z':
            # Convert to lowercase by adding 32
            result.append(chr(ord(char) + 32))
        else:
            # Leave non-letter characters unchanged
            result.append(char)

    return ''.join(result)


# Example usage:
print(solution("HelLo WoRld 123"))  # Output: "hELlO wOrLD 123"
