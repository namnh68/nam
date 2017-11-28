## This file is to store some examples related to the essence of python class

Assume, we have a Foo class like this:

```
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bar(self):
        print('Hello world')
```
1. When creating a instance class:

```
test = Foo('nam', 18)
```
At this time, it will call __init__ method and pass name='nam', age=18. Then
creating a instance class and assign to "test" variable.


