class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        res = []
        ln = len(num)
        if ln == 0:
            return True

        for i in num:

            if i == '6':
                res.append('9')
            elif i == '9':
                res.append('6')
            elif i == '8' or i == '1' or i == '0':
                res.append(i)
            else:
                return False

        newres = str("".join(res))
        print(newres)
        num = num[::-1]
        print(num)
        if newres == num:
            return True
        return False



