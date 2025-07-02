def find_min(lst):
    if len(lst) == 0:
        return None

    min_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
    return min_val
