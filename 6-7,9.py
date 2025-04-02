Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n_list = [10, 20, 30, 50, 60]
>>> total = 0
>>> for num in n_list:
...       total += num
... 
...       
>>> print(f"리스트 원소들: {n_list}")
리스트 원소들: [10, 20, 30, 50, 60]
>>> print(f"리스트 원소들의 합: {total}")
리스트 원소들의 합: 170
>>> 
>>> n_list = [10, 20, 30, 50, 60]
>>> max_value = n_list[0]
>>> for num in n_list:
...     if num > max_value:
...         max_value = num
... 
...         
>>> print(f"리스트 원소들: {n_list}")
리스트 원소들: [10, 20, 30, 50, 60]
>>> print(f"리스트 원소 중 최댓값: {max_value}")
리스트 원소 중 최댓값: 60
>>> 
