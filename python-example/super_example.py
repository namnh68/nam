class Foo(object):
    def __init__(self):
        self.name = 'Hoai Nam'


class Bar(object):
    def __init__(self, school):
        super(Bar, self).__init__()
        self.school = school

a = Bar('ptit')
print a.school