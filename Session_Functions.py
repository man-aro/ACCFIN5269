
import os
os.chdir('C:/Users/ManishArora/Tutorials/Python_Tutorials/Session_Functions/')



def Add(x, y):
    result = x + y 
    return result 


def func(x, y):
    Add = x + y
    Product = x*y
    Diff = x - y
    return Add, Product, Diff


def Func_Matrix(x,y):  
    import numpy as np 
    Matrix = np.zeros([x, y]) 
    Size = Matrix.shape
    for i in range(Size[0]):
        for j in range(Size[1]):
            Matrix[i,j] = i*j
    return Matrix

def Func(x):
    y = x**2
    add = x + y
    prod = x * y
    return add, prod

def oddeven(x):
    if x%2 == 0:
        output = 'Input is even'
    else: 
        output = 'Input is odd'
    return print(output) 

def Fibonacci(x):
    
    if x < 0: 
        output = 'Invalid Input'
    elif (x == 0) or (x == 1):
        output = x
    else: 
        a = 0 
        b = 1 
        i = 1 #i 
        while i < x:
            c = a + b
            a = b   
            b = c
            i += 1
        output = c 
    return output 


        
        


