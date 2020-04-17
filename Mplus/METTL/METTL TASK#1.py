# M+Software METTL Task #1
"""
Created by: Andre Tansil
13 April 2020
email: andretansil@gmail.com
"""

def MaxDifference(x,x_size):
    max = x[1]-x[0]
    
    for i in range(0,x_size):
        for j in range(i+0,x_size):
            if(x[j]-x[i] > max):
                max = x[j]-x[i]
                
    return max

x_size = int(input("How many array you want to input? "))
x=[]
for i in range(0,x_size):
    x.append(int(input(f'Please input your array number {i} : ')))
max = MaxDifference(x,x_size)
print(f'This set of number difference is: {max}')
