# Python Notes

## Game Plan

-   start by learning the basic python syntax
-   Then Object Oriented Programming
-   THEN we create our own servers!
-   Testing
-   SQL, and python integration

---

---

## Why Python?

-   fast, powerful, widely used.
-   high level
-   easy syntax
-   runs on servers
-   good for data science, machine learning, making servers
-   very good for resumes.

---

# VARIABLES

-   Python variable name style is _like_this_ (lower snake case)
-   There is no _keyword_ to declare a variable.

```python
chickens = 13
```

```python
chickens = 20
```

-   we can just declare and update willy nilly

The fact that there is no keyword to declare variables means there is no const  
Python developers use ALL CAPS to signify a constant. But it can still be changed.

-   "Lexical function scoped"

    ```python
    x = 42
    def my_function():
        x = 12
        print(x)    # 12

    print(x)        # 42
    ```

-   Note the different values for "x"

# Numbers

### Python has integers and floating points

```python
type(5)
# int
type(5.0)
# float
```

-   there's also complex numbers so yeah

### operations:

-   add, subtract, multiply, divide, etc
-   also have "integer divide" which takes the floor of a division

```python
10//3
# 3

int(2.33232)
# 2
```

-   also have power functions _3\*\*2_ is 3 sq.
-   ## "is_integer"

# STRINGS

