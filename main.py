def commonCharacters(strings):
    shortStr = getShortestString(strings)
    inAllList = []

    for ch in shortStr:
        if isInAll(ch, strings):
            if ch not in inAllList:     # allows for duplicate characters in the string. Only add it once
                inAllList.append(ch)
    return inAllList

def getShortestString(strings):
    shortStr = strings[0]   # initialize to the first string in the strings list
    for st in strings:
        if len(st) < len(shortStr):
            shortStr = st

    return shortStr

def isInAll(ch, strings):
    stringCount = 0     # the number of strings that the character is in

    for st in strings:
        if ch in st:
            stringCount += 1

    if stringCount < len(strings):
        return False
    else:
        return True


if __name__ == '__main__':
    print(commonCharacters(["abc", "bcd", "cbaccd"]))
    print(commonCharacters(["abc", "ab", "abc", "a"]))
    print(commonCharacters(["a", "d", "cbaccd"]))
    print(commonCharacters(["abcde", "bcd", "b"]))
    if "apple" in ["apple", "banana"]: print ("yes")
