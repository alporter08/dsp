# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both contain a sequence of comma separated elements.  However, lists are mutable whereas tuples are immutable. Lists are represented within square brackets, whereas tuples are represented within parentheses.  Tuples will work as keys in dictionaries because they are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists can contain duplicate elements whereas sets cannot.  Sets are unordered, and elements are found using a hash lookup, which results in better performance.  Lists are faster for iterating through elements.    
Sets are useful when comparing elements and finding ones that exist in one set and not another.

In the examples below, a set and a list are compared with another set and list respectively.  The output is the elements in the first sequence that do not appear in the second.

**Set example:**
```python
>>> s1 = {'dog', 'cat', 'tiger'}
>>> s2 = {'dog','bird', 'lizard'}
>>> s1-s2
set(['tiger', 'cat'])
```

**List example:**
```python
>>> l1 = ['dog', 'cat', 'tiger']
>>> l2 = ['dog', 'bird', 'lizard']
>>> for i in l1:
...     if i not in l2: 
...             print i
... 
cat
tiger
```
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda functions are small anonymous functions.  They can be used where a function would be expected.  They are useful for operations that only need to occur at the moment the function is called.  They are often used in conjuction with `map()` and `filter()`.

```python
>>> animals = [('cat', 'black'), ('dog', 'golden'), ('fish', 'blue')]
>>> sorted(animals, key=lambda animal: animal[1])
[('cat', 'black'), ('fish', 'blue'), ('dog', 'golden')]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a compact and concise way to create and manipulate lists.

**List comprehension example and comparison with `map` and `filter`**

The code below creates a list of 4 numbers (1-4) multiplied by 3.

List comprehension
```python
>>> threes = [x*3 for x in range(1,5)]
>>> threes
[3, 6, 9, 12]
```
Using `map`
```python
>>> l = range(1, 5)
>>> threes = list(map(lambda x: x*3, l))
>>> threes
[3, 6, 9, 12]
```
List comprehension
```python
>>> items = [1, -2, 4, 5, -7]
>>> positive = [x for x in items if x > 0]
>>> positive
[1, 4, 5]
```
Using `filter`
```python
>>> items = [1, -2, 4, 5, -7]
>>> pos = filter(lambda x: x > 0, items)
>>> pos
[1, 4, 5]
```
The capabilities between these list comprehensions and `map` and `filter` are similar, but some consider list comprehensions as being cleaner and more pythonic.

**Set comprehension**
```python
>>> s1 = {'cat', 'dog', 'horse'}
>>> s2 = {'fish', 'snake', 'horse'}
>>> s = {x for x in s1 if x in s2}
>>> s
set(['horse'])
```
**Dict comprehension**
```python
>>> {x: x*3 for x in range(10)}
{0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 5: 15, 6: 18, 7: 21, 8: 24, 9: 27}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





