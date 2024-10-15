def solution(s):
    # Convert the input string to a list of characters
    char_list = []

    # Iterate through the string in steps of 2
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            # Swap characters at position i and i+1
            char_list.append(s[i + 1])
            char_list.append(s[i])
            i += 2
        else:
            # Append the last character if the length is odd
            char_list.append(s[i])
            i += 1

    # Convert the list of characters back to a string
    result = ""
    for char in char_list:
        result += char

    return result


# Example usage:
print(solution("abcdef"))  # Output: "badcfe"
print(solution("hello"))  # Output: "ehllo"
