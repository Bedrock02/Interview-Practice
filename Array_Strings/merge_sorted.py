'''
Given two sorted lists, merge them to create one sorted list
Each array given is does not have duplicates within the list
'''

from collections import defaultdict


def merge_sorted_arrays(list_a, list_b):
    if not list_a and not list_b:
        return []

    if list_a and not list_b:
        return list_a

    if list_b and not list_a:
        return list_b

    low_a, high_a = list_a[0], list_a[-1]
    low_b, high_b = list_b[0], list_b[-1]

    if high_a < low_b:
        return list_a + list_b

    if high_b < low_a:
        return list_b + list_a

    if low_a <= low_b:
        return [low_a] + merge_sorted_arrays(list_a[1:], list_b)
    return [low_b] + merge_sorted_arrays(list_a, list_b[1:])


def merge_sorted_arrays_no_slice(list_a, list_b):
    if not list_a and not list_b:
        return []

    if list_a and not list_b:
        return list_a

    if list_b and not list_a:
        return list_b

    low_a, high_a = list_a[0], list_a[-1]
    low_b, high_b = list_b[0], list_b[-1]

    if high_a < low_b:
        return list_a + list_b

    if high_b < low_a:
        return list_b + list_a

    collection = []
    i = 0
    j = 0
    list_a_limit = len(list_a)
    list_b_limit = len(list_b)

    while True:

        if i >= list_a_limit and j >= list_b_limit:
            return collection

        elif i < list_a_limit and j >= list_b_limit:
            collection.append(list_a[i])
            i += 1

        elif i >= list_a_limit and j < list_b_limit:
            collection.append(list_b[j])
            j += 1

        else:
            if list_a[i] <= list_b[j]:
                collection.append(list_a[i])
                i += 1
            else:
                collection.append(list_b[j])
                j += 1


def merge_sorted_arrays_no_dups(list_a, list_b):
    if not list_a and not list_b:
        return []

    if list_a and not list_b:
        return list_a

    if list_b and not list_a:
        return list_b

    low_a, high_a = list_a[0], list_a[-1]
    low_b, high_b = list_b[0], list_b[-1]

    if high_a < low_b:
        return list_a + list_b

    if high_b < low_a:
        return list_b + list_a

    # first remove the dups from smaller collection
    smaller, larger = (list_a, list_b) if len(list_a) <= len(list_b) else (list_b, list_a)
    smaller = [item for item in smaller if not in_collection(item, larger)]
    if larger[0] <= smaller[0]:
        return [larger[0]] + merge_sorted_arrays(larger[1:], smaller)
    return [smaller[0]] + merge_sorted_arrays(larger, smaller[1:])


def merge_sorted_arrays_no_dups_no_slice(list_a, list_b):
    if not list_a and not list_b:
        return []

    if list_a and not list_b:
        return list_a

    if list_b and not list_a:
        return list_b

    low_a, high_a = list_a[0], list_a[-1]
    low_b, high_b = list_b[0], list_b[-1]

    if high_a < low_b:
        return list_a + list_b

    if high_b < low_a:
        return list_b + list_a

    collection = []
    exists_in_collection = defaultdict(bool)
    i = 0
    j = 0
    list_a_limit = len(list_a)
    list_b_limit = len(list_b)

    def insert_item(item):
        if exists_in_collection[item]:
            return
        collection.append(item)
        exists_in_collection[item] = True

    while True:

        if i >= list_a_limit and j >= list_b_limit:
            return collection

        elif i < list_a_limit and j >= list_b_limit:
            insert_item(list_a[i])
            i += 1

        elif i >= list_a_limit and j < list_b_limit:
            insert_item(list_b[j])
            j += 1

        else:
            if list_a[i] <= list_b[j]:
                insert_item(list_a[i])
                i += 1
            else:
                insert_item(list_b[j])
                j += 1


def in_collection(search_value, collection):
    if not collection:
        return False

    mid_point = len(collection) // 2
    if collection[mid_point] == search_value:
        return True

    if collection[mid_point] < search_value:
        return in_collection(search_value, collection[mid_point + 1:])
    return in_collection(search_value, collection[:mid_point])
