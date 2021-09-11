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

str1 = 'hello world'

str2 = 'hello python'

print(editMyStr(str1, str2, len(str1), len(str2)))

