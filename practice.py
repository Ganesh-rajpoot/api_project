#Python program to interchange first and last elements in a list
def inter_change(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr
# print(inter_change([1,2,3,45]))
#Python Program to Swap Two Elements in a List
def swap_two_item_list(arr,pos1,pos2):
    arr[pos1],arr[pos2] = arr[pos2],arr[pos1]
    return arr
# print(swap_two_item_list([1,2,3,4,5],1,4))
#Python | Ways to find length of list
def length_arr(arr):
    count = 0
    for i in arr:
        count += 1
    return count
# print("Length of array",length_arr([1,2,3,4,5,6,7,8]))
#Maximum of two numbers in Python
def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
# print(maximum(49,78))

#Python | Ways to check if element exists in list
def check_ele_eist(arr,item):
    if item in arr:
        return "exist"
    else:
        return "Not exist"

# print(check_ele_eist([2,3,4,5,6,1,7,88,3],2))
def clear_list(arr):
    arr = []
    return arr
# print(clear_list([2,3,4,5,6]))
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr
# print(reverse_list([1,3,4,5,6,2,7,9,0]))
#Python | Count occurrences of an element in a list
def count_occurence(arr,item):
    count = 0
    for i in arr:
        if i == item:
            count += 1
    return count
# print(count_occurence([2,3,4,5,6,1,2,3,4,5,1,3,4,5],3))
#Python Program to find sum and average of List in Python
def sum_averge(arr):
    s = 0
    l = len(arr)
    for i in arr:
        s = s+i
    
    avg = s/l
    return print("Averge",avg,' ','Summm',s)
# print(sum_averge([1,2,3,4,5]))
def sum_digit(digits):
    res = []
    for i in digits:
        sum = 0
        for j in str(i):
            sum = sum + int(j)
        res.append(sum)
    return res
# print(sum_digit([12,54,76,34,99,34]))

def multiplie_list_items(arr):
    result = 1
    for i in arr:
        result = result * i
    return result
print(multiplie_list_items([1,2,3,4,5]))


