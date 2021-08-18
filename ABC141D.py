#現時点で最も値段が高い商品に割引券を使う
import heapq
n,m = map(int,input().split())
a = list(map(lambda x: -int(x), input().split())) #heapq は最小値を返すので、符号を反転させておく
heapq.heapify(a) #aを優先度付きキューにする
for _ in range(m):
  m_e = -heapq.heappop(a) #負の切り捨て徐算は値が丸め込まれる方向が違うので、先に正の値に戻しておく
  m_e //= 2
  heapq.heappush(a,-m_e)
print(-sum(a))

"""
優先度付きキュー (Priority queue) はデータ型の一つで、具体的には最小値（最大値）を O(log⁡N) で取り出す
要素を O(logN) で挿入することが出来ます。
通常のリストだとそれぞれ O(N) ですので高速です。
「リストの要素の挿入」と「最小値（最大値）を取り出す」ことを繰り返すような時に使います。
"""