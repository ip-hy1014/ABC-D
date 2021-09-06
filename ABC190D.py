"""
初項A, 末項B(A<=B), 公差1の等差数列の和は,n = (A+B)(B-A+1)/2
(A+B)(B-A+1)=2Nの整数解A,Bを求める

A+B = x
B-A+1 = y

A = x-y+1/2
B = x+y-1/2

AとBは自然数であるから，xとyの偶奇が異なる必要がある．
"""
n = int(input())
while n % 2 == 0:
  n //= 2
sq = int(n**0.5)
ans = 0
for i in range(1,sq+1):
  if n % i == 0:
    ans += 2
if sq * sq == n:
  ans -= 1
print(ans*2)