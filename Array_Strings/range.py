'''
Given a sorted list print out the numbers such that if there exists a range,
we print the range as a - b if the range is greater than or equal to 3 (a and b inclusive).

[ -2, -1, 1, 2, 3 ,4 ,7, 9 ,10 , 11] ==> [-2, -1, 1-4, 7, 9-11]
'''


def range_it(collection):
    start_range = 0
    end_range = None
    output = ''

    for i in range(len(collection)):
        previous = i - 1
        current = i
        if previous >= 0 and collection[current] - collection[previous] == 1:
            end_range = current
        else:
            if end_range is None:
                result = "{}" if not output else ", {}"
                output += result.format(collection[current])
            else:
                result = "-{}, {}" if end_range - start_range >= 3 else ", {}, {}"
                output += result.format(collection[end_range], collection[current])
                start_range = current
                end_range = None

    if end_range is not None:
        result = "-{}" if end_range - start_range >= 3 else ", {}"
        output += result.format(collection[end_range])
    return output


def range_it_2(collection):
    result_collection = []
    start_range = 0
    end_range = None

    for i in range(len(collection)):
        previous = i - 1
        current = i
        if previous >= 0 and collection[current] - collection[previous] == 1:
            end_range = current
        else:
            if end_range is None:
                result_collection.append(collection[current])
            else:
                if end_range - start_range >= 3:
                    result_collection.append(None)
                result_collection.append(collection[end_range])
                result_collection.append(collection[current])
                end_range = None

            start_range = current

    # Check ending
    if end_range is not None:
        if end_range - start_range >= 2:
            result_collection.append(None)
        result_collection.append(collection[end_range])

    # Print out Results
    output = ""
    skip_comma = False

    for i in range(len(result_collection)):
        if i == 0:
            output += "{}".format(result_collection[i])
            continue
        if result_collection[i] is None:
            output += "-"
            skip_comma = True
        else:
            if skip_comma:
                output += "{}".format(result_collection[i])
                skip_comma = False
            else:
                output += ", {}".format(result_collection[i])
    return output
