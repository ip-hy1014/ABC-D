rgb = ["R G B","G B R", "B R G"]
s = input()
t = input()
print("Yes" if (s in rgb) == (t in rgb) else "No")