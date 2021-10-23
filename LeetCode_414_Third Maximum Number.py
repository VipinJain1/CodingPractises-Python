import collections

Q = collections.deque([10,20,30])
Q.append(40)
Q.popleft()

print (Q)