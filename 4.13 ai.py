Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for num in range(100, 1000):
...     digits = [int(d) for d in str(num)]
...     if sum(d ** 3 for d in digits) == num:
...         print(num, end=" ")
... 
...         
153 370 371 407 
