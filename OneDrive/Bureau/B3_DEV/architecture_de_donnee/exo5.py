def rotation_d(lst, n):
    return lst[-n % len(lst):] + lst[:-n % len(lst)]