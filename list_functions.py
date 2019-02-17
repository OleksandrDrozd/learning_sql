# Transform original list into a list of tuples. From [1, 2, 3] to [(1,), (2,), (3,)]
def create_list_of_tuples(original_list):
    new_list = []
    for i in original_list:
        new_list.append(tuple([i]))
    return new_list
