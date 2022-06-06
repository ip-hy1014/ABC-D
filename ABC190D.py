"""
初項A, 末項B(A<=B), 公差1の等差数列の和は,n = (A+B)(B-A+1)/2
(A+B)(B-A+1)=2Nの整数解A,Bを求める

A+B = x
B-A+1 = y

A = (x-y+1)/2
B = (x+y-1)/2

AとBは自然数であるから,xとyの偶奇が異なる必要がある

制約がN<=10**12 なのでこれは√を取れってことになる
約数全探索はO(√N)で解けるので N<=10**12 → √N<=10**6 となる

また、 2N は 2 を素因数に 1 つ以上含むため、x,y のどちらか片方しか 2 を素因数に持たないことを考えると、
M= ( N を 2 で割り切れなくなるまで割った数 ) として、 ( M の約数の個数 )×2 がこの問題の答えになります。
----------------------------------------------------------
2N=n(2a+n-1)
であるような(a,n)の個数を求めれば良いことになります。 まず、nは2Nの正の約数となります。 ここで、nを一つ決め打ちした場合に条件を満たすaが存在するかどうかを判定すればよいです。
m=2N/nとしたとき、m-n=2a-1となるため、m-nが奇数であることが必要です。逆に、m-nが奇数ならばそれに対応するaを一意に定めることができます。(m-nがOddだから偶奇が異なる)
よって、以下の問題と等価であることがわかります。
等価な問題:2Nの正の約数dであって、dと2N/dの偶奇が異なるようなものの個数を求めよ。
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

#https://zenn.dev/tea/articles/7a957e64f2d913
#答えはNの約数に含まれる奇数の数の2倍
def divisor(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border+1):
        if n%small == 0:
            table.append(small)
            big = n//small
            bigs.append(big)
    if border == sq:
        bigs.pop()
    table += reversed(bigs)
    return table
n = int(input())
ans = []
for i in divisor(n):
  if i%2!=0:
    ans.append(i)
print(len(ans)*2)
