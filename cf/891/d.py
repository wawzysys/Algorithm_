import sys
# sys.setrecursionlimit(1000000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n = sint()
	a = lint()
	b = lint()
	mm = -inf
	for i in range(n):
		mm = max(mm, a[i] - b[i])
	c = 0
	for i in range(n):
		c += (mm == a[i] -b[i])
	print(c)
	for i in range(n):
		if mm == a[i] - b[i]:
			print(i + 1, end = ' ')
	print()






if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	    solve()

	# solve()