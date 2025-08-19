class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        first_added = False
        result = []

        for p in s:
            print("\n\n")
            print("stack: ", stack)
            print("first: ", first_added)
            print("result: ", result)
            print("current: ",p)
            print("\n\n")
            
            if p == '(':
                if first_added:
                    stack.append(p)
                    result.append(p)
                else:
                    stack.append(p)
                    first_added = True
                    

            else:
                if len(stack) == 1:
                    first_added = False
                    stack.pop()
                elif first_added:
                    result.append(p)
                    stack.pop()
    
        return "".join(result)
                
            
                

sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))