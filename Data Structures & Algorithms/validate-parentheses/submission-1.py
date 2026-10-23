class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for char in s:
            if char in set(["(", "[", "{"]):
                myStack.append(char)
            else:
                if len(myStack) == 0:
                    return False
                    
                removed = myStack.pop()
                if char == ")":
                    if removed != "(":
                        return False
                elif char == "]":
                    if removed != "[":
                        return False
                elif char == "}":
                    if removed != "{":
                        return False
        
        return len(myStack) == 0