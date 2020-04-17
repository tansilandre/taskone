# M+Software METTL Task #4
"""
Created by: Andre Tansil
13 April 2020
email: andretansil@gmail.com
"""
def BinaryGap(N):
    Nbin = str(N).strip("0b")
    print(Nbin)
    NbinSize = len(Nbin)
    MaxZero = count = 0
    
    for i in range (NbinSize):
        if (Nbin[i] == '0'):
            count +=1
        elif (Nbin[i] == '1'):
            if count > MaxZero:
                MaxZero = count
            count = 0
    return MaxZero

N = int(input('Enter a number you want to find its binary gap : '))
result = BinaryGap(N)
print(f'Biggest binary gap is: {result}')