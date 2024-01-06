    """
     Complete the 'plusMinus' function below.
     
     The function accepts INTEGER_ARRAY arr as parameter.
     Given an array of integers, calculate the ratios of its 
     elements that are positive, negative, and zero. 
     Print the decimal value of each fraction on a new line with
     places after the decimal.

    Note: This challenge introduces precision problems. 
    The test cases are scaled to six decimal places, though 
    answers with absolute error of up to
    are acceptable.

    
    ########### EXAMPEL ###########
    arr = [1, 1, 0, -1, -1]
    arrLength = 5
    postive integers = 2 / arrLength -> 0.400000
    negative integers = 2 / arrLength -> 0.400000
    zeros = 1 / arrLength -> 0.200000
    """

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
