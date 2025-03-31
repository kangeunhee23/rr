Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sum_of_squares(n):
...     return sum(i**2 for i in range(1,n+1))
... 
>>> n=int(input("숫자를 입력하세요:"))
숫자를 입력하세요:5
>>> print(f"결과는{sum_of_squares(n)}입니다.")
결과는55입니다.
