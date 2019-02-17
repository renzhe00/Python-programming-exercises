# Python 练习 100 题

自己坐了一遍 [**Python-programming-exercises**](https://github.com/zhiwehu/Python-programming-exercises)，并且翻译为中文，Python 版本由 Python2.7 更新为 Python3.7

#### Question 1

Question：

编写一个程序，找到 [2000, 3200] 之间可以被 7 整除但不是 5 的倍数的所有数，获得的数字以逗号为分割打印在一行。

Hints：

使用 `range(#begin, #end)`  函数

Solution：
```python
l = []
for i in range(1000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
```
#### Question 2

Question：

编写一个程序，计算指定数字的阶乘.
```
输入: 4
输出: 40320
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

x = int(input())
print(fact(x))
```

#### Question 3

Question：

对于给定的整数 n，编写程序生成包含 `(i, i*i)` 的字典，这是区间 [1, n] 之间的整数，然后打印该字典。
```
输入： 8
输出： {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。
考虑使用 `dict()`。

Solution：
```python
n = int(input())
d = dict()
for i in range(1, n+1):
    d[i] = i*i

print(d)
```

#### Question 4

Question：

编写一个程序，它接受来自控制台的逗号分隔数字序列，并生成一个列表和一个包含每个数字的元组。
```
输入： 
34,67,55,33,12,98
输出：
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```

Hints：

- 如果输入的数据被提供给问题，则认为它是控制台输入。
- `tuple` 方法可以将 list 转换为 tuple。

Solution：
```python
values = input()
l = values.split(',')
t = tuple(l)

print(l)
print(t)
```

#### Question 5

Question：

定义一个至少包含两个方法的类：

`getString`： 从控制台获得字符串

`printString`： 将字符串大写输出

提供简单的测试例子

Hints：

使用 `__init__` 方法构造一些参数。

Solution：
```python
class InputOutString():
    def __init__(self):
        self.s = ''
    
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

test = InputOutString()
test.getString()
test.printString()
```

#### Question 6

Question：

编写一个程序，根据给定的公式计算并输出结果

Q = Square root of [(2 * C * D)/H]

其中 C=50，H=30，D 是变量，其值应以逗号分隔的顺序输入到程序中。
```
输入： 100,150,180
输出： 18,22,24
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。
将最后的结果四舍五入为整数在输出（例如 26.0，应该打印 26）。

Solution：
```python
import math

c, h, values = 50, 30, []
items = [int(x) for x in input().split(',')]
for d in items:
    value = math.sqrt(2*c*float(d)/h)
    values.append(str(round(value)))

print(','.join(values))
```

#### Question 7

Question：

编写一个程序，输入两个数字 X，Y 生成二位数组，其中第 i 行第 j 列的元素为 `i*j`。
注意：i=0,1.., X-1; j=0,1,¡­Y-1.
```
输入： 3,5
输出： [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
dims = [int(x) for x in input().split(',')]
rowNum = dims[0]
colNum = dims[1]
value = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        value[row][col] = row*col

print(value)
```

#### Question 8

Question：

编写一个程序，接受逗号分隔的单词作为输入序列，并按字母顺序排序后以逗号分隔的顺序打印单词。
```
输入： without,hello,bag,world
输出： bag,hello,without,world
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
items = [x for x in input().split(',')]
items.sort()
print(','.join(items))
```

#### Question 9

Question：

编写一个程序，一行序列作为输入，然后将句子中的字符大写输出。
```
输入：
Hello world
Practice makes perfect
输出：
HELLO WORLD
PRACTICE MAKES PERFECTD
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
for s in lines:
    print(s)
```

#### Question 10

Question：

编写一个程序，接受一系列以空格分隔的单词作为输入，在删除所有重复单词并排序后打印单词。
```
输入： hello world and practice makes perfect and hello world again
输出： again and hello makes perfect practice world
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。
我们使用 `set` 集合来自动删除重复数据，并用 `sorted()` 方法来排序数据。

Solution：
```python
words = [x for x in input().split(' ')]
words = sorted(set(words))
print(' '.join(words))
```

#### Question 11

Question：

编写一个程序，接受一系列逗号分隔的 4 位二进制数作为输入，然后检查它们是否可被 5 整除。 可被 5 整除的数字将以逗号分隔的顺序打印输出。
```
输入： 0100,0011,1010,1001
输出： 1010
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
value = []
s = [x for x in input().split(',')]
for e in s:
    dec = int(e, base=2)
    if dec%5 == 0:
        value.append(e)

print(','.join(value))
```

#### Question 12

Question：

编写一个程序，找到 [1000, 3000] 之间每一个数都是偶数的数（例如 2222）。结果以逗号分割的顺序打印在一行。

Solution：
```python
values = []
for v in range(1000, 3001):
    s = str(v)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

print(','.join(values))
```

#### Question 13

Question：

编写一个程序，计算输入的句子中字母和数字的个数。
```
输入： hello world! 123
输出： 
LETTERS 10
DIGITS 3
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
s = input()
d = {"LETTERS":0, "DIGITS":0}
for i in s:
    if i.isdigit():
        d['DIGITS']+=1
    elif i.isalpha():
        d['LETTERS']+=1
    else:
        pass

print('LETTERS: {0}\nDIGITS: {1}'.format(d['LETTERS'], d['DIGITS']))
```

#### Question 14

Question：

编写一个程序，分别计算输入句子中大写和小写字母的个数。
```
输入： Hello world!
输出：
UPPER CASE 1
LOWER CASE 9
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
s = input()
d = {'UPPER CASE':0, 'LOWER CASE':0}
for i in s:
    if i.isupper():
        d['UPPER CASE']+=1
    elif i.islower():
        d['LOWER CASE']+=1
    else:
        pass

print('UPPER CASE: {0}\nLOWER CASE: {1}'.format(d['UPPER CASE'], d['LOWER CASE']))
```

#### Question 15

Question：

编写一个程序，计算 a + aa + aaa + aaaa 的值，从终端读入 a。
```
输入： 9
输出： 11106
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
s = input()
value = int(s)+int(s*2)+int(s*3)+int(s*4)
print(value)
```

#### Question 16

Question：

使用列表推导来对列表中的每个奇数进行平方。 该列表由一系列逗号分隔的数字输入。
```
输入： 1,2,3,4,5,6,7,8,9
输出： 1,9,25,49,81
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
values = [int(x) for x in input().split(',')]
numbers = [str(x*x) for x in values if x%2!=0]

print(','.join(numbers))
```

#### Question 17

Question：

编写一个程序，可以根据控制台输入的交易日志计算银行账户的余额。交易日志格式如下：

D 100

W 200

D 表示存款，W 表示取款
```
输入：
D 300
D 300
W 200
D 100
输出：
500
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
balance = 0
while True:
    s = input()
    if not s:
        break
    value = s.split(' ')
    operation = value[0]
    amount = int(value[1])
    if operation == 'D':
        balance += amount
    elif operation == 'W':
        balance -= amount
    else:
        pass

print(balance)
```

#### Question 18

Question：

一个网站需要用户输入用户名和密码来注册，编写程序检测密码的合法性。以下是检查密码的标准：
1. [a-z] 中至少有一个。
2. [0-9] 中至少有一个。
3. [A-Z] 中至少有一个。
4. [$#@] 中至少有一个。
5. 最短密码长度 6。
6. 最长密码长度 12。

你的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。
```
输入： ABd1234@1,a F1#,2w3E*,2We3345
输出： ABd1234@1
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
import re

s = input().split(',')
correct = []
for e in s:
    if len(e)<6 or len(e)>12:
        continue
    if not re.search('[a-z]', e):
        continue
    elif not re.search('[0-9]', e):
        continue
    elif not re.search('[A-Z]', e):
        continue
    elif not re.search('[$#@]', e):
        continue
    correct.append(e)

print(','.join(correct))
```

#### Question 19

Question：

编写一个程序，按升序对（name，age，score）元组进行排序，其中 name 是字符串，age 和 score 是数字。元组由控制台输入。 排序标准是：

1. 根据 name 排序
2. 根据 age 排序
3. 根据 score 排序

排序优先级 name > age > score
```
输入：
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
输出： 
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```

Hints：

- 如果输入的数据被提供给问题，则认为它是控制台输入。
- 我们使用 `itemgetter` 开启多条件排序。

Solution：
```python
from operator import itemgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(',')))

