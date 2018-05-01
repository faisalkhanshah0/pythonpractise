# User defined exception

# user defined exception class

class ageException(Exception):
    """docstring for ageException."""
    def __init__(self, age):
        Exception.__init__(self)
        self.age = age;
        pass;
    def ShowError():
        print('Age {0} is too low to be an employee.'.format(age));

try:
    age=int(input('Enter Employee Age...'));
    if (age<18):
        raise ageException(age);
except EOFError:
    print('EOF is done.');
except ageException:
    print(ageException.ShowError());
else:
    print('Valid input.');
finally:
    print('this is finally block.');
