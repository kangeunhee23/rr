Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

print("200 + 300 + 400 =", 200 + 300 + 400)
200 + 300 + 400 = 900

width = 30
height = 60

print(width)
print(height)
SyntaxError: multiple statements found while compiling a single statement
>>> width=30
>>> height=60
>>> 
>>> print(width)
30
>>> print(height)
60
>>> 
>>> width=30
>>> height=60
>>> area=width+height
>>> print("사각형의 면적:", area)
사각형의 면적: 90
>>> 
>>> width=30
>>> height=60
>>> area=width*height
>>> print("사가형의 면적:",area)
사가형의 면적: 1800
>>> 
>>> width=40
>>> height=20
>>> area=(width*height)/2
>>> print("삼각형의 면적:",area)
삼각형의 면적: 400.0
>>> 
>>> side=int(input("정사각형의 밑변을 입력하시오:"))
정사각형의 밑변을 입력하시오: area=side*2
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    side=int(input("정사각형의 밑변을 입력하시오:"))
ValueError: invalid literal for int() with base 10: ' area=side*2'
>>> side=int(input("정사각형의 밑변을 입력하시오:"))
정사각형의 밑변을 입력하시오:40
>>> area=side**2
>>> print("정사각형의 면적:",area)
정사각형의 면적: 1600
>>> 
