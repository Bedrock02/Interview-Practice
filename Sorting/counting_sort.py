def count_sort(collection, range_num=256):
    l = [list() for _ in range(range_num)]
    for j in range(len(collection)):
        l[collection[j]].append(collection[j])

    output = []
    for i in range(len(l)):
        output.extend(l[i])
    return output
