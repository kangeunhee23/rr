Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n_list = list(map(int, input("5개의 수를 입력하세요: ").split()))
5개의 수를 입력하세요: 45 67 20 34 2
>>> total = sum(n_list)
>>> average = total / len(n_list)
>>> max_value = max(n_list)
>>> min_value = min(n_list)
>>> 
>>> print(f"합: {total}")
합: 168
>>> print(f"평균: {average:.1f}")
평균: 33.6
>>> print(f"최댓값: {max_value}")
최댓값: 67
>>> print(f"최솟값: {min_value}")
최솟값: 2
>>> 
>>> import math
>>> n = int(input("n을 입력하세요: "))
n을 입력하세요: 10
>>> n_list = list(map(int, input(f"{n}개의 수를 입력하세요: ").split()))
10개의 수를 입력하세요: 45 67 20 34 2 100 23 45 67 89
>>> mean = sum(n_list) / n
>>> variance = sum((x - mean) ** 2 for x in n_list) / n
>>> std_dev = math.sqrt(variance)
>>> print(f"합: {sum(n_list)}")
합: 492
>>> print(f"평균: {mean:.1f}")
평균: 49.2
>>> print(f"표준편차: {std_dev:.2f}")
표준편차: 29.72
