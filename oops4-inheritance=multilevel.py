class One:
    """docstring fo One."""
    def func1(self):
        print('func1 from class One.');

class Two(One):
    """docstring fo Two."""
    def func2(self):
        print('func2 from class Two.');

class Three(Two):
    """docstring fo Three."""
    def func3(self):
        print('func3 from class Three.');

three = Three();
three.func1();
three.func2();
three.func3();
print('---------');
