resu_arr = []


def all_scort(data, first, last):
    if first == last:
        sstr = ""
        for code in data:
            sstr = sstr + chr(code)
        resu_arr.append(sstr)
    else:
        j = first
        for i in range(first, last):
            data[i], data[j] = data[j], data[i]
            all_scort(data, first + 1, last)
            data[i], data[j] = data[j], data[i]


text = input()
arr_n = [ord(i) for i in text]
all_scort(arr_n, 0, len(arr_n))
resu_arr = sorted(resu_arr)
for h in resu_arr:
    print(h)
