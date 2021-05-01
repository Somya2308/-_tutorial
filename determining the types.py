Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print (3+2<5-7)
False
>>> print(222222222.2222222*33333333.33333)
7407407407406667.0
>>> 
>>> 
>>> #lets print type of variable
>>> i=30
>>> print(type(i))
<class 'int'>
>>> i=30.30
>>> print(type(i))
<class 'float'>
>>> i=30000000000000
>>> print(type(i))
<class 'int'>
>>> i='hello'
>>> print(type(i))
<class 'str'>
>>> print(type(i),i)
<class 'str'> hello
>>> print(type(j),j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(type(j),j)
NameError: name 'j' is not defined
>>> j=None
>>> print(type(j))
<class 'NoneType'>
>>> i-123456789012345678901234567890234590
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    i-123456789012345678901234567890234590
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> i=1234567890122345678912344
>>> print(type(i))
<class 'int'>
>>> i=5>6
>>> print(type(i),i)
<class 'bool'> False
>>> i=25j
>>> print(type(i),i)
<class 'complex'> 25j
>>> i=1234567890123456789012345678901234557890028475657382920237665843992
>>> print(type(i))
<class 'int'>
>>> 