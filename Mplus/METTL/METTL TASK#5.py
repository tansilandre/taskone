# M+Software METTL Task #5
"""
Created by: Andre Tansil
13 April 2020
email: andretansil@gmail.com
"""
def DGenerator(N):
    Darray = [int(i) for i in str(N)]
    count = 0
    
    for i in range(0,len(Darray)):
        count += Darray[i]
        
    return N + count

def Dlist(N):
    Dlist_ = []
    
    for i in range(0,N):
        Dlist_.append(DGenerator(i))
    
    return Dlist_

def Numberlist(N):
    Nlist = []
    
    for i in range(0,N):
        Nlist.append(i)
    
    return Nlist

def SelfNumber(N):
    Dlist_ = Dlist(N)
    Nlist = Numberlist(N)
    # print(f' Dlist {Dlist_}')
    # print(f' Nlist {Nlist}')
    
    SelfNumber = set(Nlist) -  set(Dlist_)
    
    return sorted(SelfNumber)

        
N = int(input("Please type a maximum number you want to check it's Self Number: "))
result = SelfNumber(N)
print(f'List of self number are: {result}')
