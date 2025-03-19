Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5  # 0b101
>>> b = 6  # 0b110
... 
>>> print("0b101 & 0b110 =", bin(a & b))  # AND
0b101 & 0b110 = 0b100
>>> print("0b101 | 0b110 =", bin(a | b))  # OR
0b101 | 0b110 = 0b111
>>> print("0b101 ^ 0b110 =", bin(a ^ b))  # XOR
0b101 ^ 0b110 = 0b11
>>> 
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 9
>>> print(f"{n}의 2진수 값: {bin(n)}")
9의 2진수 값: 0b1001
>>> print(f"{n}의 2진수 값에 대한 비트단위 부정값: {bin(~n)}")
9의 2진수 값에 대한 비트단위 부정값: -0b1010
>>> 
>>> a = int(input("정수 a를 입력하세요: "))
정수 a를 입력하세요: 202
>>> b = int(input("정수 b를 입력하세요: "))
정수 b를 입력하세요: 50
>>> print("a / b의 몫:", a // b)
a / b의 몫: 4
>>> print("a / b의 나머지:", a % b)
a / b의 나머지: 2
>>> 
>>> n = int(input("세 자리 정수를 입력하세요: "))
세 자리 정수를 입력하세요: 349
>>> hundreds = n // 100
... tens = (n % 100) // 10
... ones = n % 10
SyntaxError: multiple statements found while compiling a single statement
>>> n = int(input("세 자리 정수를 입력하세요: "))
... 
세 자리 정수를 입력하세요: 349
>>> hundreds = n // 100
>>> tens = (n % 100) // 10
ones = n % 10
print("백의 자리:", hundreds)
백의 자리: 3
print("십의 자리:", tens)
십의 자리: 4
print("일의 자리:", ones)
일의 자리: 9

n = int(input("세 자리 정수를 입력하세요: "))
세 자리 정수를 입력하세요: 349
ones = n % 10
tens = (n % 100) // 10
hundreds = n // 100
print(ones)
9
print(tens)
4
print(hundreds)
3
