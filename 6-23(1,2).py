Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def how_many_persons(person_list):
...     return len(person_list)
... 
>>> person1 = ['도현', 20, 1, 180.0, 100.0]
>>> person2 = ['의사무', 25, 1, 170.0, 70.0]
>>> person3 = ['평강', 22, 0, 169.0, 60.0]
>>> person4 = ['범계서', 40, 1, 150.0, 50.0]
>>> 
>>> person_list = [person1, person2, person3, person4]
>>> n_persons =
SyntaxError: invalid syntax
>>> n_persons = how_many_persons(person_list)
>>> 
>>> print(str(n_persons) + '명의 정보가 담겨 있습니다.')
4명의 정보가 담겨 있습니다.
>>> 
>>> def compute_average_age(person_list):
...      total_age = sum(person[1] for person in person_list)
...      return total_age / len(person_list)
... 
...     
>>> average_age = compute_average_age(person_list)
>>> print("평균 나이는 " + str(average_age) + "세입니다.")
평균 나이는 26.75세입니다.
>>> 
>>> def count_males_females(person_list):
...     male_count = sum(1 for person in person_list if person[2] == 1)
...     female_count = sum(1 for person in person_list if person[2] == 0)
...     return male_count, female_count
... n_male, n_female = count_males_females(person_list)
SyntaxError: invalid syntax
>>> n_male, n_female = count_males_females(person_list)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    n_male, n_female = count_males_females(person_list)
NameError: name 'count_males_females' is not defined
