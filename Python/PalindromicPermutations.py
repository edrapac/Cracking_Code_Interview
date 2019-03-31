def isPalindromicPermutation(s):
    charset = {}
    for i in range(len(s)):
        if s[i] in charset.keys():
            charset[s[i]] += 1
        else:
            charset[s[i]] = 1
            oddcount = 0
    for val in charset.values():
        if val == 1:
            oddcount += 1
            if oddcount > 1:
                return False
        if val > 1 and val % 2 != 0:
            return False

    return True
