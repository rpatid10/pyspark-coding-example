def keep_unique_characters(string: str) -> str:
    """
    Time complexity: O(n) where n is the length of string
    Space complexity: O(n) where n is the length of string
    """
    # Count how many times each character appears in the string
    char_count = {}
    result = ""
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    # Only include characters that have appeared just once in the string
    for char in string:
        if char_count[char] == 1:
            result += char

    return result



def count_words(s):
 return len(s.split(" "))

print(count_words("rahul patidar"))