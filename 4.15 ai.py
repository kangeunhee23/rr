Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fuel=500
>>> while True:
...     change = int(input("충전 또는 사용한 연료를 입력하세요 (+/- 포함): "))
...     fuel += change
...     print(f"현재 탱크량은 {fuel} 입니다.")
... 
...     if fuel < 50:
...         print("경고: 연료가 10% 미만이니 충전하세요!")
...         break
... 
...     
충전 또는 사용한 연료를 입력하세요 (+/- 포함): 60
현재 탱크량은 560 입니다.
충전 또는 사용한 연료를 입력하세요 (+/- 포함): -300
현재 탱크량은 260 입니다.
충전 또는 사용한 연료를 입력하세요 (+/- 포함): -220
현재 탱크량은 40 입니다.
경고: 연료가 10% 미만이니 충전하세요!
