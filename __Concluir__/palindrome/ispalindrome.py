def palindrome(var):
    return var == var[::-1]


s = palindrome('1')

if s:
    print('Yes')
else:
    print('No')