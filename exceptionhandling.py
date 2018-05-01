"""
try:
    text = input('enter anything');
except EOFError:
    print('why did you do an EOF on me?'); #ctrl+D
except KeyboardInterrupt:
    print('You cancelled the operation.'); #ctrl+C
else:
    print('You entered {0}'.format(text));
"""

"""
try:
    text = input('enter anything');
except (EOFError, KeyboardInterrupt):
    print('why did you do an EOF on me?'); #ctrl+D
else:
    print('You entered {0}'.format(text));
"""

try:
    text = input('enter some value');
except: #will handle all exception
    print('This will handle all exception.'); #try some interrupts like ctrl+D/ctrl+C
else:
    print('I will be executed only if there is no exception.');
print('Process Over.');
