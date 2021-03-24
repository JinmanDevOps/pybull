##编码/解码，UTF-8 GBK
'''str_s = '金满'
bytes_s = bytes(str_s,encoding='utf-8')
print(str_s)
print(bytes_s)'''

'''str_s = '金满'
bytes_s = bytes(str_s,encoding='utf-8')
str_s = bytes_s.decode(encoding='gbk')
print(str_s)'''

'''str_s = '金满'
bytes_s = bytes(str_s,encoding='utf-8')
str_s = bytes.decode(bytes_s,'gbk')
print(bytes_s)
print(str_s)'''

'''a = 13
b = 3
c = a/b
d = a//b
print(c)
print(d)
print(a%b)
print(divmod(a,b))'''

'''x = [1,3,4,5,6,6,5,4,3,2,1]
x[1] = 2
x[2] = 3
x[3] = 4
x[-1] = 5
list.append(x,6)
d = list.count(x,6)
e = x[1:-1]
print(x)
print(d)
print(e)'''

'''def func(ele):
    return ele[0]
j = [('a',1),('e',2),('b',5)]
j.sort(key=func,reverse=True)
print(j)'''

'''x = ['a','b','c',1,2]
y = x[:]
y = x.copy()
list.append(y,6)
print(y)
print(x)'''
#字典 key必须为不可变类型 数字 字符串 元组
'''x = {1:'a',2:'c',3:'d'}
dict.keys(x)
'''
'''def func(x, y, *args, **kwargs):
    print(x,y)
    print(args)
    print(kwargs)
func(1, 2, ('a,b','c,d'), [1,2,3,4], c=3, d=6)'''

'''print('hello world','how are you!',sep=' ', end='\n')
'''

'''tax = 12.5 / 100
price = 100.50
a = tax * price
print(a)
print(price + a)
print(round(a,1))
'''
'''s = 'first line. \nSecond line'
print(s)
a = r'C:\archforce\name'
print(a)
print(len(a))

cubes = [1,2,3,4,5]
cubes[2:5] = []
cubes[:] = []
print(cubes)
'''

#fibonacci series:
#the sum of two elements defines the next
'''a, b = 0 , 1
while a < 99:
    print(a,end=',')
    a,b = b,a+b
'''
'''x = int(input('please input a integer:'))
if x < 0:
    print('negtive changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')
'''
'''words = ['cat','lion','mouse']
for o in words:
    print(o,len(o))
'''
'''
for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]

for users,status in users.items():
    if status == 'active':
        active_users[user] =status
'''

'''a = ['Mary','Starry','Joe']
for i in range(len(a)):
    print(i,a[i])
'''
'''for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

for n in range(2,10):
    if n % 2 == 0:
        print('find a even number',n)
        continue
    print('find a odd number',n)'''


'''def fib(n):
   # print a fibonacci series up to n
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()
#now call the funciton we just defined:
fib(2000)
'''

'''def fib2(n):
    result = []
    a,b=0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)'''

'''def ask_ok(prompt, retries=4, reminder='do you really want to go!' ):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'ye'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
i = 5
def f(arg=i):
    print(arg)
f()
'''
'''def f1(a, L=[]):
    L.append(a)
    return L
print(f1(2))
print(f1(4))
print(f1(6))
print(f1(8))'''

'''def f(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(11))'''

'''def parrot(voltage, state='a stiff', action='voom', type='norwegian Blue'):
    print('-- This parrot wouldn\'t' , action, end=' ')
    print('if you put',voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- It\'s', state, '!' )
parrot('a million', 'bereft of life', 'fly')
parrot(1)

parrot('a thousand', state='pushing up the daisies')'''

'''def function(a):
    pass
function(0, a=0)'''


'''def cheeseshop(kind,*arguments,**keywords):
    print('-- Do you have any', kind, '?')
    print('-- I\'m sorry, we\'re all out of', kind)
    for arg in arguments:
        print(arg)
    print('_'*40)
    for kw in keywords:
        print(kw,':', keywords[kw])
cheeseshop('Money', "it\'s very runny, sir",
           'it\'s really very , VERY runny, Sir.',
           shopkeeper='Michael Palin',
           Client='John Cleese',
           Sketch='Cheese Shop Sketch')
'''

'''def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
standard_arg(arg=2)
pos_only_arg(1)
kwd_only_arg(arg=3)
combined_example(2,standard=2,kwd_only=3)

def foo(name, /,  **kwds):
    return 'name' in kwds
foo(1,**{'name': 2})'''


'''def write_multiple_items(file, separator, *args):
    file.wirte(separator,join(args))'''

