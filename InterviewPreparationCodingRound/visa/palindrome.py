def solution(input_string):
    def to_lower(c):
        # Convert character c to lowercase manually
        if 'A' <= c <= 'Z':
            return chr(ord(c) + 32)
        return c

    def is_letter(c):
        # Check if the character is a letter
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z')

    # Filter and normalize the string
    filtered = []
    for char in input_string:
        if is_letter(char):
            filtered.append(to_lower(char))

    # Check if the filtered list is a palindrome
    left = 0
    right = len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1

    return True


# Example usage:
print(solution("A man, a plan, a canal, Panama"))  # Output: True
print(solution("racecar"))  # Output: True
print(solution("hello"))  # Output: False
