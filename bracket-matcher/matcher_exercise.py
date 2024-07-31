def BracketMatcher(s):
    count = 0
    for par in s:
        if par == '(':
            count += 1
        elif par == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

print(BracketMatcher("(a((kl(mns)t)uvwz)"))