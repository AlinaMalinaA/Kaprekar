MIN = 3  # minimum number of repeats


# gets string, returns repeating part
def find_period(s):
    tail = s[::-1]  # reverse number
    for ind, d in enumerate(tail):
        temp = tail[:ind+1]
        L = len(temp)
        k = 1
        while L*k <= len(tail):
            if k < MIN:
                if temp == tail[L*k:L*(k+1)]:
                    k += 1
                else:
                    break
            else:
                return temp[::-1]
        return 0


if __name__ == "__main__":
    testString = "0.2271714922048997772828507795100222717149220489977728285077951002227171492204899777282850779510022"
    testString = testString[testString.index(".")+1:]  # removes parts before dot and dot itself
    print(find_period(testString))
    # 27171492204899777282850779510022
