# Questions for students because they aren't ready
## How to do this

1. The way you do this test is by starting from the [questions](#questions) (obviously). For each question it'll tell you if you should be programming the solution for it (**denoted by a \* at the starting of the question**). After you are done doing the questions go to [answers](#answers) and check your work.

2. If you need to be programming a solution go to the file named [functions.py](functions.py) and program your solution in the correct function. For example when you program ***unit 2 question 5***, program it under the function named ***u2q5***.

3. If a question does not start with a \*, then you don't need to program the solution. As long as whatever you think matches up with the answers you are fine.
___
## **Questions**

### **Unit 2**

1. What are the primitive data types in Python?

2. How do I assign x the value cake?

3. What data type is x below?
```
x = "3.14"
```
4. What will the code below output?

```
x = 10

if x <= 10:
    print(1)

elif x < 11:
    print(2)

if x == 10:
    print(3)

else:
    print(4)
```
5. *Write a program to take an input from the user and return the cube value of it. (You cannot use the math library)
```
function(2) -> 8
function(-3) -> -27
```
6. What data type will x be?
```
x = str(int(input()))
```
7. What will this loop print?
```
for i in range(10):
    if i < 9:
        break
    print(i)
```
8. Using a while loop ask the user for a (int) under 100 and if the user inputs a value above 100 ask them again.
___
### **Unit 3**
1. *Return the sum of all the numbers which are divisible by 15 from [1, n].
```
function(15) = 15
function(30) = 45
```
2. Why would someone use a for loop instead of a while loop?

3. *Given the input n, figure out the sum of the values 1/1 + 1/2 ... + 1/n.
```
function(1) = 1
function(2) = 1.5
function(3) = 1.8(3)
```
4. Print out a triangle shaped like this using a for loop
```
*
**
***
****
*****
```
5. *Implement a bisection search that will return the index of a given number
```
function([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) -> 0
function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) -> -1
```
6. How are floats different compared to integers?
___
### **Unit 4**
1. In this function what will x print?
```
x = 2
def foo():
    x = 3

foo()
print(x)
```
2. Create a function that will take 2 variables (int, string) and call them x and y respectively. After that return them in the opposite order.

3. Create a function that will add two numbers and return the output.

4. Following from the previous question, Change one of the parameters to become an optional parameter (set the optional parameter to 1).

5. *Following from the previous question, Using the new function make it so that it will only return a value if the sum of both the numbers is greater 20 (exclusive). If the number is less than 20 than return None.

6. Will this work? If so, what will be the output. If not, why so?
```
def foo(x=1, y):
    return x + y

print(foo(5, 10))
```
7. Will this work? If so, what will be the output. If not, why so?
```
def foo(x, y=23, z=12):
    return x + y

print(foo(x=5, z=10, y=2))
```

8. What is recursion? Give an example. The code doesn't need to anything just show how it would actually work.

9. *Given a list of numbers use print out every letter in a sentence.
```
function([1, 2, 3]) -> 6
function([1, 2, 3, 4, 5]) -> 15
```
10. *Figure out whether a string is a palindrome.
```
function("taco cat") -> True
function("Racecar") -> True
function("randomstring") -> False
```
11. Name 3 types of data structures.
___
### **Unit 5**
1. What is a list?

2. How are lists stored in RAM?

3. How would I get the last value in a list?

4. What is a tuple and how is it different from a list?

5. How would I reverse a list?

6. What are the 2 different type of possible cloning for a list? What's the difference between them? (Bonus give an example)

7. *Program a list comprehension that will list all values between -n and n (inclusive).
```
functions(2) -> [-2, -1, 0, 1, 2]
```
8. What will this list contain?
```
[i ** 2 for i in range(0, 10) if i % 2]
```
9. *Given a list of words, using a list comprehension, return a list containing all of the given list words if the word does contain an e.
```
function(["The", "quick", "brownie", "fox"]) -> ["quick", "fox"]
function(["The", "Earth", "likes", "treEs", "E"]) -> []
```
10. *Given a list of words, using a list comprehension, return a list containing all of the length of all the length of the words in order.
```
function(["The", "quick", "brownie", "fox"]) -> [3, 3, 5, 7]
function(["OH", "NO", "THE", "TABLE"]) -> [2, 2, 3, 5]
```

## **Answers**

### **Unit 2**
1. String, Integers, floats, doubles

2. 
```
x = "Cake"
```
3. String

4. 
```
1
3
```
6. String

7. Nothing

8. 
```
while True:
    num = int(input("Num: "))
    if num < 100:
        break
```
___
### **Unit 3**
2. You should use a for loop when you know how many times the loop should run. 
4.
```
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```
6. Integers can store natural numbers and floats can store numbers with a decimal point.
___
### **Unit 4**
1. 2
2. 
```
def foo(x, y):
    return y, x
```
3.
```
def foo(x, y):
    return x + y
```
4.
```
def foo(x, y=1):
    return x + y
```
6. No, the function will not work as the optional argument is before the mandatory argument.

7. Yes, the function will work and it will output the value 7.

8. Recursion is when a function call's itself.
```
def foo():
    return foo()
```
11. List, sets, tuples. Others might include hashmaps, dictionaries, trees, trie tree
___
### **Unit 5**
1. A list is a data structure that can hold multiple values.

2. Lists' data is stored side by side in RAM

3. 
```
list_name[-1]
```
4. A tuple is a type of a list but once it is created cannot be modified.

5. 
```
list_name[::-1]
```

6. Shallow and deep clone. A shallow clone will retain the memory address, which means if you were to edit the newly shallow cloned list the original list would change as well. A deep clone will create new memory addresses and if you were to edit the new list nothing would happen the the original.
```
og_list = [1, 2]
shallow_list = og_list
shallow_list[0] = 3

print(og_list)      -> [3, 2]
print(shallow_list) -> [3, 2]

og_list = [1, 2]
deep_list = og_list[:]
deep_list[0] = 3

print(og_list)   -> [1, 2]
print(deep_list) -> [3, 2]
```
8. 
```
[0, 4, 16, 36, 64]
```