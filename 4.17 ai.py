Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_of_divisors(n):
...      return sum([i for i in range(1, n // 2 + 1) if n % i == 0])
... 
...     
>>> for a in range(1, 20001):
...     b = sum_of_divisors(a)
...      if a < b and sum_of_divisors(b) == a:
...          
SyntaxError: unexpected indent
>>> for a in range(1, 20001):
...     b = sum_of_divisors(a)
...     if a < b and sum_of_divisors(b) == a:
...           print(f"{a}의 친화수 {b}")
... 
...           
220의 친화수 284
1184의 친화수 1210
2620의 친화수 2924
5020의 친화수 5564
6232의 친화수 6368
10744의 친화수 10856
12285의 친화수 14595
17296의 친화수 18416

