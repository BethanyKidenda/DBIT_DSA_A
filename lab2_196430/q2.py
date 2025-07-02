def find_max(lst):
    if len(lst) == 0:
        return None

    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val
