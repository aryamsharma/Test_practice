# Questions for students because they aren't ready
## FAQ
1. For some reason <= is formatted like `<=`. Don't ask.

2. Any questions that begin with an asterisk (\*), you are supposed to program the solution. There will be no answer written down for it. ***I will write out the files in the same format your test will be given to you in.***

3. For the questions I'm writing whenever I'm asking for an input I'll normally tell you what type of input you want but on the test they are normally vague about it do if they say numbers ***assume integers UNLESS the question talks about floats.***
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
8. *Given a list of numbers use print out every letter in a sentence.
```
function([1, 2, 3]) -> 6
function([1, 2, 3, 4, 5]) -> 15
```
9. Figure out
___
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
