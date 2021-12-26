class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        mx = 0
        for i in sentences:
            print(i)
            v = i.count(" ")

            if mx < v + 1:
                mx = v + 1
        return mx