-   single or double quotes
-   triple quoted strings!
    -   these allow you to escape special characters real easy like
    ```python
    '''
    <div>
        <h1>HI</h1>
    <div>
    '''
    ```
    -   (also use triple """ if you like)
-   a lot of string methods
-   _f-strings_ are like template literals in js

    ```python
    f"2+2={2+2}"
    # '2+2=4'

    first = "Channing"
    last = "Tatum"
    full = f"Mr. {first} {last}"

    full
    # 'Mr. Channing Tatum'
    ```

-   print(1,2,3) ...prints! shock!

-   Python is not _strictly typed_.
    -   a variable can be changed to any type.

---

# LISTS

### Lists are Python's analog to arrays

-   use square brackets _[ ]_
-   lists are ordered
-   can be _heterogeneous_ (can include multiple types of data)

---

# BOOLEANS

### True and False are always capitalized.

-   True
-   False

```python
3 < 5
# True

3 > 5
# False

'13' > 1
# This is a type error. Python doesn't like it.

```

## Equality:

-   In Python we have

| Syntax |      Description       |
| :----: | :--------------------: |
|   ==   |         equals         |
|   !=   |       not equal        |
|   is   |    object equality     |
| is not | negated object equlity |

---

-   In JS we have

    -   == _loose equality_

        ```javascript
        7 == "7"; //true
        ```

    -   === _strict equality_

            ```javascript
            7 === "7"   //false
            ```

        -Objects and arrays are only equal when they have the same identity

---

-   In PYTHON
    -   == equality (strict about types)
        ```python
        7 == "7"            #False
        ```
    -   Structures with same items **_ARE_** equal
        ```python
        [1,2,3] == [1,2,3]  #True
        ```
    -   use **_is_** to check obj identity
        ```python
        [1,2,3] is [1,2,3]  #False
        ```

---

---

---

---

---

# INDENTATION

---

---

---

---

---

## PYTHON is an indented language.

### Rather than using _{ }_ to show a code block, Python uses indentation

```python
if age >= 18:
    print("Please go vote!")    # the indentation is how python
    register_to_vote()          # knows what code is what
```

---

```python
if age >= 18:
    print("Please go vote!")    # if the second line isn't indented
register_to_vote()              # then it will ALWAYS run
```

---

As opposed to Javascript

```javascript
if (age >= 18) {
    console.log("Please go vote");
    registerToVote();
}
```

---

## In Python, everyone agrees indentation should be 4 spaces

-   ipython will automatically indent for us

---

# Running Python from a file

We don't run python from a browser. There are a few different ways in which we can run python code.

1. Use python3 straight from command line, right from the shell.
    ```
    python3 filename.py
    ```
    It will:
    - load file
    - execute code
    - take you back to the shell
    ***
2. Use ipython
    ```ipython
    %run filename.py
    ```
    - in ipython, we get access to the variables and such.
    - it won't take us out to the shell. it runs the code, and then we stay in the lovely warm python environment.
        - decent for debugging
    ***

# CONDITIONALS

## In Javascript:

```javascript
if (one === theOther) {
    console.log("hi");
} else if (one === theThird) {
    console.log("hello");
} else {
    return;
}
```

## In Python

```python
if:
    indented code
elif:           # "elif" instead of "else if"
    more
else:
    still more
```

```python
age = 19

if age >= 21:
    print("Drink like a little fishy")
elif age >= 18:
    print("Come on in. Don't you dare drink")
else:
    print("Please leave. We don't need anymore trouble with the cops")
```

---

# Ternary Operation

## In JavaScript:

```javascript
let msg = age >= 18 ? "go vote!" : "go play!";
```

## In Python

```python
msg = "go vote!" if (age >= 18) else "go play!"
```

-   in Python it's maybe a little easier to read.

---

# Boolean Operations

## And/Or/Not

-   JS - `&&`, `||`, `!`
-   python - `and`, `or`, `not`
    -   wow, so clean and simple

| Operation | Result                                     |
| --------- | ------------------------------------------ |
| `x or y`  | if `x` is false, then `y`, else `x`        |
| `x and y` | if `x` is false, then `x`, else `y`        |
| `not x`   | if `x` is false, then `True`, else `False` |

These are short circuit operations. eg: if the `x` half evaluates, then it won't run the `y` half.

### often useful to use parentheses to clarify your statements

---

# Truthiness (and falsiness)

-   in JS, some things are "falsy":
    -   `0`
    -   `0.0`
    -   `""`
    -   _undefined_
    -   _null_
    -   _NaN_
    -   _false_
-   Certain things are (maybe unexpectedly) "truthy"
    -   `{ }`
    -   `[ ]`

---

-   in Python, these things are falsy:
    -   `0`
    -   `0.0`
    -   `" "`
    -   `None`
        -   kind of like `null`. Sometimes we can use it to initialize a variable.
    -   `False`
    ***
-   These are FALSY (unlinke in JS)

    -   `[ ]` (empty list)
    -   `{ }` (empty dictionary)
    -   `set( )` (empty set)

    ***

# `While` Loops

```python
  num = 0
  while num <= 100:
    print(num)
    num += 10
  print("all done")
```

##### There is no `num++` sort of deal like int JS

---

simple input:

```python
guess = input("Enter your guess")
```

HERE IS A SIMPLE GUESSING GAME

```python
target = 37
guess = None

while guess != target:
    guess = input("Please enter a guess... ")
    if guess == 'q' or guess == 'quit':
        break
    guess = int(guess)

print("ALL DONE")

# We loop for as long as it takes to guess.
# 'q' or 'quit' escapes the loop using `break`
```

---

# For Loops

### In Python there is no equivalent to the JS `for` loop.

Python `for` loops are more like JS `for...of` loops

```python
for snack in ["Peanut", "Twizzler", "Mars Bar"]:
	print("I ate a ", snack)
```

To loop 5 times:

```python
for num in "abcde":
    print("HELLO")
```

---

# Range

-   Range is a simpler way to iterate over `x` times...

```python
for num in range(5):
	print(num)
# Makes [0, 1, 2, 3, 4]
```

-   **range**(_stop_)
-   **range**(_start_, _stop_[, *step*])

##### The range always takes the same amount of memory! It only stores the stop, start and step. It calculates the rest

---

In: `list(range(10))`  
Out: `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

---

In: `list(range(5,10))`  
Out: `[5, 6, 7, 8, 9]`

##### Note how it does not include the stop point

---

In: `list(range(-100, 0))`  
Out: `[-100, -99, ... , -1]`

##### Negative numbers!

---

In: `list(range(1, 10, 2))`  
Out: `[1, 3, 5, 7, 9]`

##### Step of 2

---

In: `list(range(10, 0, -1))`  
Out: `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`

##### To count down we add a step of `-1`

---

# FUNCTIONS

### Use the `def` keyword to define a function

```python
def add_numbers(a, b):
	sum = a + b
	print("doing maths")
	return sum
```

Return value is `None` unless explicitly changed.

## Arguments

-   arguments are required by default. Unlike in JS where we can skip some and leave them undefined.
    -   in python we will get an error.

```python
def send_email(to_email, from_email, subject, cc, bcc, body):
```

-   Python has something called _Named_ or _Keyword_ arguments
-   the order can be mixed up, but entered as like a key-value pair.

---

```python
def send_email(to_email, from_email, subject, body):
  email = f"""
    to: {to_email}
    from: {from_email}
    subject: {subject}
    ----------------------
    body: {body}
    """
  print(email)

send_email(subject="MEAOW", to_email="blue@cat.com",
   from_email="Colt@people.com", body="Hi, you are cat. meaow")
```

To check which arguments a function requires, type `help(func_name)`...`q` to get out of it.

### Default values.

```python
def power(num, power=2):
  return num ** power
```

##### This removes the need to input the argument value.

---

# Getting Help

## dir( )

"Show me the methods and attributes of this object"

```python
dir([])
['__add__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

---

## help( )

`help()` brings us to python's help utility.  
`ctrl d` to escape

---

## **WE** get to write our own "help" documentation.

### Comments and Docstrings

-   `#`: rest of line is a comment.
-   A String as the very first thing in a file/function is a _"docstring"_
    -   Use it to document what the function/file does
    -   Shown when you ask for `help(some_function)`

```python
def add_limited_numbers(a, b):
  """Add two numbers, making sure sum caps at 100."""
    sum = a + b
    # If this required a comment, go ahead
    if sum > 100:
        sum = 100
	return sum
```

### Most good python libraries have really good _internal_ documentation. So make good use of the `help()` function.
