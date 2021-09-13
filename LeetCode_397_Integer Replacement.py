
def integerReplacement(n: int) -> int:
      if n == 1:
          return 0

      if n & 1:
          return 1 + min(integerReplacement(n-1), integerReplacement(n+1))
      else:
          return 1 + integerReplacement(n//2)



n = 19
print(integerReplacement(n))
