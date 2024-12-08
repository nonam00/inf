def DEL(x, y): return x % y == 0

def f(x, A):
      return ((not DEL(x, 7)) and DEL(x, 13)) <= (x > A - 40)
      
print(max(A for A in range(1, 2000) if all(f(x, A) == 1 for x in range(1, 4000))))
