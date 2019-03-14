Title: Basic Data-Types in Python
Date: 2019-01-22 00:00
Category: Data Analytics with Python

Every variable has a type in Python. As everything in Python is an object. Datatypes are the classes, and the variables
are instances of these classes.

`type` is used to determine the class an object belongs to and
`isinstance` is used to check if an object belongs to a particular class.

```python
>>> x = 4
>>> type(x)
<type 'int'>
>>> isinstance(x, str)
False
>>> isinstance(x, int)
True
``` 


Among many various data types in Python, these are the important types are listed below.

   - integer, floats: 3, 4.5
   - string: 'hello world'
   - list: [4, 're', 1.4]
   - tuple: (4, 5)
   - set: {2, 4}
   - dictionary: {1: 'one', 2: 'two'}
   
### **Integers, Floats**

These are for storinng numerical data. Numerical data can be of three types: Integer, Float and Complex. Python offers
all these three. But let's focus on Integer and Float only.

Python interprets the decimal digits without any prefix. For example: 
```python
>>> x = 4
>>> x
4
```

For **binary numbers** append `0b` or `0B` before the number representation.
```python
>>> x = 0b111
>>> x
7
```

For **octal numbers** append `0o` or `0O` before the number representation.
```python
>>> x = 0o101
>>> x
65
```


For **hexadecimal numbers** append `0x` or `0X` before the number representation.
```python
>>> x = 0x101
>>> x
257
```

Floating points are accurate upto 15 decimal places. In representation, numbers are separated by a dot(.).
```python
>>> x = 1.12345678910111213
>>> x
1.1234567891011122
```


### **Strings**

Strings are the sequence of unicode characters. These sequence must be enclosed by single quotes, double quotes or triple quotes.
```python
>>> x = 'hello world'
>>> x
'hello world'
>>> x = "hello world"
>>> x
'hello world'
>>> x = '''hello world'''
>>> x
'hello world'
```
Slicing operations are allowed only to read values from strings like:
```python
>>> x = '''hello world'''
>>> x[6:12]
'world'
```

Value assignment at any index is not possible in string.

```python
>>> x = '''hello world'''
>>> x[6] = 'W'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```
This means once a string objects is created, it cannot be changed which makes them `immutable` data type.

### **List**

A list is a ordered sequence of items. The items can be of any data types.
```python
>>> x = [1, 'hello world', 1.2]
>>> x
[1, 'hello world', 1.2]
```
Slicing operations and Value assignment are allowed in list.
```python
>>> x = [1, 'hello world', 1.2]
>>> x[1] = 'world'
>>> x
[1, 'world', 1.2]
```

### **Tuple**

A tuple is a sequence of items like list but with a difference that once created, it cannot be
changed later. It means value assignment is not allowed, just like strings. It is defined by putting
parenthesis around comma separated items.

```python
>>> x = (2, 'hello world', 3)
>>> x
(2, 'hello world', 3)
>>> x[1] = 'world'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
Tuple is also an `immutable` data-type.

### **Set**

A set is an unordered collection of unique items.

```python
>>> x = {1, 2, 2, 3, 3, 3, 4}
>>> x
set([1, 2, 3, 4])

```
As sets are unordered, index access is not allowed on them.
```python
>>> a = {1,2,3}
>>> a[1]
Traceback (most recent call last):
  File "<string>", line 301, in runcode
  File "<interactive input>", line 1, in <module>
TypeError: 'set' object does not support indexing

```

### **Dictionary**

A dictionary is an collection of key-values pairs. They are meant to be used for accessing random key data.
```python
>>> x = {1 : 'one', 2: 'two', 3: 'three'}
>>> x[1]
'one'
>>> x[3]
'three'

```
One important thing to remember about dictionary is that only `immutable` data-types can be keys.



This pretty much covers the basic types of data-types in python. There are more specialized
data types like dates and times, queues, fixed-type arrays etc. Just like the other data types
they also have some special property which comes very handy while working with real data. We will be soon
exploring them.

Goodbye until then.