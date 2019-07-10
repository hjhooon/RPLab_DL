def check(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

str1, str2 = 'abcd', 'badc'
str3, str4 = 'sbcf', 'kabc'

print(check(str1,str2))
print(check(str3,str4))