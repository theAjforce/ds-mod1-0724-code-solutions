def is_anagram(str_1,str_2):
    if sorted(str_1) == sorted(str_2):
        return True
    else:
        return False
    
print(is_anagram('cautioned','education'))