def manual_map(function, iterable):
    result = []
    for item in iterable:
        result.append(function(item))
    return result

def square(x):
    return x * x

def friend(x):
    return[name for name in x if len(name)==4]

    def manual_filter(data, cond):
     for item in data:
        if condition(item):
            filtered_data.append(item)
    
    return filtered_data