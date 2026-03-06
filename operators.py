Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5
b=10
a
5
b
10
print(a+b)
15
print(a-b)
-5
print(a*b)
50
print(a/b)
0.5
print(a**b)
9765625
print(a//b)
0
prit(a%b)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    prit(a%b)
NameError: name 'prit' is not defined. Did you mean: 'print'?
print(a%b)
5
a+=b
a+=b
a+=b
a
35
b
10
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
45
b
10
a-=b
a
35
b
10
a*=b
a
350
b
10
a//=b
a
35
b
10
a/=b
a
3.5
b
10
a**=b
a
275854.7353515625
b
10
a%=b
a
4.7353515625
b
10
a=5
b=10
a<b
True
a>b
False
b>a
True
b<a
False
a<=b
True
a>=b
False
b<=a
False
b>=a
True
a!=b
True
b!=a
True
a==b
False
b==a
False
a=5
b=10
a<b
True
b<a
False
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<=b or b>=a
True
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
true
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=3
if type(a) is int:
    print("it is int")

    
it is int
>>> if type (a) is float:
...     print("it iS float")
... 
...     
>>> 
>>> if type(a) i not float:
...     
SyntaxError: invalid syntax
>>> if type(a) is not float:
...     print("it is int")
... 
...     
it is int
>>> a=2,3,4,5,6,7,8
>>> if 8 in a:
...     print(8)
... 
...     
8
>>> if 10 in a:
...     print(10)
... 
...     
>>> 
>>> if 10 not in a:
...     print(10)
... 
...     
10
>>> if type(a) i not float:
...     
SyntaxError: invalid syntax
>>> 
>>> a=2
>>> b=5
>>> a&b
0
>>> bin(2)
'0b10'
>>> bin(5)
'0b101'
>>> a=3
>>> b=4
>>> a&b
0
