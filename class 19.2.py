#11
class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        self._korean_quiz = 0
        self._math_quiz = 0
        self._science_quiz = 0
        self._total_score = 0
    

 def __str__(self):
        avg = self.get_avr_score()
        return f"{self._name}, {self._student_id}, 총점: {self._total_score}, 평균: {avg}"

    def get_name(self):
        return self._name

    def get_student_id(self):
        return self._student_id

    def get_korean_quiz(self):
        return self._korean_quiz

    def get_math_quiz(self):
        return self._math_quiz

    def get_science_quiz(self):
        return self._science_quiz

    def set_korean_quiz(self, score):
        self._korean_quiz = score
        self._update_total()

    def set_math_quiz(self, score):
        self._math_quiz = score
        self._update_total()

    def set_science_quiz(self, score):
        self._science_quiz = score
        self._update_total()

    def _update_total(self):
        self._total_score = self._korean_quiz + self._math_quiz + self._science_quiz

    def get_total_score(self):
        return self._total_score

    def get_avr_score(self):
        return self._total_score / 3

#13
 class Rectangle:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __str__(self):
        return f"(x = {self._x}, y = {self._y}, w = {self._width}, h = {self._height}), 면적 : {self.area()}"

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def area(self):
        return self._width * self._height

    def contains(self, r):
        return (self._x <= r._x and
                self._y <= r._y and
                self._x + self._width >= r._x + r._width and
                self._y + self._height >= r._y + r._height)

    def overlaps(self, r):
        return not (self._x + self._width <= r._x or
                    r._x + r._width <= self._x or
                    self._y + self._height <= r._y or
                    r._y + r._height <= self._y)

