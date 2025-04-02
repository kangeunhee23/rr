Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
>>> new_s_list = []
>>> for item in s_list:
...      if item not in new_s_list:
...          new_s_list.append(item)
... 
...          
>>> print(new_s_list)
['abc', 'bcd', 'abba', 'cddc', 'opq']
>>> 
>>> src = "a2b3c6a2c3f1g1"
>>> output = ""
>>> i=0
>>> while i < len(src):
...     char = src[i]
...      i += 1
...      
SyntaxError: unexpected indent
>>> while i < len(src):
...     char = src[i]
...     i+=1
...     count = int(src[i])
...     i+=1
...     output += char * count
... 
...     
>>> print(f"output = {output}")
output = aabbbccccccaacccfg
>>> 
