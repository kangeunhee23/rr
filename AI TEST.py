Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=[10,20,30]
>>> total=sum(lst)
>>> sum=100
>>> lst=[10,20,30]
>>> total=sum(lst)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    total=sum(lst)
TypeError: 'int' object is not callable
>>> print(total)
60
