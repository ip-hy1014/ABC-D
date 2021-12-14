"""
取り除く個数の最小化＝残す個数の最大化
"""
n = int(input())
a = list(map(int,input().split()))
ans = 0
b = 1
for i in range(n):
  if a[i]==b:
    b+=1
    ans+=1
if b==1:
  print(-1)
else:
  print(n-ans)