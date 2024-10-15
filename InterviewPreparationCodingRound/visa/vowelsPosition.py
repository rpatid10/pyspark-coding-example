def solution(s):
    # Define the vowels (both lowercase and uppercase)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    positions = []

    # Iterate through the string and collect positions of vowels
    for index in range(len(s)):
        char = s[index]
        # Check if the character is a vowel
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
                break

        if is_vowel:
            positions.append(index)

    return positions


# Example usage:
print(solution("Hello WORLD"))  # Output: [1, 4, 7]

def find_max_element(lst):
    max_element = lst[0]  # Initialize with the first element
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example usage
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_max_element(sample_list))  # Output: 9


def find_min(nums):
    if not nums:
        return None  # Return None if the list is empty

    # Initialize the minimum with the first element
    min_value = nums[0]

    # Iterate through the list starting from the second element
    for num in nums[1:]:
        if num < min_value:
            min_value = num  # Update the minimum value if a smaller number is found

    return min_value


# Example usage:
print(find_min([3, 1, 4, 1, 5, 9, 2]))  # Output: 1
print(find_min([10, 20, 30]))  # Output: 10
print(find_min([]))  # Output: None

