def Binary_search(data, target):
    if target < data[0] or target > data[-1]: #检测是否在范围内
        print("Not Found")
        return False
    else:
        low = 0
        high = len(data)-1
        while(low <= high):
            #mid = (low + high) // 2
            mid = low + (high - low) * (target-data[low]) // (data[high]-data[low])
            if data[mid] == target:
                print("Found Target!")
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        print("Not Found") #所有数都比较完毕
        return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
index = Binary_search(arr, 1)

print(index)