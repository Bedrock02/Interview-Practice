def minimumSwaps(arr):
    count = 0
    keep_swapping = True
    while keep_swapping:
        keep_swapping = False
        for i in range(len(arr)):
            if arr[i] != i + 1:
                dest_pos = arr[i] - 1
                if abs(arr[i] - arr[dest_pos]):
                    if abs(i - dest_pos) == 1:
                        arr[i], arr[dest_pos] = arr[dest_pos], arr[i]
                        count += 1
                    else:
                        continue
                else:
                    arr[i], arr[dest_pos] = arr[dest_pos], arr[i]
                    count += 1
                keep_swapping = True
    return count
