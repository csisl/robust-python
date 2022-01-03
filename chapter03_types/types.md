# Types

Types are a form of communication with two types of representation:

  1. Mechanical Representation
     Communicate behaviors and constraints to the Python language
  2. Semantic Representation
     Communicate behaviors and constraints to developers 
     
Python is a **strongly typed language**. This means that operations are restricted
to supported types.

For example, you cannot add a list and dict together. 

```
>>> [] + {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "dict") to list
```

It is also a **dynamically typed language**. You can change the type of a variable
at runtime.

```
>>> x = 10
>>> type(x)
<type 'int'>
>>> x = "test"
>>> type(x)
<type 'str'>
```



