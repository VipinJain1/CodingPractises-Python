class Solution:
    def calPoints(self, ops: List[str]) -> int:

        ln = len(ops)
        if ln == 0:
            return None

        stack = []

        for i in ops:
            print(stack)
            if i.isnumeric():
                stack.append(i)
            elif i.startswith("-") and i[1].isdigit():
                stack.append(i)

            else:
                if i == 'C':
                    if stack[-1] is not None:
                        stack.pop()

                elif i == 'D':
                    if stack[-1] is not None:
                        n = int(stack[-1])
                        stack.append(n * 2)
                elif i == '+':
                    if stack[-1] is not None and stack[-2] is not None:
                        n1 = int(stack[-1])
                        n2 = int(stack[-2])
                        stack.append(n1 + n2)

        # print (stack)
        return sum([int(i) for i in stack])
