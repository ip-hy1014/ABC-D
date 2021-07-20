from collections import deque
s = input()
q = int(input())
d = deque(s)
c = 0
for i in range(q):
  t = list(input().split())
  if t[0] == "1":
    c += 1
  else:
    if t[1] == "1":
      if c % 2 == 0:
        d.appendleft(t[2]) #偶数回反転の時は先頭に追加
      else:
        d.append(t[2]) #奇数回反転させたら先頭に追加した要素は末尾になるため
    else:
      if c % 2 == 0:
        d.append(t[2]) #上記の逆
      else:
        d.appendleft(t[2])
if c % 2 != 0: #偶数回反転させたら元にもどるから奇数回の時だけ最後に反転
  d.reverse()
print("".join(map(str,d)))