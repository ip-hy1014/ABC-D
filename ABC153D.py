n = int(input())
ans = 0
cnt = 1
while n > 0:
  n//=2
  ans += cnt
  cnt *= 2
print(ans)

#別解
n = int(input())
print(2**(n.bit_length())-1)