def get_indices(element, lst):
    indices = []
    for i in range(len(lst)):
        if lst[i] == element:
            indices.append(i)
    return indices
my_list = [3, 5, 2, 3, 8, 3, 1]
element = 3
indices = get_indices(element, my_list)
print(indices)
