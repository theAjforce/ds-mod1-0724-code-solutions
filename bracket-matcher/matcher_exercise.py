def BracketMatcher(s):
    list_bracket=[]
    for par in s:
        if par in ["("]:
            list_bracket.append(par)
        elif par in [")"]:
            if not list_bracket:
                return False
        current_par = list_bracket.pop()
        if current_par == "(" != ")":
            return False
        else:
            return True

print(BracketMatcher("(a((kl(mns)t)uvwz)"))