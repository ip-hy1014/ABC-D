rgb = ["R G B","G B R", "B R G"]
s = input()
t = input()
print("Yes" if (s in rgb) == (t in rgb) else "No")

#初期状態で不一致の人数が2ならNo
#別解
s = input()
t = input()
ans = 0
for i,j in zip(s,t):
  if i!=j:
    ans += 1
print("Yes" if ans!=2 else "No")
