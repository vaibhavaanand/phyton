Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,"hey",4,5,6.3]
>>> a[1]
2
>>> a[-2]
5
>>> a[2:4]
['hey', 4]
>>> len(a)
6
>>> a.insert(4,"bye"]
SyntaxError: invalid syntax
>>> a.insert(4,"bye")
>>> a
[1, 2, 'hey', 4, 'bye', 5, 6.3]
>>> a.remove(5)
>>> a
[1, 2, 'hey', 4, 'bye', 6.3]
>>> a.pop()
6.3
>>> a.pop(3)
4
>>> a
[1, 2, 'hey', 'bye']
>>> a.clear()
>>> a
[]
>>> a=[9,1,4,lilly,16]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=[9,1,4,lilly,16]
NameError: name 'lilly' is not defined
>>> a=[2,4,"lilly",8,16]
>>> a
[2, 4, 'lilly', 8, 16]
>>> a.remove("lilly")
>>> a
[2, 4, 8, 16]
>>> a.sort()
>>> a
[2, 4, 8, 16]
>>> a.reverse()
>>> a
[16, 8, 4, 2]
>>> a=["c","h","a","n"]
>>> a.count("a")
1
>>> 

