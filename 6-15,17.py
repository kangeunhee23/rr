Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> greet = "Have a beautiful day."
>>> print(greet[:4])   # 'Have'
Have
>>> print(greet[5:6])  # 'a'
a
>>> print(greet[7:16]) # 'beautiful'
beautiful
>>> print(greet[17:])  # 'day.'
day.
>>> 
>>> animals = ['dog', 'cat', 'tiger', 'lion']
>>> print(animals)
['dog', 'cat', 'tiger', 'lion']
>>> animals.append(animals.pop(0))
... print(animals)
SyntaxError: multiple statements found while compiling a single statement
>>> animals.append(animals.pop(0))
>>> print(animals)
['cat', 'tiger', 'lion', 'dog']
>>> for animal in animals:
...      print(f"I love {animal}.")
... 
...      
I love cat.
I love tiger.
I love lion.
I love dog.
