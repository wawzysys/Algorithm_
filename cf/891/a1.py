import sys
input=lambda:sys.stdin.readline().strip()
sys.setrecursionlimit(100000)
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
	t = sint()
	for _ in range(t):
		n = sint()
		a = lint()
		ss = sum(a)
		if ss %  2 == 1:
			print("NO")
		else:
			print("YES")





if __name__ == '__main__':
	# t=int(input())
	# for _ in range(t):
	#     solve()

	solve()