'''def concat(*args, sep='/'):
    return sep.join(args)
concat('earth', 'mars', 'venus', sep=".")
print(concat('earth', 'mars', 'venus', sep="."))'''

'''list(range(3,6))
args = [3,6]
list(range(*args))'''

'''def make_incrementor(n):
    return lambda x: x+n
f = make_incrementor(42)
f(0)
print(f(0))
print(f(1))
print(f(2))'''

'''pairs = [(1, 'one'), (2, 'two'), (3, "three"), (4, 'four')]
pairs.sort(key=lambda pairs:pairs[0])
pairs
print(pairs)

def my_function():
    Do nothing, but document it.

    No, really, it doesn\'t do anything
    pass
print(my_function.__doc__)'''

'''def f(ham: str, eggs: str = 'eggs') ->str:
    print('annotations:',f.__annotations__)
    print('arguments:', ham, eggs)
    return ham + ' and ' + eggs
f('spam')
print(f('spam'))'''

'''fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('tangerine'))


stack = [3, 4, 5]
stack.append(6)

from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
print(queue)'''

'''combs = []
for x in [1, 2, 3]:
    for y in [7, 8, 9]:
        if x != y:
            combs.append((x,y))
print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x**2 for x in vec if x <= 0])
print([abs(x) for x in vec])'''

'''from math import pi
print([str(round(pi, i)) for i in range(1, 6)])'''

'''matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
#print([[row[i] for row in matrix] for i in range(4)])
row1 = []
for i in range(4):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    row1.append(new_row)
print(row1)
print(list(zip(*matrix)))'''

'''a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[:]
print(a)

#元祖
t = (12345, 54321, 'hello')
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)
print(u[0])
'''
'''basket = {'apple', 'orage', 'apple', 'pear', 'orange', 'banana'}
print(basket)'''

'''a = set('abracadabra')
b = set('alacazam')'''

'''a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)'''

'''a = set('abracadabra')
b = set('abc')
print(a-b)'''

'''knights = {'gallahad': 'the true', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}.' .format(q, a) )'''

'''import math
raw_data = [56.2, float('NaN'), 51.7, 55.6, 52.3, float('NaN'), 66.6, 88.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

{x: x**2 for x in (2, 4, 6)}

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
'''
'''yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
print(percentage)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

s = 'hello, world.'
s


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f' {name:10} ==> {phone:10}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')
print(f'My hovercraft is full of {animals!a}.')
print(f'My hovercraft is full of {animals!s}.')

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print(' {0} and {1}'.format('spam', 'eggs'))
print(' {1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
    food = 'spam', adjective = 'absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other = 'Georg'))

table = {'Sjoerd': 1235, 'Jack':7689, 'Dcab':94857}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};'
      'Dcab: {0[Dcab]:d}'.format(table))
print(table)

for x in range (1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x**x))'''

'''import jinja2
from jinja2 import Template
template = Template('Hello{{ name }}!')
template.render(name='John Doe')
print(template)'''

'''squres = []
for x in range(10):
    squres.append(x**2)
print(squres)'''

'''def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b , a+b
    print()
fib(100)'''

'''def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
print(fib2(100))'''

'''def ask_ok(promt, retries = 4, reminder = 'Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', "yes"):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)'''

'''def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print('-- This parrot wouldn\'t', action, end=' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- It\'s', state, '!')
parrot(voltage=10000, action='VooooM')'''

'''def  wirte_multiple_items(file, separator, *args):
    file.write(separator,join(args))'''

'''def concat(*args, sep='/'):
    return sep.join(args)
concat('earth', 'mars', 'venus')

def my_function():
    Do nothing, but document it.

    No, really, it doesn't do anything.
     
    pass

print(my_function.__doc__)'''

'''def f(ham: str, eggs: str = 'eggs') -> str:
    print('Annotations:', f.__annotations__)
    print('Arguments:', ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))'''

'''combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))'''


'''table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

print('This {food} is {adjective}.'.format(food = 'spam', adjective = 'absolutely horrible'))

print('The story of {0}, {1}, {others}.'.format('Bill', 'Manfred', others='Geoge'))
for x in range(1, 11):
    print('{0:1d}  {1:10d}  {2:10d}'.format(x, x*x, x*x*x))
    print(repr(x).rjust(2), repr(x*x).rjust(10), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(10))
'''

'''a = 1
b = 2
result = a + b
print("计算 1 + 2 的结果")
print("计算结果为:", result)'''


import random
str_A = random.randint(1, 255)
str_B = random.randint(1, 255)
str_C = random.randint(1, 255)
str_D = random.randint(1, 255)
random_IPv4 = "%d.%d.%d.%d" % (str_A, str_B, str_C, str_D)
print(random_IPv4)