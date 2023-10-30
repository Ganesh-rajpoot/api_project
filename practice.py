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
# print(multiplie_list_items([1,2,3,4,5]))
# Python program to find second largest number in a list
def secondlargest(arr):
    l1 = list(set(arr))
    l1.sort()
    return l1[-2]
# print(secondlargest([2,3,41,2,4,5,2,4,2,5,2,5,46,5,6]))
# Python program to print even numbers in a list
def even_number(arr):
    even_num = [ i for i in arr if i % 2 == 0]
    return even_num
# print(even_number([2,3,4,6,7,8,54,7,8]))
def duplicate_element(arr):
    unique_ele = []
    duplicate_ele = []
    for i in arr:
        if i in unique_ele:
            unique_ele.append(i)
        elif i not in duplicate_ele:
            duplicate_ele.append(i)
    return duplicate_ele
# print(duplicate_element([3,4,5,6,2,3,3,4,5,6]))

# Python – Remove empty List from List
def remove_empty_list(arr):
    l = [i for i in arr if i != []]
    return l
# print (remove_empty_list([1,2,3,[],4,[],44,[],3,5,[]]))
#Convert numeric words to numbers
def num_words_to_number(strings):
    num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
    }
    result = ""
    for ele in strings.split():
        result += num_dict[ele]
    return result
# print(num_words_to_number('zero four zero one'))
def check_palindrom(txt):
    mid = (len(txt)-1)//2
    low = 0
    high = len(txt)-1
    flag = 0
    while low<=mid:
        if txt[low] == txt[high]:
            high -=1
            low +=1
        else:
            flag = 1
            break
    if flag == 0:
        return "The enter string is palindrome"
    else:
        return "The enter string is not palindrome"
    
# print(check_palindrom('amaama'))
# Reverse words in a given String in Python
def revers_string(txt):
    return txt[::-1]
# print(revers_string('ganesh'))
def revers_string_ws(txt):
    l = []
    s = txt.split()[::-1]
    for i in s:
        l.append(i)
    return ' '.join(l)
print(revers_string_ws('this is my laptop'))
