


class Student():
    pass #class is empty
    
class Marks(): pass
a = Student()
if isinstance(a, Student):print('Is instance.')
else: print('No')

b = Marks()
if isinstance(b, Marks):print('Is instance.')
else: print('No')

if issubclass(Student, object):print('Is sub.')
else: print('No')
if issubclass(Marks, object):print('Is sub.')
else: print('No')