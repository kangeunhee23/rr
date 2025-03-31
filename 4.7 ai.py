Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_prime(n):
...     if n<2:
...         return False
...     for i in range(2,int(n**0.5)+1):
...         if n%i==0:
...             return False
...         return True
... 
...     
>>> n=int(input("숫자를 입력하세요:"))
숫자를 입력하세요:5
>>> if is_prime(n):
...     print(f"{n}는 소수입니다")
... 
...     
5는 소수입니다
>>> else:
...     
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>>     else:
...         
SyntaxError: unexpected indent
>>> if is_prime(n):
...     print(f"{n}는 소수입니다")
... else:
...     print(f"{n}는 소수가 아닙니다.")
... 
...     
5는 소수입니다
