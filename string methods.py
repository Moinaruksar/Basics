Python 3.12.4 | packaged by Anaconda, Inc. | (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a n
SyntaxError: invalid syntax

a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=" "
ln(c)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ln(c)
NameError: name 'ln' is not defined. Did you mean: 'len'?
c=" "
len(c)
1
d="moina"
len(d)
5
#count
a="twinkle twinkle little star"
a.count(twinkle)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.count(twinkle)
NameError: name 'twinkle' is not defined
a="twinkle twinkle little star"
a.count("twinkle")
SyntaxError: multiple statements found while compiling a single statement
a.count("t")
5
a.count("k")
2
a.count("m")
0
a="python"
|

a[1]
'y'
a.find("n")
5
b="moina"
b.find("a")
4
c="mummy"
c.find("m")
0
a="name\nmobileno\tmailid\ncity"|
SyntaxError: invalid syntax
#RTY
a="name\nmobileno\tmailid\ncity"

print(a)
name
mobileno	mailid
city
a="name:Moina\nmobileno:987543\tmailid:kdgdy\ncity:guntur"
print(a)
name:Moina
mobileno:987543	mailid:kdgdy
city:guntur






































#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'



a="hello"
a.upper()
'HELLO'
a.lower()
'hello'
a.upper("p")
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
a.capitalize()
'Hello'
a[0]:upper()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a[0]:upper()
NameError: name 'upper' is not defined. Did you mean: 'super'?
a.title()
'Hello'






a="code"


a.isupper
<built-in method isupper of str object at 0x00007FFE6678CCE0>
a.isupper()
False
False
False
a.isalpha()
True
a.isdigit()
False
###########
a="      moina    "
a.strip()
'moina'
a.lstrip()
'moina    '
a.rstrip()
'      moina'
#split()
a="my name is moina"
a.split()
['my', 'name', 'is', 'moina']
b="monu sou tonu "
b.split()
['monu', 'sou', 'tonu']
['monu', 'sou', 'tonu']
['monu', 'sou', 'tonu']

#join()
a="monu","reenu"
a.join()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.join()
AttributeError: 'tuple' object has no attribute 'join'
##concatenation
a="code"
b="gnan"
>>> print(a+b)
codegnan
>>> print(a+" "+b)
code gnan
>>> fname="moina"
>>> lname="ruksar"
>>> print(fname+lname)
moinaruksar
>>> print(fname+" "+lname)
moina ruksar
>>> #formatting
>>> a=3
>>> b=6
>>> print(a+b)
9
>>> print("the sumis ",a+b)
the sumis  9
>>> city"guntur"
SyntaxError: invalid syntax
>>> city="guntur""
SyntaxError: unterminated string literal (detected at line 1)
>>> city="guntur"
>>> print("the city is",city)
the city is guntur
>>> #format method
>>> a="monu"
>>> b="sonu"
>>> print("hello {}{}".format(a,b))
hello monusonu
>>> print("hello {} {}".format(a,b))
hello monu sonu
>>> print("hello {} hello{}".format(a,b))
hello monu hellosonu
>>> #fstring
>>> a="monu"
>>> b="sonu"
>>> print(f"hello {a}{b}")
hello monusonu
>>> print(f"hello {a} {b}")
hello monu sonu
>>> print(f"hello {a} hello {b}")
hello monu hello sonu
