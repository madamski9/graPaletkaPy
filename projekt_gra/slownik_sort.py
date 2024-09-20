def sorted_slownik(slownik):
    lst_list = []
    for key, value in slownik.items():
        lst_list.append([key, value])

    for i in range(len(lst_list)):
        for j in range(0, len(lst_list) - i - 1):
            if lst_list[j][1] < lst_list[j + 1][1]:
                lst_list[j], lst_list[j + 1] = lst_list[j + 1], lst_list[j]

    sorted_slownik = {}
    for para in lst_list:
        key = para[0]
        value = para[1]
        sorted_slownik[key] = value

    return sorted_slownik

