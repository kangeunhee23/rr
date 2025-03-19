Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import cmath
angle=cmath.pi/6
z=complex(1,2)
rorated_z=z*cmath.exp(complex(0,angle))
print("30도 회전한 후:", rotated_z)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("30도 회전한 후:", rotated_z)
NameError: name 'rotated_z' is not defined. Did you mean: 'rorated_z'?
print("30도 회전한 후:", rorated_z)
30도 회전한 후: (-0.13397459621556118+2.232050807568877j)

for i in range(10):
    print(2<<i,end=" ")

    
2 4 8 16 32 64 128 256 512 1024 

n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 20
is_even = (n % 2 == 0)
>>> s_in_range = (0 <= n <= 100)
>>> print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
NameError: name 'is_in_range' is not defined. Did you mean: 's_in_range'?
>>> print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
NameError: name 'is_in_range' is not defined. Did you mean: 's_in_range'?
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 20
>>> print("이 수가 짝수인가요?", n % 2 == 0)
이 수가 짝수인가요? True
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 21
>>> print("이 수가 짝수인가요?", n % 2 == 0)
이 수가 짝수인가요? False
>>> 
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 120
>>> is_even = (n % 2 == 0)
>>> is_in_range = (0 <= n <= 100)
>>> print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False
>>> 
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 88
>>> is_even = (n % 2 == 0)
>>> is_in_range = (0 <= n <= 100)
>>> print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", is_even and is_in_range)
입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True
