def add(list, value):
    return add_recurse(list, value, 0)

def add_recurse(list, value, index):
    if len(list) <= index:
        list.append(value)
        return list
    return add_recurse(list, value, index+1)
    


print(add(["1","2"], "Skip"))

def contains(list, value):
    return contains_recurse(list, value, 0)

def contains_recurse(list, value, index):
    if index >= len(list): return False
    if list[index] == value: return True
    return contains_recurse(list, value, index+1)

def remove(list, value):
    pass

def size(list, value):
    pass

def as_list(list):
    return as_list_recurse(list, 0)

def as_list_recurse(list, index):
    if index >= len(list):
        return []
    return [list[index]] + as_list_recurse(list, index+1)
