def mergeSort(lst):
    if len(lst) == 1:
        return lst, 0
    else:
        n = len(lst) // 2
        lst1, count1 = mergeSort(lst[0:n])
        lst2, count2 = mergeSort(lst[n:len(lst)])
        lst, count = Count(lst1, lst2, 0)
        return lst, count1 + count2 + count


def Count(lst1, lst2, count):
    i = 0
    j = 0
    res = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] >= lst2[j]:
            res.append(lst2[j])
            count += len(lst1) - i
            j += 1
        else:
            res.append(lst1[i])
            i += 1

    res += lst1[i:]
    res += lst2[j:]
    return res, count

n=input()
a=[int(i.strip()) for i in input().split(" ") if i.strip()!=""]
print(mergeSort(a)[1])
