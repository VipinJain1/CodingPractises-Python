class Solution:
    def countPoints(self, rings: str) -> int:

        from collections import defaultdict

        d = defaultdict(list)
        cnt = 0
        end = len(rings)

        if end % 2 != 0:
            return False

        while (cnt < end):
            idx = rings[cnt + 1]
            color = rings[cnt]
            d[idx].append(color)
            cnt += 2

        total = 0
        for key, color in d.items():
            if 'R' in color and 'G' in color and 'B' in color:
                total += 1
        return total

