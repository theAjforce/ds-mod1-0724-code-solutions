#Write a function to create two lists, one for the alphabet variable below and one for the index of the alphabet variable

abc = "abcdefghijklmnopqrstuvwxyz"

def create_lists():
    abc_list = list(abc)
    index_list = list(range(1, len(abc_list)+1))
    return index_list,abc_list

abc_tuple, index_tuple = tuple(create_lists())

#Join the two lists together and return a list of tuples L = ‘abcdefghijklmnopqrstuvwxyz’ Example Output = [(1, ‘a’), (2, ‘b’), (3, ‘c’), ...]

def join_lists():
    combined = zip(abc_tuple,index_tuple)
    print(list(combined))
join_lists()