print(sorted(l,key=itemgetter(0,1,2)))
```

#### Question 20

Question：

定义一个生成器，该生成器可以在给定的范围 0 到 n 之间迭代可以被 7 整除的数字。

Hints：

使用 `yield`。

Solution：
```python
def func(n):
    i = 0
    while i<n:
        j = i
        i += 1
        if j%7==0:
            yield j

a = func(100)
try:
    while True:
        print(next(a))
except StopIteration:
    pass
```

#### Question 21

Question：

机器人从原点（0, 0）开始从平面上移动。机器人可以在给定步数的在 UP，DOWN，LEFT 和 RIGHT 方向移动。运动轨迹如下：

UP 5

DOWN 3

LEFT 3

RIGHT 2

方向之后的数字是步长。编写一个程序，经过一系列运动后机器人距离原点的距离。如果距离为浮点数，取整为整数。
```
输入：
UP 5
DOWN 3
LEFT 3
RIGHT 2
输出： 2
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
import math

position = [0, 0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(' ')
    direction, step = movement[0], int(movement[1])
    if direction == 'UP':
        position[1] += step
    elif direction == 'DOWN':
        position[1] -= step
    elif direction == 'LEFT':
        position[0] -= step
    elif direction == 'RIGHT':
        position[0] += step

print(round(math.sqrt(position[0]**2+position[1]**2)))
```

#### Question 22

Question：

编写一个程序，计算输入句子中单词的频率，并将结果按字母顺序排序。
```
输入： New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
输出： 
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
```

Hints：

如果输入的数据被提供给问题，则认为它是控制台输入。

Solution：
```python
freq = {}
lines = input()
for word in lines.split(' '):
    freq[word] = freq.get(word, 0)+1

for word in sorted(freq.keys()):
    print('{0}:{1}'.format(word, freq[word]))
```

#### Question 23

Question：

编写一个函数可以计算数字的平方。

Hints：

使用 `**` 操作符

Solution：
```python
def square(n):
    return n**2

print(square(3))
print(square(5))
```

#### Question 24

Question：

Python 有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。 但是 Python 为每个内置函数都有一个内置的文档函数。请编写一个程序来打印一些 Python 内置函数文档，例如 abs（），int（），input（）并为你自己的功能添加文档。

Hints：

内置的文档函数是 `__doc__`

Solution：
```python
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(n):
    """Return the square value of the input number.
The input number must be integer.
    """
    return n**2

print(square(2))
print(square.__doc__)
```

#### Question 25

Question：

定义一个类，它具有类参数并具有相同的实例参数。

Hints：

- 需要在 `__init__` 中定义实例参数。
- 你可以使用构造参数初始化对象，也可以稍后设置该值。

Solution：
```python
class Person():
    name = 'Person'

    def __init__(self, name = None):
        self.name = name

renzhe = Person('renzhe')
print('{0} name is {1}'.format(Person.name, renzhe.name))

renzhe11 = Person()
renzhe.name = 'renzhe11'
print('{0} name is {1}'.format(Person.name, renzhe.name))
```

#### Question 26

Question：

定一个函数，可以计算两个数字的和。

Solution：
```python
def sum(a, b):
    return a+b

print(sum(1,2))
```

#### Question 27

Question：

定义一个函数，可以将整数转换为字符串并在终端输出。

Hints：

使用 `str()` 方法

Solution：
```python
def num2str(n):
    print(str(n))

num2str(3)
```

#### Question 28

Question：

定义一个函数，可以以字符串的形式接受两个整数，然后计算它们的和并在终端输出。

Hints：

使用 `int()` 将字符串转换为整形。

Solution：
```python
def sum(a, b):
    value = int(a) + int(b)
    print(value)

sum('1', '2')
```

#### Question 29

Question：

定义一个函数，可以接受两个字符串作为输入并连接它们，然后在控制台中打印它。

Hints：

使用 `+` 连接两个字符串。

Solution：
```python
def concatenate(s1, s2):
    return s1 + s2
    
print(concatenate('1', '2'))
```

#### Question 30

Question：

定义两个函数，该函数接受两个字符串作为输入参数，并在控制台打印长度最大的字符串。如果字符串长度相同，则逐行打印。

Hints：

使用 `len()` 计算字符串的长度。

Solution：
```python
def maxLen(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1<l2:
        print(s2)
    elif l1==l2:
        print(s1)
        print(s2)
    else:
        print(s1)

maxLen('www', 'qqq')
maxLen('q', 'www')
```

#### Question 31

Question：

定义一个函数，它接受整数作为输入，如果是偶数输出 "It is an even number"，如果是奇数输出 "It is an odd number"。

Hints：

使用 `%` 操作符。

Solution：
```python
def checkNum(n):
    if n%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")

checkNum(2)
checkNum(3)
```

#### Question 32

Question：

定义一个函数，可以打印一个字典。其中键是区间 [1, 3]，值是键的平方。

Hints：

- 使用 `dict[key]=value` 将条目放入字典。
- 使用 `**` 操作符计算平方。

Solution：
```python
def dicts():
    d = dict()
    d[1] = 1
    d[2] = 2**2
    d[3] = 3**2
    print(d)

dicts()
```

#### Question 33

Question：

定义一个函数，接受两个整数参数 a, b。打印一个字典，字典的键是区间 [a, b] 之间的数，值是键的平方。

Hints：

- 使用 `dict[key]=value` 将条目放入字典。
- 使用 `**` 操作符计算平方。

Solution：
```python
def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    print(d)

dicts(1, 20)
```

#### Question 34

Question：

定义一个函数，接受两个整数参数 a, b。创建一个字典，字典的键是区间 [a, b] 之间的数，值是键的平方。最后该函数只打印值。

Hints：

- 使用 `dict[key]=value` 将条目放入字典。
- 使用 `**` 操作符计算平方。
- 使用 `dict.values()` 获取值。

Solution：
```python
def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    for v in d.values():
        print(v, end=' ')

dicts(1, 20)
```

#### Question 35

Question：

定义一个函数，接受两个整数参数 a, b。创建一个字典，字典的键是区间 [a, b] 之间的数，值是键的平方。最后该函数只打印键。

Hints：

- 使用 `dict[key]=value` 将条目放入字典。
- 使用 `**` 操作符计算平方。
- 使用 `dict.keys()` 获取键。

Solution：
```python
def dicts(a, b):
    d = dict()
    for i in range(a, b+1):
        d[i] = i**2
    
    for k in d.keys():
        print(k, end=' ')

dicts(1, 20)
```

#### Question 36

Question：

定义一个函数，接受两个整数参数 a, b。创建并打印一个列表，列表的值是区间 [a, b] 数字的平方。

Hints：

- 使用 `**` 操作符计算平方。
- 使用 `list.append(value)` 方法给列表添加值。

Solution：
```python
def printList(a, b):
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(l)

printList(1,20)
```

#### Question 37

Question：

定义一个函数，接受两个整数参数 a, b。创建一个列表，列表的值是区间 [a, b](b-a > 5) 数字的平方。该函数只输出列表的前五个元素。

Hints：

- 使用 `**` 操作符计算平方。
- 使用 `list.append(value)` 方法给列表添加值。
- 使用切片操作获得前五个元素。

Solution：
```python
def printList(a, b):
    if b-a<5:
        return
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(l[:5])

printList(1,20)
```

#### Question 38

Question：

定义一个函数，接受两个整数参数 a, b。创建一个列表，列表的值是区间 [a, b](b-a > 5) 数字的平方。该函数只输出列表的最后五个元素。

Hints：

- 使用 `**` 操作符计算平方。
- 使用 `list.append(value)` 方法给列表添加值。
- 使用切片操作获得后五个元素。

Solution：
```python
def printList(a, b):
    if b-a<5:
        return
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(l[-5:])

printList(1,20)
```

#### Question 39

Question：

定义一个函数，接受两个整数参数 a, b。创建一个列表，列表的值是区间 [a, b](b-a > 5) 数字的平方。该函数输出除前五个元素之外的其他全部元素。

Hints：

- 使用 `**` 操作符计算平方。
- 使用 `list.append(value)` 方法给列表添加值。
- 使用切片操作获得除前五个元素之外的其他全部元素。

Solution：
```python
def printList(a, b):
    if b-a<5:
        return
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(l[5:])

printList(1,20)
```

#### Question 40

Question：

定义一个函数，接受两个整数参数 a, b。创建并打印一个元组，元组的值是区间 [a, b] 数字的平方。

Hints：

- 使用 `**` 操作符计算平方。
- 使用 `list.append(value)` 方法给列表添加值。
- 使用 `tuple()` 从列表获得一个元组。

Solution：
```python
def printTuple(a, b):
    l = list()
    for i in range(a, b+1):
        l.append(i**2)
    
    print(tuple(l))

printTuple(1,20)
```

#### Question 41

Question：

使用给定的元组（1,2,3,4,5,6,7,8,9,10），编写一个程序，在一行中打印前半部分值，在另一行中打印后半部分值。

Hints：

使用切片获得部分元组。

Solution：
```python
tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)
```

#### Question 42

Question：

编写一个程序来生成和打印另一个元组，其值在给定元组（1,2,3,4,5,6,7,8,9,10）中是偶数。

Hints：

使用 `tuple()` 从列表获得一个元组。

Solution：
```python
tp = (1,2,3,4,5,6,7,8,9,10)
l = list()
for i in tp:
    if i%2==0:
        l.append(i)

print(tuple(l))
```

#### Question 43

Question：

编写一个程序，可以使用 `filter` 函数过滤列表中的偶数，列表是：[1,2,3,4,5,6,7,8,9,10]。

Hints：

- 使用 `filter()` 函数过滤列表中的元素。
- 使用 `lambda` 定义匿名函数。

Solution：
```python
l = [1,2,3,4,5,6,7,8,9,10]
evenNums = filter(lambda x: x%2==0, l)
print(list(evenNums))
```

#### Question 44

Question：

编写一个程序，使用 `map()` 创建一个列表，其中元素是 [1,2,3,4,5,6,7,8,9,10] 的平方。

Hints：

- 使用 `map()` 创建一个列表。
- 使用 `lambda` 定义匿名函数。

Solution：
```python
l = [1,2,3,4,5,6,7,8,9,10]
new_l = map(lambda x: x**2, l)
print(list(new_l))
```

#### Question 45

Question：

编写一个程序，使用 `map()` 和 `filter()` 函数创建一个列表，其中元素是 [1,2,3,4,5,6,7,8,9,10] 偶数的平方。

Hints：

- 使用 `map()` 创建一个列表。
- 使用 `filter()` 函数过滤列表中的元素。
- 使用 `lambda` 定义匿名函数。

Solution：
```python
l = [1,2,3,4,5,6,7,8,9,10]
new_l = map(lambda x: x**2, filter(lambda x: x%2==0, l))
print(list(new_l))
```

#### Question 46

Question：

编写一个程序，使用 `filter()` 函数创建一个列表，其中元素是区间 [1,20] 之间的偶数。

Hints：

- 使用 `filter()` 函数过滤列表中的元素。
- 使用 `lambda` 定义匿名函数。

Solution：
```python
evenNums = list(filter(lambda x: x%2==0, range(1,21)))
print(evenNums)
```

#### Question 47

Question：

编写一个程序，使用 `map()` 函数创建一个列表，其中元素是区间 [1, 20] 之间数字的平方。

Hints：

- 使用 `map()` 创建一个列表。
- 使用 `lambda` 定义匿名函数。

Solution：
```python
l = list(map(lambda x: x**2, range(1,21)))
print(l)
```

#### Question 48

Question：

定义一个名为 `American` 的类，它有一个名为 `printNationality` 的静态方法。

Hints：

使用 `@staticmethod` 装饰器定义类的静态方法。

Solution：
```python
class American():
    @staticmethod
    def printNationality():
        print('American')

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```

#### Question 49

Question：

定义一个类 `American` 和其子类 `NewYorker`。

Hints：

使用 `class Subclass(ParentClass)` 定义子类。

Solution：
```python
class American():
    pass

class NewYorker(American):
    pass

anAmerican = American()
anNewYorker = NewYorker()
print(anAmerican)
print(anNewYorker)
```

#### Question 50

Question：

定一个类 `Circle` 可以使用 `radius` 构造，该类还有一个计算面积的方法。

Hints：

使用 `def methodName(self)` 定义一个方法。

Solution：
```python
class Circle():
    def __init__(self, radius):
        self.PI = 3.14
        self.radius = radius
    
    def area(self):
        return self.radius**2*self.PI

aCircle = Circle(3)
print(aCircle.area())
```

#### Question 51

Question：

定义个一个类 `Rectangle` 可以初始化两个参数 `length` 和 `width`，该类有一个计算面积的方法。

Hints：

使用 `def methodName(self)` 定义一个方法。

Solution：
```python
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

rectangle = Rectangle(2, 3)
print(rectangle.area())
```

#### Question 52

Question：

定义一个类 `Shape` 和它的子类 `Square`。`Square` 类有参数为 `length` 的 `init` 函数，两个类都有 `area` 函数，返回图形的面积，`Shape` 类的默认返回 0。

Hints：

使用 `super().__init__()` 调用父类的构造方法。

Solution：
```python
class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length**2

shape = Shape()
print(shape.area())
square = Square(4)
print(square.area())
```

#### Question 53

Question：

请抛出一个 `RuntimeError` 异常。

Hints：

使用 `raise()` 抛出一个异常。

Solution：
```python
raise RuntimeError('something wrong')
```

#### Question 54

Question：

编写一个程序计算 `5/0` 并使用 `try/except` 捕获异常。

Hints：

使用 `try/except` 捕获异常。

Solution：
```python
def compute():
    try:
        5/0
    except ZeroDivisionError:
        print('division by zero!')

compute()
```

#### Question 55

Question：

定义一个异常类，该类将字符串作为属性。

Hints：

自定义的异常类继承自 `Exception`。

Solution：
```python
class MyError(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def display(self):
        print(self.msg)

myError = MyError('something wrong!')
myError.display()
```

#### Question 56

Question：

假设我们有一些 “username@companyname.com” 格式的电子邮件地址，请编写程序以打印给定电子邮件地址的用户名。 用户名和公司名称仅由字母组成。
```
输入： john@google.com
输出： john
```

Hints：

- 如果输入的数据被提供给问题，则认为它是控制台输入。
- 使用 `\w` 匹配字母。

Solution：
```python
import re

address = input()
r = re.match(r'(\w+)@(\w+).(com)', address)

print(r.group(1))
```

#### Question 57

Question：

假设我们有一些 “username@companyname.com” 格式的电子邮件地址，请编写程序以打印给定电子邮件地址的用户名。 用户名和公司名称仅由字母组成。
```
输入： john@google.com
输出： google
```

Hints：

使用 `\w` 匹配字母。

Solution：
```python
import re

address = input()
r = re.match(r'(\w+)@(\w+).(com)', address)

print(r.group(2))
```

#### Question 58

Question：

编写一个程序，接受由空格分隔的单词序列作为输入，以打印仅由数字组成的单词。
```
输入： 2 cats and 3 dogs.
输出： ['2', '3']
```

Hints：

使用 `re.findall()` 查询所有匹配串。

Solution：
```python
import re

s = input()
r = re.findall(r'\d+', s)

print(r)
```

#### Question 59

Question：

输出一个 Unicode 字符串 `hello world!`。

Hints：

使用 `u'strings'` 格式定义 Unicode 字符串。

Solution：
```python
s = u'hello world!'

print(s)
```

#### Question 60

Question：

编写一个特殊注释，表明 Python 源代码文件是 unicode。

Solution：
```python
# -*- coding: utf-8 -*-
```

#### Question 61

Question：

编写一个程序，用控制台（n> 0）输入 n 输入计算 1/2 + 2/3 + 3/4 + ... + n /n + 1。
```
输入： 5
输出： 3.55
```

Solution：
```python
n = int(input())
sum = 0.0
for i in range(1,n+1):
    sum += float(i/(i+1.0))

print('%.2f' % sum)
```

#### Question 62

Question：

编写一个程序从控制台读入 n(n>0)，计算 f(n):

f(n)=f(n-1)+100  n>0

f(0)=1
```
输入： 5
输出： 500
```

Solution：
```python
def fn(n):
    if n==0:
        return 0
    else:
        return fn(n-1)+100

n = int(input())
print(fn(n))
```

#### Question 63

Question：

Fibonacci 数列计算方法如下：

f(n)=0 if n=0

f(n)=1 if n=1

f(n)=f(n-1)+f(n-2) if n>1
```
输入： 7
输出： 13
```

Solution：
```python
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
```

#### Question 64

Question：

编写一个程，使用列表推导以逗号分隔的形式打印斐波那契数列，并通过控制台输入给定的 n。
```
输入： 7
输出： 0,1,1,2,3,5,8,13
```

Solution：
```python
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
l = [str(fib(x)) for x in range(0, n+1)]
print(','.join(l))
```

#### Question 65

Question：

请使用生成器编写程序，以逗号分隔的形式打印 0 到 n 之间的偶数，同时通过控制台输入 n。
```
输入： 10
输出： 0,2,4,6,8,10
```

Solution：
```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```

#### Question 66

Question：

请使用生成器编写程序，以逗号分隔的形式打印可在 0 和 n 之间以 5 和 7 整除的数字，同时通过控制台输入 n。
```
输入： 100
输出： 0,35,70
```

Solution：
```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```

#### Question 67

Question：

请编写断言语句以验证列表 [2,4,6,8] 中的每个数字是否是偶数。

Hints：

使用 `assert()` 函数。

Solution：
```python
l = [2,4,6,8]
for i in l:
    assert(i%2==0)
```

#### Question 68

Question：

请编写一个程序，从控制台接受基本的数学表达式并打印评估结果。
```
输入： 35+3
输出： 38
```

Hints：

使用 `eval()` 函数。

Solution：
```python
s = input()
print(eval(s))
```

#### Question 69

Question：

编写二分搜索函数搜索排序列表中的元素。该函数应返回列表中要搜索的元素的索引。

Solution：
```python
def bin_search(l, element):
    bottom, top, index = 0, len(l)-1, -1
    while top>=bottom and index==-1:
        mid = int((top+bottom)/2)
        if l[mid]==element:
            index = mid
        elif l[mid]>element:
            top = mid-1
        else:
            bottom = mid+1
    return index

l = [1,2,4,6,8,12,17,18,56]
print(bin_search(l, 1))
print(bin_search(l, 17))
print(bin_search(l, 56))
```

#### Question 70

Question：

使用 `random` 模块生成 [10, 100] 之间的随机浮点数。

Hints：

使用 `random.random()` 生成 [0, 1] 之间的浮点数。

Solution：
```python
import random

print(random.random()*100)
```

#### Question 71

Question：

使用 `random` 模块生成 [5, 95] 之间的随机浮点数。

Hints：

使用 `random.random()` 生成 [0, 1] 之间的浮点数。

Solution：
```python
import random

print(random.random()*100-5)
```

#### Question 72

Question：

编写一个程序，使用列表推导式和 `random` 模块输出 [0, 10] 之间的随机偶数。

Hints：

使用 `random.choice()` 从列表中选择一个随机数。

Solution：
```python
import random

print(random.choice([x for x in range(11) if x%2==0]))
```

#### Question 73

Question：

编写一个程序，使用随机模块和列表推导输出一个随机数，该数字可被 5 和 7 整除，介于 [0, 200] 之间。

Hints：

使用 `random.choice()` 从列表中选择一个随机数。

Solution：
```python
import random

print(random.choice([x for x in range(201) if x%5==0 and x%7==0]))
```

#### Question 74

Question：

编写一个程序来生成一个列表，其中包含 5 个介于 [100, 200] 之间的随机数。

Hints：

使用 `random.sample()` 生成随机列表。

Solution：
```python
import random

print(random.sample(range(100, 201), 5))
```

#### Question 75

Question：

编写一个程序来生成一个列表，其中包含 5 个介于 [100, 200] 之间的随机数偶数。

Hints：

使用 `random.sample()` 生成随机列表。

Solution：
```python
import random

print(random.sample([x for x in range(100, 201) if x%2==0], 5))
```

#### Question 76

Question：

编写一个程序来随机生成一个包含 5 个数字的列表，这些数字是介于 [1, 1000] 之间可以被 5 和 7 整除的数。

Hints：

使用 `random.sample()` 生成随机列表。

Solution：
```python
import random

print(random.sample([x for x in range(1, 1001) if x%5==0 and x%7==0],5))
```

#### Question 77

Question：

请编写一个程序来压缩和解压缩字符串 "hello world！hello world！hello world！hello world!"。

Hints：

使用 `zlib.compress()` 和 `zlib.decompress()` 压缩和解压字符串。

Solution：
```python
import zlib

s = b"hello world!hello world!hello world!hello world!"

s1 = zlib.compress(s)
s2 = zlib.decompress(s1)
print(s1)
print(s2)
```

#### Question 78

Question：

编写一个程序，计算 `1+1` 运行 100 次的时间。

Hints：

使用 `time` 模块。

Solution：
```python
import time

start = time.time()
for _ in range(100):
    a = 1+1
stop = time.time()
print((stop - start)*1000)
```

#### Question 79

Question：

编写一个程序，随机打乱并输出列表 [3,6,7,8]。

Hints：

使用 `random` 模块。

Solution：
```python
import random

l = [3,6,7,8]
print(l)
random.shuffle(l)
print(l)
```

#### Question 80

Question：

请编写一个程序生成所有的句子，其中主语在 ["I", "You"] 中，动词在 ["Play", "Love"] 中，宾语在 ["Hockey","Football"] 中。

Solution：
```python
subjects, verbs, objects = ["I", "You"], ["Play", "Love"], ["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = '{0} {1} {2}'.format(subjects[i], verbs[j], objects[k])
            print(sentence)
```

#### Question 81

Question：

编写一个程序，移除列表 [5,6,77,45,22,12,24] 中的偶数后在输出。

Solution：
```python
l = [5,6,77,45,22,12,24]
new_l = [x for x in l if x%2!=0]
print(new_l)
```

#### Question 82

Question：

编写一个程序，移除列表 [12,24,35,70,88,120,155] 中可以被 5 和 7 整除的数后在输出。

Solution：
```python
l = [12,24,35,70,88,120,155]
new_l = [x for x in l if x%5!=0 and x%7!=0]
print(new_l)
```

#### Question 83

Question：

编写一个程序，移除列表 [12,24,35,70,88,120,155] 中偶数位（第 0，2,4,6...）的元素后输出。

Hints：

使用 `enumerate()` 获得格式为 `(index, value)` 的元组。

Solution：
```python
l = [12,24,35,70,88,120,155]
new_l = [x for (i, x) in enumerate(l) if i%2!=0]
print(new_l)
```

#### Question 84

Question：

使用列表推导式生成 3*5*8 的三维数组，每个元素初始为 0。

Solution：
```python
l = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
print(l)
```

#### Question 85

Question：

编写一个程序，移除列表 [12,24,35,70,88,120,155] 中第 0,4,5 位置的元素后输出。

Hints：

使用 `enumerate()` 获得格式为 `(index, value)` 的元组。

Solution：
```python
l = [12,24,35,70,88,120,155]
new_l = [x for (i,x) in enumerate(l) if i not in (0,4,5)]
print(new_l)
```

#### Question 86

Question：

编写一个程序，移除列表 [12,24,35,24,88,120,155] 中值为 24 的元素。

Solution：
```python
l = [12,24,35,24,88,120,155]
l.remove(24)
print(l)
```

#### Question 87

Question：

编写一个程序，将两个列表 [1,3,6,78,35,55] 和 [12,24,35,24,88,120,155] 中共同的元素输出为一个新列表。

Solution：
```python
l1, l2 = [1,3,6,78,35,55], [12,24,35,24,88,120,155]
set1, set2 = set(l1), set(l2)
set1 &= set2
print(list(set1)) 
```

#### Question 88

Question：

编写一个程序，删除列表 [12,24,35,24,88,120,155,88,120,155] 的中重复元素后输出，并保持列表元素原来位序。

Solution：
```python
# l = [12,24,35,24,88,120,155,88,120,155]
# print(list(set(l)))

def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```

#### Question 89

Question：

定义一个类 `Person` 和它的两个子类 `Male` 和 `Female`，所有的类都有一个方法 `getGender` 可以为 `Male` 输出 Male 和为 `Female` 类输出 Female。

Hints：

使用 `Subclass(Parentclass)` 定义子类。

Solution：
```python
class Person():
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

aMale = Male()
aFemale= Female()
print aMale.getGender()
print aFemale.getGender()
```

#### Question 90

Question：

编写一个程序，计算并输出控制台输入的字符串中每个字符出现的次数。
```
输入： abcdefgabc
输出：
a,2
c,2
b,2
e,1
d,1
g,1
f,1
```

Hints：

使用 `dict` 存储键值对。

Solution：
```python
string = input()
d = dict()
for s in string:
    d[s] = d.get(s, 0)+1

print('\n'.join(['{0},{1}'.format(k, v) for (k, v) in d.items()]))
```

#### Question 91

Question：

编写一个程序，它接受来自控制台输入字符串并以相反的顺序打印。
```
输入： rise to vote sir
输出： ris etov ot esir
```

Hints：

使用 `list[::-1]` 以相反的顺序迭代列表。

Solution：
```python
s = input()
s = s[::-1]
print(s)
```

#### Question 92

Question：

编写一个程序，它接受来自控制台的字符串并打印具有偶数索引的字符。
```
输入： H1e2l3l4o5w6o7r8l9d
输出： Helloworld
```

Hints：

使用 `list[::2]` 以步长 2 迭代列表。

Solution：
```python
s = input()
s = s[::2]
print(s)
```

#### Question 93

Question：

编写写一个程序打印 [1,2,3] 的所有排列。

Hints：

使用 `itertools.permutations()` 获得一个列表的排列。

Solution：
```python
import itertools

l = [1,2,3]
print(list(itertools.permutations(l)))
```

#### Question 94

Question：

编写写一个程序来解决一个经典的古代中国难题：

我们在一个农场的鸡和兔子中数了 35 头和 94 腿。 我们有多少只兔子和多少只鸡？

Solution：
```python
def solve(heads, legs):
    s = 'No Solvtions'
    for rabbits in range(heads+1):
        chickens = heads-rabbits
        if rabbits*4+chickens*2 == legs:
            return {'rabbits': rabbits, 
                    'chickens': chickens}
    return s

solutions = solve(35, 94)
print(solutions)
```