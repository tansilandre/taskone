# M+Software METTL Task #2
"""
Created by: Andre Tansil
13 April 2020
email: andretansil@gmail.com
"""

def LongestPrefixSuffix(s):
    s_size = len(s)
    
    for part in range(s_size//2,0,-1):
        prefix = s[0:part]
        suffix = s[s_size-part:s_size]
        
        if (prefix == suffix):
            return part
        
    return 0

s = input("Insert a character you want to find the longest prefix that also a suffix: ")
result=LongestPrefixSuffix(s)
print(f'Longest prefix that contain suffix is: {result}')