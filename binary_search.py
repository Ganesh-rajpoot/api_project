def binary_search(arr,low,high,item):
    if low<=high:
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif  arr[mid]>item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
    else:
        return -1
a = [1,2,3,4,77,5,78,9]
print(binary_search(a,0,len(a)-1,3))