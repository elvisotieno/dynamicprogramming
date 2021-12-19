def pair_sum(list, target):
    '''
    funtion return all the unique pairs of list elements that sum up to given target
    time complexity: o(n)
    '''
    pairs = []  # for storing the list of pairs that sums up to k
    seen = set()  # for storing the elements of the list which are alredy seen

    for num in list:

        diff = target - num
        # if target value is found in the seen set
        # then the sum of target and list current element is equal to target
        # Thus we add target & current num touple onto the pairs list
        if diff in seen:
            pairs.append((min(diff, num), max(diff,num)))

        # if target value is not found in the seen set
        # means the sum of any element of seen set with the current element doesnot yields to target
        # Thus we simply add current element of the list to the seen set in a hop that may be this added_current_element_values can be summed up with upcomming element to produce  k
        else:
            seen.add(num)
    return pairs

list = [1, 2, 3, 4, 5, 6, 7]
pairs = pair_sum([1, 2, 3, 4, 5, 6, 7], 7)
print(pairs)