def qsort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) > 1:
        tail = arr[1:]
    else:
        tail = []
    head = arr[0]
    return (
        qsort([x for x in tail if x < head]) +
        [head] +
        qsort([x for x in tail if x >= head])
    )
