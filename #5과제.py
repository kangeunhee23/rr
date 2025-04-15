Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def inch2cm(inch):
...     return inch * 2.54
... 
>>> for i in range(1,6):
...     print(f"{i} 인치={inch2cm(i):.2f} 센티미터")
... 
...     
1 인치=2.54 센티미터
2 인치=5.08 센티미터
3 인치=7.62 센티미터
4 인치=10.16 센티미터
5 인치=12.70 센티미터
>>> 
>>> def mean_of_n(nums):
...     return sum(nums)/len(nums)
... 
>>> def max_of_n(nums):
...     return max(nums)
... 
>>> def min_of_n(nums):
...     return min(nums)
... 
>>> nums=[3,45,32,5,7,8,4,44,5,90,17]
>>> 
>>> print("평균값은", mean_of_n(nums))
평균값은 23.636363636363637
>>> print("최댓값은", max_of_n(nums))
최댓값은 90
>>> print("최솟값은",min_of_n(nums))
최솟값은 3
>>> 
>>> def sum_range(n1,n2):
...     return sum(range(n1,n2+1))
... 
>>> print("10에서 20까지의 정수의 합:", sum_range(10,20))
10에서 20까지의 정수의 합: 165
>>> print("40에서 100까지의 정수의 합:",sum_range(40,100))
40에서 100까지의 정수의 합: 4270
>>> 
