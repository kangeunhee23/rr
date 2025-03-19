Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> total=sum(range(1,11))
>>> print("1에서 10까지의 합:", total)
1에서 10까지의 합: 55
>>> 
>>> print(1*2*3*4*5*6*7*8*9*10)
3628800
>>> 
>>> print("a n a**n")
a n a**n
>>> for a in range(2,7):
...     n=2
...     print(f"{a} {n} {a**n]")
...     
SyntaxError: incomplete input
>>> 
>>> celsius=float(input("섭씨 온도를 입력하세요:"))
섭씨 온도를 입력하세요:30
>>> fahrenheit=(9/5)*celsius+32
>>> print(f"섭씨 {celsius} 도는 화씨 {fahrenheit:.1f} 도 입니다.")
섭씨 30.0 도는 화씨 86.0 도 입니다.
>>> 
>>> fahrenheit = float(input("화씨 온도를 입력하세요: "))
화씨 온도를 입력하세요: 86
>>> celsius = (5/9) * (fahrenheit - 32)
>>> print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")
화씨 86.0 도는 섭씨 30.0 도 입니다.
>>> 
>>> PI = 3.141592
>>> radius = 11
>>> circumference = 2 * PI * radius
>>> area = PI * radius ** 2
>>> print(f"원의 반지름 = {radius}, 원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.12f}")
원의 반지름 = 11, 원의 둘레 = 69.115024, 원의 면적 = 380.132632000000
