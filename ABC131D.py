n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
c = 0
for a,b in l:
  c += a
  if c > b:
    print("No")
    break
else:
  print("Yes")