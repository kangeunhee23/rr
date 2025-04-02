Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [3, 5, 7]
>>> list2 = [2, 3, 4, 5, 6]
>>> for num1 in list1:
...      for num2 in list2:
...           print(f"{num1} * {num2} = {num1 * num2}")
... 
...           
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
>>> list1 = ["I like", "I love"]
>>> list2 = ["pancakes.", "kiwi juice.", "espresso."]
>>> for phrase in list1:
...       for food in list2:
...             print(f"{phrase} {food}")
... 
...             
I like pancakes.
I like kiwi juice.
I like espresso.
I love pancakes.
I love kiwi juice.
I love espresso.
