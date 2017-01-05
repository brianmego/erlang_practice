def qsort(arr):
    if len(arr) == 0:
        return []
    pivot = arr[0]
    tail = arr[1:]
    return (
        qsort([x for x in tail if x < pivot]) +
        [pivot] +
        qsort([x for x in tail if x >= pivot])
    )
