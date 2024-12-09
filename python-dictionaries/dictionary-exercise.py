def making_dict(n):
    binary_dict = {}
    for num in range(n+1):
        bin_dict_str = ''
        temp_remain = num
        while temp_remain != 0:
            remainder = temp_remain % 2
            bin_dict_str = str(remainder) + bin_dict_str
            temp_remain//=2
        if len(bin_dict_str) <4:
            bin_dict_str = '0'* (4-len(bin_dict_str)) +bin_dict_str
        binary_dict[num] = bin_dict_str
    return binary_dict

print(making_dict(15))