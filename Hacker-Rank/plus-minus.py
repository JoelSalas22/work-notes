def plusMinus(arr):
    # Write your code here
    length_of_array = len(arr)
    post_total = 0
    neg_total = 0
    zero_total = 0
    for element in arr:
        if element < 0:
            neg_total += 1
        elif element > 0:
            post_total += 1
        else:
            zero_total += 1
    # print(postTotal)
    # print(negTotal)
    # print(zeroTotal)
    neg_ratio = neg_total / length_of_array
    post_ratio = post_total / length_of_array
    zero_ratio = zero_total / length_of_array
    print(post_ratio)
    print(neg_ratio)
    print(zero_ratio)
