def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
BinarySearch([10,20,30,40,50], 20)
print(BinarySearch([4,4,4,4,4], 4))

print('*************************************')

def selection_sort(nlist):
    for i in range(0, len(nlist) - 1):
        smallest = i
        for j in range(i + 1, len(nlist)):
            if nlist[j] < nlist[smallest]:
                smallest = j
        nlist[i], nlist[smallest] = nlist[smallest], nlist[i]

#input list
alist = [1, 74, 96, 5, 42, 63]
print('Input List\n', alist)

#sort list
selection_sort(alist)
print('Sorted List\n', alist)