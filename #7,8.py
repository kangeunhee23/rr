Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(10,20,30,40)
>>> t[0]
10
>>> t[0:2]
(10, 20)
>>> t[1:]
(20, 30, 40)
>>> t[:3]
(10, 20, 30)
>>> t[1::2]
(20, 40)
>>> t[::-1]
(40, 30, 20, 10)
>>> 
>>> import math
>>> for degree in range(0.181,10):
...     rad=math.radians(degree)
...     sin_val=round(math.sin(rad),3)
...     cos_val=round(math.cos(rad),3)
...     tan_val=round(math.tan(rad),3)
... 
...     
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for degree in range(0.181,10):
TypeError: 'float' object cannot be interpreted as an integer
>>> for degree in range(0.181,10):
...     rad=math.radians(degree)
...     sin_val=round(math.sin(rad),3)
...     cos_val=round(math.cos(rad),3)
...     tan_val=round(math.tan(rad),3)
...     print(f"sin({degree})={sin_val:>5},cos({degree})={cos_val:>5},tan{degree})=tan_val:>6}")
...     
SyntaxError: f-string: single '}' is not allowed
>>> for degree in range(0.181,10):
...     rad=math.radians(degree)
...     sin_val=round(math.sin(rad),3)
...     cos_val=round(math.cos(rad),3)
...     tan_val=round(math.tan(rad),3)
...     print(f"sin({degree})={sin_val:>5},cos({degree})={cos_val:>5},tan{degree})={tan_val:>6}")
... 
...     
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for degree in range(0.181,10):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
>>> tup=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
>>> temp=[]
>>> for i in tup:
...     if i not in temp:
...         temp.append(i)
... 
...         
>>> result=tuple(temp)
>>> print("중복 제거 튜플:",result)
중복 제거 튜플: (1, 2, 5, 4, 3, 7, 8, 9)
