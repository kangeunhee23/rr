Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
...     print("맛나 식당에 오신것을 환영합니다. 메뉴는 다음과 같습니다.")
...     print("-햄버거(입력 b)")
...     print("-피자(입력 p)")
... choice=input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip()
SyntaxError: invalid syntax
>>>     choice=input("메뉴를 선택하세요(알파벳 b,c,p 입력):").strip()
...     
SyntaxError: unexpected indent
>>> while True:
...     print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
...     print("- 햄버거(입력 b)")
...     print("- 치킨(입력 c)")
...     print("- 피자(입력 p)")
...     
...     choice = input("메뉴를 선택하세요(알파벳 b, c, p 입력): ").strip()
...     
...     if choice in ['b', 'c', 'p']:
...         if choice == 'b':
...             print("햄버거를 선택하셨습니다.")
...         elif choice == 'c':
...             print("치킨을 선택하셨습니다.")
...         else:
...             print("피자를 선택하셨습니다.")
...         break  # 올바른 입력이면 반복 종료
...     else:
...         print("메뉴를 다시 입력하세요.")
... 
...         
맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.
- 햄버거(입력 b)
- 치킨(입력 c)
- 피자(입력 p)
메뉴를 선택하세요(알파벳 b, c, p 입력): b
햄버거를 선택하셨습니다.
