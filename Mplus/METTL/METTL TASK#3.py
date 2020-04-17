# M+Software METTL Task #3
"""
Created by: Andre Tansil
13 April 2020
email: andretansil@gmail.com
"""

def CompressString(s):
    s = list(s)
    s_size = len(s)
    count = 1
    result = []
    for i in range(0,s_size-1):
        if (s[i] == s[i+1]):
            count += 1
        else:
            result.append(s[i])
            result.append(str(count))
            count = 1
    result = ("".join(result))
    return result


s = input("Please type string you want to compress: ") + "z"
result = CompressString(s)
print(f'Compressed string is {result}')