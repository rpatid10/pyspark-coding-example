class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to match closing brackets with opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Check if stack is not empty and top of stack matches the opening bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If stack is empty, all brackets are matched; otherwise, it's invalid
        return not stack




