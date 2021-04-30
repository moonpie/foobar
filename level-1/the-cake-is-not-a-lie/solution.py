def solution(s):

    max_slices = 0
    min_leftovers = len(s)

    for slice_size in range(len(s)):
        if slice_size == 0:
            continue
        for start_index in range(len(s) - slice_size):
            pattern = s[start_index:start_index + slice_size]
            slices = s.count(pattern)
            leftovers = len(s) - (len(pattern) * slices)
            if leftovers < min_leftovers:
                min_leftovers = leftovers
                max_slices = slices
            start_index += 1

    return max_slices