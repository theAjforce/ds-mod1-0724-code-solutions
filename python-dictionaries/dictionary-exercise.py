def making_dict(n):
    binary_dict = {}
    for num in n:
        bin_dict_str = ''
        temp_remain = num
        while num > 0:
            remainder = num % 2
            bin_dict_str = str(remainder) + bin_dict_str
            temp_remain //=2
        if len(bin_dict_str) <4:
            bin_dict_str = '0'* (4-len(bin_dict_str)) +bin_dict_str
        binary_dict[num] = bin_dict_str
    return binary_dict

print(making_dict(15))