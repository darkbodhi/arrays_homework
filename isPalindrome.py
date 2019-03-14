my_string = str()
n = int()

def isPalindrome(my_sting):
    if my_sting.isalpha():
        pass
    else:
        raise Exception("Error. The string consists not of alphabetic symbols.")
    s = list(my_string)
    while n < len(s):
       if s[n] == s[0 - n]:
           l = True
           n += 1
       else:
           l = False

    return l