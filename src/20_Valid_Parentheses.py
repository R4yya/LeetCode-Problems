class Solution:
    def isValid(self, brackets: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for bracket in brackets:
            if bracket in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[bracket] != top_element:
                    return False
            else:
                stack.append(bracket)

        return not stack
