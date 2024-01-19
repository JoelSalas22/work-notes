def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    min_num = min(arr)
    max_num = max(arr)
    for i in arr:
        if i <= min_num:
            min_num = i
        if i >= max_num:
            max_num = i
    min_sum = sum(arr) - max_num
    max_sum = sum(arr) - min_num
    print(f"{min_sum} {max_sum}")
