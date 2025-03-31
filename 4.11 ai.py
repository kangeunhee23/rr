Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> depth=30
>>> up=7
>>> down=2
>>> position=0
>>> days=0
>>> 
>>> while position + up<depth:
...     days+=1
...     position+=up
...     if position>=depth:
...         break
...     position-=down
... 
...     
>>> days+=1
>>> print(f"우물을 탈출하는데 걸린 날은 {days] 일입니다.")
SyntaxError: f-string: unmatched ']'
>>> print(f"우물을 탈출하는데 걸린 날은 {days} 일입니다.")
우물을 탈출하는데 걸린 날은 6 일입니다.
