def solution(s):
    result = []

    for char in s:
        if 'a' <= char <= 'z':  # Check if char is a lowercase letter
            if char == 'z':
                result.append('a')
            else:
                result.append(chr(ord(char) + 1))
        elif 'A' <= char <= 'Z':  # Check if char is an uppercase letter
            if char == 'Z':
                result.append('A')
            else:
                result.append(chr(ord(char) + 1))
        else:  # Non-letter characters
            result.append(char)

    return ''.join(result)


# Example usage:
print(solution("abc123XYz!"))  # Output: "bcd123YZa!"
