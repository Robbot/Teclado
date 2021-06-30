class ClassTest:
    def instance_method(self):
        print(f"Called instance of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
print(book.book_type)

print(book) #This would not be possible without __repr__ method in class

hardcover = Book.hardcover("Harry Potter", 1500)
print(hardcover)
paperback = Book.paperback("Python 101", 600)
print(paperback)


"""
Antoher example provided by Teclado
We’ve looked at how we can define classes and methods, including some special methods like `__init__` and `__len__`.

All these methods had something in common: the `self` parameter at the start. As a reminder, here’s some code:
"""

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

"""
When we create a new object from the `Student` class and we call a method, we are automagically passing in the `self` parameter:
"""

rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())

"""
This is identical to that last line:
"""

print(Student.average(rolf))

"""
When we do `object.method()`, Python is in the background calling `Class.method(object)`, so that `self` is always the object that called the method.

Indeed, if we were to have two objects:
"""

rolf = Student('Rolf', 'MIT')
anne = Student('Anne', 'Cambridge')

rolf.marks.append(78)
rolf.marks.append(99)

anne.marks.append(34)
anne.marks.append(56)

print(rolf.average())
print(anne.average())

"""
In the first case, `self` would be the `rolf` object, and in the second case `self` would be the `anne` object.

Notice that this knowledge now lets us do some very weird stuff (not recommended, as it’ll likely break things):
"""

Student.average('hello')  # self is now 'hello', comment this out to run the rest of the file.

"""
Just remember `self` is a parameter like any other; and you can give it any value you want. However, because the method is then accessing `’hello’.marks`, you’ll get an error for the string doesn’t have that property.

Anyway, so why is this important?

The first type of method we’ve looked at is called “instance method”: one that takes the caller object as the first argument (that’s `self`).

There are two more types of method:

* One that takes the caller’s class as the first argument; and
* One that takes nothing as the first argument.
"""

## @classmethod
"""
Let’s look at the one that takes the caller’s class as the first argument.
"""

class Foo:
  @classmethod
  def hi(cls):
    print(cls.__name__)

my_object = Foo()
my_object.hi()  # prints Foo

## @staticmethod
"""
Now one that takes nothing as the first argument.
"""

class Foo:
  @staticmethod
  def hi():
    print("I don't take arguments!")

my_object = Foo()
my_object.hi()

"""
Those are some terrible examples! Let’s look at some more in the next section.
"""