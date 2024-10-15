def find_min(nums):
    if not nums:
        return None

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
print(find_min([]))