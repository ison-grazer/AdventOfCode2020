path_name = 'Day1.txt'


def get_number(lst):
    for i in lst:
        for j in lst:
            for k in lst:
                if i+j+k == 2020:
                    return i * j * k


# Reads from file, default is String so cast to int.
def read_file(path):
    f = open(path, 'r')
    l = f.readlines()
    lst = []
    for i in l:
        lst.append(int(i.rstrip()))
    #for the visuals
    print(get_number(lst))
    return get_number(lst)


read_file(path_name)
