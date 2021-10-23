import heapq


def k_Closest_Points_To_Origin(a, k):
    d = dict()
    res = []
    finalresult = []
    if k > len(a):
        return a
    for i in a:
        x = i[0]
        y = i[1]
        val = x**2 + y**2
        if val in d.keys():
            d[val].append([x, y])
        else:
            d[val] = [x, y]
    res = heapq.nsmallest(k, d.items(), key=lambda x: x[0])
    for i in res:
        finalresult.append(i[1])

    return finalresult


a = [[1, 2], [3, 4], [5, 6], [-3, 3], [0, 3], [-1, 1]]
k = 5

print(k_Closest_Points_To_Origin(a, k))
