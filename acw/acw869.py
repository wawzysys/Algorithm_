#/E/0Code/Algorithm/acw/acw869.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
MOD = 10 ** 9 + 7
def div(n):
	i = 2
	while i <= n / i:
		while n % i == 0:
			cnt[i] += 1
			n = n // i
		i  += 1
	if n > 1:
		cnt[n] += 1

if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()
	n = sint()
	ans = 1
	cnt = defaultdict(int)
	for _ in range(n):
		m = sint()
		div(m)
	for v in cnt.values():
		ans *= (v + 1) % MOD
	print(ans % MOD)