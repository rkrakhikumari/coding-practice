def sec_largest(arr):
    first = sec = float("-inf")
    for num in arr:
        if num > first:
            sec = first
            first = num
        elif num > sec and num != first:
            sec = num
    return num
    
print(sec_largest([1,2,3,4,5,6,8,98,9080,754,5,24,5657]))
