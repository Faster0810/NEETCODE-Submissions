class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ")": "(", #must match (
            "]": "[", #must match [
            "}": "{" # must match {
        }

        for char in s:

            if char in mapping:#This checks if character is one of mapping's.

                if not stack:
                    return False

                top = stack.pop()#Remove the last opening bracket.


                if mapping[char] != top:#Check If Brackets Match
                    return False

            else:
                stack.append(char)#If Opening Bracket

        return not stack              