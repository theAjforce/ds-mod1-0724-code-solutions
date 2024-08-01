def letters_to_symbols(s):
    result = ""
    count = 1
    current_letter = ""
    for letter in s:
        if letter == current_letter:
            count += 1
        else:
            if current_letter:
                result += str(count) + current_letter
                count = 1
        current_letter = letter
    if count > 0:
        result += str(count) + current_letter
    return result

print(letters_to_symbols("aaabbbsssxxx"))