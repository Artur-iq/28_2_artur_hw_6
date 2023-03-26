def selection_sort(l1st):
    val = len(l1st)
    for i in range(val):
        min_val = i
        for v in range(i+1, val):
            if l1st[v] < l1st[min_val]:
                min_val = v
        l1st[i], l1st[min_val] = l1st[min_val], l1st[i]
    return l1st
l1st = [17,81,70,6,4,3,5,6,1000]

print(selection_sort(l1st))


def binary_search(item, l1st):
    left = 0
    right = len(l1st) - 1
    while left <= right:
        mid = (left + right) // 2
        if l1st[mid] == item:
            return mid
        elif l1st[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1

l1st = [777, 10202, 77, 1488, 60404]
item = 1488
result = binary_search(item, l1st)
if result != -1:
    print(f"Элемент {item} найден в позиции {result}")
else:
    print("Элемент не найден")