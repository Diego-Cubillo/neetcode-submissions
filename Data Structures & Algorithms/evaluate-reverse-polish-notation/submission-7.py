class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        for char in tokens:
            if char in {"+", "-", "/", "*"}:

                num2 = myStack.pop()
                num1 = myStack.pop()
                
                match char:
                    case "+": myStack.append(num1 + num2)
                    case "-": myStack.append(num1 - num2)
                    case "*": myStack.append(num1 * num2)
                    case "/": myStack.append(int(num1 / num2))
            else:
                myStack.append(int(char))
        
        return myStack.pop()