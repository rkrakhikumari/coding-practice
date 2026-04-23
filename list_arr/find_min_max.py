def find_min_max(arr):
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    return min , max
    
print(find_min_max([1,2,3,4,56,78,9,9,0])) #(0,78)
