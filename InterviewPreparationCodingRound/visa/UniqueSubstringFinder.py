def count_unique_substrings(string: str) -> int:
    unique_substrings = set()

    # Generate all possible substrings
    n = len(string)
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = string[start:end]
            print(unique_substrings.add(substring))

    return len(unique_substrings)


print(count_unique_substrings("aaaaaaa"))  # Output should be 7
print(count_unique_substrings("aaaaccdcc"))  # Output should be 20
