import collections
class Solution:
    def removeOuterParentheses(self, Str: str) -> str:
        stk1 = []
        stk2 = []
        stringB = []
        open = 0
        close = 0
        for i in range(len(Str)):
            if Str[i]=='(':
                if len(stk1)==0:
                    open+=1
                    stk1.append(Str[i])
                else:
                    open+=1
                    stk2.append(Str[i])
            else:
                if len(stk2)==0:
                    close+=1
                    stringB.append('')
                    stk1.pop()
                else:
                    if stk2[-1]== Str[i] and (close+1)==open:
                        close+=1
                        temp = collections.deque()
                        while stk2:
                            temp.appendleft(stk2.pop())
                        for i in range(len(temp)):
                            stringB.append(temp[i])
                        stk1.pop()
                    else:
                        close+=1
                        stk2.append(Str[i])
        return "".join(letter for letter in stringB)

obj = Solution()
print(obj.removeOuterParentheses('()()()()(())'))