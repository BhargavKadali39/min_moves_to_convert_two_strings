#simple yet confusing

def editMyStr(str1, str2, m, n):
    if m == 0:
        return n
    if n== 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editMyStr(str1, str2, m-1, n-1)
    return 1 + min(editMyStr(str1, str2, m, n-1),
                   editMyStr(str1, str2, m-1, n),
                   editMyStr(str1, str2, m-1, n-1))

str1 = str(input('Enter string 1 :\n'))

str2 = str(input('Enter string 2 :\n'))

print(editMyStr(str1, str2, len(str1), len(str2)))

#Don't give input very big,as it might get stuck in a loop for a long time.
