#1
a=123
b=334

print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__truediv__(3))

#3
# upper()사용가능

#5
a=1
b=1
c=2
d=3
e=3

print("1:",sum([a is b, a is c, a is d, a is e]))
print("2:", sum([b is a, b is c, b is d, b is e]))
print("3 :", sum([c is a, c is b, c is d, c is e]))
print("10 :", sum([ d is a, d is b, d is c, d is e]))

#7
class Dog:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"이름은 {self.name}이고 나이는{self.age}살입니다."
my_dog= Dog("Mango",3)
print(my_dog)

#9
class Counter:
      def __init__(self, number):
          self.__number = number
      def __str__(self):
           return f'C({self.__number})'
      def __add__(self, other):
           new_number = self.__number + other.__number
           if new_number >= 100:
            new_number=0
            return Counter(new_number)
      def __sub__(self, other):
          new_number = self.__number - other.__number
          if new_number < -1:
                new_number = 0
          return Counter(new_number)

c1 = Counter(10)
c2=Counter(20)
c3=c1+c2
c4=c1-c2
print('c3=',c3)
print('c4=',c4)




