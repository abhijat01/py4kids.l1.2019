# Plan 

* More on variables, types and operations 
* Introduce lists and indexing 
* Changing lists - append and pop 
* For loop with lists 
* Introduce range 

# Variables continued 

Will the following code work? 

```python
a=49 
b=input("Enter number:")
c=b+a
```

What is wrong with it? How can you fix it? 

```python
a=49 
b=input("Enter number:")
b = int(b) 
c=b+a
print(c)
```

What does int(b) mean? 

Guess the output of the following code:
```python
a=5
b=9
c=b*a
print(c) 
c = a/b 
print(c) 
c = b/a
print(c) 
c = b//a 
print(c) 
c = b%a 
print(c)  
```

# Keeping track of more than one thing at a time 

```python
kids=["Prateek", "Svadrut", "Meghna", "Sanjana", "Ishaan", "Sid", "Ari" , "Shloak"] 

print(kids[0] )
print(kids[4])
print(kids[9] )
```
Listing all kids 
```python
kids=["Prateek", "Svadrut", "Meghna", "Sanjana", "Ishaan", "Sid", "Ari" , "Shloak"] 

print(kids[0] )
print(kids[4])

for kid in kids: 
    print("The kid is:{}".format(kid))
```
What does ``for`` do ? What about the indents? What is the "`:`"?

## Two dimensional data 

![](./code-02/simple_matrix.png)<!-- .element height="50%" width="50%" -->


## Complex Two dimensional data, homework 
![](./code-02/joke_matrix.png)<!-- .element height="50%" width="50%" -->

You can download the Joke code by [clicking here](https://raw.githubusercontent.com/abhijat01/py4kids.l1.2019/master/module-01/code-02/joke_matrix.py) . For viewing the code online, go to the [github page](./code-02/joke_matrix.py) 


