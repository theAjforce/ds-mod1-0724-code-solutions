def making_dict():
    binary_dict = {}
    for num in range(15):
        binary_dict[num] = bin(num)
    return binary_dict
print(making_dict())