#递归版本
def binary_search(data, target, low, high):
    if low > high: #所有数都比较完毕
        print("Not Found")
        return low
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            print("Found Target!")
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

#循环版本
def Binary_search(data, target):
    if target < data[0] or target > data[-1]: #检测是否在范围内
        print("Not Found")
        return False
    else:
        low = 0
        high = len(data)-1
        while(low <= high):
            mid = (low + high) // 2
            if data[mid] == target:
                print("Found Target!")
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        print("Not Found") #所有数都比较完毕
        return False

arr = [1, 5, 15, 17, 20]
index = binary_search(arr, 16, 0, len(arr)-1)
#index_2 = Binary_search(arr, 4.5)

print(index)