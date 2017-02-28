# Example for setattr build-in function

class Foo():
    def do_something(self, name, value):
        setattr(self, name, value) # This is quivalent to "self.name = value"

bar = Foo()
bar.do_something('abc', 'hoai nam')
print bar.abc
