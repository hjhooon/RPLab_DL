def sort_tuple(input_dict):
    value = input_dict.values()
    value = sorted(value)
    key = input_dict.keys()
    t1 = ()
    for i in value:
        for k in key:
            if i == input_dict.get(k):
                t1 = t1 + (k,)
    return t1

input_dict = {'c':2,'a':10,'f':1,'z':4}
print(sort_tuple(input_dict))

input_dict = {'2':'c','10':'a','1':'f','4':'z'}
print(sort_tuple(input_dict))
