Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> PI=3.141592
>>> radius=int(input("원의 반지름을 입력하세요:"))
원의 반지름을 입력하세요:11
>>> circumference=2*PI*radius
>>> area=PI*(radius**2)
>>> print(f"원의 둘레 = {circumference},원의 면적={area}")
원의 둘레 = 69.115024,원의 면적=380.132632
>>> 
>>> import math
>>> for i in range(1,11):
...                      print(f"{i}의 제곱근={math.sqrt(i)}")
... 
...                      
1의 제곱근=1.0
2의 제곱근=1.4142135623730951
3의 제곱근=1.7320508075688772
4의 제곱근=2.0
5의 제곱근=2.23606797749979
6의 제곱근=2.449489742783178
7의 제곱근=2.6457513110645907
8의 제곱근=2.8284271247461903
9의 제곱근=3.0
10의 제곱근=3.1622776601683795
>>> 
>>> import math
>>> a=int(input("밑변을 입력하세요:"))
밑변을 입력하세요:5
>>> b=int(input("높이를 입력하세요:"))
높이를 입력하세요:12
>>> c=math.sqrt(a**2+b**2)
>>> print("빗변:",c)
빗변: 13.0
>>> 
>>> z=complex(1,2)
>>> rotated_z=z*complex(0,1)
>>> print("90도 회전한 후:",rotated_z)
90도 회전한 후: (-2+1j)
