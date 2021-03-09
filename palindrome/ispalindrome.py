def palindrome(var):
    return var == var[::-1]


s = palindrome('ovo')

if s:
    print('Yes')
else:
    print('No')